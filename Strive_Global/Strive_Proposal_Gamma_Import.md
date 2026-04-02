# STRIVE Global -- Full HubSpot CRM Overhaul Proposal

**Prepared by:** Sayer
**Date:** March 25, 2026

---

## A Note on This Proposal

Proposals are inherently a starting point -- not a final blueprint. This document reflects our understanding of your challenges, a proposed solution, and the resources required to execute successfully.

We recognize that you, as the client, live with these challenges daily, and there may be details we have yet to uncover. Our goal is to use this as a conversation starter -- to refine, align, and ensure we are solving the right problems in the right order.

If any aspect of the scope, solution, or pricing feels misaligned, let's use that as a basis for further discussion.

---

## 1. Executive Summary

STRIVE Global is a PE-backed (Essex Bay Capital) benefits technology company headquartered in Denver, CO with approximately 51 employees. STRIVE offers white-labeled employee benefits apps, AI-powered benefits assistants, scalable microsites, and a rewards platform (Divi) distributed through a broker channel model. Sales motions range from $6K client-level deals to $400K+ enterprise broker packs.

This proposal outlines a comprehensive CRM overhaul delivered in two phases over 16-18 weeks:

- **Phase 1 (Weeks 1-8):** CRM Foundation -- pipeline restructuring, contact classification, deal health scoring, automated board dashboards, data normalization, and parent-child broker structures
- **Phase 2 (Weeks 9-18):** CPQ implementation, AI-powered data enrichment at scale, email sequencing, marketing automation, commission visibility, and integration preparation for NetSuite and Bill.com

The phased approach is strongly recommended. STRIVE's data quality issues make it risky to build CPQ on unclassified contacts and corrupted pipeline data. Phase 1 creates the clean foundation that Phase 2 depends on. Phase 1 can also stand alone if Phase 2 is deferred -- giving the board a natural checkpoint to evaluate ROI before committing to the full investment.

---

## 2. The Problem

STRIVE's CRM is a liability, not an asset. After 10 years of organic growth, the HubSpot instance has become a bottleneck:

- **120+ hours per year** spent on manual board report preparation (1+ full business day per month)
- **Zero contact classification** across the entire database -- no way to distinguish clients from prospects from brokers
- **Pipeline is under-reported** because deals are quoted manually outside the CRM
- **Forecasting is gut feel** -- no probability weighting, no deal health scoring, no objective pipeline reviews
- **Reps default to LinkedIn** over the CRM because HubSpot data is unreliable
- **Board reporting** requires manual calculations for pipeline segmentation, win rates, and deal analysis

This is not a technology problem. It is a data infrastructure problem that compounds every quarter as the team scales.

---

## 3. The ROI: Why This Investment Pays for Itself

### Total Investment vs. Return

| | Investment | Year 1 Return | Payback Period | Year 1 Net ROI |
|---|-----------|---------------|----------------|----------------|
| **Full CRM Overhaul** | **$46,950** | **$56,400 - $106,500** | **5-7 months** | **20% - 127%** |

These are conservative estimates using only quantifiable savings. They exclude revenue uplift from improved pipeline visibility, faster sales cycles from CPQ, and expansion revenue from cross-sell automation.

### Pillar 1: Time Savings -- $45,600 - $77,700/year

| Activity | Current State | Future State | Annual Savings |
|----------|--------------|--------------|----------------|
| Board report preparation | 8-10 hrs/month manual work | 15-30 min dashboard pull | **$14,400 - $18,000** |
| Pipeline segmentation | 2-3 hrs/week manual calculation | Real-time dashboard | **$15,000 - $22,500** |
| Manual quote creation | 30-60 min per quote, error-prone | 10 min CPQ with e-sign | **$12,600 - $30,000** |
| Commission validation | Spreadsheet reconciliation | CRM-based validation workflow | **$3,600 - $7,200** |

These are hours Andrea and Jodi get back for revenue-generating activities -- selling, coaching, and strategic planning.

### Pillar 2: Tool Cost Reduction -- $10,800 - $28,800/year

| Tool | Current/Planned Cost | Replaced By | Annual Savings |
|------|---------------------|-------------|----------------|
| Apollo (under evaluation) | $3,600 - $12,000/year | HubSpot Breeze AI (included in Enterprise) | **$3,600 - $12,000** |
| External contract tool (PandaDoc, etc.) | $6,000 - $12,000/year | HubSpot CPQ (included in Enterprise) | **$6,000 - $12,000** |
| Unused HubSpot seats (5-8 service seats) | $1,200 - $4,800/year | Seat/license audit and consolidation | **$1,200 - $4,800** |

