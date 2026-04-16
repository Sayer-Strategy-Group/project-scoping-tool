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
- **Phase 1 (V1) estimate:** 168-270 hrs (median ~219) / ~$30,000 fixed fee
- **Phase 2 (V2) estimate:** 56-90 hrs (median ~73) / ~$11,500 fixed fee
- **Total:** 224-360 hrs (median ~292) / ~$41,500
- **Approach:** Two-phase -- Phase 1 HubSpot-native CPQ (10-12 weeks), Phase 2 Railway production platform (4-6 weeks)
- **Verbal quote given:** $25,000 (Billy on intro call, pre-discovery benchmark)
- **Notable factors:** Sayer owns all development including NetSuite (TPI not involved). Dynamic weight calculation engine replicates 5 Excel spreadsheets (HIGHEST-COMPLEXITY workstream -- 28-44 hrs, validated 2026-04-04). Excel files: no VBA, no external refs, no circular formulas. Dorm Mattress is primary driver (9-level nesting, 180+ paths). SoFlux OX and Vinyl Cover share ~80% code reuse. Remaining unknown: "Special Case Check with Delbert" in Dorm Mattress. Kuebix API fully reviewed (quickRate endpoint, Basic Auth, multi-carrier LTL). Multiple shipping origins with routing logic. Architecture shifted 2026-04-04 from n8n middleware to hybrid HubSpot custom code + Railway production API -- production deliverables must be standalone code, not n8n dependent. Two-phase structure: V1 (HubSpot-native) then V2 (Railway hardening). Ops Hub Pro required (~$800/mo). Railway hosting (~$5-20/mo). Government RFP excluded (future phase). Vesco PE portfolio company. Patrick (CFO) is budget authority. Pricing evolved: A/B options ($19.5K/$33K) -> single fee ($34.5K) -> two-phase ($30K + $11.5K) as architecture changed.
- **Status:** Proposal in progress. Pre-engagement gate cleared 2026-04-04. Architecture revised to hybrid HubSpot/Railway same day.
- **Actuals:** Not yet completed

