# American Bedding -- Scoping Decisions

**Scoped by:** Kyle Harbuck / Claude
**Date:** April 2, 2026 (revised from initial scope same date)
**Industry:** Manufacturing (mattresses/bedding -- institutional, camps, government)
**Systems:** HubSpot Sales Hub Pro + Commerce Hub Pro, NetSuite ERP, Kuebix TMS, n8n middleware

**Revision note:** Initial scope used A/B option structure ($19,500 / $33,000) with TPI involvement and Cubics API at 45% confidence. Revised after: (1) Kyle confirmed Sayer owns all NetSuite work, (2) Kuebix API documentation fully reviewed, (3) dynamic weight calculation selected over pre-calculated approach, (4) multiple shipping origins confirmed, (5) single fixed fee selected over A/B options.

---

## Decisions Log

### D1: Phase 1 scope limited to inside sales CPQ only
- **Category:** scope-boundary
- **Decision:** Phase 1 covers inside sales quoting workflow (camps, education, institutional) only. Government RFP automation deferred to Phase 2. Customer-facing configurator deferred.
- **Alternatives considered:** Full scope with RFP automation in one phase -- rejected, RFP process is fundamentally different (written proposals, 50+ contract clauses, teaming partners) and would 2x+ the estimate; include guided selling configurator -- rejected per Kyle, Phase 1 is rep quoting only
- **Rationale:** Billy's "start small, build one brick at a time" recommendation from the Mar 16 call. Mike confirmed camps/education channel first. Government RFP has a completely different workflow (Don Reynolds manages manually in spreadsheets) that requires separate discovery. Inside sales at 65 quotes/week delivers immediate, measurable time savings.
- **Assumption:** Government sales (35% of revenue) can continue on current manual process during Phase 1 without business disruption
- **Invalidation trigger:** Client insists government RFP automation is urgent or a regulatory requirement forces timeline
- **Estimate impact:** Reduces scope from ~400+ hrs to 168-284 hrs. Phase 2 will be scoped separately.
- **Calibration source:** Strive Global -- phased approach validated for complex engagements
- **Confidence:** high

### D2: Sayer owns all development including NetSuite
- **Category:** approach
- **Decision:** Sayer handles HubSpot, NetSuite, and middleware development. TPI (NetSuite implementation partner) is not involved in this engagement.
- **Alternatives considered:** TPI handles NetSuite-side work (SuiteScript, OAuth setup, UserEvent scripts) -- rejected per Kyle's direction; Sayer specs requirements and TPI implements -- rejected, adds coordination overhead and timeline risk
- **Rationale:** Kyle confirmed Sayer does everything. This gives Sayer full control over timeline and integration architecture. TPI's involvement would add a coordination dependency and potential scheduling conflicts given their ongoing NetSuite stabilization work.
- **Assumption:** American Bedding provides NetSuite admin access with sufficient permissions for API integration, SuiteQL queries, and integration record creation
- **Invalidation trigger:** NetSuite admin access is restricted or TPI has locked down the environment in a way that requires their involvement
- **Estimate impact:** +40-60 hrs vs. TPI handling NetSuite side. Absorbed into workstreams 2 and 3. Significant change from initial scope where TPI involvement was assumed.
- **Calibration source:** Top Down Auto -- ERP involvement adds 1.5-2x complexity multiplier
- **Confidence:** high

### D3: Hybrid architecture -- HubSpot custom code + Railway API (revised from n8n)
- **Category:** approach
- **Decision:** ~~Use n8n as the integration middleware layer~~ -- **REVISED (2026-04-04).** Production deliverable must be standalone code, not dependent on n8n. Two-tier hybrid architecture: HubSpot custom code actions for lightweight triggers and simple logic, Railway-hosted API for heavy orchestration (weight calculation, Kuebix multi-carrier calls, NetSuite integration). n8n may be used for prototyping/validation during development but is not the production runtime.
- **Alternatives considered:** n8n as production middleware -- rejected, creates runtime dependency on n8n platform for a 65-quote/week operation; HubSpot custom code only -- risky, 20-second timeout may not accommodate weight calc + Kuebix API + NetSuite write-back in a single execution; Railway only -- possible but loses HubSpot-native workflow triggers; Celigo/Commercient -- rejected, don't handle custom CPQ logic
- **Rationale:** Production code must be version-controlled, testable, and maintainable by any developer -- not tied to a specific workflow platform. Railway provides unlimited execution time for complex orchestration. HubSpot custom code handles simple in-workflow logic (discount calc, tax, triggers). Hybrid splits work at the natural complexity boundary.
- **Assumption:** Railway hosting available (~$5-20/mo). HubSpot Ops Hub Professional for custom code actions.
- **Invalidation trigger:** Railway becomes unavailable or client requires all logic inside HubSpot
- **Estimate impact:** +36-64 hrs vs. original n8n approach. Absorbed into two-phase structure (see D11).
- **Calibration source:** none -- first hybrid HubSpot + Railway architecture. Track actuals carefully.
- **Confidence:** high

