# Requirements: HelloSpoke HubSpot CRM Implementation

**Defined:** 2026-04-16
**Core Value:** HelloSpoke's sales team has one system of record that connects pipeline, billing, commissions, and reporting.

## v1 Requirements

Requirements for this engagement. Each maps to roadmap phases.

### CRM Foundation

- [ ] **CRM-01**: Existing HubSpot instance audited and cleaned of legacy configuration
- [ ] **CRM-02**: User roles and permissions configured for 15-18 users across sales, ops, and bookkeeping
- [ ] **CRM-03**: Team structure and ownership rules established
- [ ] **CRM-04**: Sales pipeline redesigned with standardized stages, entry/exit criteria, and required fields
- [ ] **CRM-05**: Deal scoring model configured to prioritize pipeline opportunities
- [ ] **CRM-06**: Lead vs. deal vs. account definitions standardized across teams
- [ ] **CRM-07**: Contact and company properties configured for multifamily real estate vertical (up to 25 custom properties)
- [ ] **CRM-08**: Parent-child company associations built for portfolio management
- [ ] **CRM-09**: Custom objects created for Rev IO billing data and multifamily properties (up to 2)
- [ ] **CRM-10**: Deduplication strategy defined and merge rules established for Salesforce migration

### Data Migration

- [ ] **MIG-01**: Salesforce data audit completed — object inventory, record counts, data quality assessment
- [ ] **MIG-02**: Field mapping document created — Salesforce fields to HubSpot properties (up to 50 mappings)
- [ ] **MIG-03**: Phase A migration complete — inactive/closed customers and completed deals imported and validated
- [ ] **MIG-04**: Phase B migration complete — active pipeline (open deals, active accounts) imported and validated
- [ ] **MIG-05**: Phase C migration complete — leads and prospect data imported and validated
- [ ] **MIG-06**: Post-migration data integrity verified — record counts match, associations intact, no data loss
- [ ] **MIG-07**: Outdated/low-quality records archived rather than migrated

### Integrations

- [ ] **INT-01**: Rev IO REST API connection established with authentication and error handling
- [ ] **INT-02**: HubSpot custom object for Rev IO billing records created and associated with deals
- [ ] **INT-03**: Rev IO account, invoice, payment, and usage data syncing to HubSpot (one-way: Rev IO → HubSpot)
- [ ] **INT-04**: Webhook or batch sync mechanism operational for ongoing Rev IO data flow
- [ ] **INT-05**: QuickBooks Online OAuth2 authentication configured with token refresh handling
- [ ] **INT-06**: Revenue actuals from QuickBooks paid invoices syncing to HubSpot deal properties
- [ ] **INT-07**: Revenue reconciliation logic defined — QB vs. HubSpot source-of-truth rules documented
- [ ] **INT-08**: QuotaPath HubSpot-side data flow configured — deal properties and custom objects feed commission calculations
- [ ] **INT-09**: End-to-end data chain tested: Rev IO → HubSpot custom object → deal → QuotaPath
- [ ] **INT-10**: Sync monitoring and error alerting established for all integrations

### Enablement

- [ ] **ENB-01**: Up to 10 automated workflows deployed — lead routing, stage triggers, follow-ups, notifications
- [ ] **ENB-02**: Executive dashboard built — pipeline health, forecasting, revenue metrics
- [ ] **ENB-03**: Sales performance dashboard built — activity, conversion rates, deal velocity, actuals vs targets
- [ ] **ENB-04**: Admin training session delivered and recorded (Christina + ops team)
- [ ] **ENB-05**: Sales rep training session delivered and recorded
- [ ] **ENB-06**: Ops/bookkeeping training session delivered and recorded (integration views, billing data, commission visibility)
- [ ] **ENB-07**: Workflow quick-reference guides provided for each role

### Project Management