### HelloSpoke (VoIP / Telecom — Multifamily Real Estate)
- **Scoped:** 2026-04-16 (revised same day after CPQ scope correction)
- **System:** HubSpot CRM (existing instance reconfiguration) + Salesforce migration + HubSpot CPQ native (AI) + Rev IO billing + QuickBooks Online + QuotaPath (assist)
- **Size:** 15-18 users, 30 employees, <50K Salesforce records (assumed)
- **Median estimate:** 234 hrs / $35,100
- **Range:** 158-346 hrs / $23,700-$51,900
- **Fixed fee proposed:** $42,000 (full scope) / $22,000 (reduced — CRM foundation only, Phases 1-2)
- **Approach:** Single engagement, 14 weeks. Phased data migration (inactive → active → leads). Integrations + CPQ built together in Phase 3 (weeks 5-11). Enablement Phase 4 (weeks 10-14).
- **Verbal quote given:** None — clean pricing slate
- **Notable factors:** Salesforce contract expires October 2026 (hard deadline with buffer). First-time Rev IO and QuickBooks integrations for Sayer — premium applied (American Bedding NetSuite pattern). Rev IO has no native HubSpot marketplace app; REST API with Basic Auth, sandbox available but webhooks don't work in sandbox. QuickBooks native HubSpot integration insufficient for revenue actuals use case — custom build required (OAuth2, webhook, reconciliation). **CPQ is a material standalone workstream (38 hrs med), not a QuotaPath fallback** — initially (incorrectly) combined with QuotaPath as "fallback-only" in D4; re-scoped as dedicated workstream in D10 after transcript re-read. HubSpot CPQ native is HelloSpoke's declared direction ("they have the AI CPQ" per Billy, still in testing); PandaDoc is change-order fallback if AI CPQ falls short. CPQ scope covers: product library (up to 50 SKUs), dual dynamic templates (VoIP + Notify SaaS) with product-driven T&Cs, bulk line-item import up to 300 lines (property management deals), parent-child property auto-creation with dedup (fixes current Salesforce duplicate pain), quote approval workflow (2 tiers), native e-sig replacing DocuSign (vendor tripled rate), close-won amount auto-sync to deal. QuotaPath trimmed to HubSpot-side data flow only (10 hrs med, no longer covers quoting). Integration chain: Rev IO → HubSpot custom object → deal → QuotaPath; QB reconciles revenue actuals against same deal data; CPQ feeds quote → Rev IO billing record creation. Existing HubSpot instance (provisioned ~Feb 2026 via HubSpot Growth team demo). Jeremy Wiley is budget-aware decision maker; Christina Edwards is ops lead/project liaison. Elastic/ALN database integration, Campfire ERP, ClickUp sync explicitly excluded.
- **Status:** Proposal drafted (revised 2026-04-16 PM with CPQ workstream), pending client review
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
- **First-time integrations** (HelloSpoke): Rev IO (telecom billing) and QuickBooks (revenue actuals) are both first-time for Sayer. Applied American Bedding's NetSuite pattern (40-60 hrs for unfamiliar API). Rev IO: REST API + Basic Auth, no native HubSpot app, sandbox available but webhooks don't work in sandbox — plan for production cutover testing. QuickBooks: native HubSpot integration exists but is one-way only, no company sync, only 3 custom fields visible — insufficient for revenue actuals use case; custom build with OAuth2 required. For future scopes with unfamiliar billing/accounting APIs: budget 20-44 hrs per integration including API discovery phase.
- **Integration chain dependencies** (HelloSpoke): When 3+ systems form a data chain (Rev IO → HubSpot → QuotaPath + QuickBooks), the custom object design in HubSpot is the linchpin. Get the HubSpot data model wrong and all downstream integrations break. Budget extra hours for data architecture design before building connectors. The chain also means integration workstreams can't fully parallelize — build in dependency sequencing.
- **Salesforce migration with tool consolidation** (HelloSpoke): When a client is migrating from Salesforce AND consolidating multiple tools (ClickUp, Calendly, DocuSign, Zendesk, QuickBooks), scope the migration separately from the consolidation. Client will naturally request adjacent tools mid-project — explicit exclusions in the proposal prevent scope creep. Jeremy self-de-scoped Elastic/ALN and ClickUp in discovery; document client's own words as the scope boundary.
- **CPQ is distinct from commission tracking** (HelloSpoke): Commission-tracking tools (QuotaPath, CaptivateIQ, Spiff) are NOT CPQ. They ingest commission-qualifying events from upstream systems; they do not configure products, generate quotes, or collect signatures. Do not bundle CPQ scope under commission tooling in proposals. When a client mentions "we're also looking at QuotaPath," that's NOT a signal CPQ is covered -- always confirm by asking: (1) who creates quotes today, (2) what signature tool is in play, (3) are there bulk/complex quoting patterns. HelloSpoke's original proposal combined them (D4) and had to be re-scoped same day when transcript re-read revealed Jeremy and Billy's clear CPQ requirements. +34 median hrs ($7K pricing delta) were at stake. For future scopes: if discovery mentions any of {quote templates, product catalog, line items, signature tool, DocuSign/PandaDoc, pricing approval}, CPQ is a separate workstream -- full stop.
- **HubSpot CPQ native (with AI) premium** (HelloSpoke): First Sayer HubSpot AI CPQ build. Client is actively testing the AI CPQ features -- stability unproven in production. Scoped at 28/38/52 hrs covering product library (50 SKUs), dual dynamic quote templates with product-driven T&Cs, bulk line-item import (up to 300 lines -- uncommon scale from multifamily property management), parent-child auto-creation with dedup, 2-tier approval workflow, native e-sig migration, and close-won amount sync. PandaDoc as change-order fallback if HubSpot CPQ AI falls short during build. Track actuals carefully -- this is the baseline for future HubSpot CPQ scopes. Compare to American Bedding's hybrid HubSpot/Railway CPQ (168-270 hrs) which has far heavier custom dev (weight calc engine, multi-carrier freight, NetSuite integration); HelloSpoke's CPQ is pure HubSpot-native with integration feeds, so sits in lower band.
- **Middleware architecture** (American Bedding): ~~n8n as integration middleware between 3+ systems~~ -- REVISED. Production deliverables must be standalone code, not n8n-dependent. Hybrid architecture selected: HubSpot custom code actions for lightweight triggers, Railway-hosted API for heavy orchestration (weight calc, multi-carrier freight, NetSuite integration). n8n acceptable for prototyping only. Architecture shift added 36-64 hrs but delivered a production-grade, testable codebase. Two-phase pricing (V1 HubSpot-native, V2 Railway hardening) absorbs the cost increase while reducing sticker shock. First hybrid HubSpot/Railway project -- track actuals carefully.

---

## How to Use This File

1. **Before scoping:** Read this file. Check if the new client resembles any baselined project (industry, system, size, complexity).
2. **During scoping:** Note any decisions or adjustments in the client's `_decisions.md` file.
3. **After scoping:** Add a new Project Baseline entry above with estimated data.
4. **After project closes:** Run the conversational retro, record actuals, and extract new Estimation Adjustments.