### D4: Dynamic weight calculation with composition architecture
- **Category:** approach
- **Decision:** Replicate Excel shipping calculator logic as a composition of shared utilities + per-product modules, rather than pre-calculating and storing weight per SKU or using a single template across products.
- **Alternatives considered:** Pre-calculated weights stored as product properties -- rejected per Kyle; handles standard SKUs but fails for custom orders (non-standard sizes) that Caleb says are common; Hybrid approach (pre-calc for standard, dynamic for custom) -- adds maintenance burden of two systems; Single template for all products -- rejected after validation revealed each product has unique physics (different core materials, different component sets, different seam allowances)
- **Rationale:** Each of the 5 product lines represents a physically different product with different materials and construction. Dorm has innerspring + foam + batting + cover (most components). Camp has foam core with 4 density series + fire barrier. Dura-Last has poly fiber fill (single material). SoFlux/Vinyl are covers only (no core). A single template would force shared assumptions that don't hold. Composition architecture: shared utilities (fabric area calc, cube volume, cover material weights, packaging logic) composed by per-product modules that add their own unique weight drivers.
- **Assumption:** ~~The 5 Excel files do not contain VBA macros, external data references, or circular formulas~~ -- **VALIDATED (2026-04-04).** All 5 Excel files received from Caleb and analyzed. Confirmed: no VBA macros, no external data references, no circular formulas. All logic is deterministic nested IF/AND formulas expressible in n8n.
- **Invalidation trigger:** ~~Excel files contain hidden complexity (VBA, external links, iterative calculations) that makes replication infeasible within budget~~ -- **TESTED (2026-04-04): trigger did NOT fire.** Files contain nested IF/AND formulas only. Dorm Mattress is the primary complexity driver (9-level nesting, 180+ calculation paths: 3 construction types x 5 foam options x 4 batting options x 3 covers). Remaining risk: Dorm Mattress notes reference "#VALUE! errors" and "Special Case Check with Delbert" -- undocumented business logic requiring client clarification at kickoff.
- **Estimate impact:** +20-30 hrs vs. pre-calculated approach. Workstream 5 (Dynamic Weight Calculation Engine) at 28-44 hrs median 36 (published). Validated estimate: 30-41 hrs (median ~35). Published range retained since validated range falls within it. Dorm Mattress accounts for ~40% of workstream hours. SoFlux OX and Vinyl Cover share ~80% code reuse.
- **Build constraint:** Each product module must be validated cell-by-cell against its own Excel file. Do NOT derive formulas by analogy from another product -- reverse-engineering confirmed that seam allowances, packaging dimensions, and construction constants differ across products even when the formula structure looks similar (e.g., Camp vs. Dura-Last use different seam offsets for cover weight calc despite identical formula shapes). Intermediate calculation rows may appear duplicated in Excel (e.g., Camp shows "Barrier Wt." and "Fire Barrier Wt." as separate rows with identical values -- only one is summed into the total).
- **Calibration source:** First validated dynamic weight calculation engine. Per-calculator complexity: Dorm (HIGH -- 9-level nesting, 180+ paths, innerspring/foam/batting), Camp (MEDIUM -- 2-3 level nesting, 48 paths, foam series + fire barrier), Dura-Last (LOW-MEDIUM -- 2-level nesting, 12 paths, poly fiber only), SoFlux OX (LOW -- linear, covers only), Vinyl (LOW -- ~95% shared base with SoFlux). Architecture: composition pattern with shared utilities, not a single template -- each product has unique physics.
- **Confidence:** high

### D5: Recommend Operations Hub Professional
- **Category:** tier
- **Decision:** Recommend American Bedding add Operations Hub Professional for workflow custom code actions, data quality automation, and programmable automation.
- **Alternatives considered:** Skip Ops Hub -- limits automation to basic workflow actions; Ops Hub Starter -- doesn't include custom code actions
- **Rationale:** Ops Hub Pro enables custom code actions in workflows (JavaScript/Python within HubSpot), data quality automation for incoming product data, and programmable automation for tax/discount calculations. While n8n handles the heavy integration work, Ops Hub Pro handles in-HubSpot logic. ~$800/mo additional license cost.
- **Assumption:** Additional ~$800/mo license cost is acceptable to client
- **Invalidation trigger:** Client declines the additional HubSpot spend; all automation routes through n8n instead
- **Estimate impact:** No hour change -- reduces risk and simplifies some workstreams
- **Calibration source:** Strive Global -- Enterprise tier capabilities were underutilized; explicit tier recommendation prevents this
- **Confidence:** medium

