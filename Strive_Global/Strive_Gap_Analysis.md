# STRIVE Global -- Gap Analysis & Follow-Up Questions

**Prepared by:** Kyle Harbuck, Harbuck Consulting / Sayer
**Date:** March 21, 2026
**Sources:** Discovery call (Mar 19, 2026), discovery questionnaire (Feb 24, 2026), intro call (Feb 20, 2026)

---

## Current State Assessment

### What We Know

**CRM Infrastructure:**
- HubSpot Sales Hub Enterprise (confirmed), Marketing Hub, Service Hub
- 3 core seats, 10 sales seats, 10 service seats (23 total -- likely over-provisioned)
- Outlook integration active (with known email logging defect)
- HubSpot CMS hosting forms
- One active automation: broker trial form request (Slack notification)
- No other sales automations or workflows in place

**Pipeline & Sales Process:**
- Single pipeline mixing pre-pipeline (FTA-0) and active deals
- Stages: FTA-0 through FTA-6 (Closed Won), plus need for "Contracting" stage
- Two deal categories needed: partner-level and client-level (not separate pipelines)
- Product segmentation (microsite, AI, app, rewards) captured through product set fields, not pipeline structure
- Deal size range: $6K client deals to $400K+ broker packs
- Average deal size: ~$30K (skewed by blended reporting)
- Lead sources: broker referral (primary), inbound, self-prospected

**Data Quality:**
- 10 years of contact records with zero contact type classification
- No way to distinguish clients, prospects, brokers, or partners
- Duplicate and dead records throughout the database
- Contacts not properly associated to companies
- No enrichment tools currently integrated (LinkedIn Navigator and MyEdge available but not feeding CRM)

**Forecasting & Reporting:**
- No algorithmic forecasting -- gut feel only
- No probability weighting by stage
- No deal health scoring
- Board reports take 1+ full business day to prepare manually
- Key metrics (deal velocity, deal age, stage progression) not trusted
- Average deal size inflated by blended partner + client reporting

**Quoting & Contracts:**
- Manual quote creation (no templates, no product library)
- Contracts sent via DocuSign through COO
- Pipeline under-reported because deals exist outside CRM during quoting
- No standardized pricing structure for broker packs

**Team & Adoption:**
- Reps prospect in LinkedIn Sales Navigator; activity not logged in HubSpot
- Meetings logged after the fact, not in real-time
- Email logging creates noise (emails to broker-associated contacts log to all deals)
- No email sequencing, proposal generation, or contract management tools
- Sales onboarding is tribal knowledge (Slack-based Q&A)

---

### What We Don't Know (Gaps)

| # | Gap | Impact on Scope | Priority |
|---|-----|----------------|----------|
| 1 | Exact contact/company/deal record counts in HubSpot | Determines enrichment and dedup effort (could swing workstream 3 by 20+ hours) | CRITICAL |
| 2 | Complete product/pricing inventory (SKUs, bundles, pricing models) | Cannot build CPQ product library without this (Option B workstream 13) | CRITICAL for B |
| 3 | Service Hub usage details | May be paying for unused seats; may have workflows to preserve | HIGH |
| 4 | COO identity (Lauren vs. Zach Beegal) | Affects stakeholder map, admin access, NDA process | HIGH |
| 5 | Outlook email logging defect scope | Determines if fix is config change (2 hrs) or platform bug requiring HubSpot support (unknown timeline) | MEDIUM |
| 6 | Existing workflow inventory beyond broker trial form | May have stale or broken automations that conflict with new builds | MEDIUM |
| 7 | Divi product positioning (standalone vs. bundled) | Affects product library structure and reporting segmentation | MEDIUM |
| 8 | Historical deal data reliability | Determines if we can calibrate probability percentages from actual data vs. using industry benchmarks | MEDIUM |
| 9 | Jodi's Wagmo stage naming framework | Could accelerate stage design if available | LOW |
| 10 | NetSuite entity structure and admin contact | Scopes integration prep work (Option B) | LOW for now |

