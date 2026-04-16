# HelloSpoke — HubSpot CRM Implementation

## What This Is

A full CRM implementation engagement for HelloSpoke, a 30-person VoIP company serving the multifamily real estate vertical. Migrating from Salesforce to HubSpot CRM with billing integration (Rev IO), accounting sync (QuickBooks Online), and commission automation (QuotaPath). 15-18 users across sales, operations, and bookkeeping will be on the new system by August 2026.

## Core Value

HelloSpoke's sales team has one system of record that connects pipeline, billing, commissions, and reporting — replacing the current fragmented toolchain that causes manual work, data errors, and poor adoption.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] R1: Reconfigure existing HubSpot instance with user roles, permissions, and team structure for 15-18 users
- [ ] R2: Redesign sales pipeline with standardized stages, entry/exit criteria, deal scoring, and lead/deal definitions
- [ ] R3: Configure contact and company objects with multifamily real estate properties, parent-child associations, and custom objects
- [ ] R4: Migrate Salesforce data (contacts, companies, deals, activities) in phased approach: inactive → active pipeline → leads (<50K records)
- [ ] R5: Build Rev IO billing integration — custom object in HubSpot, REST API sync (accounts, invoices, payments, usage), deal association
- [ ] R6: Build QuickBooks Online revenue actuals integration — custom sync for paid invoices → HubSpot deal properties (OAuth2, webhook)
- [ ] R7: Configure HubSpot-side data flow for QuotaPath commission tracking (custom objects, deal properties, data architecture)
- [ ] R8: Build automated workflows — lead routing, stage-change triggers, follow-up automation, notifications (up to 10)
- [ ] R9: Deliver executive and sales dashboards — pipeline, forecasting, actuals vs targets (up to 2 dashboards, 20+ reports)
- [ ] R10: Train 3 user groups — admin (Christina), sales reps, ops/bookkeeping — with recorded sessions
- [ ] R11: Project management — kickoff, weekly syncs, milestone reviews, change management for 14-week engagement

### Out of Scope

- Elastic/ALN database integration — Jeremy de-scoped as future aspiration ("at some point"), not immediate need
- Campfire ERP integration — ERP evaluation still TBD on HelloSpoke's side, excluded per Kyle/Cameron direction
- ClickUp-to-HubSpot sync — removed from scope per Kyle
- Zendesk migration or integration — not discussed as a need in discovery calls
- Email template design or marketing automation — not part of this engagement
- Custom HubSpot UI extensions — standard configuration only
- Ongoing data sync maintenance post-go-live — engagement ends after hypercare
- HubSpot licensing costs — client responsibility
- QuotaPath platform implementation — QuotaPath handles their own; Sayer assists with HubSpot-side only
- Native HubSpot CPQ build — only if QuotaPath falls through (would be a change order)

## Context

### Client Profile
- **Company:** HelloSpoke — VoIP/telecom platform for multifamily real estate
- **Size:** 30 employees, Louisville KY
- **Website:** hellospoke.com
- **Key contacts:** Jeremy Wiley (decision-maker), Christina Edwards (Director of Ops, project liaison), Ryan Sweeney (sales), Sara Hines (reporting/CS)

### Current Systems
- **Salesforce** — CRM, contract expires October 2026
- **Rev IO** — telecom billing platform (accounts, invoices, usage)
- **QuickBooks Online** — accounting, revenue tracking
- **QuotaPath** — commission tracking (evaluating, demo completed, pricing received ~$9-12K/yr)
- **ClickUp** — project management
- **Calendly** — scheduling
- **DocuSign** — e-signatures
- **Zendesk** — support
- **Elastic** — NoSQL database (telecom records)
- **ALN** — multifamily property database

### Discovery Findings
- Salesforce adoption is poor — Christina reports it was overloaded and complicated for sales
- Duplicate accounts exist in Salesforce from auto-creation during quoting
- Commission tracking is manual and error-prone (over/underpayments)
- Quoting process uses cumbersome CSV imports
- Jeremy is budget-aware but willing to pay fairly; prior frustration with expensive Salesforce change requests
- HubSpot Growth team (Zack Grimm) ran a demo in February 2026 — existing HubSpot instance provisioned

### Integration Research
- **Rev IO:** REST API at restapi.rev.io/v1, Basic Auth, sandbox available. No native HubSpot marketplace app. Webhooks supported but not in sandbox. First-time integration for Sayer.
- **QuickBooks:** Native HubSpot integration exists but insufficient (one-way, no company sync, 3 custom field limit, no deal-to-invoice matching). Custom build required with OAuth2. Revenue actuals sync needs webhook → sync service → HubSpot update pattern. First-time for Sayer at this depth.
- **QuotaPath:** Handles own implementation. HubSpot-side work is custom object design and data flow architecture (Rev IO → HubSpot custom object → deal → QuotaPath).

### Calibration References
- Milestone Group ($26,075, 10 users, no major integrations) — HelloSpoke is materially more complex
- Strive Global ($32,400 median Option B, 23 users, existing HubSpot reconfig) — similar user count, less integration depth
- American Bedding ($30K+$11.5K, first-time NetSuite/Kuebix integration pattern) — first-time integration premium precedent

## Constraints

- **Timeline:** Salesforce contract expires October 2026 — must complete migration with buffer. 14-week timeline targets August completion.
- **Pricing:** Fixed fee only, no hours shown to client (Cam directive). Payment terms: equal installments every 15 days, net-15, 5% tech/admin fee.
- **Integration dependencies:** Rev IO data must flow into HubSpot before QuotaPath can calculate commissions. Salesforce data must be in HubSpot before QuickBooks integration (per discovery call agreement).
- **API access:** Rev IO and QuickBooks integrations require client-provided credentials and sandbox access before development can begin.
- **HubSpot tier:** Minimum Sales Hub Professional required for custom objects and workflows. Exact tier of existing instance TBD.
- **Data migration order:** Phased: inactive customers → active pipeline → leads. Each phase validated before proceeding.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Exclude Elastic/ALN | Jeremy self-de-scoped in March 26 discovery call; future aspiration not immediate need | — Pending |
| Exclude Campfire ERP | ERP evaluation TBD on client side; prevents ERP complexity premium | — Pending |
| QuotaPath-primary, CPQ fallback | QuotaPath further along (demo done, pricing received); CPQ is change order if QP falls through | — Pending |
| First-time integration premium | Rev IO + QuickBooks are both new for Sayer; American Bedding NetSuite pattern applied (40-60 hrs precedent) | — Pending |
| Phased data migration | Reduces risk per load; agreed in discovery calls; allows validation between batches | — Pending |
| Fixed fee $35K full / $22K reduced | No verbal quote given; priced above median to account for integration uncertainty | — Pending |
| Existing HubSpot reconfig | Instance provisioned ~Feb 2026; audit in Week 1 to assess cleanup needed | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-16 after initialization*
