# American Bedding -- CPQ Scope Summary

**Date:** April 2, 2026 (revised April 4, 2026)
**Discovery Calls:** March 16, 2026 (Intro) / March 23, 2026 (Follow-up)
**Prepared by:** Harbuck Consulting / Sayer

---

**Systems in Scope:** HubSpot CPQ (Sales Hub Pro + Commerce Hub Pro + Ops Hub Pro), NetSuite ERP (integration), Kuebix TMS (freight API), Railway (production API hosting)
**Approach:** Two-phase, inside sales CPQ with automated freight and dynamic weight calculation
**Phase 1 (V1):** HubSpot-native CPQ -- 168-240 hrs (median ~200) / ~$30,000
**Phase 2 (V2):** Railway production platform -- 60-90 hrs (median ~75) / ~$11,500
**Total:** 228-330 hrs (median ~275) / ~$41,500
**Estimated Timeline:** Phase 1: 10-12 weeks | Phase 2: 4-6 weeks (after Phase 1 go-live)

**Revision history:**
- April 2, 2026 AM: Initial A/B option structure ($19,500 / $33,000) with n8n middleware and TPI involvement
- April 2, 2026 PM: Revised to single $34,500 fee after Sayer confirmed as sole developer, Kuebix API reviewed, dynamic weight calc selected, multiple ship origins confirmed
- April 4, 2026: Architecture shift from n8n to hybrid HubSpot custom code + Railway. Two-phase pricing to reduce sticker shock. Excel calculators validated (pre-engagement gate cleared).

---

## Phase 1 (V1): HubSpot-Native CPQ

**Goal:** Get reps quoting in HubSpot. Eliminate the 4-system quoting process. Deliver immediate time savings.
**Known limitation:** Complex multi-line quotes may approach HubSpot's 20-second custom code execution limit. Manual fallback available for edge cases.

| Workstream | Min | Max | Median | Notes |
|---|---|---|---|---|
| HubSpot CPQ Architecture & Configuration | 14 | 22 | 18 | Commerce Hub CPQ setup, custom properties, approval workflows, payment terms |
| Product Catalog Sync (NetSuite to HubSpot) | 20 | 32 | 26 | SuiteQL extraction of 700 SKUs, custom properties, HubSpot custom code sync trigger. Initial bulk load + incremental sync. |
| NetSuite Quote-to-Order Integration | 22 | 36 | 29 | OAuth 2.0 M2M, quote -> estimate -> sales order via HubSpot custom code, credit hold check, price level sync |
| Kuebix Freight Integration + Origin Routing | 22 | 34 | 28 | HubSpot custom code -> quickRate API, multi-carrier LTL, origin warehouse routing, manual override fallback |
| Dynamic Weight Calculation Engine | 28 | 44 | 36 | Weight calc in HubSpot custom code actions. Validated (2026-04-04): no VBA/external refs/circular formulas. Dorm (HIGH -- 9-level nesting, 180+ paths), Camp (MED), Dura-Last (MED), SoFlux OX/Vinyl (LOW, ~80% reuse). Highest-complexity workstream. |
| Quote Template Design | 12 | 20 | 16 | HubL/HTML/CSS matching NetSuite format. Line items, discounts, tax, shipping, terms, acceptance flow |
| Discount, Tax & Payment Terms Logic | 10 | 18 | 14 | 10% volume discount, state-based tax, prepay/net 10/30/60, credit hold integration. HubSpot custom code. |
| Training & Documentation | 10 | 16 | 13 | Sales (Caleb, Don) + Admin (Sarah-Beth, Patrick). Recorded sessions. Admin guide + user card. |
| Testing & QA | 14 | 24 | 19 | E2E integration testing, weight calc validation against Excel baselines, freight validation, UAT, 2-week hypercare |
| Project Management | 16 | 24 | 20 | Kickoff, weekly syncs, milestone reviews, scope creep prevention. ~10% of total. |
| **PHASE 1 TOTAL** | **168** | **270** | **219** | |