- [ ] **PM-01**: Kickoff meeting completed with timeline, milestones, and communication cadence aligned
- [ ] **PM-02**: Weekly status syncs conducted for duration of engagement
- [ ] **PM-03**: Project tracker maintained with workstream status, blockers, and milestones
- [ ] **PM-04**: Scope change requests managed through formal approval process
- [ ] **PM-05**: Cross-vendor coordination completed (QuotaPath, Rev IO, QuickBooks touchpoints)
- [ ] **PM-06**: Project handoff documentation delivered at engagement close

## v2 Requirements

Deferred to future engagement. Tracked but not in current roadmap.

### Future Integrations

- **FUT-01**: Elastic database integration for unified data layer and custom dashboards
- **FUT-02**: ALN multifamily property database sync for automated account creation
- **FUT-03**: ClickUp-to-HubSpot implementation status visibility for sales reps
- **FUT-04**: Zendesk integration for customer service visibility in CRM

### Advanced Features

- **ADV-01**: Native HubSpot CPQ build (if QuotaPath doesn't proceed)
- **ADV-02**: Campfire ERP integration (pending HelloSpoke's ERP evaluation)
- **ADV-03**: AI-powered data preprocessing for varied file format imports
- **ADV-04**: Advanced commission approval workflows beyond QuotaPath standard

## Out of Scope

| Feature | Reason |
|---------|--------|
| Elastic/ALN database integration | Jeremy de-scoped as future aspiration in March 26 call |
| Campfire ERP integration | ERP evaluation TBD on HelloSpoke's side |
| ClickUp-to-HubSpot sync | Removed per Kyle direction |
| Zendesk migration or integration | Not discussed as a need in discovery |
| Email template design / marketing automation | Not part of this engagement |
| Custom HubSpot UI extensions | Standard configuration only |
| Ongoing sync maintenance post-go-live | Engagement ends after hypercare |
| HubSpot licensing costs | Client responsibility |
| QuotaPath platform implementation | QuotaPath handles their own |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| CRM-01 | Phase 1 | Pending |
| CRM-02 | Phase 1 | Pending |
| CRM-03 | Phase 1 | Pending |
| CRM-04 | Phase 1 | Pending |
| CRM-05 | Phase 1 | Pending |
| CRM-06 | Phase 1 | Pending |
| CRM-07 | Phase 1 | Pending |
| CRM-08 | Phase 1 | Pending |
| CRM-09 | Phase 1 | Pending |
| CRM-10 | Phase 1 | Pending |
| PM-01 | Phase 1 | Pending |
| PM-02 | Phase 1 | Pending |
| PM-03 | Phase 1 | Pending |
| MIG-01 | Phase 2 | Pending |
| MIG-02 | Phase 2 | Pending |
| MIG-03 | Phase 2 | Pending |
| MIG-04 | Phase 2 | Pending |
| MIG-05 | Phase 2 | Pending |
| MIG-06 | Phase 2 | Pending |
| MIG-07 | Phase 2 | Pending |
| PM-04 | Phase 2 | Pending |
| INT-01 | Phase 3 | Pending |
| INT-02 | Phase 3 | Pending |
| INT-03 | Phase 3 | Pending |
| INT-04 | Phase 3 | Pending |
| INT-05 | Phase 3 | Pending |
| INT-06 | Phase 3 | Pending |
| INT-07 | Phase 3 | Pending |
| INT-08 | Phase 3 | Pending |
| INT-09 | Phase 3 | Pending |
| INT-10 | Phase 3 | Pending |
| PM-05 | Phase 3 | Pending |
| ENB-01 | Phase 4 | Pending |
| ENB-02 | Phase 4 | Pending |
| ENB-03 | Phase 4 | Pending |
| ENB-04 | Phase 4 | Pending |
| ENB-05 | Phase 4 | Pending |
| ENB-06 | Phase 4 | Pending |
| ENB-07 | Phase 4 | Pending |
| PM-06 | Phase 4 | Pending |

**Coverage:**
- v1 requirements: 38 total
- Mapped to phases: 38
- Unmapped: 0

---
*Requirements defined: 2026-04-16*
*Last updated: 2026-04-16 after roadmap creation — PM-02/03 assigned to Phase 1, PM-04 assigned to Phase 2*
