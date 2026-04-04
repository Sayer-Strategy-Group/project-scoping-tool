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
- **Scoped:** 2026-04-02 (revised same day from initial A/B structure to single fixed fee)
- **System:** HubSpot CPQ (Sales Hub Pro + Commerce Hub Pro) + NetSuite ERP + Kuebix TMS + n8n middleware
- **Size:** 3-5 sales users, 700 SKUs (40-60 core), 65+ quotes/week, multiple shipping warehouses
- **Median estimate:** 226 hrs / $33,900
- **Range:** 168-284 hrs / $25,200-$42,600
- **Fixed fee presented:** $34,500
- **Approach:** Single-phase, 10-12 weeks (inside sales CPQ only)
- **Verbal quote given:** $25,000 (Billy on intro call, pre-discovery benchmark)
- **Notable factors:** Sayer owns all development including NetSuite (TPI not involved). Dynamic weight calculation engine replicates 5 Excel spreadsheets in n8n (HIGHEST-COMPLEXITY workstream -- 28-44 hrs published, 30-41 hrs validated). Excel files received and analyzed 2026-04-04: no VBA, no external refs, no circular formulas. Dorm Mattress is primary driver (9-level nesting, 180+ paths: 3 construction x 5 foam x 4 batting x 3 covers). SoFlux OX and Vinyl Cover share ~80% code reuse. Camp and Dura-Last are moderate complexity. Remaining unknown: "Special Case Check with Delbert" in Dorm Mattress. Kuebix API fully reviewed (quickRate endpoint, Basic Auth, multi-carrier LTL). Multiple shipping origins with routing logic. n8n as middleware (not HubSpot custom code). Recommended Ops Hub Pro (~$800/mo). Government RFP excluded (Phase 2). Vesco PE portfolio company. Patrick (CFO) is budget authority. Initial scope used A/B options ($19,500/$33,000) but revised to single fee after: (1) Sayer confirmed as sole developer, (2) Kuebix API reviewed (45% -> high confidence), (3) dynamic weight calc selected, (4) multiple ship origins confirmed.
- **Status:** Proposal in progress (Gamma). Pre-engagement gate cleared 2026-04-04 (Excel files validated).
- **Actuals:** Not yet completed

---

## Cross-Project Patterns

Patterns observed across multiple scoping sessions. Updated as more projects complete.

- **PE firms** (Arkview, Milestone): Parent-child company structures are always needed. Budget ~8-11 hrs for contact/company management. FINRA compliance adds constraints (no call recording, manual NDA tracking). Budget gatekeepers often absent from discovery -- flag this risk every time.
- **Existing HubSpot instances** (Strive): Reconfiguration scoping is harder than greenfield. Assume data quality work will hit max estimate. Always audit before committing hours.
- **ERP involvement** (Top Down): The scoping skill's 1.5-2x multiplier held up. 22 open questions after discovery = too many unknowns for fixed-fee. Recommend phased with ERP in Phase 2.
- **Verbal quotes from Cameron** (Arkview): Estimates should land in lower-middle of verbal range to leave buffer. Track verbal quotes alongside formal estimates.
- **Multi-option proposals** (Strive): Offering A/B options with "start A, plan B" recommendation works well when phases are naturally separable. American Bedding was initially scoped as A/B but revised to single fee when no natural standalone subset existed (CPQ without freight automation leaves reps in a fifth system). A/B works when Option A delivers standalone value; it fails when the core problem requires all components.
- **Manufacturing/CPQ** (American Bedding): Freight/TMS integration is a unique complexity factor not covered by standard scoping skill ranges. Kuebix API (quickRate endpoint) is well-documented and straightforward once credentials are obtained. Dynamic weight calculation from Excel spreadsheets is the real risk -- nested IF/AND formulas with product-specific logic paths. Always get the Excel files and validate complexity BEFORE committing a fixed fee. Desktop Excel spreadsheets as data source = data centralization is a prerequisite workstream. **VALIDATED (2026-04-04):** Excel analysis confirmed nested IF/AND formulas only -- no VBA, no external refs, no circular formulas. Complexity ranged from simple linear calcs (SoFlux OX, Vinyl Cover -- ~80% code reuse between them) to 9-level nested IFs with 180+ calculation paths (Dorm Mattress). The pre-engagement gate pattern works: getting files early converted the highest-risk workstream from "medium confidence" to "high confidence" without changing the fee. Future manufacturing/CPQ scopes: budget complexity by product line, not uniformly across all calculators.
- **ERP adjacency vs. ERP build** (Top Down Auto, American Bedding): When ERP is already live with working sync, use 1.25x adjacency premium instead of full 1.5-2x. The full multiplier is for greenfield ERP implementations with unresolved data questions. However, when consultant (not the ERP partner) owns NetSuite development, add 40-60 hrs for direct API work including OAuth setup, SuiteQL, and estimate/sales order creation.
- **Middleware architecture** (American Bedding): n8n as integration middleware between 3+ systems is viable and avoids HubSpot custom code action limitations (20s timeout, 128MB). First project using this pattern -- track actuals carefully for calibration.

---

## How to Use This File

1. **Before scoping:** Read this file. Check if the new client resembles any baselined project (industry, system, size, complexity).
2. **During scoping:** Note any decisions or adjustments in the client's `_decisions.md` file.
3. **After scoping:** Add a new Project Baseline entry above with estimated data.
4. **After project closes:** Run the conversational retro, record actuals, and extract new Estimation Adjustments.
