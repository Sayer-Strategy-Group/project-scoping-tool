# Workstream Catalog

## Supported System Categories

| Category | Examples | Common Workstreams |
|----------|----------|--------------------|
| **CRM** | HubSpot, Salesforce, Zoho, Pipedrive | Pipeline setup, contact/company properties, lifecycle stages, automations, reporting, integrations |
| **ERP** | NetSuite, QuickBooks, SAP B1, Odoo | Chart of accounts, inventory, order management, AP/AR, reporting, data migration |
| **Marketing Automation** | Klaviyo, Mailchimp, HubSpot Marketing, ActiveCampaign | List migration, flow/automation setup, template design, segmentation, analytics |
| **Phone/VoIP** | Aircall, RingCentral, Dialpad, JustCall | Call routing, IVR setup, CRM integration, call recording, reporting |
| **Data/BI** | Metabase, Looker, Power BI, Tableau | Dashboard design, data modeling, source connections, calculated fields |
| **Integration/Middleware** | n8n, Zapier, Make, custom API | Endpoint mapping, field mapping, sync logic, error handling, monitoring |
| **Data Migration** | Any source to any target | Data audit, cleansing, dedup, mapping, test loads, validation, cutover |

## CRM Workstreams

- **CRM Architecture & Setup** -- Tier selection rationale, portal config, user roles/permissions, team structure
- **Pipeline & Deal Management** -- Pipeline stages, deal properties, required fields, stage automation, probability mapping
- **Contact & Company Management** -- Properties (standard + custom), lifecycle stages, lead status, association labels, dedup strategy
- **Automations & Workflows** -- Lead routing, task creation, stage-change triggers, notification workflows, SLA enforcement
- **Email & Communication** -- Templates, sequences, connected inboxes, tracking, meeting links
- **Reporting & Dashboards** -- Standard reports, custom reports, dashboards per role, KPI definitions
- **Integrations** -- Each integration is its own line item (CRM-to-ERP, CRM-to-Phone, CRM-to-Marketing, etc.)
- **Training & Adoption** -- Admin training, end-user training by role, documentation, go-live support

## ERP Workstreams

- **ERP Data Assessment** -- Current state audit, data quality evaluation, export feasibility, cost analysis
- **Data Migration** -- Extract, cleanse, transform, load, validate (per entity: contacts, products, transactions, etc.)
- **ERP Integration Build** -- API mapping, sync logic, conflict resolution, error handling, monitoring
- **ERP Reporting Alignment** -- Map finance model to CRM/operational reporting, reconciliation workflows

## Marketing Automation Workstreams

- **Platform Setup & Configuration** -- Account setup, domain auth, tracking, compliance (CAN-SPAM, GDPR)
- **List & Segment Migration** -- Export, cleanse, import, segment rebuild, tag/property mapping
- **Flow & Automation Build** -- Recreate or build new flows (welcome, abandoned cart, re-engagement, etc.)
- **Template Design** -- Email templates, landing pages, forms (count x complexity)
- **Integration** -- Connect to CRM, ecommerce, data warehouse

## Phone/VoIP Workstreams

- **System Selection & Setup** -- Vendor evaluation, number porting, IVR/routing design
- **CRM Integration** -- Call logging, click-to-call, contact sync, activity tracking
- **Training** -- Admin + end-user training, call scripts, escalation procedures

## Data/BI Workstreams

- **Dashboard Design** -- Requirements gathering, wireframe, build per dashboard
- **Data Source Connection** -- Per source: connect, model, validate
- **Calculated Fields & Logic** -- Custom metrics, derived fields, business logic

## Cross-Cutting Workstreams

These apply to every project. Size them proportionally:

- **Project Management** -- Kickoff, weekly syncs, status updates, change management (typically 10-15% of total hours)
- **Data Migration** -- Per-source: audit, map, cleanse, test load, validate, cutover
- **User Acceptance Testing (UAT)** -- Test scripts, user testing sessions, bug fixes, sign-off
- **Documentation & SOPs** -- Process docs, admin guides, training materials
- **Go-Live & Hypercare** -- Cutover plan, go-live support, 2-week post-launch monitoring