These savings are recurring and compound every year.

### Pillar 3: Pipeline Visibility -- $150K+ Captured

- If 20% of active pipeline is uncaptured today, and the average deal is $30K, capturing just 5 additional deals = **$150K+ in pipeline visibility** the board can track
- Deal health scoring ensures the team focuses on winnable deals
- Weighted probability by stage (5% through 100%) gives the board confidence that pipeline numbers mean something concrete
- Segmented reporting eliminates the blended average problem where $400K broker packs distort metrics alongside $6K client deals

### Pillar 4: Expansion Revenue Potential -- $150K - $750K

- Parent-child broker structure enables systematic microsite-to-app expansion prospecting
- Today, 250 microsite clients from the Howden pack deal have no path to app upsell in the CRM
- Each converted client represents $6K - $30K in incremental revenue
- If 10% of pack clients convert to app deals: **$150K - $750K in expansion revenue potential**

### Pillar 5: Strategic Enablement

- **Scaling infrastructure:** New rep onboarding drops from weeks of tribal knowledge to days with documented CRM process and recorded training
- **AI readiness:** Clean, classified, enriched CRM data is the prerequisite for AI-powered operations -- this engagement builds the data foundation for Jodi's AI knowledge assistant vision
- **Board confidence:** PE investors see operational maturity. Board meetings shift from "explain the numbers" to "here are the numbers -- let's talk strategy"

---

## 4. Objectives

1. Separate pre-pipeline deals from active pipeline to eliminate metric distortion and enable accurate forecasting
2. Classify all contact records by type using AI enrichment, unlocking segmented marketing and targeted outreach
3. Implement deal health scoring to replace gut-feel forecasting with objective pipeline reviews
4. Deliver automated dashboards for partner, seller, and CEO/board reporting -- eliminating 8-10 hours/month of manual assembly
5. Implement HubSpot CPQ with a complete product library, quote templates, e-signatures, and automated reminders -- replacing manual quoting and capturing deals currently invisible in the pipeline
6. Build contract management workflows to replace the manual DocuSign process through the COO
7. Deploy AI-powered data enrichment at scale using HubSpot Breeze credits to auto-classify and enrich the full database
8. Establish parent-child company structures for broker pack tracking, enabling microsite-to-app expansion prospecting
9. Launch email sequencing for broker prospecting and client expansion outreach
10. Build marketing automation foundation: newsletter templates and segmented campaigns by contact type
11. Prepare data infrastructure for future NetSuite and Bill.com integration (prep only -- integration build separate)
12. Audit and optimize HubSpot seat/license allocation to reduce unnecessary subscription costs
13. Implement commission visibility and validation workflow tied to closed-won deals
14. Standardize close won/lost reasons, lead source tracking, and data entry requirements across the team

---

## 5. Scope of Work

### Phase 1: CRM Foundation (Weeks 1-8)

#### Workstream 1: CRM Architecture & Configuration Review
**12 median hours | $1,800**

**Customer Story:** STRIVE's HubSpot instance needs auditing and optimization to support the team's actual workflows.

**Recommended Approach:**
- Audit current portal configuration, user roles, and permission sets
- Reconfigure team structure for partner vs. client sellers
- Review seat allocation across all hubs
- Establish naming conventions and organizational standards

**Assumptions:** Existing Enterprise instance. Up to 23 licensed users.

#### Workstream 2: Pipeline Restructuring
**24 median hours | $3,600**

**Customer Story:** Pre-pipeline deals mixed with active deals distort metrics. Partner and client deals need segmentation.

**Recommended Approach:**
- Separate pre-pipeline into its own pipeline or board view
- Configure partner-level and client-level deal categories
- Map stage probabilities (5/20/40/50/60/80/90/100)
- Add Contracting stage. Configure required fields per stage.
- Automate pre-pipeline to active pipeline transitions with deal age reset

**Assumptions:** Same stages for both categories. Product segmentation via product set fields.

#### Workstream 3: Contact & Company Classification + Cleanup
**24 median hours | $3,600**

