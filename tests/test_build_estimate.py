"""Tests for the shared scoping-workbook generator (scripts/build_estimate.py).

These run with no external dependencies (no API keys) — they exercise the
scope.json -> schema -> workbook path against the committed fixture. This is the
guardrail that keeps a teammate from producing a workbook whose task breakdown
disagrees with its top-line estimate.
"""
import copy
import json
from datetime import date
from pathlib import Path

import pytest

import build_estimate as be

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURE = REPO_ROOT / "tests" / "fixtures" / "example_scope.json"
COMMITTED_FIXTURE = REPO_ROOT / "tests" / "fixtures" / "example_scope_committed.json"
SCHEMA = REPO_ROOT / "templates" / "scoping-schema.json"


@pytest.fixture(scope="module")
def scope():
    with FIXTURE.open() as fh:
        return json.load(fh)


@pytest.fixture(scope="module")
def committed():
    with COMMITTED_FIXTURE.open() as fh:
        return json.load(fh)


def test_fixture_validates_against_schema(scope):
    errors = be.validate_scope(scope)
    assert errors == [], "fixture should validate cleanly: %s" % errors


def test_cost_invariant_holds(scope):
    """cost.{min,max,median} must equal hours.{min,max,median} * rate."""
    for w in scope["workstreams"]:
        for k in ("min", "max", "median"):
            assert round(w["cost"][k], 2) == round(w["hours"][k] * w["rate"], 2), w["id"]


def test_task_subtotals_reconcile_to_medians(scope):
    """Every workstream's task hours must sum to its median (the Sheet-2 check)."""
    for w in scope["workstreams"]:
        tasks = w.get("tasks") or []
        if tasks:
            assert sum(t["hours"] for t in tasks) == w["hours"]["median"], w["id"]


def test_totals_reconcile_to_budget_summary(scope):
    for k in ("min", "max", "median"):
        assert sum(w["hours"][k] for w in scope["workstreams"]) == scope["budgetSummary"]["totalHours"][k]


def test_build_workbook_produces_required_sheets(scope):
    wb = be.build_workbook(scope)
    required = ["Scoping Estimate", "Task Breakdown", "Deliverables & Acceptance",
                "Risk Register", "Assumptions"]
    for sheet in required:
        assert sheet in wb.sheetnames
    # Optional Approach Comparison present because the fixture has approaches.
    assert "Approach Comparison" in wb.sheetnames


def test_scoping_estimate_has_totals_row(scope):
    wb = be.build_workbook(scope)
    est = wb["Scoping Estimate"]
    total_rows = [r for r in range(1, est.max_row + 1)
                  if str(est.cell(row=r, column=1).value).strip().upper() == "TOTAL"]
    assert len(total_rows) == 1
    # SUM formulas land on the hour + cost columns
    tr = total_rows[0]
    assert str(est.cell(row=tr, column=5).value).startswith("=SUM(")


def test_task_breakdown_integrity_formula_targets_correct_rows(scope):
    """Each subtotal's CHECK must compare to the matching workstream's Sheet-1 median."""
    wb = be.build_workbook(scope)
    tb = wb["Task Breakdown"]
    checks = [tb.cell(row=r, column=6).value for r in range(1, tb.max_row + 1)
              if tb.cell(row=r, column=6).value and "IF(" in str(tb.cell(row=r, column=6).value)]
    # One integrity check per workstream that has tasks.
    with_tasks = [w for w in scope["workstreams"] if w.get("tasks")]
    assert len(checks) == len(with_tasks)
    assert all("'Scoping Estimate'!E" in c for c in checks)


# --------------------------------------------------------------------------- #
# Committed / T&M mode (parity with the committed/T&M reference layout)
# --------------------------------------------------------------------------- #
def test_committed_fixture_validates(committed):
    assert be.validate_scope(committed) == []


