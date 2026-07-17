# Scoping Calibration Data

Claude MUST read this file before generating any new scoping estimate. Use these patterns
to adjust baseline hour ranges from the scoping skill.

> **Privacy note:** Project baselines below are anonymized to firm-type labels (Client A, B, …).
> Identifying client names, individuals, and company-specific tells are intentionally omitted so
> this learning data can live in a team-shared repo. Raw client records live outside this repo.

---

## Estimation Adjustments

Adjustments derived from completed projects. Each entry includes the source project and
the specific lesson. These override the scoping skill's default ranges when applicable.

*No completed projects with actuals yet. Adjustments will be added as retros are completed.*

---

## Project Baselines

Estimated data from scoped projects. When a project closes and actuals are recorded,
add an "Actuals" section and move learnings into Estimation Adjustments above.

### Client A — PE / Real Estate
- **System:** HubSpot Sales Hub Professional
- **Size:** 5 paid users, <1,000 contacts, 2 pipelines
- **Median estimate:** 121 hrs / $18,150
- **Range:** 86-156 hrs / $12,900-$23,400
- **Approach:** Single-phase, 6-8 weeks
- **Verbal quote given:** $15,000-$30,000 (EL on call)
- **Notable factors:** FINRA compliance (no call recording), PE firm parent-child structures, close personal relationship (scope creep risk flagged), budget gatekeeper not in discovery
- **Status:** Pending SOW delivery
- **Actuals:** Not yet completed

### Client B — PE / Real Estate Investment
- **System:** HubSpot CRM (Sales Hub Starter or Smart CRM)
- **Size:** 10 users, 4 offices, 2,000-5,000 contacts
- **Fixed fee proposed:** $26,075
- **Approach:** 3-phase, 6-8 weeks
- **Notable factors:** Prior CRM abandonment after 2 months (adoption risk), wide age range (varying tech comfort), Google Workspace + Fireflies integration, PE firm with multi-office structure
- **Status:** Proposal delivered
- **Actuals:** Not yet completed

### Client C — Automotive / Manufacturing
- **System:** HubSpot Sales Hub Professional + NetSuite ERP integration
- **Size:** 6-10 sales/CSR users, multi-brand/subsidiary
- **Median estimate:** 304 hrs / $45,600
- **Range:** 192-434 hrs / $28,800-$65,100
- **Approach:** Phased -- CRM first (6-8 wks), then ERP integration (6-10 wks)
- **Notable factors:** Legacy ERP data extraction risk, NetSuite multi-subsidiary, product catalog digitization, 22 open ERP questions, ERP complexity premium applied
- **Status:** Pending follow-up call for ERP clarification
- **Actuals:** Not yet completed

### Client D — Insurance / Pet Wellness
- **System:** HubSpot Sales Hub Enterprise (reconfiguration)
- **Size:** 23 users, existing HubSpot instance with 10 years of data
- **Option A median:** 119 hrs / $17,850 (CRM Foundation only)
- **Option B median:** 216 hrs / $32,400 (Full CRM Overhaul)
- **Range A:** 86-156 hrs | **Range B:** 160-280 hrs
- **Approach:** Recommended Option A first, Option B as Phase 2
- **Notable factors:** 10 years of uncoded contact data (HIGH risk), pipeline under-reporting from LinkedIn usage, AI enrichment pilot proposed (500 records), CPQ complexity with multiple pricing models, prior insurance-vertical engagement used as historical reference
- **Status:** Proposal in progress
- **Actuals:** Not yet completed

### Client E — VoIP / Multifamily Property Management
- **System:** HubSpot Sales Hub Professional + Salesforce migration + telecom-billing/accounting/comp integrations + project-mgmt↔HubSpot onboarding integration (Tier B architecture)
- **Size:** 15-18 users, single entity, multifamily real estate VoIP
- **Median estimate:** 266 hrs / $39,900 (revised)
- **Range:** 190-360 hrs / $28,500-$54,000
- **Approach:** Concurrent 4-phase, 12-16 weeks
- **Notable factors:** Salesforce contract expiration = hard deadline. Deal stage Decision Maker Bought-In when scope refined. Client lead's 45-50% discount joke signals pricing pressure. Broken legacy project-mgmt↔Salesforce integration explicitly excluded. **First project-mgmt-tool integration** — Tier B (HubSpot form + middleware + native integration) targets 28-36 hrs (median 32). Mandatory field gating flagged as process redesign scope creep, priced as optional add-on (8-14 hrs). Scope refinement pattern: originally the project-mgmt-to-HubSpot sync was OUT OF SCOPE; moved in-scope after a call commitment and ops discovery specification.
- **Status:** Revised proposal pending delivery
- **Actuals:** Not yet completed