**Customer Story:** 10 years of uncoded contacts. Zero classification. Cannot segment for outreach or reporting.

**Recommended Approach:**
- Define contact type taxonomy (client, prospect, broker, partner)
- Run AI enrichment pilot on 500 records
- Build classification rules. Execute full database classification.
- Normalize, deduplicate, fix associations. Establish duplicate protection.

**Assumptions:** +30-50% data quality premium. Up to 30 custom properties. HubSpot Breeze credits.

#### Workstream 4: Deal Health Scoring & Forecasting
**10 median hours | $1,500**

**Customer Story:** No algorithmic forecasting today. Gut feel only.

**Recommended Approach:**
- Create deal score: stage + time-in-stage + activity recency
- Classify deals as Healthy, At Risk, or Stale
- Replace free-form close won/lost with categorized dropdowns

**Assumptions:** Scoring formula defined collaboratively. Industry benchmarks as starting point.

#### Workstream 5: Data Normalization & Deduplication (Extended)
**14 median hours | $2,100**

**Customer Story:** Beyond basic cleanup, the full database needs comprehensive normalization for long-term data quality.

**Recommended Approach:**
- Full database normalization (capitalization, phone formats, addresses)
- Advanced deduplication with configurable matching rules
- Merge strategy for duplicate records (preserve most complete record)
- Ongoing duplicate protection rules for sustained data quality

**Assumptions:** Extends Phase 1 cleanup comprehensively. Full +50% data quality premium applied.

#### Workstream 6: Parent-Child Structure (Broker Packs)
**8 median hours | $1,200**

**Customer Story:** The Howden 250-pack deal needs tracking. Each microsite client should be a child of the broker parent, enabling app upsell prospecting.

**Recommended Approach:**
- Configure company-to-company association labels (parent broker, child client)
- Build per-broker intake forms in HubSpot CMS
- Automate child contact creation from form submissions
- Generate segmented lists by parent broker for expansion prospecting

**Assumptions:** Depends on microsite form link from Andrea. Enables crawl-walk-run product expansion tracking.

#### Workstream 7: Automations & Workflows
**14 median hours | $2,100**

**Customer Story:** Almost no automation beyond broker trial form. Outlook logging defect creating noise.

**Recommended Approach:**
- Fix Outlook email logging issue
- Lead source tracking. Form-to-CRM automation.
- Stage-change notifications. Duplicate protection.
- Pre-pipeline auto-transition workflows

**Assumptions:** Up to 10 workflows. Outlook fix may require HubSpot support.

#### Workstream 8: Reporting & Dashboards
**20 median hours | $3,000**

**Customer Story:** Board reports take 1+ day. Andrea needs clonable partner dashboards. Jodi needs CEO-level visibility.

**Recommended Approach:**
- Build partner, seller, CEO/board, and pipeline health dashboards
- Configure up to 15 custom reports
- Set up report scheduling and export

**Assumptions:** 4 dashboards. All Andrea's requested metrics included.

#### Workstream 9: Email & Communication Fix
**6 median hours | $900**

**Customer Story:** Outlook emails log to every deal a contact is associated with.

**Recommended Approach:**
- Audit integration. Configure association rules.
- Domain exclusions. Validate with sample scenarios.

**Assumptions:** Root cause diagnosis week 1.

#### Workstreams 10-12: Training (Admin, End Users, Executive)
**17 median hours | $2,550**

**Customer Story:** Admin, sales team, and Jodi each need role-appropriate training on the reconfigured CRM.

**Recommended Approach:**
- 1-2 admin sessions: pipeline management, reporting, workflows, data hygiene
- 2-3 end-user sessions: daily CRM usage, deal entry, activity logging, dashboards, mobile
- 1 executive session: CEO dashboard, forecast consumption, board report scheduling

**Assumptions:** All sessions virtual. Recorded for future onboarding.

#### Workstream 13: UAT, Go-Live & Documentation (Phase 1)
**10 median hours | $1,500**

**Customer Story:** Controlled go-live with testing and 2-week hypercare.

**Recommended Approach:**
- Test scripts. 2 UAT sessions. Bug fix window.
- Go-live cutover plan. Admin guide + user guide.
- 2-week hypercare post-launch.

**Assumptions:** Phase 1 go-live. Phase 2 has separate UAT cycle.

#### Workstream 14: Project Management (Phase 1)
**18 median hours | $2,700**

