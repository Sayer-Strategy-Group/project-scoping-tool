# Arkview Capital -- HubSpot CRM Implementation Scope Summary

**Date:** March 2, 2026
**Prepared by:** Kyle H / Harbuck Consulting
**Discovery Call:** February 26, 2026 (Cameron Taggart + Frank C)

---

## Recommendation: HubSpot Sales Hub Professional

Sales Hub Professional is recommended over Starter for Arkview Capital because:

- **Workflow automation** -- The deal stage progression, NDA tracking, partner review notifications, and task creation discussed on the call all require Professional-tier workflow automation. Starter does not support custom workflows.
- **Multiple pipelines** -- Two distinct pipelines (M&A and Real Estate) with different stage definitions require Professional. Starter limits pipeline customization.
- **Required fields per stage** -- Enforcing data entry at stage gates (e.g., requiring NDA status before advancing) is a Professional feature.
- **Custom reporting** -- The conversion rate and pipeline health reports Frank wants need Professional's custom report builder. Starter only offers pre-built reports.
- **Future-proofing** -- When investor comms, LP management, or marketing tools are added later, Professional provides the foundation without re-platforming.

**Estimated licensing:** ~$90-100/user/month for Professional (5 paid seats = ~$450-500/month). View-only seats for Jess/Brian at no additional cost.

---

## Systems in Scope

- HubSpot Sales Hub Professional (CRM)
- Microsoft 365 / Outlook integration

## Approach

Single-phase implementation (recommended), contingent on real estate pipeline discovery with Vijay/Philip before kickoff. Fallback: two-phase split if real estate discovery is delayed.

## Estimated Hours

**86-156 hrs (median: 121 hrs)**

## Estimated Investment

**$12,900-$23,400 (median: $18,150) at $150/hr**

## Estimated Timeline

**6-8 weeks**

---

## Workstream Breakdown (Median Hours)

| Workstream | Median Hours |
|---|---|
| CRM Architecture & Setup | 8 |
| Contact & Company Management | 11 |
| Pipeline: M&A (5 stages) | 8 |
| Pipeline: Real Estate (TBD stages) | 8 |
| Automations & Workflows | 14 |
| Email & Communication (Outlook) | 8 |
| Reporting & Dashboards | 9 |
| Data Migration: Contact Import | 12 |
| Training: Admin (Frank) | 6 |
| Training: End Users (deal team + EA) | 6 |
| Training: Operations (Jess - optional) | 3 |
| UAT & Go-Live | 9 |
| Documentation & SOPs | 6 |
| Project Management | 13 |
| **TOTAL** | **121** |

---

## Key Risks

| # | Risk | Severity |
|---|---|---|
| 1 | **Scope creep from close relationship** -- Shared office / sublease creates informal scope pressure | HIGH |
| 2 | **FINRA compliance constraints** -- Email tracking, data residency (India EA), recording restrictions | HIGH |
| 3 | **Real estate pipeline undefined** -- Vijay/Philip discovery not yet done; half the pipeline build is unscoped | MEDIUM |
| 4 | **Budget gatekeeper misalignment** -- Jess controls budget but wasn't in detailed discovery | MEDIUM |
| 5 | **NDA automation expectations** -- Cameron discussed auto-attach; not feasible without e-signature tool | MEDIUM |

---

## Assumptions

- HubSpot Sales Hub Professional tier
- 5 paid seats + view-only access for Jess/Brian
- Under 1,000 contacts for initial import (client populates template)
- 2 pipelines: M&A (5 confirmed stages) + Real Estate (stages TBD)
- NDA tracking is manual (checkbox), not automated
- No call recording or transcription (FINRA)
- No marketing automation in Phase 1
- Up to 25 custom properties, 8 workflows, 8 custom reports
- Adobe Acrobat signing remains external to HubSpot

---

## Outstanding Items (Need from Client)

1. **Real estate pipeline discovery** -- Schedule call with Vijay and Philip for deal stage definitions
2. **Contact volume estimate** -- How many contacts across all categories (deal sourcing, vendors, LPs, lenders)?
3. **FINRA compliance review** -- Client must review HubSpot tracking/storage with compliance counsel
4. **Budget authority sign-off** -- SOW must be reviewed by Jess/Brian, not just Frank verbal agreement
5. **EA task definition** -- What specific CRM tasks will the India-based EA perform?
6. **Investor comms scope** -- Is Jess/Brian follow-up call for LP management expected in this phase or deferred?

---

## How This Fits with Cameron's Verbal Quotes

Cameron quoted $15,000-$30,000 on the call. Our median estimate of **$18,150** lands in the lower-middle of that range. The full max of $23,400 is still within the quoted ceiling.

The gap between our max ($23,400) and Cameron's ceiling ($30,000) provides buffer for:
- Real estate pipeline turning out more complex than assumed
- Contact volume being higher than expected
- Additional automation requests during build

If scope stays as-defined, the project should land between **$15,000-$20,000** -- which is a defensible number to present to Jess as cost-conscious without leaving money on the table.

---

## Phase 2 (Future -- Not in This SOW)

These were discussed on the call but explicitly deferred:
- Investor communications and LP management (requires Jess/Brian discovery)
- Marketing tools (LinkedIn posting, email campaigns)
- DocuSign or e-signature integration for NDA automation
- Advanced reporting or Breeze AI features
- LinkedIn Sales Navigator integration