def test_committed_phase_amounts_and_summary_reconcile(committed):
    """committedAmount = committedHours * blendedRate; subtotal/fee/grand match committedSummary."""
    blended = committed["engagement"]["blendedRate"]
    pct = committed["engagement"]["techFeePct"]
    for p in committed["phases"]:
        assert p["committedAmount"] == p["committedHours"] * blended, p["id"]
    subtotal = sum(p["committedAmount"] for p in committed["phases"])
    fee = round(subtotal * pct / 100)
    cs = committed["committedSummary"]
    assert subtotal == cs["consultingSubtotal"]
    assert fee == cs["techFee"]
    assert subtotal + fee == cs["grandTotal"]
    # Committed-example economics: 232 hrs * $135 = $31,320; +5% tech fee = $1,566; grand = $32,886.
    assert (cs["consultingSubtotal"], cs["techFee"], cs["grandTotal"]) == (31320, 1566, 32886)


def test_committed_task_subtotals_reconcile_to_committed_hours(committed):
    for p in committed["phases"]:
        tasks = p.get("tasks") or []
        if tasks:
            assert sum(t["hours"] for t in tasks) == p["committedHours"], p["id"]


# --------------------------------------------------------------------------- #
# Schedule (engagement.startDate) — optional, ranges-mode-only, backward compatible
# --------------------------------------------------------------------------- #
def test_schedule_absent_without_start_date(scope):
    """No engagement.startDate -> no Schedule sheet, fully backward compatible."""
    assert be.compute_schedule(scope) is None
    wb = be.build_workbook(scope)
    assert "Schedule" not in wb.sheetnames


def test_schedule_absent_in_committed_mode_even_with_start_date(committed):
    """v1 schedule covers ranges mode only — committed/phase mode has no workstreams[]."""
    s = copy.deepcopy(committed)
    s["engagement"]["startDate"] = "2026-08-03"
    assert be.compute_schedule(s) is None


def test_schedule_sequential_chains_and_concurrent_spans_full_timeline(scope):
    s = copy.deepcopy(scope)
    s["engagement"]["startDate"] = "2026-08-03"
    pm = next(w for w in s["workstreams"] if w["category"] == "pm")
    pm["scheduling"] = "concurrent"

    schedule = be.compute_schedule(s)
    assert schedule["start_date"] == date(2026, 8, 3)
    assert schedule["end_date"] > schedule["start_date"]

    sequential = [w for w in s["workstreams"] if w.get("scheduling", "sequential") == "sequential"]
    # Each sequential workstream's start == the previous one's end (single-track chain).
    prev_end = schedule["start_date"]
    for w in sequential:
        sched = schedule["workstreams"][w["id"]]
        assert sched["start"] == prev_end, w["id"]
        assert sched["end"] >= sched["start"]
        prev_end = sched["end"]
    assert prev_end == schedule["end_date"]

    # Concurrent workstream spans the full project window, not a sequential slice.
    pm_sched = schedule["workstreams"][pm["id"]]
    assert pm_sched["start"] == schedule["start_date"]
    assert pm_sched["end"] == schedule["end_date"]

    # Task-level dates within a workstream stay inside its own window.
    for w in sequential:
        sched = schedule["workstreams"][w["id"]]
        for t in sched["tasks"]:
            assert sched["start"] <= t["start"] <= t["end"] <= sched["end"]


def test_schedule_sheet_rendered_when_start_date_set(scope):
    s = copy.deepcopy(scope)
    s["engagement"]["startDate"] = "2026-08-03"

    wb = be.build_workbook(s)
    assert "Schedule" in wb.sheetnames
    # Inserted right after Task Breakdown.
    assert wb.sheetnames[2] == "Schedule"

    ws = wb["Schedule"]
    header_row = next(r for r in range(1, ws.max_row + 1)
                       if ws.cell(row=r, column=1).value == "#")
    headers = [ws.cell(row=header_row, column=c).value for c in range(1, 8)]
    assert headers == ["#", "Workstream", "Task", "Hours", "Start Date", "End Date", "Duration (wks)"]

    # A final bold PROJECT rollup row exists with the overall window.
    project_rows = [r for r in range(1, ws.max_row + 1)
                     if ws.cell(row=r, column=2).value == "PROJECT"]
    assert len(project_rows) == 1


