# American Bedding -- CPQ Phase 1 Scope Summary

**Date:** April 2, 2026
**Discovery Calls:** March 16, 2026 (Intro) / March 23, 2026 (Follow-up)
**Prepared by:** Harbuck Consulting / Sayer

---

**Systems in Scope:** HubSpot CPQ (Sales Hub Pro + Commerce Hub Pro), NetSuite ERP (integration), Kuebix TMS (freight API), n8n (middleware)
**Approach:** Single-phase, inside sales CPQ with automated freight and dynamic weight calculation
**Estimated Hours:** 168-284 hrs (median: 226)
**Fixed Fee:** $34,500
**Estimated Timeline:** 10-12 weeks

**Revision note:** Replaces initial A/B option structure ($19,500 / $33,000). Single fee reflects expanded scope: Sayer owns all NetSuite development, dynamic weight calculation engine, multiple shipping origins, and fully reviewed Kuebix API integration.

---

## Workstream Breakdown

| Workstream | Min | Max | Median | Notes |
|---|---|---|---|---|
| HubSpot CPQ Architecture & Configuration | 14 | 22 | 18 | Commerce Hub CPQ setup, custom properties, approval workflows, payment terms |
| Product Catalog Sync (NetSuite to HubSpot) | 20 | 36 | 28 | SuiteQL extraction of 700 SKUs, custom properties (weight, freight class, dims, cover type, foam series), n8n scheduled sync |
| NetSuite Quote-to-Order Integration | 22 | 40 | 31 | OAuth 2.0 M2M, quote -> estimate -> sales order, credit hold check, price level sync |
| Kuebix Freight Integration + Origin Routing | 22 | 38 | 30 | n8n -> quickRate API, multi-carrier LTL, origin warehouse routing, manual override fallback |
| Dynamic Weight Calculation Engine | 28 | 44 | 36 | Replicate 5 Excel calculators in n8n. Validated (2026-04-04): no VBA/external refs/circular formulas. Dorm (HIGH -- 9-level nesting, 180+ paths), Camp (MED), Dura-Last (MED), SoFlux OX/Vinyl (LOW, ~80% reuse). Highest-complexity workstream. Dorm Mattress sampling strategy needed for testing. |
| Quote Template Design | 12 | 20 | 16 | HubL/HTML/CSS matching NetSuite format. Line items, discounts, tax, shipping, terms, acceptance flow |
| Discount, Tax & Payment Terms Logic | 10 | 18 | 14 | 10% volume discount, state-based tax, prepay/net 10/30/60, credit hold integration |
| Training & Documentation | 10 | 16 | 13 | Sales (Caleb, Don) + Admin (Sarah-Beth, Patrick). Recorded sessions. Admin guide + user card. |
| Testing & QA | 14 | 24 | 19 | E2E integration testing, weight calc validation, freight validation, UAT, 2-week hypercare |
| Project Management | 16 | 26 | 21 | Kickoff, weekly syncs, milestone reviews, scope creep prevention. ~12% of total. |
| **TOTAL** | **168** | **284** | **226** | |

At $150/hr: $25,200 - $42,600 (median $33,900)
**Fixed fee presented: $34,500** (median + buffer for integration unknowns)

---

## Key Risks

1. **Excel weight calculator complexity** (MEDIUM severity, LOW likelihood) -- 5 spreadsheets validated (2026-04-04): no VBA, no external refs, no circular formulas. Dorm Mattress is the primary complexity driver (9-level nested IFs, 180+ calculation paths). Remaining risk is undocumented business logic ("Special Case Check with Delbert" noted in Dorm Mattress calculator). **Mitigation:** Clarify Delbert edge cases at kickoff. Build Dorm Mattress calculator first with sampling strategy for 180+ paths. Test against known weights.

2. **NetSuite data quality** (HIGH severity, HIGH likelihood) -- SKU duplicates, missing attributes from Jan 2026 launch. **Mitigation:** Week 1 data audit via SuiteQL before building sync.

3. **Scope creep via Vesco relationship** (HIGH severity, MEDIUM likelihood) -- Government RFP enthusiasm and close personal relationships. **Mitigation:** SOW signed by budget authority (Mike/Patrick). Phase boundary iron-clad.

4. **NetSuite still stabilizing** (HIGH severity, MEDIUM likelihood) -- TPI may make changes that break integration. **Mitigation:** Build against documented REST API, not custom SuiteScript. Establish TPI change notification channel.

5. **Multiple shipping origins** (MEDIUM severity, HIGH likelihood) -- Wrong origin = wrong freight = wrong price. **Mitigation:** Map all warehouses at kickoff. Test each origin with known quotes.

---

## Assumptions

- HubSpot Sales Hub Professional + Commerce Hub Professional (existing)
- Operations Hub Professional recommended (separate license cost)
- NetSuite REST API access with OAuth 2.0 M2M credentials
- Kuebix API credentials provided by client
- n8n middleware (hosting TBD)
- Up to 700 products, flat catalog (one record per SKU)
- Up to 30 custom properties (overages are change orders)
- Excel calculators validated: no VBA macros, no external data references, no circular formulas (confirmed 2026-04-04)
- SOW signed by Mike Taylor or Patrick (CFO)
- All work conducted remotely
- 10-12 week timeline

---

## Exclusions

- Government RFP automation (Phase 2)
- Customer-facing product configurator / guided selling (Phase 2)
- External storefront (Shopify -- Phase 3)
- VoIP / call capture integration
- AI lead enrichment
- NetSuite reimplementation or new module deployment
- Ongoing Kuebix TMS administration
- Marketing Hub configuration
- Ongoing managed services beyond 2-week hypercare
- HubSpot/NetSuite license procurement (recommendations only)

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

**Single-phase HubSpot CPQ with n8n middleware.** This eliminates the 4-system quoting process (NetSuite + Excel + Kuebix + HubSpot) and automates freight calculation -- the #1 pain point consuming 10-60 minutes per quote across 65 quotes/week. The Kuebix API is fully reviewed and the integration path is well-defined. The dynamic weight calculation engine is the highest-complexity workstream. The Excel shipping calculators have been received and validated (2026-04-04) -- the pre-engagement gate is cleared. No VBA, no external refs, no circular formulas. The $34,500 fixed fee is confirmed.

The $34,500 fixed fee pays for itself within 7-9 months through labor savings alone (65 quotes/week x 20-30 min avg savings = ~$38K-$58K/year). The real return is operational: single-interface quoting, automated freight, quote visibility for leadership, and the foundation for Phase 2 government RFP automation.

---

**Next Steps:**
1. ~~Get Excel shipping calculator files from Caleb for technical review~~ -- **COMPLETE (2026-04-04).** Pre-engagement gate cleared. Clarify Dorm Mattress "Special Case Check with Delbert" at kickoff.
2. Confirm Kuebix API credentials are available
3. Kyle/Cam review this scope summary and proposal
4. Present proposal to Mike/Patrick for approval
5. SOW signed by budget authority
6. Schedule kickoff within 1-2 weeks of signed SOW
