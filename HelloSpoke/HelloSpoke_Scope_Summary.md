# HelloSpoke -- HubSpot CRM Implementation Proposal

## 1. Executive Summary

HelloSpoke is migrating from Salesforce to HubSpot CRM to centralize sales operations, streamline billing and commission workflows, and improve reporting visibility. This proposal outlines a fixed-fee engagement covering CRM configuration, Salesforce data migration, a redesigned Configure-Price-Quote (CPQ) process, integration with Rev IO (billing), QuickBooks Online (accounting), and QuotaPath (commissions), plus sales process redesign, reporting, and team enablement.

The engagement is structured in four phases over 14 weeks, completing well ahead of HelloSpoke's October 2026 Salesforce contract expiration. Each phase has defined success criteria and deliverables, with phase overlaps that compress the timeline while managing risk.

## 2. Objectives

- Migrate all active contacts, companies, deals, and pipeline data from Salesforce to HubSpot CRM
- Redesign the sales pipeline with standardized stage definitions, entry/exit criteria, and deal scoring
- Build custom objects and properties for multifamily real estate data and Rev IO billing records
- Build a working CPQ process in HubSpot so reps can configure, price, quote, and e-sign without admin intervention -- including dynamic product templates, bulk line-item import, and parent-child property auto-creation
- Replace DocuSign with HubSpot native e-signature
- Integrate Rev IO billing data into HubSpot for commission tracking and operational visibility
- Connect QuickBooks Online for revenue actuals reporting and financial reconciliation
- Support QuotaPath implementation with HubSpot-side data flow architecture
- Automate lead routing, follow-up workflows, and stage-change notifications
- Deliver executive dashboards for pipeline, forecasting, and performance tracking
- Train admin, sales, and operations teams on the new system

## 3. Phased Scope of Work

### Phase 1: CRM Foundation (Weeks 1-4)

**Goal:** HubSpot is configured as HelloSpoke's CRM -- correct users, pipeline, objects, and data model -- ready to receive migrated data.

**Workstream 1.1: CRM Architecture & Setup**

*Customer Story:* HelloSpoke wants to reconfigure their existing HubSpot instance as a production-ready CRM environment to replace Salesforce.

*Deliverables:*
- Audit existing HubSpot instance for current configuration, users, and data
- Configure user roles, permissions, and team structure for 15-18 users
- Set up HubSpot branding, notification preferences, and connected inboxes
- Configure lifecycle stages, lead status values, and default properties
- Establish naming conventions and data governance rules

*Assumptions:* Existing HubSpot instance is relatively new with minimal legacy configuration. HubSpot Sales Hub Professional tier (or higher) is active. Includes up to 18 paid user seats.

**Workstream 1.2: Pipeline & Deal Management**

*Customer Story:* HelloSpoke needs a redesigned sales funnel with clear stage definitions so reps use it consistently and leadership can trust pipeline reporting.

*Deliverables:*
- Conduct sales process workshop to define pipeline stages and entry/exit criteria
- Build custom deal pipeline for VoIP and SaaS product sales
- Configure deal properties for product specifications, MRR, and contract terms
- Implement deal scoring to prioritize pipeline opportunities
- Define lead vs. deal vs. account terminology aligned across teams

*Assumptions:* Includes one primary sales pipeline. Includes up to 30 custom deal properties. Sales process workshop is virtual, up to 2 hours.

**Workstream 1.3: Contact & Company Management**

*Customer Story:* HelloSpoke needs clean, well-structured contact and company records with multifamily real estate context and parent-child relationships for portfolio tracking.

*Deliverables:*
- Configure contact and company properties specific to multifamily real estate and VoIP
- Build custom objects for multifamily property associations and Rev IO billing data (up to 2)
- Set up parent-child company structures for portfolio management
- Design deduplication strategy for Salesforce migration (unique identifiers, merge rules)
- Configure association labels and relationship types

*Assumptions:* Includes up to 25 custom contact/company properties. Deduplication handled during migration, not as an ongoing automated process.

