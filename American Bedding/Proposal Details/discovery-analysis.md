# American Bedding -- Discovery Analysis

**Prepared by:** Kyle Harbuck / Claude
**Date:** April 2, 2026
**Discovery sources:**
- Intro Call: March 16, 2026 (Kyle, Billy Leigh, Mike Taylor, Sarah-Beth Knight, Kaitlynn Akins)
- Follow-up Call: March 23, 2026 (Kyle, Billy, Cameron Taggart, Mike Taylor, Sarah-Beth, Caleb, Don Reynolds)

---

## Client Profile

| Field | Detail |
|-------|--------|
| Company | American Bedding |
| Parent | Vesco (PE portfolio company) |
| Industry | Manufacturing -- mattresses for camps, missions, education, dorms, government/military |
| Customer retention | ~70% (repeat customers) |
| Key channels | Inside sales (camps/missions/education), government contracts (~35% of revenue), website/inbound |
| Quote volume | 65 quotes/week (Caleb handles inside sales) |
| Quote sources | 60% email, 20% phone, 20-25% website forms |
| Quote processing time | 10 minutes to 1 hour per quote |
| SKU count | ~700 total, 40-60 core SKUs used regularly |

---

## Decision-Maker Map

| Name | Role | Relevance | Budget Authority |
|------|------|-----------|-----------------|
| Patrick | CFO | NetSuite owner, approves scope and budget | **Yes -- primary** |
| Mike Taylor | VP Sales | Business sponsor, wants sales team efficiency | Influences |
| Sarah-Beth Knight | Operations / HubSpot Admin | Technical POC, evaluated CPQ previously | No |
| Don Reynolds | Government Sales Lead | Government channel owner, RFP process expert, potential Phase 2 champion | No |
| Caleb | Inside Sales | Primary end user, handles 65+ quotes/week | No |
| Kaitlynn Akins | Vesco Portfolio Advisor | Portfolio-level sponsor, introduced Sayer | Influences (PE level) |

**Note:** Patrick was not in the March 16 intro call. Both calls confirmed he is the SOW signer. Kaitlynn influences at the PE level but may not sign.

---

## Systems Architecture

```
[Inbound Leads]
     |
     v
[HubSpot CRM] <--ZoomInfo (enrichment + prospecting)
     |
     | (bi-directional sync: deal stages, close date, amount)
     | (does NOT sync: quote PDFs, line items, pricing during deal)
     v
[NetSuite ERP] <-- Launched Jan 1, 2026 (TPI partner, Atlanta)
     |
     |--- Quote generation (manual)
     |--- Opportunity → Sales Order → Work Order → Invoice
     |
     v
[Cubics TMS] <-- Manual freight rate lookup
     |         Requires: destination zip, weight, freight class
     |         NO API integration currently
     |
[Excel Spreadsheets] <-- Weight/dimension calculators per product line
     |                    Camp Mattress, Dorm Mattress, Dura-Last, SoFlux OX, Vinyl Cover
     |                    Hardcoded IF/AND formulas, desktop files (not centralized)
```

**Current integrations:**
- HubSpot ↔ NetSuite: Two-way sync at opportunity level (stages, close date, deal amount). 2-10 min sync delay.
- HubSpot ↔ ZoomInfo: Contact enrichment + outbound prospecting
- Cubics: Manual entry only (no API)
- Excel: Manual maintenance on individual desktops

---

## Current State -- Pain Points

### 1. Systems Fragmentation (Primary Pain)
Quoting requires navigating 4 systems in sequence:
1. **HubSpot** -- Capture lead/contact info, log opportunity
2. **NetSuite** -- Create opportunity, build quote with pricing
3. **Excel** -- Look up product weight, freight class, dimensions (per product line)
4. **Cubics** -- Enter weight + zip + freight class to get freight rate, manually transcribe back to quote

This loop takes 10 minutes for simple quotes, up to 1 hour for complex ones. Caleb handles 65 quotes/week through this process.

### 2. No Quote Visibility in HubSpot
- HubSpot shows deal stages and amounts, but NO quote PDFs, line items, or pricing during the deal lifecycle
- Quote amounts sync only after deal closure
- Sales leadership cannot see quote activity, versions, or edits without going to NetSuite
- Multiple quote versions per opportunity are common (grant budgeting, customer comparisons) but invisible in HubSpot

### 3. SKU Bloat and Product Complexity
- 700+ SKUs in NetSuite, but only 40-60 are core
- Significant duplication -- legacy/unused variants never cleaned up
- SKUs not loaded into HubSpot yet (paused during NetSuite implementation)
- Customers often don't know product specs (mattress type, size, foam series, cover) -- sales must guide them through selection

### 4. Manual Freight Calculation
- Weight and freight class data lives in Excel spreadsheets, NOT in NetSuite
- Each product line has its own calculator with hardcoded formulas (5 spreadsheets provided)
- Cubics requires manual data entry for each freight quote
- Sometimes waits until next business day for truckload rates
- Future carrier requirements may need dimensional data (L x W x H) -- 2+ year threat

### 5. Manual Payment Hold Process
- Customers with overdue payments are placed on hold manually
- No automated flags prevent quoting to blocked customers
- Risk of quoting and shipping to customers who owe money

