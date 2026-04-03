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

### D3: n8n as middleware over HubSpot custom code actions
- **Category:** approach
- **Decision:** Use n8n as the integration middleware layer for all NetSuite and Kuebix API orchestration. Recommend Ops Hub Professional for simpler HubSpot-native automations.
- **Alternatives considered:** HubSpot custom code actions (Ops Hub Pro) as primary middleware -- rejected due to 20-second execution limit and 128MB memory cap, which may not accommodate multi-carrier Kuebix rate calls + weight calculations; Celigo/Commercient connectors -- rejected, don't handle custom CPQ logic or Kuebix integration; Zapier -- rejected, less capable than n8n for complex orchestration
- **Rationale:** n8n is Kyle's primary automation tool with deep expertise. No execution time limits. Full access to all three APIs (HubSpot, NetSuite REST, Kuebix). Visual workflow debugging. Self-hosted = no per-operation costs at 65 quotes/week volume.
- **Assumption:** n8n instance is available (Sayer-hosted or client infrastructure TBD)
- **Invalidation trigger:** Client refuses external middleware and insists on HubSpot-native only
- **Estimate impact:** No net hour change vs. Ops Hub custom code, but significantly reduces risk of execution timeouts
- **Calibration source:** none -- first n8n-as-middleware CPQ project
- **Confidence:** high

### D4: Dynamic weight calculation (replicate Excel formulas in n8n)
- **Category:** approach
- **Decision:** Replicate Excel shipping calculator logic in n8n to dynamically calculate weight/volume for any product configuration, rather than pre-calculating and storing weight per SKU.
- **Alternatives considered:** Pre-calculated weights stored as product properties -- rejected per Kyle; handles standard SKUs but fails for custom orders (non-standard sizes) that Caleb says are common; Hybrid approach (pre-calc for standard, dynamic for custom) -- adds maintenance burden of two systems
- **Rationale:** American Bedding has 5 product-line calculators (Dorm, Camp, Dura-Last, Vinyl covers, SoFlux covers) with nested IF formulas calculating weight from foam density, cover material, innerspring type, dimensions, and packaging. Customers frequently request custom sizes. Dynamic calculation handles any configuration.
- **Assumption:** The 5 Excel files do not contain VBA macros, external data references, or circular formulas that can't be expressed as deterministic n8n logic
- **Invalidation trigger:** Excel files contain hidden complexity (VBA, external links, iterative calculations) that makes replication infeasible within budget
- **Estimate impact:** +20-30 hrs vs. pre-calculated approach. Workstream 5 (Dynamic Weight Calculation Engine) at 28-44 hrs median 36. **HIGH-RISK workstream -- get Excel files before finalizing fee.**
- **Calibration source:** none -- first dynamic weight calculation engine. No precedent in calibration system.
- **Confidence:** medium

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

### D6: Single fixed-fee pricing, not A/B options
- **Category:** pricing
- **Decision:** Present a single $34,500 fixed fee for Phase 1. No A/B option structure.
- **Alternatives considered:** A/B pricing (initial scope had A: $19,500 / B: $33,000) -- rejected because the revised scope has no natural subset that delivers standalone value. A "CPQ without freight automation" leaves reps in a fifth system (worse than today); Timeline-based options (standard vs. accelerated) -- unnecessary complexity
- **Rationale:** Unlike Strive where Option A (CRM foundation) and Option B (full overhaul) were genuinely distinct deliverables, the revised American Bedding scope IS the CPQ integration. Freight automation via Kuebix is inseparable from the quoting workflow -- without it, reps still manually look up shipping, which is the #1 pain point. The initial A/B scope made sense when Cubics was at 45% confidence; now that Kuebix API is fully reviewed, the integration is core scope.
- **Assumption:** Client is prepared for investment above Billy's $25K verbal benchmark
- **Invalidation trigger:** Client pushback on $34.5K forces scope reduction
- **Estimate impact:** No hour change -- pricing strategy only. $34,500 vs. initial Option B at $33,000 (+$1,500 for Sayer doing NetSuite work and dynamic weight calc)
- **Calibration source:** Strive Global -- A/B works for naturally separable phases, not here
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

### D10: Fixed fee at $34,500 with value-based justification
- **Category:** pricing
- **Decision:** Price Phase 1 at $34,500 fixed fee. Frame against value delivered, not hours consumed.
- **Alternatives considered:** $25,000 (Billy's verbal benchmark) -- predates scope expansion; $28,000 (tightened scope) -- would require cutting dynamic weight calc or single-origin assumption; $33,000 (initial Option B) -- didn't include Sayer doing NetSuite or dynamic weight calc; $40,000+ -- exceeds what scope justifies
- **Rationale:** Internal estimate: 168-284 hrs (median 226) at $150/hr = median $33,900. $34,500 rounds up slightly for integration unknowns. ROI: 65 quotes/week x 20-30 min avg savings = ~$38K-$58K/year in labor savings. Payback in ~7-9 months. Billy's $25K was a pre-discovery benchmark before understanding full scope.
- **Assumption:** Client accepts value-based framing and doesn't anchor exclusively on $25K
- **Invalidation trigger:** Client has hard budget cap below $30K
- **Estimate impact:** $34,500 / $150 = 230 hrs budget -- aligns with 226 hr median with 4 hrs buffer. Tight but manageable if risks are controlled.
- **Calibration source:** Top Down Auto median was $45,600 for larger scope. American Bedding is ~75% of complexity at ~75% of price -- consistent.
- **Confidence:** medium