**Customer Story:** Formal project management prevents scope creep and keeps all parties aligned.

**Recommended Approach:**
- Kickoff, weekly syncs, status updates, scope control
- Milestone reviews and change request process

**Assumptions:** ~12% of Phase 1 hours. Lesson learned from prior engagement.

**Phase 1 Subtotal: 177 median hours | $26,550**

---

### Phase 2: CPQ, Enrichment & Integrations (Weeks 9-18)

#### Workstream 15: CPQ Implementation
**45 median hours | $6,750**

**Customer Story:** STRIVE manually creates every quote. Pricing is inconsistent. Deals are quoted outside the CRM and never enter the pipeline, causing systematic under-reporting. Jodi sees CPQ as critical to de-risking contracts and capturing accurate pipeline data.

**Recommended Approach:**
- Build complete product library (apps, microsites, AI assistant, broker packs, Divi/rewards, bundles)
- Configure pricing models: license fees, revenue share, flat per-head, bundle discounts
- Design quote templates branded to STRIVE
- Configure e-signature capability within HubSpot
- Set up automated quote reminders for unsigned quotes
- Build quote-to-deal automation (auto-update deal amount and products on quote acceptance)

**Assumptions:**
- Requires complete product/pricing inventory from Andrea before build begins
- Multiple pricing models supported: license + rev share, flat per-head, bundles/discounts
- Uses HubSpot Enterprise CPQ capabilities (included in current license)
- Industry benchmark: 40-60 hours for CPQ rollout (Process Pro Consulting)

#### Workstream 16: Contract Management Workflows
**11 median hours | $1,650**

**Customer Story:** Contracts currently go through COO via DocuSign with no CRM tracking. Status is invisible in HubSpot.

**Recommended Approach:**
- Build quote-to-contract automation workflow
- Configure contract status tracking properties on deals
- Set up renewal and expiry notification workflows
- Establish contracting stage requirements (auto-advance on signature)

**Assumptions:** Replaces manual DocuSign process. Contract templates managed in HubSpot.

#### Workstream 17: Data Enrichment at Scale
**12 median hours | $1,800**

**Customer Story:** Phase 1 pilots AI enrichment on 500 records. Phase 2 scales it to the full database and sets up ongoing auto-enrichment for new contacts.

**Recommended Approach:**
- Scale HubSpot Breeze AI enrichment to full contact database
- Configure auto-enrichment rules for new inbound contacts
- QA and validate enrichment results across contact types
- Document enrichment accuracy and coverage metrics

**Assumptions:** Uses HubSpot Breeze credits (5-10K). Extends Phase 1 pilot to full database.

#### Workstream 18: Email Sequencing
**8 median hours | $1,200**

**Customer Story:** No email sequencing tool today. Reps do all outreach manually.

**Recommended Approach:**
- Build broker prospecting sequence (warm outreach to new broker contacts)
- Build microsite-to-app expansion sequence (upsell existing microsite clients)
- Configure up to 4 total sequences with enrollment triggers
- Set up sequence performance reporting

**Assumptions:** Uses HubSpot Sales Hub Enterprise sequences (included in current license).

#### Workstream 19: Marketing Automation Foundation
**11 median hours | $1,650**

**Customer Story:** STRIVE pays for Marketing Hub but runs zero campaigns. Contact classification (Phase 1) enables segmented outreach.

**Recommended Approach:**
- Design newsletter email template branded to STRIVE
- Build 2-3 segmented campaign workflows (by contact type: client, broker, prospect)
- Configure unsubscribe management and CAN-SPAM compliance
- Set up campaign performance reporting

**Assumptions:** Leverages Marketing Hub (already licensed). Depends on Phase 1 contact classification.

#### Workstream 20: Commission Visibility & Validation
**6 median hours | $900**

**Customer Story:** Andrea manages commissions in password-protected spreadsheets. Jodi needs to validate before release.

**Recommended Approach:**
- Build CRM-based commission view tied to closed-won deals and rep assignment
- Configure validation workflow: Jodi reviews and approves before release
- Create commission summary report by rep and time period

**Assumptions:** Visibility and validation only -- not a full commission calculation engine.

#### Workstream 21: NetSuite Integration Prep
**11 median hours | $1,650**

