"""Generate American Bedding CPQ Phase 1 Scoping Estimate -- Single Fixed Fee"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# ============================================================
# STYLES
# ============================================================
header_font = Font(name='Arial', size=11, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='1F4E79', end_color='1F4E79', fill_type='solid')
body_font = Font(name='Arial', size=10)
bold_font = Font(name='Arial', size=10, bold=True)
total_font = Font(name='Arial', size=10, bold=True, color='1F4E79')
rate_fill = PatternFill(start_color='DAEEF3', end_color='DAEEF3', fill_type='solid')
alt_fill = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')
actuals_fill = PatternFill(start_color='E2EFDA', end_color='E2EFDA', fill_type='solid')
green_header_fill = PatternFill(start_color='548235', end_color='548235', fill_type='solid')
green_header_font = Font(name='Arial', size=11, bold=True, color='FFFFFF')
thin_border = Border(
    left=Side(style='thin'), right=Side(style='thin'),
    top=Side(style='thin'), bottom=Side(style='thin')
)
wrap_align = Alignment(wrap_text=True, vertical='top')
currency_fmt = '$#,##0'
section_font = Font(name='Arial', size=11, bold=True, color='1F4E79')

sev_high_fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')
sev_med_fill = PatternFill(start_color='FFEB9C', end_color='FFEB9C', fill_type='solid')
sev_low_fill = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')


def style_header_row(ws, row, max_col):
    for col in range(1, max_col + 1):
        cell = ws.cell(row=row, column=col)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell.border = thin_border


def apply_data_styles(ws, data_start, data_end, max_col):
    for r in range(data_start, data_end + 1):
        is_alt = (r - data_start) % 2 == 1
        for c in range(1, max_col + 1):
            cell = ws.cell(row=r, column=c)
            cell.font = body_font
            cell.border = thin_border
            cell.alignment = wrap_align
            if is_alt:
                cell.fill = alt_fill


# ============================================================
# SHEET 1: APPROACH COMPARISON
# ============================================================
ws1 = wb.active
ws1.title = 'Approach Comparison'

ws1.merge_cells('A1:C1')
ws1.cell(row=1, column=1, value='American Bedding -- CPQ Phase 1: Approach Comparison').font = Font(
    name='Arial', size=14, bold=True, color='1F4E79'
)

headers = ['Dimension', 'Recommended: HubSpot CPQ + n8n Middleware', 'Alternative: NetSuite Quoting + HubSpot Visibility']
for i, h in enumerate(headers, 1):
    ws1.cell(row=3, column=i, value=h)
style_header_row(ws1, 3, 3)

comparisons = [
    ('Description',
     'HubSpot becomes the quoting interface. n8n middleware orchestrates product data from NetSuite, freight rates from Kuebix, and dynamic weight calculations. Reps create and manage quotes without leaving HubSpot.',
     'Keep quoting in NetSuite. Build enhanced sync to push quote PDFs, line items, and status into HubSpot for visibility. Reps still create quotes in NetSuite but leadership sees everything in HubSpot.'),
    ('Investment', '$34,500 fixed fee', '~$18,000-$22,000 (reduced scope)'),
    ('Rep Experience',
     'Single interface -- no system jumping. Quote creation, freight, pricing, and approval all in HubSpot.',
     'Still requires NetSuite for quote creation. HubSpot is read-only for quote data.'),
    ('Freight Automation',
     'Full -- Kuebix API via n8n with dynamic weight calculation. Multi-carrier LTL rate shopping automated.',
     'None or partial -- manual Kuebix entry continues, or NetSuite-side integration (TPI scope).'),
    ('Weight Calculation',
     'Dynamic engine in n8n replicates Excel formula logic for all 5 product lines. Handles custom sizes.',
     'Manual -- sales reps continue using Excel spreadsheets for weight/dimension lookups.'),
    ('NetSuite Integration',
     'Bi-directional: product catalog sync, quote-to-estimate creation, estimate-to-sales-order conversion, credit hold check.',
     'Enhanced one-way: quote visibility in HubSpot. No quote creation from HubSpot.'),
    ('Shipping Origin Routing',
     'Automated -- n8n determines correct warehouse origin per product/order for Kuebix API calls.',
     'Not applicable -- freight handled manually.'),
    ('Risk Level',
     'MEDIUM -- 3-system integration through n8n middleware. Kuebix API fully reviewed. Dynamic weight calc is highest-risk workstream.',
     'LOW -- simpler scope but does not solve the core pain point (4-system juggling).'),
    ('Value Delivery',
     'HIGH -- eliminates system-jumping, automates freight, reduces quote time from 10-60 min to under 5 min.',
     'LOW -- improves visibility for leadership but does not reduce rep workload or automate anything.'),
    ('Payback Period', '7-9 months on labor savings alone', '12-18 months (visibility value harder to quantify)'),
    ('Phase 2 Readiness',
     'Strong foundation for government RFP automation, customer configurator, and external storefront.',
     'Minimal -- Phase 2 would still need to move quoting to HubSpot.'),
]

for i, (dim, a, b) in enumerate(comparisons, 4):
    ws1.cell(row=i, column=1, value=dim)
    ws1.cell(row=i, column=2, value=a)
    ws1.cell(row=i, column=3, value=b)

apply_data_styles(ws1, 4, 4 + len(comparisons) - 1, 3)

rec_row = 4 + len(comparisons) + 1
ws1.merge_cells(f'A{rec_row}:C{rec_row}')
ws1.cell(row=rec_row, column=1, value='Recommendation').font = section_font
ws1.merge_cells(f'A{rec_row + 1}:C{rec_row + 1}')
ws1.cell(row=rec_row + 1, column=1, value=(
    'HubSpot CPQ + n8n Middleware is recommended. The core pain point is 4-system juggling '
    'that costs Caleb 10-60 minutes per quote across 65 quotes/week. The alternative (enhanced '
    'visibility) does not reduce that workload -- it only lets leadership see what is happening. '
    'The recommended approach eliminates the system-jumping entirely, automates the freight calculation '
    'that is the single biggest time sink, and builds the foundation for Phase 2 government RFP '
    'automation. The Kuebix API has been fully reviewed and the integration path is well-defined. '
    'The dynamic weight calculation engine is the highest-risk workstream -- getting the Excel '
    'spreadsheets from Caleb before finalizing the engagement is critical.'
)).font = body_font
ws1.cell(row=rec_row + 1, column=1).alignment = wrap_align

ws1.column_dimensions['A'].width = 25
ws1.column_dimensions['B'].width = 55
ws1.column_dimensions['C'].width = 55
ws1.freeze_panes = 'A4'

# ============================================================
# SHEET 2: SCOPING ESTIMATE
# ============================================================
ws2 = wb.create_sheet('Scoping Estimate')

ws2.cell(row=1, column=1, value='Hourly Rate:').font = bold_font
ws2.cell(row=1, column=2, value=150).font = bold_font
ws2.cell(row=1, column=2).fill = rate_fill
ws2.cell(row=1, column=2).number_format = currency_fmt

headers2 = ['Workstream', 'Description', 'Min Hours', 'Max Hours', 'Median Hours',
            'Rate', 'Min Cost', 'Max Cost', 'Median Cost', 'Notes / Assumptions',
            'Actual Hours', 'Actual Cost', 'Variance']
for i, h in enumerate(headers2, 1):
    ws2.cell(row=3, column=i, value=h)
style_header_row(ws2, 3, 13)

for col in [11, 12, 13]:
    cell = ws2.cell(row=3, column=col)
    cell.fill = green_header_fill
    cell.font = green_header_font

workstreams = [
    ('HubSpot CPQ Architecture & Configuration',
     'Configure Commerce Hub CPQ module. Custom deal/quote/line item properties. Quote approval workflows. Quote numbering and validity settings (30-day window). Payment terms configuration (prepay, net 10/30/60).',
     14, 22,
     'Commerce Hub Professional confirmed. Standard CPQ config with custom properties for manufacturing context. Approval workflows for discount overrides.'),

    ('Product Catalog Sync (NetSuite to HubSpot)',
     'SuiteQL extraction of 700 SKUs from NetSuite. Map to HubSpot products with custom properties: weight components, freight class, dimensions (L x W x H), cover type, foam series, construction type. Build n8n scheduled sync for ongoing price and product updates.',
     20, 36,
     'Flat catalog approach -- one product per SKU, custom properties for filtering. SuiteQL batch queries efficient (1-2 API calls for full catalog). Ongoing sync handles NetSuite price changes. OAuth 2.0 M2M auth.'),

    ('NetSuite Quote-to-Order Integration',
     'OAuth 2.0 M2M setup in NetSuite. Quote acceptance triggers NetSuite Estimate creation via REST API. Estimate-to-Sales Order conversion on fulfillment. Customer credit status check before quoting. Payment terms sync. Price level sync from NetSuite.',
     22, 40,
     'Bi-directional: HubSpot quote -> NetSuite estimate -> sales order -> work order. Customer credit hold check reads AR data before allowing quote. 1.25x ERP adjacency premium applied (existing integration, not greenfield).'),

    ('Kuebix Freight Integration + Origin Routing',
     'n8n workflow: collect line item weights and dimensions from quote -> determine origin warehouse based on product/order rules -> POST /action/quickRate to Kuebix -> parse multi-carrier LTL response -> write cheapest rate as freight line item on quote. Manual override option. Error handling with fallback to manual entry.',
     22, 38,
     'Kuebix API fully reviewed (OpenAPI 3.0.2). Basic Auth. quickRate returns multi-carrier quotes sorted by price. Full street address required (not just zip). Origin routing adds complexity for multiple warehouse locations. persist=false prevents phantom shipments.'),

    ('Dynamic Weight Calculation Engine',
     'Replicate Excel formula logic in n8n for all 5 product lines: Dorm Mattress, Camp Mattress, Dura-Last Poly-Fiber, SoFlux OX Covers, Vinyl Covers. Panel calculations, fabric weight by cover type (Anti-Bac Vinyl 283.5 g/yd2, SoFlux OX 121.9 g/yd2, Pinstripe 102.1 g/yd2), foam weight by density/thickness, innerspring weight by size, cotton batting, insulator pad, packaging weight. Cube volume for LTL/TL determination. Validate against known Excel outputs.',
     28, 44,
     'HIGHEST-RISK WORKSTREAM. 5 separate Excel spreadsheets with nested IF/AND formulas. Each product line has different calculation paths. Must get Excel files from Caleb and verify no VBA/macros before committing. Test formula replication on 3 product lines before building all 5.'),

    ('Quote Template Design',
     'Custom HubL/HTML/CSS quote template matching current NetSuite quote format. Line item table (Qty, Item #, Description, Unit Price, Amount). Subtotal, volume discount (10%), state-based tax, shipping line, total. Damaged freight policy terms. Delivery instructions field. Customer acceptance flow (clickwrap or e-sign). PDF optimization.',
     12, 20,
     'Reference: 5 NetSuite PDF quote examples provided. Must match header/footer, line item format, terms section. HubSpot Flow theme supports custom properties in line item table. @media print CSS for PDF generation.'),

    ('Discount, Tax & Payment Terms Logic',
     'Volume discount automation (10% threshold -- confirm if automatic or requires approval above certain levels). State-based tax calculation (9.75% TN, exempt for out-of-state -- may need broader state tax table). Payment terms workflow (prepay for new customers, net 10/30/60 for established). Credit hold check integration from NetSuite AR data.',
     10, 18,
     'Tax logic may need external service for multi-state accuracy beyond TN. Discount approval thresholds TBD at kickoff. Credit hold is a read from NetSuite customer record -- flags but does not hard-block.'),

    ('Training & Documentation',
     'Sales team training (Caleb, Don): new HubSpot quoting workflow, product selection, freight review. Admin training (Sarah-Beth, Patrick): system management, product catalog updates, sync monitoring, troubleshooting. All sessions virtual and recorded. Admin guide + user quick reference card.',
     10, 16,
     '2-3 sessions total. Emphasis on showing reps the time savings. Admin guide covers n8n workflow monitoring and product sync management. Record for future onboarding.'),

    ('Testing & QA',
     'End-to-end integration testing across all 3 systems. Quote accuracy validation (compare HubSpot output to known NetSuite quotes from the 5 examples). Weight calculation validation (compare n8n output to Excel calculators). Freight calculation validation (compare n8n/Kuebix output to manual Kuebix lookups). UAT with Caleb and Don. 2-week hypercare post go-live.',
     14, 24,
     'Test matrix covers: product sync accuracy, weight calc per product line, freight quote accuracy, quote template rendering, NetSuite estimate creation, sales order conversion, credit hold flagging. 2 UAT sessions minimum.'),

    ('Project Management',
     'Kickoff meeting, weekly status calls, milestone reviews. Coordination with American Bedding team (Mike, Sarah-Beth, Caleb, Patrick). Documentation and change request management. Scope creep prevention (especially government RFP boundary). Go-live planning.',
     16, 26,
     '~12% of total hours. Weekly syncs with Sarah-Beth (primary POC). Milestone reviews with Mike/Patrick at weeks 4, 8, and go-live. All change requests documented formally.'),
]

for i, (name, desc, min_h, max_h, notes) in enumerate(workstreams, 4):
    row = i
    ws2.cell(row=row, column=1, value=name)
    ws2.cell(row=row, column=2, value=desc)
    ws2.cell(row=row, column=3, value=min_h)
    ws2.cell(row=row, column=4, value=max_h)
    ws2.cell(row=row, column=5).value = f'=AVERAGE(C{row},D{row})'
    ws2.cell(row=row, column=6).value = '=$B$1'
    ws2.cell(row=row, column=7).value = f'=C{row}*$B$1'
    ws2.cell(row=row, column=8).value = f'=D{row}*$B$1'
    ws2.cell(row=row, column=9).value = f'=E{row}*$B$1'
    ws2.cell(row=row, column=10, value=notes)
    for col in [11, 12, 13]:
        ws2.cell(row=row, column=col).fill = actuals_fill
    ws2.cell(row=row, column=13).value = f'=IF(K{row}="","",K{row}-E{row})'

total_row = 4 + len(workstreams)
ws2.cell(row=total_row, column=1, value='TOTAL').font = total_font
for col in [3, 4, 5, 7, 8, 9, 11, 12]:
    cl = get_column_letter(col)
    ws2.cell(row=total_row, column=col).value = f'=SUM({cl}4:{cl}{total_row - 1})'
    ws2.cell(row=total_row, column=col).font = total_font
    ws2.cell(row=total_row, column=col).border = thin_border
ws2.cell(row=total_row, column=6).value = '=$B$1'
ws2.cell(row=total_row, column=6).font = total_font

for col in [7, 8, 9, 12]:
    for row in range(4, total_row + 1):
        ws2.cell(row=row, column=col).number_format = currency_fmt

apply_data_styles(ws2, 4, total_row - 1, 10)
for row in range(4, total_row + 1):
    for col in [11, 12, 13]:
        ws2.cell(row=row, column=col).fill = actuals_fill
        ws2.cell(row=row, column=col).border = thin_border
        ws2.cell(row=row, column=col).font = body_font

# Fixed fee row
fee_row = total_row + 2
ws2.cell(row=fee_row, column=1, value='FIXED FEE PRESENTED:').font = Font(name='Arial', size=11, bold=True, color='1F4E79')
ws2.cell(row=fee_row, column=9, value=34500).font = Font(name='Arial', size=11, bold=True, color='1F4E79')
ws2.cell(row=fee_row, column=9).number_format = currency_fmt
ws2.cell(row=fee_row, column=10, value='Fixed fee. Client sees this number only -- no hours breakdown in proposal.').font = body_font

widths = {1: 30, 2: 55, 3: 12, 4: 12, 5: 14, 6: 10, 7: 12, 8: 12, 9: 14, 10: 55, 11: 14, 12: 14, 13: 12}
for col, w in widths.items():
    ws2.column_dimensions[get_column_letter(col)].width = w
ws2.freeze_panes = 'B4'

# ============================================================
# SHEET 3: RISK REGISTER
# ============================================================
ws3 = wb.create_sheet('Risk Register')

headers3 = ['#', 'Risk', 'Severity', 'Likelihood', 'Impact', 'Mitigation', 'Owner', 'Status']
for i, h in enumerate(headers3, 1):
    ws3.cell(row=1, column=i, value=h)
style_header_row(ws3, 1, 8)

risks = [
    (1, 'Excel weight calculator logic more complex than analyzed -- VBA macros, external references, or circular formulas',
     'HIGH', 'MEDIUM',
     'Dynamic weight engine blows past 44 hrs max estimate. Fixed fee becomes untenable. Workstream 5 is unbounded.',
     'Get all 5 Excel files from Caleb BEFORE finalizing engagement. Test formula replication on Dorm Mattress calculator first (most complex). If VBA or external refs found, re-scope as time-and-materials for weight engine only.',
     'Kyle (pre-engagement)', 'Open'),

    (2, 'NetSuite data quality -- SKU duplicates, stale pricing, missing attributes from Jan 2026 launch',
     'HIGH', 'HIGH',
     'Product sync imports bad data into HubSpot. Quotes show wrong prices or descriptions. Customer trust eroded.',
     'NetSuite item data audit during Week 1. Define cleanup scope before building sync. SuiteQL queries validate data quality before bulk import. Flag items missing required fields (weight, freight class, dimensions).',
     'Consultant + Sarah-Beth', 'Open'),

    (3, 'Scope creep via Vesco/Kaitlynn relationship -- government RFP work creeps into Phase 1',
     'HIGH', 'MEDIUM',
     'Informal requests bypass SOW. Government-specific requirements consume hours budgeted for CPQ. Don Reynolds enthusiasm for Phase 2 pulls scope.',
     'SOW signed by Mike Taylor or Patrick (budget authority), not Kaitlynn. Phase 1/Phase 2 boundary iron-clad in SOW. All change requests documented formally. Weekly hours tracking visible to client.',
     'Kyle + Mike', 'Open'),

    (4, 'NetSuite still stabilizing (launched Jan 1, 2026) -- API schema changes, TPI updates, data quality shifts',
     'HIGH', 'MEDIUM',
     'Integration breaks after TPI makes changes. Data model shifts invalidate SuiteQL queries. API access disrupted during maintenance.',
     'Build integration against documented REST API (not custom SuiteScript). Version-lock API endpoints. Establish communication channel with TPI for change notifications even though they are not directly involved.',
     'Consultant', 'Open'),

    (5, 'Multiple shipping origins add routing complexity -- wrong origin = wrong freight quote = wrong price',
     'MEDIUM', 'HIGH',
     'Incorrect origin address sent to Kuebix. Freight quotes are wrong. Customer receives inaccurate pricing. Trust and margin impact.',
     'Map all warehouse addresses at kickoff with ops team. Define explicit routing rules (which products/regions ship from which warehouse). Test each origin with known Kuebix quotes. Build fallback to default origin if routing is ambiguous.',
     'Consultant + Mike', 'Open'),

    (6, 'HubSpot CPQ limitations -- no calculated fields, no product variants, no native tax engine',
     'MEDIUM', 'HIGH',
     'Workarounds needed for freight as line item (must be pre-computed by n8n). Product selection UX is less polished than dedicated CPQ. Tax calculation requires external logic.',
     'Pre-compute all calculated values in n8n before quote is published. Use custom properties and filtered views for product selection. Document workaround patterns for admin team. Tax logic in Ops Hub custom code or n8n.',
     'Consultant', 'Open'),

    (7, 'Kuebix API rate limits undocumented -- high quote volume could hit throttling',
     'MEDIUM', 'LOW',
     '65 quotes/week (plus revisions) could exceed undocumented rate limits. Freight quotes fail silently or are throttled.',
     'Confirm rate limits with Kuebix support before build begins. Implement response caching for repeat origin/destination/weight combinations (many camp quotes go to similar destinations). Build graceful fallback to manual entry if API is unavailable.',
     'Consultant', 'Open'),

    (8, 'Adoption risk -- sales reps switching from NetSuite quoting to HubSpot quoting',
     'MEDIUM', 'MEDIUM',
     'Caleb and Don revert to old process because it is familiar. New system goes unused. ROI unrealized.',
     'Executive mandate from Mike. Show concrete time savings in training (side-by-side demo). 2-week parallel run where both systems are used. Monitor adoption metrics. Caleb is motivated (he described the pain) -- leverage that.',
     'Mike + Consultant', 'Open'),

    (9, 'Freight class determination per product is unclear or inconsistent',
     'MEDIUM', 'MEDIUM',
     'Wrong freight class sent to Kuebix. Shipping costs are systematically over or under estimated. Margin impact across all quotes.',
     'Confirm freight class source at kickoff (NetSuite item record field vs. static lookup table vs. calculated from product specs). Document freight class per product line. Validate against known Kuebix quotes for 5 example orders.',
     'Consultant + Caleb', 'Open'),

    (10, 'Budget authority anchored on Billy $25K verbal benchmark -- $34.5K creates sticker shock',
     'MEDIUM', 'MEDIUM',
     'Patrick (CFO) or Mike expects $25K. $34.5K proposal triggers budget negotiation or scope reduction request.',
     'Frame $25K as pre-discovery estimate from intro call. Proposal explicitly shows scope expansion since then: Sayer doing all NetSuite work (not TPI), dynamic weight calculation engine, multiple shipping origins, full Kuebix API integration. Value-based ROI framing ($38K-$58K/year savings, 7-9 month payback).',
     'Kyle + Billy', 'Open'),
]

for i, (num, risk, sev, lik, impact, mit, owner, status) in enumerate(risks, 2):
    ws3.cell(row=i, column=1, value=num)
    ws3.cell(row=i, column=2, value=risk)
    ws3.cell(row=i, column=3, value=sev)
    ws3.cell(row=i, column=4, value=lik)
    ws3.cell(row=i, column=5, value=impact)
    ws3.cell(row=i, column=6, value=mit)
    ws3.cell(row=i, column=7, value=owner)
    ws3.cell(row=i, column=8, value=status)
    sev_cell = ws3.cell(row=i, column=3)
    if sev == 'HIGH':
        sev_cell.fill = sev_high_fill
    elif sev == 'MEDIUM':
        sev_cell.fill = sev_med_fill
    else:
        sev_cell.fill = sev_low_fill

apply_data_styles(ws3, 2, len(risks) + 1, 8)
for i, (_, _, sev, *_) in enumerate(risks, 2):
    c = ws3.cell(row=i, column=3)
    if sev == 'HIGH':
        c.fill = sev_high_fill
    elif sev == 'MEDIUM':
        c.fill = sev_med_fill
    else:
        c.fill = sev_low_fill

widths3 = {1: 5, 2: 50, 3: 12, 4: 12, 5: 45, 6: 55, 7: 25, 8: 10}
for col, w in widths3.items():
    ws3.column_dimensions[get_column_letter(col)].width = w
ws3.freeze_panes = 'A2'

# ============================================================
# SHEET 4: ASSUMPTIONS & EXCLUSIONS
# ============================================================
ws4 = wb.create_sheet('Assumptions & Exclusions')

ws4.cell(row=1, column=1, value='Scope Assumptions').font = section_font
assumptions = [
    'HubSpot Sales Hub Professional + Commerce Hub Professional (existing)',
    'Operations Hub Professional recommended (separate license ~$800/mo -- not included in project fee)',
    'Up to 700 products in HubSpot product library (flat catalog, one record per SKU)',
    'NetSuite REST API access with OAuth 2.0 M2M credentials provided by client',
    'Kuebix API credentials (username, API key, 15-character Client ID) provided by client',
    'n8n middleware hosted by Sayer or on client infrastructure (hosting cost separate from project fee)',
    'Multiple shipping origin addresses -- client provides complete warehouse list with routing rules at kickoff',
    'Freight class stored as a property per product in NetSuite or as a static lookup per product line',
    'Up to 30 custom properties across deals, quotes, and line items (overages are change orders)',
    '10-12 week implementation timeline',
    'All work conducted remotely',
    'Rate: $150/hr (internal tracking -- client sees fixed fee only)',
    'Fixed fee: $34,500 -- 5 equal payments of $7,245 ($6,900 + 5% tech/admin fee) every 15 days, Net-15',
    'Dynamic weight calculation covers 5 product lines (Dorm, Camp, Dura-Last, SoFlux OX, Vinyl)',
    'Excel shipping calculators do not contain VBA macros or external data references (must verify before engagement)',
    'Quote template matches current NetSuite format (5 PDF examples as reference)',
    'SOW signed by Mike Taylor (VP) or Patrick (CFO) -- budget authority, not just project champion',
]
for i, a in enumerate(assumptions, 2):
    ws4.cell(row=i, column=1, value=i - 1)
    ws4.cell(row=i, column=2, value=a)

gap = len(assumptions) + 3
ws4.cell(row=gap, column=1, value='Out of Scope').font = section_font
exclusions = [
    'Government RFP automation, compliance tracking, bid management (Phase 2)',
    'Customer-facing product configurator / guided selling decision tree (Phase 2)',
    'External storefront build (Shopify or HubSpot Commerce -- Phase 3)',
    'VoIP / call capture system selection or integration',
    'AI lead enrichment from call transcripts',
    'NetSuite reimplementation, new module deployment, or SuiteScript development',
    'Ongoing Kuebix TMS administration or carrier management',
    'HubSpot Marketing Hub configuration or marketing automation',
    'Custom self-service pricing portal',
    'Ongoing managed services beyond 2-week hypercare post go-live',
    'HubSpot or NetSuite license procurement or tier changes (recommendations provided only)',
    'Data migration from external systems beyond NetSuite product catalog sync',
    'TPI (NetSuite partner) coordination or management -- Sayer works directly in NetSuite',
]
for i, e in enumerate(exclusions, gap + 1):
    ws4.cell(row=i, column=1, value=i - gap)
    ws4.cell(row=i, column=2, value=e)

gap2 = gap + len(exclusions) + 2
ws4.cell(row=gap2, column=1, value='Client Responsibilities').font = section_font
responsibilities = [
    'Provide Kuebix API credentials (username, API key, 15-character Client ID)',
    'Provide NetSuite admin access or create OAuth 2.0 M2M integration record with API permissions',
    'Provide all 5 Excel shipping calculator files for technical review (action item from Mar 23 call)',
    'Provide complete warehouse address list with product/region routing rules',
    'Confirm freight class per product line (or provide lookup reference)',
    'Designate primary point of contact (Sarah-Beth recommended)',
    'Ensure Caleb and Don availability for 2+ UAT sessions during weeks 9-10',
    'SOW signed by Mike Taylor or Patrick (CFO) -- budget authority',
    'Validate 5-10 sample quotes against current NetSuite output during UAT',
    'Provide 5-10 recent quotes with known freight costs for validation testing',
]
for i, r in enumerate(responsibilities, gap2 + 1):
    ws4.cell(row=i, column=1, value=i - gap2)
    ws4.cell(row=i, column=2, value=r)

gap3 = gap2 + len(responsibilities) + 2
ws4.cell(row=gap3, column=1, value='Open Items (Confirm During Kickoff)').font = section_font
open_items = [
    'NetSuite item types in use (InventoryItem vs. AssemblyItem vs. NonInventoryItem)',
    'NetSuite price level structure (single price list vs. multiple price levels per customer tier)',
    'Exact number and full street addresses of all shipping warehouses',
    'Routing rules: which products or regions ship from which warehouse',
    'Discount approval thresholds -- is 10% always automatic? Do higher discounts need Mike/Patrick approval?',
    'Credit hold workflow details -- what triggers a hold, who can override, should quote creation be blocked or just flagged?',
    'Quote validity period (30 days per current NetSuite quotes -- confirm or adjust)',
    'Whether Excel spreadsheets contain VBA macros or external data references (blocker for weight calc engine)',
    'Dimensional data future-proofing -- carriers may require L x W x H per item (affects data model decisions)',
    'Kuebix rate limits and acceptable API call volume (confirm with Kuebix support)',
    'Operations Hub Professional -- client decision on whether to add this tier',
    'n8n hosting location -- Sayer infrastructure or client-provided environment',
]
for i, o in enumerate(open_items, gap3 + 1):
    ws4.cell(row=i, column=1, value=i - gap3)
    ws4.cell(row=i, column=2, value=o)

for row in ws4.iter_rows(min_row=2, max_col=3):
    for cell in row:
        cell.font = body_font
        cell.alignment = wrap_align

ws4.column_dimensions['A'].width = 5
ws4.column_dimensions['B'].width = 90

# SAVE
output_path = '/Users/harbuckconsulting/projects/project-scoping-tool/American Bedding - CPQ Discussion/American_Bedding_CPQ_Estimate.xlsx'
wb.save(output_path)
print(f'Saved to: {output_path}')
