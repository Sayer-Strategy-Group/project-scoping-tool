# Excel Deliverable Specifications

## Workbook Structure

Output file: `{ClientName}_Scoping_Estimate.xlsx`

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
- Color coding: Blue fill (#DCE6F1) for input cells (rate, assumptions), black text for formula cells

### Sheet 2: "Risk Register"

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
- Color-coded severity column:
  - HIGH: Red fill (#FF0000), white text
  - MEDIUM: Yellow fill (#FFD700), black text
  - LOW: Green fill (#00B050), white text
- Filter-ready headers (auto-filter on header row)

### Sheet 3: "Assumptions & Exclusions"

**Sections (use merged header rows for each):**
1. Scope Assumptions -- what's included
2. Out of Scope -- explicit exclusions
3. Client Responsibilities -- what client must provide
4. Open Items -- unresolved questions that could affect scope

### Sheet 4: "Approach Comparison" (if applicable)

**Layout:**
- Side-by-side comparison matrix
- Color coding: Green fill (#C6EFCE) for advantages, Red fill (#FFC7CE) for disadvantages
- Recommendation section at bottom (merged cells, bold)

## Formatting Standards

| Property | Value |
|----------|-------|
| Body font | Arial 10pt |
| Header font | Arial 11pt, bold |
| Header row fill | Dark blue (#1F4E79), white text |
| Alternating rows | Light gray (#F2F2F2) on even rows |
| Currency format | $#,##0 |
| Borders | Thin borders on all data cells |
| Column widths | Auto-fit with minimum padding (description columns: 40+ chars wide) |
| Freeze panes | Top row + first column frozen |
| Print area | Set on all sheets |

## openpyxl Generation Instructions

Use Python with openpyxl to generate the workbook. Follow these steps:

```python
# 1. Check if openpyxl is installed, install if needed
# pip install openpyxl (run via Bash if not available)

# 2. Key imports
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, numbers
from openpyxl.utils import get_column_letter

# 3. Create workbook and sheets
wb = Workbook()
# Rename default sheet, add additional sheets

# 4. Apply formatting
header_fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
header_font = Font(name="Arial", size=11, bold=True, color="FFFFFF")
body_font = Font(name="Arial", size=10)
alt_row_fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin")
)

# Severity fills for risk register
high_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
medium_fill = PatternFill(start_color="FFD700", end_color="FFD700", fill_type="solid")
low_fill = PatternFill(start_color="00B050", end_color="00B050", fill_type="solid")

# 5. Set column widths appropriately
# 6. Apply freeze panes: ws.freeze_panes = "B2"
# 7. Set print area: ws.print_area = "A1:J{last_row}"
# 8. Apply number format for currency columns: cell.number_format = '$#,##0'
```

**Important:** Write the complete Python script to a temporary file and execute via Bash. Clean up the script after successful generation.