### D6: Two-phase pricing (revised from single fixed fee)
- **Category:** pricing
- **Decision:** ~~Present a single $34,500 fixed fee~~ -- **REVISED (2026-04-04).** Two-phase pricing: Phase 1 (V1) at ~$30,000, Phase 2 (V2) at ~$11,500. Total ~$41,500. Reduces sticker shock vs. a single $41-42K fee.
- **Alternatives considered:** Single $34,500 fixed fee -- no longer viable, architecture shift from n8n to hybrid HubSpot/Railway adds 36-64 hrs; single $41,500 fee -- sticker shock against $25K verbal anchor; A/B options (original) -- still rejected, CPQ without freight has no standalone value
- **Rationale:** The two-phase split follows a natural maturity boundary, not an artificial scope cut. Phase 1 (V1) delivers a working HubSpot-native CPQ -- reps start quoting in HubSpot immediately. Phase 2 (V2) migrates the heavy orchestration to a Railway production platform for scalability and maintainability. Unlike the original A/B rejection (where Option A left reps in a fifth system), Phase 1 here delivers full standalone value with known limitations (HubSpot timeout risk on complex multi-line quotes). Phase 2 eliminates those limitations.
- **Assumption:** Client commits to Phase 2 after seeing Phase 1 value. Phase 1 at ~$30K is close enough to Billy's $25K anchor to negotiate.
- **Invalidation trigger:** Client has hard budget cap below $25K for Phase 1
- **Estimate impact:** Phase 1: 168-240 hrs (median ~200) at ~$30,000. Phase 2: 60-90 hrs (median ~75) at ~$11,500. Total: 228-330 hrs / ~$41,500.
- **Calibration source:** Strive Global -- phased "start A, plan B" approach validated. American Bedding original A/B rejection still holds (scope cut ≠ maturity phasing).
- **Confidence:** high

### D7: Flat product catalog in HubSpot (one SKU per combination)
- **Category:** approach
- **Decision:** Maintain a flat product catalog in HubSpot with one product record per SKU. Use custom properties (size, cover_type, foam_density, construction_type) for filtering. No product variant system.
- **Alternatives considered:** Third-party CPQ tool with native variants (DealHub, PandaDoc CPQ) -- adds another system and license cost; Custom variant logic -- over-engineering for 700 SKUs where only 40-60 are commonly used
- **Rationale:** HubSpot has no native product variant system. Product library supports 100K products. Custom properties enable filtered selection. 80/20 rule applies -- 40-60 core products handle 80% of quotes. Custom orders create standalone line items.
- **Assumption:** 700 SKUs is manageable in HubSpot product library
- **Invalidation trigger:** SKU count grows beyond manageability or product attribute combinations grow exponentially
- **Estimate impact:** No change -- this is the simplest viable approach
- **Calibration source:** none -- first product catalog migration of this type
- **Confidence:** high

### D8: Kuebix quickRate API for automated LTL freight
- **Category:** approach
- **Decision:** Use Kuebix POST /action/quickRate endpoint for multi-carrier LTL rate shopping. Auto-select cheapest quote and write as freight line item on HubSpot quote. Manual override available.
- **Alternatives considered:** Static freight rate table in HubSpot -- doesn't account for carrier rate changes or fuel surcharges; Manual Kuebix entry continues -- this is the core pain point; Kuebix createAndBook -- appropriate only after quote acceptance, not during quoting
- **Rationale:** Kuebix API fully reviewed (OpenAPI 3.0.2 spec). Single POST returns quotes from all configured carriers simultaneously. Basic Auth is simple to implement in n8n. Required fields (origin address, destination address, weight, freight class, handling units) map cleanly to HubSpot data. `persist: false` prevents phantom shipments during quoting. **Confidence upgraded from 45% (initial "Cubics" scope) to HIGH after full API documentation review.**
- **Assumption:** American Bedding provides Kuebix API credentials (username, API key, 15-char Client ID). Rate limits sufficient for 65 quotes/week.
- **Invalidation trigger:** Kuebix credentials not available or API imposes restrictive rate limits
- **Estimate impact:** Workstream 4 at 22-38 hrs (median 30) includes origin routing for multiple warehouses. Initial scope was 16-40 hrs at 45% confidence -- revised range is tighter with higher confidence.
- **Calibration source:** none -- first TMS/freight API integration
- **Confidence:** high

