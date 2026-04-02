# STRIVE vs. Wagmo: Scope Triangulation Analysis

**Purpose:** Calibrate Strive scoping estimates against Wagmo actuals and industry benchmarks.
**Date:** March 22, 2026

---

## Wagmo Actuals: 119 Hours

| Category | Tasks | Hours |
|----------|-------|-------|
| Discovery & Planning | Instance review, sandbox, optimizer, sales flow artifact, project plan, presentation deck | 20 hrs |
| Pipeline/Sales Path Build | Sales path build (sandbox + prod), record types, stage names, fields, validations, flows, action buttons, required fields | 36 hrs |
| Testing & Iteration | Test cases, run tests, review feedback, adjustments, retest | 7 hrs |
| Training | Walkthrough, video, doc, feedback/review | 2.5 hrs |
| Deployment (Salesforce-specific) | Change sets (4 pushes), sandbox connection, production testing, error resolution | 12.5 hrs |
| Reporting & Dashboards | Scope/design, report build, dashboard build, test filtering, feedback iterations, competitor reports, historical trends | 20 hrs |
| Partner/Referral | Design + sandbox build + flow changes | 11 hrs |
| **TOTAL** | | **119 hrs** |

---

## What Wagmo DID NOT Include (but Strive needs)

| Work Area | Strive Needs | Wagmo Had? |
|-----------|-------------|------------|
| Contact/data classification & cleanup | 10 years uncoded data, AI enrichment, dedup, normalization | NO |
| CPQ / Quoting | Product library, templates, e-sign, pricing models | NO |
| Email sequencing | 4 sequences, enrollment triggers | NO |
| Marketing automation | Newsletters, segmented campaigns | NO |
| Integration prep | NetSuite + Bill.com data readiness | NO |
| Commission tracking | CRM-based view + validation workflow | NO |
| Seat/license audit | 23 seats across 3 hubs | NO |
| Formal project management | Kickoff, weekly syncs, status updates | NO (informal) |
| Parent-child company structure | Broker pack tracking, per-broker forms | Partially (partner/referral: 11 hrs) |

---

## Adjustment Factors: Wagmo to Strive

| Factor | Direction | Rationale |
|--------|-----------|-----------|
| Salesforce vs. HubSpot | -15 to -20% | No change sets, no sandbox/prod deployment, simpler config UI |
| AI tooling (2026 vs. 2024) | -10 to -15% | Claude/AI accelerates documentation, test cases, report logic |
| Strive complexity vs. Wagmo | +30 to +50% | Two deal categories, pre-pipeline separation, probability mapping, more dashboards, required fields per stage, auto-transitions |
| Data cleanup (net new scope) | +18-30 hrs (Option A) / +30-40 hrs (Option B) | Wagmo had zero data cleanup; Strive has 10 years |
| CPQ (net new scope) | +40-60 hrs | Industry benchmark for CPQ rollout (Process Pro Consulting) |
| Marketing/sequences (net new) | +12-20 hrs | Net new capability build |
| Integration prep + commission + seat audit | +12-20 hrs | Net new scope items |
| Scope creep buffer | +10-15% | Kyle's Wagmo experience: first gig, scope creep occurred |

---

## Triangulation: Three Estimation Methods

### Method 1: Wagmo Actuals Adjusted

Wagmo comparable scope (pipeline + reporting + partner) = 87 hrs (excluding deployment)
Apply Salesforce-to-HubSpot discount: 87 * 0.82 = ~71 hrs
Apply complexity premium (Strive is harder): 71 * 1.4 = ~100 hrs
Add AI tooling discount: 100 * 0.88 = ~88 hrs

So the COMPARABLE workstreams (pipeline, reporting, partner tracking) = ~88 hrs for Strive

Now add what Wagmo didn't have:
- Contact cleanup: +25 hrs (Option A) / +38 hrs (Option B)
- Training (formal, 3 audiences): +17 hrs
- PM: +15 hrs (Option A) / +25 hrs (Option B)
- UAT/docs/hypercare: +10 hrs
- Email fix: +6 hrs
- CPQ (Option B only): +50 hrs
- Sequences + marketing (Option B only): +16 hrs
- Commission + integration prep + seat audit (Option B only): +20 hrs

**Method 1 Totals:**
- Option A: 88 + 25 + 17 + 15 + 10 + 6 = **161 hrs**
- Option B: 88 + 38 + 17 + 25 + 10 + 6 + 50 + 16 + 20 = **270 hrs**

### Method 2: Industry Benchmarks

Monetizely benchmark for multi-hub rollout: 100-250 hours
Strive is Enterprise rebuild + CPQ + enrichment = high end of "multi-hub"
Data cleanup: $5K-$15K = 33-100 hrs at $150/hr
CPQ specifically: 40-60 hrs (Process Pro Consulting)

**Method 2 Totals:**
- Option A (rebuild without CPQ): 150-200 hrs
- Option B (rebuild + CPQ + enrichment + marketing): 250-350 hrs

### Method 3: Bottom-Up Re-Estimate (Wagmo-Informed)

Rebuilding each workstream estimate using Wagmo actuals as the anchor where applicable:

**Option A:**
| Workstream | V1 Median | Wagmo Comparable | V2 Median | Rationale |
|-----------|-----------|-----------------|-----------|-----------|
| CRM Architecture | 9 | 14 (discovery) | 12 | HubSpot simpler than SFDC, but Enterprise with 3 hubs |
| Pipeline Restructuring | 14 | 36 (sales path) | 24 | More complex than Wagmo (2 categories, pre-pipeline, probabilities, auto-transitions). HubSpot offset: -20% |
| Contact Cleanup | 18 | 0 | 24 | 10 years of data. Industry says $5K-$15K for cleanup. Conservative at 24 hrs. |
| Deal Health Scoring | 8 | incl. in pipeline | 10 | Scoring formula, thresholds, close reason standardization |
| Reporting & Dashboards | 14 | 20 | 20 | More dashboards than Wagmo (4 vs 2). More reports (12 vs 6). AI helps but scope is larger. |
| Automations & Workflows | 12 | 8 (validations partial) | 14 | 8 workflows + Outlook fix + dup protection |
| Email Fix | 6 | 0 | 6 | Unchanged -- could be quick or require support ticket |
| Training: Admin | 6 | 1 (video) | 6 | Wagmo training was minimal; Strive needs proper sessions |
| Training: End Users | 8 | 1 (walkthrough) | 8 | Same |
| Training: Executive | 3 | 0 | 3 | Same |
| UAT/Go-Live/Docs | 8 | 7 (testing) | 10 | Wagmo testing was 7 hrs; add documentation deliverables |
| Project Management | 13 | 0 | 18 | ~12% of total. Wagmo had zero formal PM (scope creep lesson) |
| **TOTAL** | **119** | | **155** | **+30% over V1** |

**Option B (additional workstreams):**
| Workstream | V1 Median | V2 Median | Rationale |
|-----------|-----------|-----------|-----------|
| CPQ Implementation | 18 | 45 | Industry benchmark: 40-60 hrs. Multiple pricing models (license+rev share, flat, bundles). Product library, templates, e-sign, reminders. |
| Contract Mgmt Workflows | 8 | 10 | Quote-to-contract, status tracking, renewals |
| Data Enrichment at Scale | 8 | 12 | Full database AI enrichment, QA, validation |
| Data Normalization Extended | 12 | 14 | Full normalization + advanced dedup + merge strategy |
| Parent-Child (Broker Packs) | 6 | 8 | Per-broker forms, auto child creation, list generation |
| Email Sequencing | 6 | 8 | 4 sequences + enrollment triggers + reporting |
| Marketing Automation | 8 | 10 | Newsletter + 2-3 campaigns + compliance |
| Commission Visibility | 6 | 6 | Unchanged |
| NetSuite Integration Prep | 8 | 10 | Field mapping, data readiness, documentation |
| Bill.com Integration Prep | 6 | 6 | Unchanged |
| Seat/License Optimization | 3 | 3 | Unchanged |
| Advanced Reporting | 8 | 10 | Automated board reports, coverage, pace-to-goal |
| Additional PM | 10 | 16 | ~12% of Phase 2 |
| **Phase 2 Total** | **107** | **158** | **+48% over V1** |
| **OPTION B TOTAL** | **216** | **313** | **+45% over V1** |

---

## V2 Summary

| | V1 Median Hrs | V2 Median Hrs | V1 Median Cost | V2 Median Cost | Change |
|---|---|---|---|---|---|
| **Option A** | 119 | 155 | $17,850 | $23,250 | +30% |
| **Option B** | 216 | 313 | $32,400 | $46,950 | +45% |

### Cross-Validation

| Method | Option A | Option B |
|--------|----------|----------|
| Wagmo-adjusted | 161 hrs | 270 hrs |
| Industry benchmarks | 150-200 hrs | 250-350 hrs |
| Bottom-up re-estimate | 155 hrs | 313 hrs |
| **Average** | **155 hrs** | **311 hrs** |

The three methods converge around **155 hrs for Option A** and **280-313 hrs for Option B**. The V1 estimates were 23-45% under where they should be.

---

## Key Under-Scoped Areas (V1 vs V2)

| Workstream | V1 | V2 | Gap | Why |
|-----------|-----|-----|-----|-----|
| **CPQ** | 18 hrs | 45 hrs | **+150%** | Industry says 40-60 hrs. Multiple pricing models, product library, templates. This was the biggest miss. |
| **Pipeline** | 14 hrs | 24 hrs | +71% | Wagmo's simpler pipeline took 36 hrs in SFDC. HubSpot is easier but Strive's requirements are more complex. |
| **Reporting** | 14 hrs | 20 hrs | +43% | More dashboards and reports than scoped. Wagmo's simpler reporting took 20 hrs. |
| **Contact Cleanup** | 18 hrs | 24 hrs | +33% | Industry benchmark for data cleanup: $5K-$15K. 10 years of uncoded data is at the high end. |
| **PM** | 13/23 hrs | 18/34 hrs | +38/+48% | Wagmo scope creep lesson. Formal PM prevents informal scope expansion. |

---

## Sources

- [Monetizely: The Real Cost of HubSpot Implementation](https://www.getmonetizely.com/articles/the-real-cost-of-hubspot-implementation-in-2025-breakdowns-benchmarks-and-pricing-models)
- [Process Pro Consulting: HubSpot CPQ](https://www.processproconsulting.com/resources/what-is-hubspot-cpq-a-more-robust-way-to-quote-in-hubspot)
- [Pixcell: HubSpot Implementation Cost](https://www.pixcell.io/blog/hubspot-implementation-cost)
- [Insidea: HubSpot Implementation Cost 2026](https://insidea.com/blog/hubspot/hubspot-implementation-cost/)
- [RevPartners: HubSpot Implementation](https://revpartners.io/hubspot-onboarding-implementation)
- [Evenbound: HubSpot Cost Guide](https://evenbound.com/blog/how-much-does-hubspot-cost)