**Phase 1 Success Criteria:**
1. All 15-18 users provisioned with correct roles and team ownership rules
2. Sales pipeline has defined stages with entry/exit criteria the sales team recognizes as accurate
3. Contact, company, and custom objects configured with multifamily real estate properties and parent-child associations
4. Deduplication strategy documented and merge rules configured before any data imports
5. Kickoff complete, weekly sync cadence running, shared project tracker live

---

### Phase 2: Salesforce Migration (Weeks 3-6)

**Goal:** All active and historical Salesforce data is in HubSpot, validated for integrity, with outdated records archived.

**Workstream 2.1: Data Audit & Mapping**

*Customer Story:* HelloSpoke wants to understand exactly what's in Salesforce and how it maps to HubSpot before any data moves.

*Deliverables:*
- Conduct Salesforce data audit: object inventory, record counts, data quality assessment
- Map Salesforce fields to HubSpot properties (up to 50 field mappings)
- Identify and flag duplicate records, orphaned data, and quality issues
- Document archival decisions for outdated/low-quality records

**Workstream 2.2: Phased Data Migration**

*Customer Story:* HelloSpoke wants data migrated safely in batches with validation at each step, avoiding "garbage in, garbage out."

*Deliverables:*
- Phase A: Inactive/closed customers and completed deals -- import and validate
- Phase B: Active pipeline (open deals, active accounts) -- import and validate
- Phase C: Leads and prospect data -- import and validate
- Post-migration data integrity verification: record counts match, associations intact, no data loss

*Assumptions:* Total records under 50,000 across all objects. Salesforce data exportable in standard CSV format. HelloSpoke provides Salesforce admin access for audit. Up to 2 test loads before final cutover per phase.

**Phase 2 Success Criteria:**
1. Complete field mapping document exists before any data moves
2. Inactive customers and closed deals imported and verified -- record counts match SF exports
3. Active pipeline imported with every deal having correct stage, owner, and associations
4. Leads and prospects imported with data quality flags resolved or archived
5. Post-migration integrity check confirms no data loss; scope change process in place

---

### Phase 3: Integration & Quoting Build (Weeks 5-11)

**Goal:** Rev IO, QuickBooks Online, and QuotaPath data flows are operational and monitored in HubSpot, and the sales team can configure, price, quote, and collect signatures in HubSpot without admin intervention.

**Workstream 3.1: Rev IO Integration**

*Customer Story:* HelloSpoke needs billing and usage data from Rev IO visible in HubSpot so sales and operations can track account health, and commission data flows to QuotaPath.

*Deliverables:*
- Investigate Rev IO REST API (v1) documentation, authentication (Basic Auth), and available endpoints
- Set up Rev IO sandbox environment for development and testing
- Build HubSpot custom object to store billing records (invoices, payments, usage)
- Develop sync logic: Rev IO account/invoice data to HubSpot custom object to deal association
- Configure webhook subscriptions or batch sync for ongoing data flow
- Build error handling, logging, and monitoring for ongoing sync

*Assumptions:* HelloSpoke provides Rev IO API credentials and sandbox access. Integration is one-way: Rev IO to HubSpot. Includes up to 30 field mappings. Webhook testing requires production environment (Rev IO sandbox limitation).

**Workstream 3.2: QuickBooks Online Integration**

*Customer Story:* HelloSpoke needs revenue actuals from QuickBooks visible alongside pipeline data in HubSpot for accurate forecasting and commission validation.

*Deliverables:*
- Evaluate HubSpot's native QuickBooks integration for baseline capability
- Build custom revenue sync: QuickBooks paid invoices to HubSpot deal properties
- Configure OAuth 2.0 authentication and token refresh handling
- Build reconciliation logic to handle QB vs. HubSpot revenue discrepancies
- Define "source of truth" rules (which system is authoritative for which metric)

*Assumptions:* HelloSpoke provides QuickBooks Online admin access and API credentials. Native integration may be used for basic sync; custom integration required for revenue actuals. Integration focus is QB to HubSpot (revenue data).

**Workstream 3.3: CPQ & Quoting (HubSpot CPQ Native)**

*Customer Story:* HelloSpoke's sales reps need to build quotes independently -- today, quoting is a bottleneck (Jeremy has to help on most quotes, CSV errors are cryptic, and the current tool creates duplicate property records). The new HubSpot CPQ process must handle two product lines, bulk property management quotes (up to 300 line items), dynamic terms and conditions per product, and native e-signature -- with final quoted amounts auto-syncing back to the deal on close-won.