### D9: NetSuite OAuth 2.0 M2M + SuiteQL for data access
- **Category:** approach
- **Decision:** Use NetSuite REST API with OAuth 2.0 Machine-to-Machine authentication. Use SuiteQL for product catalog queries and price list extraction.
- **Alternatives considered:** Token-Based Authentication (TBA) -- still supported but Oracle pushing OAuth 2.0 for new integrations; SOAP/SuiteTalk -- deprecated with 2027.1 EOL; SuiteScript RESTlets -- more complex to deploy; Third-party connector (Celigo) -- doesn't handle custom CPQ flows
- **Rationale:** American Bedding's NetSuite is new (Jan 1, 2026), so start with Oracle's recommended modern pattern. SuiteQL provides SQL-like query access. REST API has full CRUD for estimates and sales orders. OAuth 2.0 M2M doesn't require user interaction for token refresh.
- **Assumption:** NetSuite admin can create OAuth 2.0 M2M integration record
- **Invalidation trigger:** NetSuite instance has REST API disabled or TPI has locked down integration capabilities
- **Estimate impact:** OAuth 2.0 setup is ~2-4 hrs. SuiteQL queries efficient -- catalog extraction in 1-2 API calls.
- **Calibration source:** Top Down Auto -- NetSuite integration scoped at 28 hrs median for read-only. This project adds write-back so 22-40 hrs range.
- **Confidence:** high

### D10: ~~Fixed fee at $34,500~~ Superseded by D6 revision and D11
- **Category:** pricing
- **Decision:** ~~Price Phase 1 at $34,500 fixed fee~~ -- **SUPERSEDED (2026-04-04).** Architecture shift from n8n to hybrid HubSpot/Railway changed the cost basis. See D6 (revised) and D11 for current pricing: Phase 1 ~$30,000, Phase 2 ~$11,500.
- **Original rationale (preserved for calibration):** Internal estimate: 168-284 hrs (median 226) at $150/hr = median $33,900. $34,500 rounded up for integration unknowns. ROI: 65 quotes/week x 20-30 min avg savings = ~$38K-$58K/year. Payback ~7-9 months. Billy's $25K was a pre-discovery benchmark.
- **Confidence:** superseded

### D11: Two-phase architecture -- V1 HubSpot-native, V2 Railway production platform
- **Category:** approach + pricing
- **Decision:** Split the engagement into two phases along a maturity boundary. Phase 1 (V1) delivers a working HubSpot-native CPQ using custom code actions -- reps start quoting in HubSpot. Phase 2 (V2) migrates heavy orchestration (weight engine, Kuebix freight, NetSuite integration) to a Railway-hosted production API with proper codebase, unit tests, and CI/CD.
- **Alternatives considered:** Single-phase delivery with Railway from day one -- higher upfront cost (~$41.5K single fee), sticker shock against $25K verbal anchor; n8n as production middleware -- rejected, creates platform dependency (see D3 revision); HubSpot custom code only (no Railway) -- risky at 65 quotes/week with multi-line orders hitting 20s timeout
- **Rationale:** Phase 1 delivers immediate value: reps move from 4-system quoting to HubSpot. Known limitation is HubSpot's 20s execution timeout for complex multi-line quotes -- manageable with manual fallback. Phase 2 eliminates that limitation by moving heavy logic to Railway (unlimited execution time, proper error handling, retry logic). This is a maturity boundary, not a scope cut -- both phases deliver the same functionality, V2 makes it production-grade and scalable. Reduces sticker shock: ~$30K Phase 1 is closer to Billy's $25K anchor than ~$41.5K all-in.
- **Phase 1 (V1) scope:**
  - HubSpot CPQ architecture and configuration
  - Product catalog sync (initial load + HubSpot custom code sync)
  - Weight calculation engine in HubSpot custom code actions
  - Kuebix freight integration via HubSpot custom code
  - NetSuite quote-to-order via HubSpot custom code
  - Quote templates, discount/tax/terms, training, testing, PM
  - Known limitation: complex multi-line quotes may hit 20s timeout; manual fallback for edge cases
- **Phase 2 (V2) scope:**
  - Railway project setup (CI/CD, env config, monitoring, logging)
  - Migrate weight engine to Railway API with unit test coverage
  - Migrate Kuebix orchestration to Railway (multi-line, multi-carrier without timeout)
  - Migrate NetSuite integration to Railway (proper OAuth token management, retry logic)
  - Automated catalog sync (Railway cron)
  - Eliminate all HubSpot timeout constraints
- **Assumption:** Railway hosting available (~$5-20/mo). Phase 2 starts after Phase 1 go-live. Client sees Phase 1 value before committing Phase 2.
- **Invalidation trigger:** Client requires all logic inside HubSpot (no external services) -- would need to accept timeout limitations
- **Estimate impact:** Phase 1: 168-240 hrs (median ~200) / ~$30,000. Phase 2: 60-90 hrs (median ~75) / ~$11,500. Total: 228-330 hrs / ~$41,500.
- **Calibration source:** Strive Global validated "start A, plan B" phasing. American Bedding original A/B rejection (D6 original) still holds -- scope cut ≠ maturity phasing. First hybrid HubSpot/Railway architecture.
- **Confidence:** high
