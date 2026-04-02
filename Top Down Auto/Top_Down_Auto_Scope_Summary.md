# Top Down Auto -- Implementation Scope Summary

**Date:** March 5, 2026
**Discovery Call:** February 11, 2026
**Prepared by:** Harbuck Consulting / Sayer

---

**Systems in Scope:** HubSpot CRM (Sales Hub Professional), NetSuite ERP (data cleanup + integration), Legacy ERP (Intuitive data extraction), Atlas/CalTrend migration
**Approach:** Phased (CRM first, then ERP integration) -- recommended
**Estimated Hours:** 192-434 hrs (median: 304)
**Estimated Investment:** $28,800-$65,100 (at $150/hr, median ~$45,600)
**Estimated Timeline:** Phase 1: 6-8 weeks (CRM) + Phase 2: 6-10 weeks (ERP integration)

---

## Workstream Breakdown

### CRM Workstreams (HubSpot Sales Hub Professional) -- Median: 114 hrs

| Workstream | Median Hours |
|---|---|
| CRM Architecture & Setup | 14 |
| Pipeline & Deal Management | 16 |
| Contact & Company Management | 18 |
| Automations & Workflows | 20 |
| Email & Communication | 10 |
| Reporting & Dashboards | 16 |
| Training & Adoption (Admin) | 8 |
| Training & Adoption (End Users) | 12 |

### ERP Workstreams -- Median: 134 hrs

| Workstream | Median Hours |
|---|---|
| ERP Data Assessment | 18 |
| Legacy Data Extraction (Intuitive) | 28 |
| NetSuite Data Cleanup | 20 |
| Product Catalog Digitization | 16 |
| Atlas-to-NetSuite Migration | 14 |
| CRM-ERP Integration (HubSpot <-> NetSuite) | 28 |
| SKU Cross-Reference Build | 10 |

### Cross-Cutting Workstreams -- Median: 56 hrs

| Workstream | Median Hours |
|---|---|
| Project Management | 24 |
| UAT & Testing | 14 |
| Documentation & SOPs | 8 |
| Go-Live & Hypercare | 10 |

---

## Key Risks

1. **NetSuite data quality worse than expected** (HIGH severity, High likelihood) -- Integration mapping breaks; CRM shows bad data; reps lose trust
2. **CRM-ERP integration direction undefined** (HIGH severity, High likelihood) -- Bidirectional sync = 2x complexity vs. read-only
3. **ERP readiness gates CRM value** (HIGH severity, High likelihood) -- CRM launches without product/order data; adoption suffers
4. **Multi-subsidiary NetSuite structure complicates integration** (HIGH severity, High likelihood) -- API calls multiply per subsidiary
5. **Legacy ERP (Intuitive) data extraction fails** (HIGH severity, Medium likelihood) -- CRM loses historical context; warranty processing breaks

---

## Assumptions

- HubSpot Sales Hub Professional tier (workflows, multiple pipelines, custom reporting)
- 6-10 inside sales/CSR users plus 2-3 admin users
- NetSuite remains ERP source of truth
- Alexis can export structured data from Intuitive without $25K fee
- Integration is initially read-only from NetSuite to HubSpot
- Product catalog digitization limited to MVP (high-volume SKUs only)
- Up to 30 custom properties in HubSpot; overages are change orders

---

## Exclusions

- Phone/VoIP system replacement (Nextiva) -- separate phase
- Marketing automation (Klaviyo replacement / HubSpot Marketing Hub) -- separate phase
- E-commerce platform consolidation (Magento/WooCommerce) -- 2027-2028 per client
- NetSuite reimplementation or new module deployment
- Full legacy catalog digitization beyond MVP
- Custom self-service pricing portal
- Ongoing NetSuite administration or support

---

## Outstanding Items (Need from Client)

- 22 ERP clarifying questions must be resolved before finalizing scope (see ERP Questions document)
- Key decisions needed: data architecture (warehouse vs. direct), integration direction (read-only vs. bidirectional), customer record mapping strategy
- Alexis POC on Intuitive data extraction before committing integration hours
- Atlas technical spec required to scope CalTrend migration
- Brand/subsidiary mapping documentation from client

---

## Recommendation

**Phased approach.** Stand up HubSpot CRM for pipeline tracking, quote management, and call logging in Phase 1 (6-8 weeks). This delivers immediate value to Stephanie and the inside sales team without depending on ERP data readiness. Phase 2 (6-10 weeks) tackles ERP data cleanup, Intuitive extraction, and NetSuite-HubSpot integration with better information from Phase 1. The number of ERP unknowns -- Intuitive extraction feasibility, Atlas complexity, NetSuite data quality, architecture decision -- makes concurrent execution risky. Revisit after follow-up call with Alexis, Terry, and Shafi resolves the open items.

---

**Next Steps:**
1. Schedule follow-up call with Alexis (IT/dev), Terry, and Shafi (ERP experts)
2. Send ERP Clarifying Questions to client in advance of call
3. Revisit scope and approach after answers are in hand
4. Finalize SOW for Phase 1 (CRM) once pipeline stages and property list are approved by Stephanie