**Customer Story:** Jodi wants HubSpot data feeding NetSuite for month-end close. Clean CRM data is the prerequisite.

**Recommended Approach:**
- Document data readiness for API connection
- Create field mapping between HubSpot and NetSuite entities
- Identify data gaps that would block integration
- Produce integration readiness report with recommendations

**Assumptions:** PREP ONLY. Actual integration build requires separate SOW with NetSuite admin involvement.

#### Workstream 22: Bill.com Integration Prep
**6 median hours | $900**

**Customer Story:** Bill.com handles AR/AP. Integration with HubSpot would automate revenue recognition.

**Recommended Approach:**
- Document AR/AP field mapping requirements
- Assess data readiness for future integration
- Produce integration readiness report

**Assumptions:** PREP ONLY. Actual build requires separate SOW.

#### Workstream 23: Seat/License Optimization
**3 median hours | $450**

**Customer Story:** Mixed versions, unused seats, and unclear allocation across hubs.

**Recommended Approach:**
- Audit all 23 current seats across core, sales, and service hubs
- Identify unused or misallocated seats
- Produce cost savings recommendation with specific seat changes
- Verify CPQ and sequence capabilities on current Enterprise tier

**Assumptions:** Deliverable: cost savings memo. Does not include license procurement.

#### Workstream 24: Advanced Reporting
**11 median hours | $1,650**

**Customer Story:** Phase 2 data (CPQ, marketing, enrichment) feeds into expanded reporting.

**Recommended Approach:**
- Configure automated board report delivery (scheduled email)
- Build pipeline coverage vs. quota tracking
- Add pace-to-goal reporting
- Create marketing campaign ROI reporting

**Assumptions:** Extends Phase 1 dashboards with Phase 2 data sources.

#### Workstream 25: Additional Project Management (Phase 2)
**16 median hours | $2,400**

**Recommended Approach:**
- Phase 2 PM, weekly syncs, milestone reviews
- Change request management and hours tracking

**Assumptions:** ~12% of Phase 2 hours.

**Phase 2 Subtotal: 140 median hours | $21,000**

---

### Optional Add-On: Client Success Pipeline
**11 median hours | $1,650**

A Client Success pipeline to track client health, renewals, and billing integration is available as an optional add-on. This workstream requires a separate discovery call with the Client Success team to define requirements and is not included in the base project cost.

---

## 6. Deliverables & Timeline

| Phase / Week Range | Scope Highlights |
|-------------------|-----------------|
| Phase 1: Weeks 1-3 | CRM audit, contact classification rules, AI enrichment pilot, Outlook fix diagnosis, seat/license audit, parent-child structure |
| Phase 1: Weeks 4-6 | Full contact classification and cleanup, data normalization, deduplication, duplicate protection |
| Phase 1: Weeks 7-8 | Pipeline restructuring, deal health scoring, automations, dashboards, Phase 1 UAT and go-live |
| Phase 2: Weeks 9-12 | CPQ product library build, quote templates, e-signatures, contract workflows, full database enrichment |
| Phase 2: Weeks 13-16 | Email sequences, marketing automation, commission visibility, integration prep, advanced reporting |
| Phase 2: Weeks 17-18 | Phase 2 training, UAT, go-live, documentation, hypercare begins |

---

## 7. Engagement Model & Pricing

| Component | Model | Fee |
|-----------|-------|-----|
| Phase 1: CRM Foundation (Weeks 1-8) | Fixed Fee | $26,550 |
| Phase 2: CPQ + Enrichment + Integrations (Weeks 9-18) | Fixed Fee | $21,000 |
| **Project Total** | **Fixed Fee** | **$46,950** |

**Note:** Total median hours reflect 313 hours at $150/hr, calibrated against prior comparable engagement and industry benchmarks (CPQ: 40-60 hrs industry standard per Process Pro Consulting).

**Payment Terms:**
- Phase 1: 50% ($13,275) at Phase 1 kickoff, 50% ($13,275) at Phase 1 handoff
- Phase 2: 50% ($10,500) at Phase 2 kickoff, 50% ($10,500) at Phase 2 handoff
- Net-15 terms on all invoices

**Technology & Administrative Fee:** To help offset the costs of our technology stack and internal systems that improve project speed, quality, and efficiency, a 5% Technology & Administrative fee is applied to each invoice.

