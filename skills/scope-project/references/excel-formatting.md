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

## openpyxl Generation Instructions

Use Python with openpyxl. **Do not define fills/fonts/borders inline** — import
everything from `scripts/brand_styles.py` (repo root):

```python
# Generator script lives anywhere under the repo; shim the repo root onto sys.path:
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent  # adjust .parent count to reach repo root
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from brand_styles import (
    HEADER_FILL, HEADER_FONT, SECONDARY_HEADER_FILL, SECONDARY_HEADER_FONT,
    BODY_FONT, BOLD_BODY_FONT, TITLE_FONT, ALT_ROW_FILL, INPUT_FILL,
    THIN_BORDER, CURRENCY_FMT, severity_fill,
    style_header_row, style_secondary_header_cells,
    apply_data_styles, apply_data_styles_rows, apply_input_fill_cells,
    get_column_letter,
)

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Scoping Estimate"

# Headers: one call, on-brand
style_header_row(ws, row=1, max_col=10)

# Actuals columns get the quieter secondary header
style_secondary_header_cells(ws, row=1, cols=[11, 12])

# Data rows with alternating Grey 300 striping
apply_data_styles(ws, data_start=2, data_end=last_row, max_col=10)

# Risk severity
cell.fill = severity_fill("HIGH")

# Currency columns
cell.number_format = CURRENCY_FMT

# Freeze panes + print area per sheet
ws.freeze_panes = "B2"
ws.print_area = f"A1:J{last_row}"
```

Python 3.9 compatible — no `X | None` or `tuple[X, Y]` syntax in generated scripts.

**Important:** Write the complete Python script to a temporary file and execute via
Bash. Clean up the script after successful generation.
