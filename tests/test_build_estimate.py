"""Tests for the shared scoping-workbook generator (scripts/build_estimate.py).

These run with no external dependencies (no API keys) — they exercise the
scope.json -> schema -> workbook path against the committed fixture. This is the
guardrail that keeps a teammate from producing a workbook whose task breakdown
disagrees with its top-line estimate.
"""
import json
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
