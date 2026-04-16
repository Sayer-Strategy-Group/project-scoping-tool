# Roadmap: HelloSpoke HubSpot CRM Implementation

## Overview

A 14-week consulting engagement migrating HelloSpoke from Salesforce to HubSpot CRM with a native HubSpot CPQ build and three integrated systems (Rev IO billing, QuickBooks Online revenue actuals, QuotaPath commissions). The engagement runs in four phases: establish the CRM foundation, migrate Salesforce data, build integrations and quoting, then enable the team and hand off a running system. Phase overlap is expected — migration begins while CRM configuration is being finalized, and integration/quoting build starts as migration validates.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: CRM Foundation** - Audit, configure, and design the HubSpot instance for HelloSpoke's team and pipeline
- [ ] **Phase 2: Salesforce Migration** - Audit SF data and execute phased migration of contacts, companies, deals, and activities
- [ ] **Phase 3: Integration & Quoting Build** - Connect Rev IO, QuickBooks, and QuotaPath to HubSpot with monitored data flows, and build the HubSpot native CPQ with e-signature
- [ ] **Phase 4: Enablement & Go-Live** - Deploy automations, build dashboards, train all user groups, and hand off the system

## Phase Details

### Phase 1: CRM Foundation
**Goal**: HubSpot is configured as HelloSpoke's CRM — correct users, pipeline, objects, and data model — ready to receive migrated data
**Depends on**: Nothing (first phase)
**Requirements**: CRM-01, CRM-02, CRM-03, CRM-04, CRM-05, CRM-06, CRM-07, CRM-08, CRM-09, CRM-10, PM-01, PM-02, PM-03
**Success Criteria** (what must be TRUE):
  1. All 15-18 users are provisioned with correct roles and team ownership rules in HubSpot
  2. The sales pipeline has defined stages with entry/exit criteria and required fields that the sales team recognizes as accurate
  3. Contact, company, and custom objects are configured with multifamily real estate properties and parent-child associations
  4. A deduplication strategy is documented and merge rules are configured before any Salesforce data is imported
  5. Kickoff is complete, weekly sync cadence is running, and a shared project tracker is live
**Plans**: TBD

### Phase 2: Salesforce Migration
**Goal**: All active and historical Salesforce data is in HubSpot, validated for integrity, with outdated records archived
**Depends on**: Phase 1
**Requirements**: MIG-01, MIG-02, MIG-03, MIG-04, MIG-05, MIG-06, MIG-07, PM-04
**Success Criteria** (what must be TRUE):
  1. A complete field mapping document (up to 50 mappings) exists before any data moves
  2. Inactive customers and closed deals are imported and verified — record counts match Salesforce exports
  3. Active pipeline (open deals and active accounts) is imported and every deal has correct stage, owner, and associations
  4. Leads and prospect records are imported with data quality flags resolved or archived
  5. Post-migration integrity check confirms no data loss and scope change process is in place for any discovered gaps
**Plans**: TBD

### Phase 3: Integration & Quoting Build
**Goal**: Rev IO, QuickBooks Online, and QuotaPath data flows are operational and monitored in HubSpot, and the sales team can configure, price, quote, and e-sign in HubSpot without admin intervention
**Depends on**: Phase 1 (partial overlap with Phase 2 permitted once custom objects exist)
**Weeks**: 5-11
**Requirements**: INT-01, INT-02, INT-03, INT-04, INT-05, INT-06, INT-07, INT-08, INT-09, INT-10, CPQ-01, CPQ-02, CPQ-03, CPQ-04, CPQ-05, CPQ-06, CPQ-07, CPQ-08, PM-05
**Success Criteria** (what must be TRUE):
  1. Rev IO billing data (accounts, invoices, payments, usage) is syncing to HubSpot custom objects and associated with deals via REST API
  2. QuickBooks paid invoice revenue actuals are appearing on HubSpot deal properties with documented source-of-truth reconciliation rules
  3. Sales reps can build standard quotes end-to-end without admin assistance; bulk imports of up to 300 line items succeed with clear validation
  4. HubSpot native e-signature is live, DocuSign is retired, and close-won automation syncs the final quoted amount to the deal amount
  5. QuotaPath can pull commission-relevant data from HubSpot deal properties and custom objects — end-to-end chain (Rev IO → HubSpot → QuotaPath) is tested
  6. All three integrations have error alerting and sync monitoring in place
  7. Cross-vendor coordination with QuotaPath, Rev IO, and QuickBooks touchpoints is complete and documented
**Plans**: TBD

### Phase 4: Enablement & Go-Live
**Goal**: HelloSpoke's team is trained, automations are running, dashboards are live, and the system is handed off with documentation
**Depends on**: Phase 2 (data in HubSpot), Phase 3 (integrations operational)
**Requirements**: ENB-01, ENB-02, ENB-03, ENB-04, ENB-05, ENB-06, ENB-07, PM-06
**Success Criteria** (what must be TRUE):
  1. Up to 10 automated workflows are live — lead routing, stage-change triggers, follow-up sequences, and notifications are firing correctly
  2. Executive and sales dashboards are published with pipeline health, forecasting, and actuals vs. targets visible to leadership
  3. All three user groups (admin/ops, sales reps, ops/bookkeeping) have completed recorded training sessions
  4. Each role has a quick-reference workflow guide and Christina (admin) can manage the system without Sayer assistance
  5. Project handoff documentation is delivered and the engagement is formally closed

## Progress

**Execution Order:**
Phases execute in numeric order with allowed overlap between Phase 1/2 and Phase 2/3 boundary weeks.

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. CRM Foundation | 0/TBD | Not started | - |
| 2. Salesforce Migration | 0/TBD | Not started | - |
| 3. Integration & Quoting Build | 0/TBD | Not started | - |
| 4. Enablement & Go-Live | 0/TBD | Not started | - |