*Deliverables:*
- Configure HubSpot CPQ with the HelloSpoke product library: VoIP setup fees, VoIP monthly recurring charges, equipment charges, Notify SaaS per-property pricing, and bundled packages (up to 50 products)
- Build two primary quote templates with product-driven terms and conditions: one VoIP template, one Notify (SaaS) template, plus a combined template for customers taking both services on a single bill
- Build a bulk line-item import path for property management deals (CSV upload, up-front validation, clear error messaging, up to 300 line items per quote)
- Configure parent-child property auto-creation from quote line items with deduplication logic so re-quoting an existing property does not create duplicate sub-accounts
- Configure a quote approval workflow with up to two approval tiers (rep self-serve for standard pricing; routed approval for non-standard pricing)
- Replace DocuSign with HubSpot native e-signature (including template setup for MSAs, NDAs, and SOWs)
- Build close-won automation: final quoted amount auto-syncs to the deal amount on signature return; close date auto-updates to signature date
- Configure the handoff from closed-won quote to Rev IO billing record creation (feeds Workstream 3.1)
- Train the admin and rep teams on quote creation, bulk import, and approval flow; document configuration for future product and T&C updates

*Assumptions:* HubSpot Sales Hub Professional (or Commerce Hub) tier supports the required quote customization and product library. HubSpot AI CPQ features are active on HelloSpoke's instance and stable enough for production use by go-live. DocuSign is being sunsetted by HelloSpoke (no parallel run required). Up to 2 dynamic quote templates plus 1 combined template. Approval workflow supports up to 2 tiers. Bulk import supports up to 300 line items per quote. If HubSpot CPQ capabilities fall short during build, PandaDoc integration can be scoped as a change order.

**Workstream 3.4: QuotaPath Coordination**

*Customer Story:* HelloSpoke is implementing QuotaPath for commission tracking and needs HubSpot configured to feed the right deal, billing, and property data into QuotaPath's system for commission calculation.

*Deliverables:*
- Design data flow architecture: Rev IO to HubSpot custom object to deal properties to QuotaPath
- Configure deal properties required for QuotaPath commission calculations (MRR, commission type, rep assignment)
- Coordinate with QuotaPath implementation team on field mapping and data format
- Test end-to-end data chain with sample deal and billing transactions

*Assumptions:* QuotaPath handles their own platform implementation. Sayer's role is HubSpot-side configuration and data flow architecture. QuotaPath deal closes and begins implementation in parallel. If QuotaPath does not proceed, the HubSpot-side commission data architecture can be repurposed for internal reporting.

**Phase 3 Success Criteria:**
1. Rev IO billing data syncing to HubSpot custom objects and associated with deals via REST API
2. QuickBooks paid invoice revenue actuals appearing on HubSpot deal properties with documented reconciliation rules
3. Sales reps can build standard quotes end-to-end without admin assistance; bulk imports of up to 300 line items succeed with clear validation
4. HubSpot native e-signature is live, DocuSign is retired, and close-won automation syncs quoted amount to deal amount
5. QuotaPath can pull commission data from HubSpot -- end-to-end chain tested
6. All three integrations have error alerting and sync monitoring in place
7. Cross-vendor coordination with QuotaPath, Rev IO, and QuickBooks is complete and documented

---

### Phase 4: Enablement & Go-Live (Weeks 10-14)

**Goal:** HelloSpoke's team is trained, automations are running, dashboards are live, and the system is handed off with documentation.

**Workstream 4.1: Automations & Workflows**

*Customer Story:* HelloSpoke wants to automate as much outreach and administrative work as possible so reps can focus on selling.

*Deliverables:*
- Build lead routing workflows based on territory, product line, or round-robin
- Configure stage-change automations (task creation, notifications, required actions)
- Set up follow-up sequence automation for new leads and stalled deals
- Build internal notification workflows for deal milestones and escalations

*Assumptions:* Includes up to 10 automated workflows. Uses HubSpot Professional workflow capabilities.

**Workstream 4.2: Reporting & Dashboards**

