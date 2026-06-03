# Example: Acme Corp Scoping

## Input: Discovery Notes

> "Met with Acme Corp. 15-person team, currently using spreadsheets and QuickBooks.
> Want HubSpot CRM for sales pipeline, need to migrate 5,000 contacts from Mailchimp
> and integrate with QuickBooks for invoice sync. Also need Aircall for phone system
> integrated with HubSpot. Timeline: want live in 8 weeks."

## Parsed Complexity Indicators

- **Users:** 15 (Medium tier)
- **Systems:** HubSpot CRM, QuickBooks (ERP), Mailchimp (Marketing), Aircall (Phone)
- **Data sources:** 3 (spreadsheets, Mailchimp, QuickBooks)
- **Integrations:** 2 (QuickBooks sync, Aircall integration)
- **Data migration:** 1 source (Mailchimp, 5K contacts)
- **ERP involvement:** Yes (QuickBooks -- triggers complexity premium)
- **Timeline pressure:** 8 weeks is tight for 4 systems

## Output: Workstream Breakdown

| # | Workstream | Min | Max | Median |
|---|-----------|-----|-----|--------|
| 1 | CRM Architecture & Setup | 8 | 16 | 12 |
| 2 | Pipeline & Deal Management | 8 | 14 | 11 |
| 3 | Contact & Company Management | 8 | 16 | 12 |
| 4 | Automations & Workflows | 12 | 24 | 18 |
| 5 | Reporting & Dashboards | 8 | 16 | 12 |
| 6 | QuickBooks Integration | 12 | 24 | 18 |
| 7 | Aircall Integration | 8 | 16 | 12 |
| 8 | Mailchimp Data Migration | 10 | 20 | 15 |
| 9 | Training (Admin + End-User) | 6 | 10 | 8 |
| 10 | Project Management | 8 | 16 | 12 |
| | **TOTAL** | **88** | **172** | **130** |

## Output: Key Risks Identified

| Risk | Severity | Likelihood |
|------|----------|------------|
| Data quality from spreadsheets (no validation, likely duplicates) | HIGH | HIGH |
| QuickBooks API limitations (rate limits, field restrictions) | MEDIUM | MEDIUM |
| 8-week timeline tight for 4 systems | HIGH | MEDIUM |
| Mailchimp list health unknown (bounces, unsubscribes) | MEDIUM | MEDIUM |
| Phone number porting timeline (carrier-dependent) | MEDIUM | LOW |
| Adoption risk (moving from spreadsheets to CRM) | HIGH | MEDIUM |

## Output: Recommended Approach

**Phased approach recommended** due to ERP involvement and data quality concerns:

- **Phase 1 (Weeks 1-5):** CRM setup + Mailchimp migration. Establishes the foundation. Allows data quality assessment early.
- **Phase 2 (Weeks 4-8, overlapping):** QuickBooks integration + Aircall setup. Builds on clean CRM data. Phone porting can start in parallel.

Rationale: The spreadsheet-to-CRM migration is the highest-risk item. Getting data clean and CRM functional before layering on integrations reduces cascading failure risk. The 2-week overlap between phases keeps total timeline within 8 weeks.

## Output: Cost Summary (at $150/hr)

- **Min:** $13,200
- **Max:** $25,800
- **Median:** $19,500