def test_schedule_sheet_is_formula_driven_not_static(scope):
    """Regression guard: dates must be live formulas referencing the input
    cells ($C$2 start date, $C$3 capacity, $C$4 computed end), NOT
    pre-computed static values -- verified end-to-end with a real formula
    engine (recalculating after changing $C$2) during development; this test
    pins the formula SHAPE so a future edit can't silently revert to statics.
    """
    s = copy.deepcopy(scope)
    s["engagement"]["startDate"] = "2026-08-03"
    pm = next(w for w in s["workstreams"] if w["category"] == "pm")
    pm["scheduling"] = "concurrent"

    wb = be.build_workbook(s)
    ws = wb["Schedule"]

    # Input cells: start date is a plain value (the seed), capacity is a plain
    # value, and the project end date is a formula derived from both.
    assert not str(ws.cell(row=2, column=3).value).startswith("=")
    assert not str(ws.cell(row=3, column=3).value).startswith("=")
    end_formula = str(ws.cell(row=4, column=3).value)
    assert end_formula.startswith("=$C$2")
    assert "SUMIF(" in end_formula and "$C$3" in end_formula

    header_row = next(r for r in range(1, ws.max_row + 1)
                       if ws.cell(row=r, column=1).value == "#")
    first_data_row = header_row + 1

    # First sequential task's Start Date formula references $C$2 directly (no
    # rows above it to accumulate) and its End Date adds its own hours.
    first_start = str(ws.cell(row=first_data_row, column=5).value)
    first_end = str(ws.cell(row=first_data_row, column=6).value)
    assert first_start.startswith("=$C$2+(0/$C$3)")
    assert first_end.startswith("=$C$2+((0+D%d)/$C$3)" % first_data_row)

    # A later sequential row's cumulative-hours term is a bounded SUMIFS over
    # the hidden Track column, not a static number.
    later_rows = [r for r in range(first_data_row + 1, ws.max_row + 1)
                  if str(ws.cell(row=r, column=8).value) == "SEQ"]
    assert later_rows, "expected at least one later sequential task row"
    later_formula = str(ws.cell(row=later_rows[0], column=5).value)
    assert "SUMIFS(" in later_formula and '"SEQ"' in later_formula

    # A concurrent row's dates are exactly the project start/end cells.
    conc_rows = [r for r in range(first_data_row, ws.max_row + 1)
                 if str(ws.cell(row=r, column=8).value) == "CONC"]
    assert conc_rows
    assert ws.cell(row=conc_rows[0], column=5).value == "=$C$2"
    assert ws.cell(row=conc_rows[0], column=6).value == "=$C$4"

    # Duration column is always computed from the row's own start/end cells.
    assert str(ws.cell(row=first_data_row, column=7).value) == (
        "=(F%d-E%d)/7" % (first_data_row, first_data_row))

    # The Track helper column is hidden -- an internal aid, not a deliverable.
    assert ws.column_dimensions["H"].hidden is True


def test_schedule_capacity_defaults_from_total_hours_and_timeline(scope):
    """No explicit capacityHoursPerWeek -> derived as totalHours.median / estimatedTimelineWeeks."""
    s = copy.deepcopy(scope)
    s["engagement"]["startDate"] = "2026-08-03"
    s["engagement"].pop("capacityHoursPerWeek", None)
    weeks = s["engagement"]["estimatedTimelineWeeks"]
    median = s["engagement"]["totalHours"]["median"]

    schedule = be.compute_schedule(s)
    assert schedule["capacity"] == pytest.approx(median / weeks)


def test_committed_mode_sheets_and_layout(committed):
    wb = be.build_workbook(committed)
    # 5 sheets, no Approach Comparison (matches the committed/T&M reference layout).
    assert "Approach Comparison" not in wb.sheetnames
    for sheet in ["Scoping Estimate", "Task Breakdown", "Deliverables & Acceptance",
                  "Risk Register", "Assumptions"]:
        assert sheet in wb.sheetnames
    est = wb["Scoping Estimate"]
    labels = [str(est.cell(row=r, column=1).value or "") for r in range(1, est.max_row + 1)]
    assert "P1" in labels and "CONT" in labels  # phase rollup rendered
    # Sheet-2 integrity formula targets the committed Est. Hours column (C), not E.
    tb = wb["Task Breakdown"]
    checks = [tb.cell(row=r, column=5).value for r in range(1, tb.max_row + 1)
              if tb.cell(row=r, column=5).value and "IF(" in str(tb.cell(row=r, column=5).value)]
    assert checks and all("'Scoping Estimate'!C" in c for c in checks)