At $150/hr: $25,200 - $40,500 (median $32,850)
**Phase 1 fixed fee: ~$30,000**

---

## Phase 2 (V2): Railway Production Platform

**Goal:** Scale and harden. Migrate heavy orchestration from HubSpot custom code to a Railway-hosted API. Eliminate all timeout constraints. Deliver a production-grade, testable, version-controlled codebase.
**Prerequisite:** Phase 1 go-live and client validation of CPQ workflow.

| Workstream | Min | Max | Median | Notes |
|---|---|---|---|---|
| Railway Infrastructure Setup | 8 | 12 | 10 | Project setup, CI/CD pipeline, environment config, monitoring, logging, health checks |
| Weight Engine Migration | 10 | 16 | 13 | Migrate all 5 calculators from HubSpot custom code to Railway API. Add unit test coverage for all calculation paths. Dorm Mattress sampling strategy for 180+ paths. |
| Kuebix Freight Migration | 8 | 14 | 11 | Migrate freight orchestration to Railway. Multi-line, multi-carrier without timeout risk. Retry logic for carrier API failures. |
| NetSuite Integration Migration | 10 | 16 | 13 | Migrate OAuth token management, catalog sync (Railway cron), quote-to-order flow. Proper retry and error handling. |
| HubSpot Rewiring | 6 | 10 | 8 | Update HubSpot custom code actions to call Railway API instead of running logic locally. Thin trigger layer. |
| Integration Testing | 8 | 12 | 10 | E2E testing of Railway API + HubSpot triggers. Load testing at 65+ quotes/week. Regression against Phase 1 baseline. |
| Project Management | 6 | 10 | 8 | Milestone reviews, documentation updates. |
| **PHASE 2 TOTAL** | **56** | **90** | **73** | |

At $150/hr: $8,400 - $13,500 (median $10,950)
**Phase 2 fixed fee: ~$11,500**

---

## Combined Summary

| Phase | Min | Max | Median | Fixed Fee |
|---|---|---|---|---|
| Phase 1 (V1): HubSpot-Native CPQ | 168 | 270 | 219 | ~$30,000 |
| Phase 2 (V2): Railway Production Platform | 56 | 90 | 73 | ~$11,500 |
| **TOTAL** | **224** | **360** | **292** | **~$41,500** |

---

## Key Risks

1. **HubSpot custom code timeout** (MEDIUM severity, MEDIUM likelihood) -- Phase 1 runs weight calc + Kuebix API call in HubSpot custom code actions (20-second limit). Single-product quotes are safe. Complex multi-line quotes with multiple product lines and carriers may approach the limit. **Mitigation:** Test with largest known quote configurations. Manual fallback for edge cases. Phase 2 eliminates this risk entirely.

2. **Excel weight calculator complexity** (MEDIUM severity, LOW likelihood) -- 5 spreadsheets validated (2026-04-04): no VBA, no external refs, no circular formulas. Dorm Mattress is the primary complexity driver (9-level nested IFs, 180+ calculation paths). Remaining risk is undocumented business logic ("Special Case Check with Delbert" noted in Dorm Mattress calculator). **Mitigation:** Clarify Delbert edge cases at kickoff. Build Dorm Mattress calculator first with sampling strategy for 180+ paths. Test against known weights.

3. **NetSuite data quality** (HIGH severity, HIGH likelihood) -- SKU duplicates, missing attributes from Jan 2026 launch. **Mitigation:** Week 1 data audit via SuiteQL before building sync.

4. **Scope creep via Vesco relationship** (HIGH severity, MEDIUM likelihood) -- Government RFP enthusiasm and close personal relationships. **Mitigation:** SOW signed by budget authority (Mike/Patrick). Phase boundary iron-clad.

5. **NetSuite still stabilizing** (HIGH severity, MEDIUM likelihood) -- TPI may make changes that break integration. **Mitigation:** Build against documented REST API, not custom SuiteScript. Establish TPI change notification channel.