### Client F — Manufacturing / Custom Doors (ADD-ON SCOPE)
- **System:** HubSpot Service Hub (existing portal -- ticket pipeline add-on) + VoIP (assessment only, no build)
- **Size:** ~1.5 customer support agents, 3 ticket-pipeline manipulators, 7 VoIP seats (future)
- **Median estimate:** 60 hrs / $9,500 single fixed fee
- **Range:** 46-74 hrs / $7,245-$11,655 (with 5% Sayer tech fee bundled)
- **Approach:** Single-phase add-on, kicks off after current CRM go-live + 1-2 wk settle period
- **Notable factors:** **First ticket-pipeline-only add-on baseline in Sayer history** -- no prior ticket-only scope in calibration set. Add-on to active CRM build (going live shortly). Ticket pipeline replicates an existing Google Sheet (issue type, doors, reason, ERD date, priority, status, resolution, cost, replacement PO). VoIP integration flagged as obscure on call -- scoped as TIME-BOXED ASSESSMENT + WRITTEN MEMO ONLY (8-14 hrs WS-07), not a build. Memo deliverable presents Phase 2 path: custom build IF API supports, OR migration recommendation to a mainstream VoIP provider. Knowledge base explicitly back-burnered post-ERP. Customer ID data quality gap surfaced on training call. 5% Sayer tech fee bundled into single fixed fee for clean budget instrument (sponsor needs one number for internal approvers). Existing engagement contract structure (MSA / change order vs add-on SOW) TBD before send.
- **Status:** Scope deliverables drafted, awaiting review and client send
- **Actuals:** Not yet completed

### Client G — Manufacturing / CPQ
- **System:** HubSpot CPQ (Sales Hub Pro + Commerce Hub Pro) + NetSuite ERP + TMS + middleware
- **Size:** 3-5 sales users, 700 SKUs (40-60 core), 65+ quotes/week, multiple shipping warehouses
- **Phase 1 (V1) estimate:** 168-270 hrs (median ~219) / ~$30,000 fixed fee
- **Phase 2 (V2) estimate:** 56-90 hrs (median ~73) / ~$11,500 fixed fee
- **Total:** 224-360 hrs (median ~292) / ~$41,500
- **Approach:** Two-phase -- Phase 1 HubSpot-native CPQ (10-12 weeks), Phase 2 production platform (4-6 weeks)
- **Verbal quote given:** $25,000 (EL on intro call, pre-discovery benchmark)
- **Notable factors:** Sayer owns all development including NetSuite (no third-party integrator). Dynamic weight calculation engine replicates 5 Excel spreadsheets (HIGHEST-COMPLEXITY workstream -- 28-44 hrs, validated). Excel files: no VBA, no external refs, no circular formulas. Primary driver product has 9-level nesting, 180+ paths. Two secondary products share ~80% code reuse. Remaining unknown: one special-case calculation needs SME confirmation. TMS API fully reviewed (rate endpoint, Basic Auth, multi-carrier LTL). Multiple shipping origins with routing logic. Architecture shifted from middleware to hybrid HubSpot custom code + hosted production API -- production deliverables must be standalone code. Two-phase structure: V1 (HubSpot-native) then V2 (production hardening). Ops Hub Pro required (~$800/mo). Hosting (~$5-20/mo). Government RFP excluded (future phase). Client is a PE portfolio company; CFO is budget authority. Pricing evolved: A/B options ($19.5K/$33K) -> single fee ($34.5K) -> two-phase ($30K + $11.5K) as architecture changed.
- **Status:** Proposal in progress. Pre-engagement gate cleared. Architecture revised to hybrid HubSpot/hosted-API.
- **Actuals:** Not yet completed