**Budget Flexibility:** Phase 1 can stand alone as a complete engagement at $26,550. If budget is constrained, STRIVE can approve Phase 1 only and engage Phase 2 as a separate project after demonstrating Phase 1 ROI to the board.

---

## 8. The Story for the Board

> "We have a HubSpot Enterprise license that we're paying for but not using. Ten years of data sitting in the CRM with no classification, no forecasting, no automation. Our sales leader spends more than a full day every month building board reports by hand. Deals are quoted in email and never enter the pipeline. We're flying blind.
>
> This investment fixes the foundation. Phase 1 gives us clean data, accurate pipeline reporting, and automated board dashboards within 8 weeks. Phase 2 adds quoting automation, AI-powered data enrichment, and prepares us for NetSuite integration -- all using tools we're already paying for.
>
> The investment pays for itself within 6 months through time savings alone. The real return is pipeline visibility, board-ready reporting without manual assembly, and the data infrastructure to scale the sales team and leverage AI.
>
> We're not buying new software. We're unlocking the software we already own."

---

## 9. Project Governance

### Sayer Responsibilities
- Lead configuration, QA, and implementation across all workstreams
- Conduct weekly check-ins and milestone reviews
- Provide documentation, training, and go-live support for each phase
- Manage project timeline and proactively communicate risks or blockers
- Deliver ROI tracking framework for post-project measurement
- Produce seat/license optimization memo with cost savings recommendations
- Deliver integration readiness reports for NetSuite and Bill.com

### STRIVE Responsibilities
- Designate 1 primary point of contact (Andrea recommended)
- Ensure Jodi and Andrea availability for discovery, UAT, and training
- Provide complete product/pricing inventory before Phase 2 CPQ build
- Provide contact classification rules and validate AI enrichment results
- Confirm deal stage definitions and probability framework
- Communicate standardized close won/lost reason categories
- Share 3-5 recent quotes/proposals across deal types for CPQ reference
- Mandate CRM usage across sales team (executive sponsorship critical)
- Complete UAT testing within agreed timeline for each phase
- Provide full HubSpot admin access
- Identify NetSuite admin contact for integration prep coordination
- Provide commission validation requirements and current spreadsheet structure

---

## 10. Assumptions & Constraints

- HubSpot Sales Hub Enterprise (existing instance -- reconfiguration)
- Up to 23 licensed users across core, sales, and service seats
- Outlook as primary email platform
- Up to 40 custom contact/company properties (expanded for CPQ and enrichment)
- 1 active sales pipeline with pre-pipeline separated
- 2 deal categories: partner-level and client-level
- Stage probability mapping using Jodi's framework
- AI enrichment using HubSpot Breeze credits (5-10K)
- Up to 12 automated workflows
- 4-5 dashboards with up to 20 custom reports
- Complete product/pricing inventory provided before Phase 2
- Marketing Hub leveraged for campaigns (already licensed)
- 16-18 week phased timeline
- Phase 1 can stand alone if Phase 2 is deferred
- Estimates calibrated against prior comparable engagement and industry benchmarks
- All work conducted remotely
- Scope changes managed through formal change request

### Out of Scope
- NetSuite integration build (prep only -- actual build requires separate SOW)
- Bill.com integration build (prep only)
- Client Success pipeline (available as optional add-on)
- Full commission calculation engine (visibility and validation only)
- Custom API development or middleware beyond HubSpot native
- Data migration from external systems (internal cleanup only)
- Ongoing managed services beyond 2-week hypercare per phase
- HubSpot license procurement or tier changes (recommendations provided)
- AI knowledge assistant for sales onboarding (future initiative)
- LinkedIn Sales Navigator integration (recommended for future)

---

## 11. Approval & Next Steps

Please confirm alignment on scope and structure so we can move forward with scheduling a formal kickoff and assigning your Sayer team.

If any scope areas, phasing, or pricing need to be adjusted, we welcome the conversation. This proposal is designed with budget flexibility -- Phase 1 can be approved independently with Phase 2 engaged after demonstrating ROI.

**To move forward with this engagement:**
1. Provide written approval of this proposal via email (full project or Phase 1 only)
2. Schedule project kickoff within 1-2 weeks of written approval

Upon written approval, Sayer will issue a Master Services Agreement (MSA) via DocuSign, with this Scope of Work included. Once the MSA is executed, Sayer will finalize the implementation plan and begin onboarding.