---

## Follow-Up Questions for Andrea & Jodi

### Must-Have Before Finalizing Scope

**1. Product Library Inventory** (for Andrea)
We need a complete list of everything STRIVE sells, with pricing structures, to scope CPQ correctly.
- What are all the individual products? (App, Microsite, AI Assistant, Rewards/Divi -- any others?)
- What bundles exist? (e.g., Microsite + AI, Full Platform)
- What pricing models apply to each? (Fixed license, per-head, rev share, hybrid)
- Are there standard discount tiers or is pricing fully custom?
- Can Andrea share 3-5 recent quotes or proposals as examples?

**2. Service Hub Usage** (for Jodi)
- Who on the team is actively using Service Hub? (NPS, support tickets, etc.)
- Are there active workflows or automations in Service Hub that need to be preserved?
- Is the Client Success team using it for client health tracking, or is that entirely in Excel?

**3. COO Clarification** (for Jodi)
- Is the COO Lauren or Zach Beegal? (Public records show Zach; Jodi referenced Lauren in Feb call.)
- Who controls HubSpot admin access and would need to be involved in configuration decisions?

**4. Outlook Email Logging Issue** (for Andrea)
- Is the email-logging-to-all-deals issue affecting all users or specific ones?
- When did it start? Has anyone opened a HubSpot support ticket?
- Is this specific to broker contacts associated with multiple deals, or happening with all contacts?

### Should-Have Before Kickoff

**5. Microsite Client Intake Form** (for Andrea)
- Can Andrea share the HubSpot form link for the microsite/broker order form? (She mentioned sending it during the call.)
- Are there separate forms per broker, or one shared form?

**6. Existing Automations** (for Andrea)
- Beyond the broker trial form request, are there any other workflows running in HubSpot?
- Are there any scheduled reports or notification workflows currently active?

**7. Divi / Rewards Positioning** (for Andrea/Jodi)
- Is Divi sold as a standalone product, a bundled add-on, or both?
- Does it need its own deal tracking, or is it always a line item on existing deals?
- Is there a client expansion motion for Divi (Client Success upselling rewards spend)?

**8. Historical Data Quality** (for Andrea)
- How far back does deal data go in HubSpot? (Deals created, amounts, stages, dates)
- Is the historical data reliable enough to calculate actual conversion rates by stage?
- Or should we plan to use Jodi's industry benchmark framework (5/20/40/50/60/80/90/100) as the starting point?

**9. Wagmo Stage Framework** (for Jodi)
- Did Jodi locate the stage naming convention from Wagmo that she mentioned on the call?
- If so, can she share it as a reference for STRIVE's stage design?

**10. NetSuite Details** (for Jodi -- Option B only)
- What entities exist in NetSuite? (Customers, invoices, products, chart of accounts?)
- Who is the NetSuite admin we'd coordinate with for integration prep?
- Is there a data dictionary or field map available?

**11. SOW Authority** (for Jodi)
- Does Jodi sign the SOW as CEO, or does the Essex Bay board need to approve expenditures of this size?
- What is the approval timeline? (This affects when we can schedule kickoff.)

---

## Recommendations

1. **Get HubSpot access ASAP.** Record counts and a quick portal audit will make the difference between rough estimates and confident ones. This is the single biggest thing that will sharpen the scope.

2. **Start with Option A, plan for Option B.** The CRM Foundation work (pipeline, contacts, dashboards) is prerequisite for everything in Option B. Even if the board approves the full overhaul, the phased timeline ensures Option A is completed first.

3. **Run the AI enrichment pilot early.** Before committing to the full contact cleanup, test HubSpot's Breeze AI credits on 500 records. Measure: classification accuracy, fields populated, records that need manual review. This de-risks the largest single workstream.

4. **Board presentation framing.** Jodi should position this as infrastructure investment, not a software project. The ROI narrative (separate document) provides the language: "This unlocks pipeline visibility, eliminates 120+ hours/year of manual reporting, and builds the data foundation for AI-powered operations."
