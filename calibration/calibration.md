# Scoping Calibration Data

Claude MUST read this file before generating any new scoping estimate. Use these patterns
to adjust baseline hour ranges from the scoping skill.

---

## Estimation Adjustments

Adjustments derived from completed projects. Each entry includes the source project and
the specific lesson. These override the scoping skill's default ranges when applicable.

*No completed projects with actuals yet. Adjustments will be added as retros are completed.*

---

## Project Baselines

Estimated data from scoped projects. When a project closes and actuals are recorded,
add an "Actuals" section and move learnings into Estimation Adjustments above.

### Arkview Capital (PE / Real Estate)
- **Scoped:** 2026-03-02
- **System:** HubSpot Sales Hub Professional
- **Size:** 5 paid users, <1,000 contacts, 2 pipelines
- **Median estimate:** 121 hrs / $18,150
- **Range:** 86-156 hrs / $12,900-$23,400
- **Approach:** Single-phase, 6-8 weeks
- **Verbal quote given:** $15,000-$30,000 (Cameron on call)
- **Notable factors:** FINRA compliance (no call recording), PE firm parent-child structures, close personal relationship (scope creep risk flagged), budget gatekeeper (Jess) not in discovery
- **Status:** Pending SOW delivery
- **Actuals:** Not yet completed

### Milestone Group (PE / Real Estate Investment)
- **Scoped:** 2026-02 (exact date in discovery notes)
- **System:** HubSpot CRM (Sales Hub Starter or Smart CRM)
- **Size:** 10 users, 4 offices, 2,000-5,000 contacts
- **Fixed fee proposed:** $26,075
- **Approach:** 3-phase, 6-8 weeks
- **Notable factors:** Prior DealCloud abandonment after 2 months (adoption risk), age range 25-65 (varying tech comfort), Google Workspace + Fireflies integration, PE firm with multi-office structure
- **Status:** Proposal delivered (generate_proposal.py output)
- **Actuals:** Not yet completed

### Top Down Auto (Automotive / Manufacturing)
- **Scoped:** 2026-03-05
- **System:** HubSpot Sales Hub Professional + NetSuite ERP integration
- **Size:** 6-10 sales/CSR users, multi-brand/subsidiary
- **Median estimate:** 304 hrs / $45,600
- **Range:** 192-434 hrs / $28,800-$65,100
- **Approach:** Phased -- CRM first (6-8 wks), then ERP integration (6-10 wks)
- **Notable factors:** Legacy ERP (Intuitive) data extraction risk, NetSuite multi-subsidiary, product catalog digitization, 22 open ERP questions, ERP complexity premium applied
- **Status:** Pending follow-up call for ERP clarification
- **Actuals:** Not yet completed

### Strive Global (Insurance / Pet Wellness)
- **Scoped:** 2026-03-21
- **System:** HubSpot Sales Hub Enterprise (reconfiguration)
- **Size:** 23 users, existing HubSpot instance with 10 years of data
- **Option A median:** 119 hrs / $17,850 (CRM Foundation only)
- **Option B median:** 216 hrs / $32,400 (Full CRM Overhaul)
- **Range A:** 86-156 hrs | **Range B:** 160-280 hrs
- **Approach:** Recommended Option A first, Option B as Phase 2
- **Notable factors:** 10 years of uncoded contact data (HIGH risk), pipeline under-reporting from LinkedIn usage, AI enrichment pilot proposed (500 records), CPQ complexity with multiple pricing models, existing Wagmo historical reference used
- **Status:** Proposal in progress
- **Actuals:** Not yet completed

### American Bedding (Manufacturing / CPQ)
- **Scoped:** 2026-03 (CPQ discussion, not full scope)
- **System:** HubSpot CPQ
- **Status:** CPQ-specific consultation, not a full implementation scope
- **Actuals:** N/A

---

## Cross-Project Patterns

Patterns observed across multiple scoping sessions. Updated as more projects complete.

- **PE firms** (Arkview, Milestone): Parent-child company structures are always needed. Budget ~8-11 hrs for contact/company management. FINRA compliance adds constraints (no call recording, manual NDA tracking). Budget gatekeepers often absent from discovery -- flag this risk every time.
- **Existing HubSpot instances** (Strive): Reconfiguration scoping is harder than greenfield. Assume data quality work will hit max estimate. Always audit before committing hours.
- **ERP involvement** (Top Down): The scoping skill's 1.5-2x multiplier held up. 22 open questions after discovery = too many unknowns for fixed-fee. Recommend phased with ERP in Phase 2.
- **Verbal quotes from Cameron** (Arkview): Estimates should land in lower-middle of verbal range to leave buffer. Track verbal quotes alongside formal estimates.
- **Multi-option proposals** (Strive): Offering A/B options with "start A, plan B" recommendation works well for larger engagements. Option A should always be standalone-viable.

---

## How to Use This File

1. **Before scoping:** Read this file. Check if the new client resembles any baselined project (industry, system, size, complexity).
2. **During scoping:** Note any decisions or adjustments in the client's `_decisions.md` file.
3. **After scoping:** Add a new Project Baseline entry above with estimated data.
4. **After project closes:** Run the conversational retro, record actuals, and extract new Estimation Adjustments.