### 6. Government RFP Complexity (Separate Channel)
- 35% of business, entirely manual process outside HubSpot/NetSuite
- RFPs require: written proposals, cut sheets, contract clause compliance checklists (52+ pages per solicitation)
- 15 leads/week quoted to 7+ teaming partners
- Each RFP: ~6+ hours of manual work (Don Reynolds)
- Tracked in spreadsheets, no system integration
- GSA platform changes frequently (recent full catalog reformat)
- **Explicitly deferred to Phase 2 by all parties**

---

## Desired Future State

1. **Single-pane quoting in HubSpot** -- Sales team creates and manages quotes without leaving HubSpot
2. **Automated freight calculation** -- Cubics API integration eliminates manual lookups (Cameron confirmed "open API documentation" exists)
3. **Guided selling interface** -- Decision tree/questionnaire helps customers who don't know product specs self-qualify
4. **Full quote visibility** -- All quote versions, edits, cancellations, approvals visible in HubSpot
5. **Price book sync** -- NetSuite product/pricing data mirrored to HubSpot
6. **SKU rationalization** -- Reduce 700 to 40-60 core, clean up duplicates
7. **Automated payment holds** -- Flag blocked customers, prevent quoting until resolved
8. **Government bid tracking** -- System-integrated forecasting (Phase 2)
9. **VoIP/call capture** -- Not selected yet, wide open (Phase 3+)
10. **External storefront** -- Shopify or HubSpot Commerce (Phase 3+, Billy recommended deferring)

---

## Budget Signals

- **$25,000 verbal anchor** -- Billy Leigh stated on March 16 intro call: "The initial project cost estimate for similar setups is around $25,000 based on previous engagements" (27:07)
- This was framed as the starting point for inside sales CPQ, not full scope including government RFP
- No explicit budget ceiling stated by Patrick or Mike
- **Phased approach preferred** -- Start small, iterate. Billy: "Start with smaller, high-impact projects to build momentum"
- Vesco is the PE sponsor -- portfolio-level investment appetite exists but specific budget TBD

---

## Complexity Indicators

| Factor | Rating | Detail |
|--------|--------|--------|
| User count | Low | 3-5 sales users (Caleb + Don + 1-2 others) |
| SKU count | Medium-High | 700 total, 40-60 core -- rationalization needed |
| System integrations | High | 4 systems (HubSpot, NetSuite, Cubics, Excel) |
| Data quality | Medium | NetSuite data is fresh (Jan 2026), but Excel weight data is desktop-based and uncentralized |
| ERP involvement | Medium | NetSuite is live with basic sync. Enhancement needed, not full build |
| Custom objects | Low | Standard HubSpot objects likely sufficient |
| Regulatory | Low (Phase 1) | No FINRA or compliance concerns for inside sales. Government compliance is Phase 2 |
| Change management | Low-Medium | Small sales team, motivated leadership. Don Reynolds is a willing Phase 2 champion |

---

## Open Items / Unknowns

### Technical
1. **Cubics API capability** -- Cameron found "open API documentation" but no technical review completed. Unknown: auth method, endpoints, rate limits, error handling, data format coverage
2. **HubSpot Commerce Hub tier** -- Sarah-Beth said it "has the functionality built within it, but there may be a third-party integration needed." Tier confirmation required (Pro minimum)
3. **NetSuite quote sync depth** -- Can we push quote PDFs and line items into HubSpot via the existing connector, or does it require middleware/custom integration? TPI partner involvement unclear
4. **SKU data quality in NetSuite** -- 700 SKUs with unknown duplication patterns. 40-60 core estimate is from Mike/Don, not validated against data
5. **Freight dimension requirements** -- Carriers may require L x W x H in addition to weight in 2+ years. Affects data model decisions now

### Business
6. **TPI (NetSuite partner) role** -- Still under contract for support. Would they need involvement for HubSpot-NetSuite integration changes? Cost/timeline implications unknown
7. **Patrick's budget position** -- CFO approves spend but was not in detailed discovery call. Risk of misalignment between champion expectations (Mike/Sarah-Beth) and budget authority
8. **Government RFP Phase 2 timing** -- "After CPQ confidence built" but no specific trigger or timeline defined
9. **VoIP selection** -- Wide open, no vendor selected. Mentioned by Billy as enrichment source but not prioritized

### Data Needed from Client
- Caleb: Copy of Excel weight/freight spreadsheet for technical review
- Caleb: Sample quoting data sets from HubSpot and NetSuite
- Don Reynolds: Sample RFP solicitations and government bid tracking spreadsheet
- Patrick: Confirm NetSuite integration status and TPI involvement scope
- Cameron: Cubics API documentation link for technical assessment
- Sarah-Beth: HubSpot Commerce Hub tier confirmation

---

## Key Quotes from Discovery

> "We handled 65 quotes last week -- 60% via email, 20% phone, 20-25% website form submissions." -- Caleb (March 23, 05:48)

> "The initial project cost estimate for similar setups is around $25,000 based on previous engagements." -- Billy Leigh (March 16, 27:07)

> "Most customers don't know exact mattress sizes or specs." -- Caleb (March 23, 12:30)

> "About 35% of business comes from government bids, which require detailed RFP responses versus simple quotes." -- Mike Taylor (March 16, 24:33)

> "Start with smaller, high-impact projects to build momentum and avoid complexity overload." -- Billy Leigh (March 23, 45:41)