*Customer Story:* HelloSpoke leadership needs real-time dashboards that accurately reflect sales performance, pipeline health, and revenue gaps.

*Deliverables:*
- Build executive dashboard with pipeline, forecasting, and revenue metrics
- Create sales performance dashboard (activity, conversion rates, deal velocity)
- Configure actuals-vs-targets reporting using QuickBooks revenue data
- Set up scheduled report delivery to leadership

*Assumptions:* Includes up to 2 dashboards with 10+ reports each. Commission reporting handled within QuotaPath.

**Workstream 4.3: Training & Adoption**

*Customer Story:* HelloSpoke wants their team confident using HubSpot from day one, with training tailored to each role's daily workflow.

*Deliverables:*
- Session 1: Admin training (Christina + ops team) -- system config, data management, reporting
- Session 2: Sales rep training -- daily workflows, pipeline management, activity logging
- Session 3: Operations/bookkeeping -- integration views, billing data, commission visibility
- Record all sessions for future onboarding reference
- Provide workflow quick-reference guides for each role

*Assumptions:* Sessions scheduled within two weeks of go-live. Delivered virtually. Additional sessions beyond 3 can be scoped separately.

**Phase 4 Success Criteria:**
1. Up to 10 automated workflows live and firing correctly
2. Executive and sales dashboards published with pipeline, forecasting, and actuals vs. targets
3. All three user groups have completed recorded training sessions
4. Christina (admin) can manage the system without Sayer assistance; each role has a quick-reference guide
5. Project handoff documentation delivered and engagement formally closed

---

## 4. Project Management (Cross-Phase)

- Host kickoff meeting to align on timeline, milestones, and communication cadence
- Conduct weekly 30-minute status syncs with project stakeholders
- Maintain project tracker with workstream status, blockers, and upcoming milestones
- Manage scope change requests through formal approval process
- Coordinate across QuotaPath, Rev IO, and QuickBooks vendor touchpoints
- Deliver project handoff documentation at engagement close

## 5. Deliverables & Timeline

| Phase | Weeks | Key Deliverables |
|-------|-------|-----------------|
| 1: CRM Foundation | 1-4 | HubSpot configured, pipeline designed, custom objects live, dedup strategy |
| 2: Salesforce Migration | 3-6 | Field mapping, 3-phase migration, validation, archival |
| 3: Integration & Quoting Build | 5-11 | Rev IO sync, QuickBooks revenue actuals, HubSpot CPQ with e-sig and bulk quoting, QuotaPath data flow |
| 4: Enablement & Go-Live | 10-14 | 10 workflows, 2 dashboards, 3 training sessions, handoff docs |

**Total timeline:** 14 weeks from kickoff
**Target completion:** Before August 2026 (providing 2+ month buffer before October Salesforce contract end)

## 6. Engagement Model & Pricing

**Model:** Fixed Fee

**Total Investment (Full Scope, Phases 1-4):** $42,000

**Project Timeline:** 14 weeks

**Payment Terms:**
- Equal installments of $14,000 every 15 days (3 payments)
- Net-15 terms on all invoices
- Technology & Administrative Fee: 5% applied to each invoice to offset costs of project tooling, quality systems, and internal infrastructure

**Optional Reduced Scope (CRM Foundation Only -- Phases 1-2):**
- Includes: CRM configuration, pipeline design, Salesforce migration
- Excludes: Rev IO integration, QuickBooks integration, CPQ build, QuotaPath coordination
- Total Investment: $22,000
- Project Timeline: 8 weeks
- Payment Terms: Equal installments of $11,000 (2 payments), net-15
- 5% Technology & Administrative Fee applied
- Integrations and CPQ (Phases 3-4) can be scoped as a follow-on engagement

## 7. Project Governance

**Sayer Responsibilities:**
- Lead CRM configuration, integration development, and data migration
- Host weekly check-ins and progress reviews
- Deliver documentation, training sessions, and walkthroughs
- Manage project timeline and escalate blockers proactively
- Coordinate with QuotaPath vendor team on HubSpot-side requirements
- Deliver CPQ configuration including product library, dynamic templates, bulk import, approval workflow, and native e-signature migration off DocuSign

