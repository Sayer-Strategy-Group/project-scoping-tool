# Excel Deliverable Specifications

## Brand

All workbooks follow the Sayer brand (see the `sayer-brand-guidelines` skill).
The executable spec lives in `scripts/brand_styles.py` at the repo root — **import
styles from there; never hard-code hex values in generator scripts.** If the brand
skill and `brand_styles.py` ever disagree, fix both in the same commit.

## Workbook Structure

Output file: `{ClientName}_Scoping_Estimate.xlsx`

Default to **5 sheets** (validated standard — include Task Breakdown and
Deliverables & Acceptance without being asked). Approach Comparison is an
optional additional sheet when multiple implementation approaches are on the
table. Schedule is an optional additional sheet (ranges mode) when
`engagement.startDate` is set — set it whenever a project start date is known,
per the standing rule to scope schedule alongside scope and budget, not just
on request.

### Sheet 1: "Scoping Estimate"

**Columns:**
- A: Workstream
- B: Description
- C: Min Hours
- D: Max Hours
- E: Median Hours
- F: Rate (reference a single configurable rate cell)
- G: Min Cost (= Min Hours x Rate)
- H: Max Cost (= Max Hours x Rate)
- I: Median Cost (= Median Hours x Rate)
- J: Notes/Assumptions

**Requirements:**
- Totals row at bottom with SUM formulas
- Rate modeling section: single configurable rate cell that all cost columns reference
- Input cells (rate, assumptions): Cool Grey fill (`INPUT_FILL`); formula cells plain
- Actuals columns (post-project calibration): secondary header style (`SECONDARY_HEADER_FILL`, Grey 700 + white text) to preserve the forecast-vs-reality visual split

### Sheet 2: "Task Breakdown"

Per-workstream task detail with hours per task.

**Requirements:**
- Tasks grouped under workstream section rows
- Formula-based integrity checks: workstream subtotals must reference back to
  Sheet 1 ("Scoping Estimate") and surface any mismatch (e.g., a `CHECK` column
  comparing the subtotal against the Sheet 1 median hours)
- Phase subtotal rows styled with `BOLD_BODY_FONT`; use `apply_data_styles_rows`
  so striping skips section/subtotal rows

### Sheet 3: "Deliverables & Acceptance"

**Columns:**
- A: # (sequential)
- B: Deliverable
- C: Description
- D: Workstream
- E: Acceptance Criteria

### Sheet 4: "Risk Register"

**Columns:**
- A: # (sequential)
- B: Risk
- C: Severity (HIGH / MEDIUM / LOW)
- D: Likelihood (HIGH / MEDIUM / LOW)
- E: Impact
- F: Mitigation
- G: Owner
- H: Status