### Client H — Electrical Products Distribution / Manufacturer's Rep (CRM + Native CPQ)
- **System:** HubSpot Revenue Hub Enterprise (CRM + native CPQ/Quotes + Product Library). ERP/accounting system integration **explicitly OUT OF SCOPE** (deferred to a future SOW).
- **Size:** 9 CRM seats future-state (6 today: President, VP-Sales, 4 Inside Sales); ~1,951 distributor/customer accounts across 56 states; ~20 external manufacturer's reps (not seats). Sells *through* reps *to* electrical distributors; does not track end customers.
- **Phase 2 (implementation) estimate:** 148–290 hrs (median 211) / **$22,200–$43,500 (median $31,650)** fixed fee at $150/hr blended.
- **Approach:** Single combined Phase 2 package, phased for delivery (Foundation → Migration → CPQ → Reporting → Adoption + PM). Native HubSpot CPQ only. Follows a signed Phase 1 discovery T&M engagement (MD-led, $275/$250 rates — distinct from the $150/hr implementation blend).
- **Notable factors:** **First native-CPQ baseline with ERP integration deliberately excluded** — the ~1.5–2x ERP multiplier (Client C) and the +40–60 hr consultant-owned-ERP premium (Client G) were intentionally NOT applied, which is what holds the median (211 hrs) below Client C (304) and Client G (292). Enterprise tier justified by custom-object model (Manufacturer's-Rep object + Distributor-as-Company) + territory-based teams/permissions + quote approvals — **structural drivers, not the 9-seat headcount**. Migration is a single CLEAN Excel export (~1,951 rows) kept in the Medium band (not Large) despite volume, because data quality is clean; salesperson/territory code maps to ~20 rep territories and drives ownership/routing. Confidential distributor pricing = field-level/team permissions (HIGH-severity risk). Adoption risk HIGH (net-new CRM for a spreadsheet/ERP shop, cf. Client B abandonment). Activities/quotes start fresh — no reconstruction from mailboxes/quote logs/printed quotes. License is client-procured (not in Sayer fee). CRM-only portion (~$25,050) lands next to Client B's 10-user $26,075.
- **Status:** Scoped (post-discovery, first implementation estimate). Open: verify Enterprise bundle includes Commerce Hub for native CPQ; confirm seat provisioning timing; ERP-integration feasibility call pending (future SOW).
- **Actuals:** Not yet completed

---

## Cross-Project Patterns

Patterns observed across multiple scoping sessions. Updated as more projects complete.

- **PE firms** (Client A, Client B): Parent-child company structures are always needed. Budget ~8-11 hrs for contact/company management. FINRA compliance adds constraints (no call recording, manual NDA tracking). Budget gatekeepers often absent from discovery -- flag this risk every time.
- **Existing HubSpot instances** (Client D): Reconfiguration scoping is harder than greenfield. Assume data quality work will hit max estimate. Always audit before committing hours.
- **ERP involvement** (Client C): The scoping skill's 1.5-2x multiplier held up. 22 open questions after discovery = too many unknowns for fixed-fee. Recommend phased with ERP in Phase 2.
- **Verbal quotes from EL** (Client A): Estimates should land in lower-middle of verbal range to leave buffer. Track verbal quotes alongside formal estimates.
- **Multi-option proposals** (Client D): Offering A/B options with "start A, plan B" recommendation works well when phases are naturally separable. Client G was initially scoped as A/B but revised to single fee when no natural standalone subset existed (CPQ without freight automation leaves reps in a fifth system). A/B works when Option A delivers standalone value; it fails when the core problem requires all components.
- **Manufacturing/CPQ** (Client G): Freight/TMS integration is a unique complexity factor not covered by standard scoping skill ranges. The TMS rate API is well-documented and straightforward once credentials are obtained. Dynamic weight calculation from Excel spreadsheets is the real risk -- nested IF/AND formulas with product-specific logic paths. Always get the Excel files and validate complexity BEFORE committing a fixed fee. Desktop Excel spreadsheets as data source = data centralization is a prerequisite workstream. **VALIDATED:** Excel analysis confirmed nested IF/AND formulas only -- no VBA, no external refs, no circular formulas. Complexity ranged from simple linear calcs (~80% code reuse between two products) to 9-level nested IFs with 180+ calculation paths. The pre-engagement gate pattern works: getting files early converted the highest-risk workstream from "medium confidence" to "high confidence" without changing the fee. Future manufacturing/CPQ scopes: budget complexity by product line, not uniformly across all calculators.
- **ERP adjacency vs. ERP build** (Client C, Client G): When ERP is already live with working sync, use 1.25x adjacency premium instead of full 1.5-2x. The full multiplier is for greenfield ERP implementations with unresolved data questions. However, when consultant (not the ERP partner) owns NetSuite development, add 40-60 hrs for direct API work including OAuth setup, SuiteQL, and estimate/sales order creation.
- **Middleware architecture** (Client G): ~~middleware between 3+ systems~~ -- REVISED. Production deliverables must be standalone code, not middleware-dependent. Hybrid architecture selected: HubSpot custom code actions for lightweight triggers, hosted API for heavy orchestration (weight calc, multi-carrier freight, NetSuite integration). Low-code tools acceptable for prototyping only. Architecture shift added 36-64 hrs but delivered a production-grade, testable codebase. Two-phase pricing (V1 HubSpot-native, V2 production hardening) absorbs the cost increase while reducing sticker shock. First hybrid HubSpot/hosted-API project -- track actuals carefully.
- **Add-on scopes to active engagements** (Client F): Add-ons to live engagements should sit meaningfully BELOW the smallest full-CRM reference in calibration history. Client F at $9,500 sits ~50% below Client A ($18,150 full CRM, 5 users) and signals "this is supplementary." Add-ons should phase to start AFTER the active engagement's go-live + 1-2 week settle period to preserve adoption momentum -- never run concurrent with training cadence. Single fixed-fee with bundled tech fee is the cleanest budget instrument when the decision-maker needs to surface one number to internal approvers. **Time-boxed integration assessments** (Client F WS-07): when an integration target is obscure or unfamiliar to Sayer, scope a 8-14 hr research + memo workstream BEFORE any build commitment. Memo deliverable presents both Phase 2 paths (build OR migrate) so client always has a forward route. This avoids the "spend 30 hrs discovering the API does not work" failure mode.
- **Native CPQ with ERP integration deferred** (Client H): When a manufacturing/distribution client wants CPQ but the ERP integration's feasibility is unconfirmed, scope **native HubSpot CPQ only** (Product Library + Quotes + approvals) and defer the ERP integration to a future SOW — do NOT apply the Client C ERP multiplier or the Client G consultant-owned-ERP premium to the CPQ hours. This keeps a 9-seat Enterprise CRM+CPQ build's median (~211 hrs / ~$31.6k) between the CRM-only reference (Client B, ~$26k) and a full CPQ+ERP build (Client G, ~$41.5k). The trade-off surfaced as a risk (manual price maintenance until integrated) rather than as scoped hours. **Enterprise tier for a small seat count** is justified by structural drivers — custom objects, territory-based teams/permissions, quote approvals — not headcount; when those drivers are present, don't down-tier to Pro just because seats are few. **Clean single-source migration exports stay in the Medium band regardless of row volume** (~1,951 rows here) — volume alone doesn't push to Large; data quality does.

---

## Pricing Negotiation Patterns

Patterns from proposals that entered a negotiation phase before signing. Read this alongside Project Baselines when a client pushes back on a delivered proposal.

### Protocol

**1. Internal BATNA alignment before any call.**
Before getting on the phone, align Kyle + Cameron + Billy on three things: (a) rate floor for this engagement, (b) which workstreams can be trimmed or deferred without gutting value, (c) whether the client qualifies as a "good logo" that justifies a relationship discount.

**2. Get off email.**
Acknowledge the feedback, signal flexibility, propose a 15-minute call. Do not negotiate price in writing — one reply email to schedule, then close on the call.

**3. Two levers: scope trim before rate cut.**
- Training/Enablement hours are almost always the first trim — they're deferrable and addable as Phase 2.
- Data QA / foundational architecture workstreams are typically non-negotiable — they protect Sayer's delivery risk.
- Cut rate only if scope trimming alone won't close. Frame any rate cut as a "relationship investment," not a correction of an overpriced proposal. Stated floor: $150/hr (Associate rate).

**4. Sandbox ≠ production argument.**
When a client self-builds integrations and says "I thought the price would drop more since we removed integrations" — the counter is: connecting and validating in a sandbox is not the same as a production go-live. Data QA / Pre-Production Audit hours don't track 1:1 with integration build hours removed. Sandbox → production issues become a Sayer liability if not explicitly audited.

**5. Billy's close pattern.**
When a client is a good logo (brand value, campfire/expansion potential), Billy gets on the call as the senior voice. Core values applied: "Win the work, not the relationship" / "Zero In > Move Fast > Win Big." First-round relationship discount is a calculated bet on future work, not a margin concession.

### Negotiation Reference (anonymized)

- **Proposal delivered:** $28,700 (164 hrs × $175/hr, already −$15K from v1 anchor)
- **Client push:** targets ~$25K via email; cites removed integrations as justification
- **Sayer response:** good logo + expansion play. Floor: $150/hr → ~$26,400. Get on a call.
- **Negotiating room:** Training/Enablement (12 hrs median) is first trim; optional add-ons already excluded. Sandbox-to-production argument defends Data QA hours.
- **Decision:** Internal BATNA + 15-min close call with Kyle + Cameron + Billy + the client

---

## How to Use This File

1. **Before scoping:** Read this file. Check if the new client resembles any baselined project (industry, system, size, complexity).
2. **During scoping:** Note any decisions or adjustments in the client's `_decisions.md` file (kept locally, outside this repo).
3. **After scoping:** Add a new Project Baseline entry above using a firm-type label — do not commit identifying client names, individuals, or company-specific tells.
4. **After project closes:** Run the conversational retro, record actuals, and extract new Estimation Adjustments.
