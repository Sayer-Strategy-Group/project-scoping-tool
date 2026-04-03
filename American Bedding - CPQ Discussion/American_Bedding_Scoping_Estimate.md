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
| Dynamic Weight Calculation Engine | 28 | 44 | 36 | Replicate 5 Excel calculators in n8n. Dorm, Camp, Dura-Last, SoFlux OX, Vinyl. **Highest-risk workstream.** |
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

1. **Excel weight calculator complexity** (HIGH severity, MEDIUM likelihood) -- 5 spreadsheets with nested IF/AND formulas. If VBA macros or external references exist, dynamic weight engine is unbounded. **Mitigation:** Get Excel files from Caleb BEFORE finalizing engagement. Test replication on 1 product line first.

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
- Excel calculators contain no VBA macros or external data references
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

1. **Caleb:** All 5 Excel shipping calculator files for technical review (action item from Mar 23 -- still pending)
2. **Sarah-Beth:** NetSuite admin access or OAuth 2.0 M2M integration record creation
3. **Mike/Sarah-Beth:** Complete warehouse address list with routing rules
4. **Caleb:** Freight class per product line (or lookup reference)
5. **Patrick:** Kuebix API credentials (username, API key, Client ID)
6. **Mike/Patrick:** SOW signing authority confirmation
7. **Caleb:** 5-10 recent quotes with known freight costs for validation testing

---

## Recommendation

**Single-phase HubSpot CPQ with n8n middleware.** This eliminates the 4-system quoting process (NetSuite + Excel + Kuebix + HubSpot) and automates freight calculation -- the #1 pain point consuming 10-60 minutes per quote across 65 quotes/week. The Kuebix API is fully reviewed and the integration path is well-defined. The dynamic weight calculation engine is the highest-risk workstream and the engagement should not be finalized until Caleb provides the Excel files for technical verification.

The $34,500 fixed fee pays for itself within 7-9 months through labor savings alone (65 quotes/week x 20-30 min avg savings = ~$38K-$58K/year). The real return is operational: single-interface quoting, automated freight, quote visibility for leadership, and the foundation for Phase 2 government RFP automation.

---

**Next Steps:**
1. Get Excel shipping calculator files from Caleb for technical review (pre-engagement gate)
2. Confirm Kuebix API credentials are available
3. Kyle/Cam review this scope summary and proposal
4. Present proposal to Mike/Patrick for approval
5. SOW signed by budget authority
6. Schedule kickoff within 1-2 weeks of signed SOW