6. **Multiple shipping origins** (MEDIUM severity, HIGH likelihood) -- Wrong origin = wrong freight = wrong price. **Mitigation:** Map all warehouses at kickoff. Test each origin with known quotes.

---

## Assumptions

- HubSpot Sales Hub Professional + Commerce Hub Professional (existing)
- Operations Hub Professional required (custom code actions -- separate license cost ~$800/mo)
- NetSuite REST API access with OAuth 2.0 M2M credentials
- Kuebix API credentials provided by client
- Railway hosting available (~$5-20/mo for production API)
- Up to 700 products, flat catalog (one record per SKU)
- Up to 30 custom properties (overages are change orders)
- Excel calculators validated: no VBA macros, no external data references, no circular formulas (confirmed 2026-04-04)
- SOW signed by Mike Taylor or Patrick (CFO)
- All work conducted remotely
- Phase 1: 10-12 weeks | Phase 2: 4-6 weeks (starts after Phase 1 go-live)
- Production code delivered as a version-controlled codebase (not n8n workflows)

---

## Exclusions

- Government RFP automation (future phase -- separate engagement)
- Customer-facing product configurator / guided selling (future phase)
- External storefront (Shopify -- future phase)
- VoIP / call capture integration
- AI lead enrichment
- NetSuite reimplementation or new module deployment
- Ongoing Kuebix TMS administration
- Marketing Hub configuration
- Ongoing managed services beyond 2-week hypercare per phase
- HubSpot/NetSuite license procurement (recommendations only)
- n8n as production runtime (may be used for prototyping only)

---

## Outstanding Items (Need from Client)

1. ~~**Caleb:** All 5 Excel shipping calculator files for technical review~~ -- **RECEIVED AND VALIDATED (2026-04-04).** No VBA, no external refs, no circular formulas. Dorm Mattress identified as primary complexity driver (9-level nesting, 180+ calculation paths).
2. **Sarah-Beth:** NetSuite admin access or OAuth 2.0 M2M integration record creation
3. **Mike/Sarah-Beth:** Complete warehouse address list with routing rules
4. **Caleb:** Freight class per product line (or lookup reference)
5. **Patrick:** Kuebix API credentials (username, API key, Client ID)
6. **Mike/Patrick:** SOW signing authority confirmation
7. **Caleb:** 5-10 recent quotes with known freight costs for validation testing
8. **Caleb/Delbert:** Clarify "Special Case Check with Delbert" referenced in Dorm Mattress calculator. Undocumented business logic that may affect weight calculation edge cases. Resolve at kickoff or during Week 5 weight engine build.

---

## Recommendation

**Two-phase HubSpot CPQ with hybrid architecture.** Phase 1 eliminates the 4-system quoting process and gets reps quoting in HubSpot using custom code actions for all integration logic. Phase 2 hardens the platform by migrating heavy orchestration to a Railway-hosted production API -- eliminating HubSpot timeout constraints and delivering a testable, version-controlled codebase.

The Kuebix API is fully reviewed and the integration path is well-defined. The Excel shipping calculators have been received and validated (2026-04-04) -- the pre-engagement gate is cleared.

Phase 1 (~$30,000) pays for itself within 7-9 months through labor savings alone (65 quotes/week x 20-30 min avg savings = ~$38K-$58K/year). Phase 2 (~$11,500) delivers production durability and eliminates the timeout risk for complex quotes.

---

**Next Steps:**
1. ~~Get Excel shipping calculator files from Caleb for technical review~~ -- **COMPLETE (2026-04-04).** Pre-engagement gate cleared.
2. Confirm Kuebix API credentials are available
3. Kyle/Cam review this scope summary and proposal
4. Present proposal to Mike/Patrick for approval
5. SOW signed by budget authority
6. Schedule Phase 1 kickoff within 1-2 weeks of signed SOW