**Requirements:**
- Color-coded severity column via `severity_fill(level)`:
  - HIGH: light red fill (`SEV_HIGH`, #FFC7CE), black text
  - MEDIUM: Sayer Yellow fill (`SEV_MEDIUM`, #FEC700), black text
  - LOW: light green fill (`SEV_LOW`, #C6EFCE), black text
- Filter-ready headers (auto-filter on header row)

### Sheet 5: "Assumptions"

**Sections (use merged header rows for each):**
1. Scope Assumptions -- what's included
2. Out of Scope -- explicit exclusions
3. Client Responsibilities -- what client must provide
4. Open Items -- unresolved questions that could affect scope

### Sheet 3 (ranges mode only, optional): "Schedule"

Present only when `engagement.startDate` is set on scope.json — fully backward
compatible (omitted entirely on scope.json records without it, including
committed/T&M mode for v1). Inserted at index 2, right after Task Breakdown.

**Columns:**
- A: # (sequential)
- B: Workstream
- C: Task
- D: Hours
- E: Start Date
- F: End Date
- G: Duration (wks)

**Requirements:**
- Metadata block: Project Start Date (`$C$2`) + Assumed Capacity hrs/week (`$C$3`)
  as `INPUT_FILL` cells, plus a **Computed Project End Date** (`$C$4`, a formula,
  not an input) and a caption explaining the model.
- **Dates are LIVE Excel formulas, not static values** — editing `$C$2` or `$C$3`
  in the spreadsheet recalculates every task, workstream, and the project end date
  automatically, matching Sheet 1's single-rate-cell pattern. No regeneration
  needed to see a new start date's effect. A hidden helper column ("Track",
  column H, `SEQ`/`CONC` per row) lets a bounded `SUMIFS` compute "cumulative
  sequential hours before this row" while correctly ignoring interleaved
  concurrent rows — see `compute_schedule()`/`build_schedule_sheet()` in
  `scripts/build_estimate.py` for the exact formula shapes.
- One row per task (synthesized as a single row from the workstream median if a
  workstream has no `tasks[]`), followed by a bold "— window" rollup row per
  workstream (min start / max end via direct cell references to its first/last
  task rows), followed by a final bold "PROJECT" row (`=$C$2` / `=$C$4`).
- Model: `scheduling: "sequential"` (default) workstreams consume capacity in
  `workstreams[]` array order — a single-track critical-path approximation with
  no dependency graph. `scheduling: "concurrent"` workstreams (PM/governance,
  an externally-gated feasibility spike) span the full computed project window
  (`$C$2` to `$C$4`) instead of blocking it.

### Sheet 6: "Approach Comparison" (optional, if applicable)

**Layout:**
- Side-by-side comparison matrix
- Color coding: light green fill (`SEV_LOW`, #C6EFCE) for advantages, light red fill (`SEV_HIGH`, #FFC7CE) for disadvantages
- Recommendation section at bottom (merged cells, bold)

## Formatting Standards

| Property | Value |
|----------|-------|
| Font | Calibri (brand fallback — Rethink Sans does not survive xlsx round-tripping) |
| Title | Calibri 14pt bold (`TITLE_FONT`) |
| Header row | Sayer Yellow fill (#FEC700), black bold 11pt (`HEADER_FILL` + `HEADER_FONT`) |
| Secondary header (actuals) | Grey 700 fill (#2E2E2E), white bold 11pt (`SECONDARY_HEADER_FILL` + `SECONDARY_HEADER_FONT`) |
| Body | Calibri 11pt (`BODY_FONT`) |
| Alternating rows | Grey 300 (#E3E3E3) on alternating data rows (`ALT_ROW_FILL`) |
| Input cells | Cool Grey (#D6D6D6) fill (`INPUT_FILL`) |
| Currency format | `$#,##0` (`CURRENCY_FMT`) |
| Borders | Thin Grey 500 (#BCBCBC) borders on all data cells (`THIN_BORDER`) |
| Column widths | Auto-fit with minimum padding (description columns: 40+ chars wide) |
| Freeze panes | Top row + first column frozen |
| Print area | Set on all sheets |

## Generation: use the shared generator, not a hand-written script

**Do NOT hand-write a per-client openpyxl script.** The workbook is produced from the
structured `scope.json` (see `templates/scoping-schema.json`) by the single shared
generator at the repo root:

```bash
python3 scripts/build_estimate.py {ClientFolder}/scope.json
# validate the record without writing a workbook:
python3 scripts/build_estimate.py {ClientFolder}/scope.json --validate-only
```

This is the de-duplication win: one code path, driven by data, produces an identical
on-brand workbook every time — including the Sheet-2 → Sheet-1 integrity formulas. The
old per-client `build_estimate.py` scripts in client folders are retired.

This spec document describes **what the generator emits** (so you can understand or modify
it), not a workbook to assemble by hand. If you change the workbook layout, change
`scripts/build_estimate.py` and its test (`tests/test_build_estimate.py`) — then update this
spec in the same commit.

All styling is imported from `scripts/brand_styles.py` (the brand single-source-of-truth):
`HEADER_FILL`/`HEADER_FONT` (primary Sayer-Yellow header), `SECONDARY_HEADER_*` (Grey-700
actuals header), `apply_data_styles` (Grey-300 striping), `INPUT_FILL` (Cool-Grey input
cells), `severity_fill()` (risk traffic-light), `CURRENCY_FMT`. Never hard-code hex.

Python 3.9 compatible — no `X | None` or `tuple[X, Y]` syntax in the generator.
