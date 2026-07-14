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
optional 6th sheet when multiple implementation approaches are on the table.

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
