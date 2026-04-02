# STRIVE Global -- Implementation Scope Summary

**Prepared by:** Kyle Harbuck, Harbuck Consulting / Sayer
**Date:** March 21, 2026

---

## Option A: CRM Foundation

**Systems in Scope:** HubSpot Sales Hub Enterprise (reconfiguration)
**Approach:** Phased -- Foundation First (data cleanup weeks 1-4, then pipeline + dashboards weeks 5-8)
**Estimated Hours:** 86-156 hrs (median: 119)
**Estimated Investment:** $12,900-$23,400 (median $17,850 at $150/hr)
**Estimated Timeline:** 6-8 weeks

**Workstream Breakdown:**

| Workstream | Median Hours |
|-----------|-------------|
| CRM Architecture & Config Review | 9 |
| Pipeline Restructuring | 14 |
| Contact & Company Classification + Cleanup | 18 |
| Deal Health Scoring & Forecasting | 8 |
| Reporting & Dashboards | 14 |
| Automations & Workflows | 12 |
| Email & Communication Fix | 6 |
| Training: Admin | 6 |
| Training: End Users | 8 |
| Training: Executive | 3 |
| UAT, Go-Live & Documentation | 8 |
| Project Management | 13 |
| **Total** | **119** |

**Key Risks:**
1. 10 years of uncoded contact data (HIGH severity, HIGH likelihood) -- mitigated by AI enrichment pilot on 500 records first
2. Pipeline under-reporting from reps using LinkedIn (HIGH severity, HIGH likelihood) -- mitigated by executive mandate from Jodi
3. Scope creep from close relationship (HIGH severity, MEDIUM likelihood) -- mitigated by formal SOW and change request process

**Key Assumptions:**
- Existing HubSpot Sales Hub Enterprise instance (reconfiguration, not new setup)
- Up to 23 licensed users across sales, core, and service seats
- Up to 30 custom properties, 8 workflows, 12 custom reports
- AI enrichment using existing HubSpot Breeze credits (5-10K)
- All work conducted remotely

**Outstanding Items (Need from Client):**
- HubSpot portal access for record count audit
- Service Hub usage confirmation (preserve or deprecate)
- COO identity clarification (Lauren vs. Zach Beegal)
- Outlook email logging defect details

---

## Option B: Full CRM Overhaul

**Systems in Scope:** HubSpot Sales Hub Enterprise, Marketing Hub, Service Hub (reconfiguration + expansion)
**Approach:** Phased -- Phase 1 CRM Foundation (weeks 1-6), Phase 2 CPQ + Enrichment + Integrations (weeks 7-14)
**Estimated Hours:** 160-280 hrs (median: 216)
**Estimated Investment:** $24,000-$42,000 (median $32,400 at $150/hr)
**Estimated Timeline:** 10-14 weeks

**Additional Workstreams (beyond Option A):**

| Workstream | Median Hours |
|-----------|-------------|
| CPQ Implementation | 18 |
| Contract Management Workflows | 8 |
| Data Enrichment at Scale | 8 |
| Data Normalization & Dedup (Extended) | 12 |
| Parent-Child Structure (Broker Packs) | 6 |
| Email Sequencing | 6 |
| Marketing Automation Foundation | 8 |
| Commission Visibility & Validation | 6 |
| NetSuite Integration Prep (prep only) | 8 |
| Bill.com Integration Prep (prep only) | 6 |
| Seat/License Optimization | 3 |
| Advanced Reporting | 8 |
| Additional PM | 10 |
| **Phase 2 Total** | **107** |

**Optional Add-On:** Client Success Pipeline (+8 median hours / $1,200). Requires separate CS team discovery.

**Additional Risks (Option B specific):**
- CPQ product library complexity with multiple pricing models (MEDIUM) -- mitigate by auditing 5 recent quotes first
- NetSuite/Bill.com scope bleed from prep to build (MEDIUM) -- mitigate with explicit SOW boundary

**Additional Items Needed (Option B):**
- Complete product/pricing inventory (all SKUs, bundles, pricing models)
- 3-5 recent quotes/proposals across deal types
- NetSuite admin contact and entity structure
- Commission validation requirements

---

## Side-by-Side Comparison

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Median Hours | 119 | 216 |
| Median Cost | $17,850 | $32,400 |
| Timeline | 6-8 weeks | 10-14 weeks |
| Pipeline Fix | Yes | Yes |
| Contact Classification | Yes | Yes + extended enrichment |
| Dashboards | 3-4 dashboards, 12 reports | 4-5 dashboards, 20 reports |
| Forecasting | Deal health scoring | Deal health + weighted probability |
| CPQ / Quoting | No | Yes (full product library, quotes, e-sign) |
| Marketing Automation | No | Yes (newsletter, segmented campaigns) |
| Email Sequences | No | Yes (4 sequences) |
| Integration Prep | No | Yes (NetSuite + Bill.com) |
| Commission Tracking | No | Yes (visibility + validation) |
| Seat Optimization | No | Yes (audit + cost savings memo) |
| Board Report Automation | Manual export from dashboards | Scheduled automated delivery |
| Payback Period | 5-7 months | 4-7 months |
| Can Phase? | N/A (single phase) | Yes -- Phase 1 = Option A, Phase 2 = additive |

---

## Recommendation

**Start with Option A. Plan for Option B.**

Option A delivers the highest-ROI fixes first: pipeline clarity, contact classification, board dashboards, and deal health scoring. It pays for itself within 5-7 months through time savings alone.

Option B should follow as Phase 2 once the foundation is clean. CPQ built on dirty data produces inaccurate quotes. Marketing automation targeting unclassified contacts wastes effort. The phased approach lets Jodi demonstrate Phase 1 ROI to the board before requesting Phase 2 budget.

If the board approves the full overhaul upfront, the phased timeline ensures each phase delivers standalone value with a natural checkpoint between them. Phase 1 can proceed immediately; Phase 2 begins only after Phase 1 data quality is validated.