**HelloSpoke Responsibilities:**
- Provide access to HubSpot, Salesforce, Rev IO, QuickBooks, and relevant data sources
- Assign project liaison (Christina Edwards) for approvals and feedback
- Provide Rev IO and QuickBooks API credentials and sandbox access
- Attend milestone reviews, sales process workshop, and training sessions
- Provide Salesforce data exports and field mapping support
- Deliver detailed dashboard/reporting requirements (Jeremy Wiley)
- Communicate scope changes through formal change request process

## 8. Assumptions & Constraints

- HelloSpoke maintains required HubSpot licenses (Sales Hub Professional or higher recommended; Commerce Hub if required by HubSpot for AI CPQ features)
- HubSpot AI CPQ features are enabled and stable on HelloSpoke's instance by the start of Phase 3
- Salesforce data volume is under 50,000 records; data is exportable in standard CSV format
- Rev IO REST API is accessible and documented; sandbox available for testing
- QuickBooks Online API access provided with admin credentials
- QuotaPath proceeds with their own implementation on a parallel timeline
- HelloSpoke sunsets DocuSign in favor of HubSpot native e-signature (no parallel run required)
- Scope assumptions listed in each workstream define the boundaries of this engagement
- All work is remote unless otherwise agreed
- Scope changes require formal written approval and may impact cost or timeline
- Engagement assumes kickoff within 2 weeks of written approval

## 9. Key Risks

| # | Risk | Severity | Likelihood | Impact | Mitigation |
|---|------|----------|------------|--------|------------|
| 1 | Salesforce data quality worse than expected | High | Medium | Migration hours exceed estimate; duplicates propagate | SF data audit in Phase 2 before migration; phased approach with validation |
| 2 | Rev IO API limitations or poor documentation | High | Medium | Integration scope increases; custom workarounds needed | API investigation early in Phase 3; sandbox testing first |
| 3 | Existing HubSpot instance has legacy config | Medium | Medium | Cleanup adds hours to Phase 1 | Instance audit in Week 1; flag conflicts before building new config |
| 4 | HubSpot AI CPQ features unstable or missing needed functionality | High | Medium | CPQ scope shifts to PandaDoc as change order; delays Phase 3 | Validate HubSpot AI CPQ capabilities in Week 1 of Phase 3 before building; PandaDoc scoped as fallback change order |
| 5 | QuotaPath deal falls through | Medium | Low | Commission tracking deferred; HubSpot-side config repurposed for internal reporting | HubSpot data flow architecture delivers value regardless of QuotaPath outcome |
| 6 | Stakeholder availability for workshops/reviews | Medium | Medium | Delays in Phase 1 pipeline design, Phase 3 quoting workshop, Phase 4 training | Weekly cadence at kickoff; Christina as dedicated liaison |
| 7 | QuickBooks revenue reconciliation complexity | Medium | Medium | Discrepancies between QB and HubSpot figures | Define source-of-truth rules in Phase 3; reconciliation dashboard |
| 8 | Bulk quote import edge cases (300+ line items, state/zip validation) | Medium | High | CPQ import fails for property management deals in production | Early validation harness with HelloSpoke's actual quote CSVs; clear error messaging design reviewed with Ryan |
| 9 | Salesforce contract timeline pressure | Low | Low | October deadline creates urgency if project slips | 14-week timeline targets August; 2+ month buffer |
| 10 | Sales team adoption resistance | Medium | Medium | Reps revert to old workflows | Role-tailored training in Phase 4; simplified data entry; deal scoring |
| 11 | Scope creep from adjacent systems | Medium | High | Elastic/ALN, Campfire, Zendesk added mid-project | Explicit exclusions documented; formal change order process |
| 12 | Rev IO sandbox webhook limitation | Low | High | Can't test real-time events until production | Plan production cutover in Phase 3; batch sync as interim |

## 10. Approval & Next Steps

To move forward with this engagement:

1. Email written approval of the Full Scope proposal or the Optional Reduced Scope
2. Confirm HubSpot instance tier and provide portal access
3. Provide Rev IO API credentials and sandbox access
4. Provide QuickBooks Online admin access
5. Schedule kickoff meeting within 1-2 weeks of approval

Upon approval, Sayer will deliver a detailed project plan with weekly milestones and workstream dependencies.
