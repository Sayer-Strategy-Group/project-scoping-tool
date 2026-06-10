---
name: systems-implementation-scoping
description: Generate professional implementation scoping packages from discovery notes. Use when the user provides discovery call notes, client requirements, or asks to scope a systems implementation project. Covers CRM (HubSpot, Salesforce, etc.), ERP (NetSuite, QuickBooks, etc.), marketing automation (Klaviyo, Mailchimp, etc.), phone/VoIP systems, data migrations, integrations, and multi-system projects. Outputs workstream-based hour estimates (min/max/median), risk registers, phased vs. concurrent approach comparisons, formatted Excel deliverables, and client-ready summaries.
---

# Systems Implementation Scoping Skill

Generate complete scoping packages from discovery notes for systems implementation projects.

## When to Use This Skill

Trigger when the user:
- Shares discovery call notes and asks to scope an implementation
- Asks to estimate hours for a CRM, ERP, or multi-system project
- Wants a risk register for a systems implementation
- Needs phased vs. concurrent approach comparison
- Asks for a scoping deliverable (Excel, summary, or SOW-ready estimates)
- Says "scope this", "estimate this project", or references client discovery notes

## Supported System Categories

This skill is NOT limited to one platform. It applies to any combination of:

| Category | Examples | Common Workstreams |
|----------|----------|--------------------|
| **CRM** | HubSpot, Salesforce, Zoho, Pipedrive | Pipeline setup, contact/company properties, lifecycle stages, automations, reporting, integrations |
| **ERP** | NetSuite, QuickBooks, SAP B1, Odoo | Chart of accounts, inventory, order management, AP/AR, reporting, data migration |
| **Marketing Automation** | Klaviyo, Mailchimp, HubSpot Marketing, ActiveCampaign | List migration, flow/automation setup, template design, segmentation, analytics |
| **Phone/VoIP** | Aircall, RingCentral, Dialpad, JustCall | Call routing, IVR setup, CRM integration, call recording, reporting |
| **Data/BI** | Metabase, Looker, Power BI, Tableau | Dashboard design, data modeling, source connections, calculated fields |
| **Integration/Middleware** | n8n, Zapier, Make, custom API | Endpoint mapping, field mapping, sync logic, error handling, monitoring |
| **Data Migration** | Any source → any target | Data audit, cleansing, dedup, mapping, test loads, validation, cutover |

## Workflow

### Step 1: Parse Discovery Notes

Extract structured information from raw discovery notes. Look for:

1. **Client Profile**
   - Company name, industry, size (employees, revenue if known)
   - Current systems and tools in use
   - Key stakeholders and decision-makers
   - Internal IT resources and their availability/authority

2. **Current State / Pain Points**
   - What's broken or manual today
   - Data fragmentation (where does data live now?)
   - Process gaps and workarounds
   - Compliance or regulatory requirements

3. **Desired Future State**
   - Systems to implement or migrate to
   - Key outcomes the client expects
   - Timeline expectations or hard deadlines
   - Budget signals (explicit or implied)

4. **Complexity Indicators** (flag these — they drive hour estimates)
   - Number of users
   - Number of data sources to migrate/integrate
   - Custom object or field requirements
   - Duplicate data or data quality issues
   - Multi-entity or multi-brand structures
   - ERP/accounting system involvement (always adds complexity)
   - Existing vendor lock-in or export fees
   - Stakeholder alignment concerns (who controls what)

5. **Unknowns and Blockers**
   - Missing information that affects scope
   - Dependencies on third parties
   - Unresolved decisions (e.g., which tier, which vendor)
   - Cost blockers (e.g., export fees, licensing)

**If discovery notes are sparse:** Ask the user ONE question at a time to fill critical gaps before generating estimates. Prioritize: system count, user count, data sources, and integration requirements.

### Step 2: Define Workstreams

Break the project into workstreams based on systems involved. Each workstream gets its own hour estimate.

**Standard Workstream Template:**

For each system in scope, apply relevant workstreams from this master list:

#### CRM Workstreams
- **CRM Architecture & Setup** — Tier selection rationale, portal config, user roles/permissions, team structure
- **Pipeline & Deal Management** — Pipeline stages, deal properties, required fields, stage automation, probability mapping
- **Contact & Company Management** — Properties (standard + custom), lifecycle stages, lead status, association labels, dedup strategy
- **Automations & Workflows** — Lead routing, task creation, stage-change triggers, notification workflows, SLA enforcement
- **Email & Communication** — Templates, sequences, connected inboxes, tracking, meeting links
- **Reporting & Dashboards** — Standard reports, custom reports, dashboards per role, KPI definitions
- **Integrations** — Each integration is its own line item (CRM↔ERP, CRM↔Phone, CRM↔Marketing, etc.)
- **Training & Adoption** — Admin training, end-user training by role, documentation, go-live support

#### ERP Workstreams
- **ERP Data Assessment** — Current state audit, data quality evaluation, export feasibility, cost analysis
- **Data Migration** — Extract, cleanse, transform, load, validate (per entity: contacts, products, transactions, etc.)
- **ERP Integration Build** — API mapping, sync logic, conflict resolution, error handling, monitoring
- **ERP Reporting Alignment** — Map finance model to CRM/operational reporting, reconciliation workflows

#### Marketing Automation Workstreams
- **Platform Setup & Configuration** — Account setup, domain auth, tracking, compliance (CAN-SPAM, GDPR)
- **List & Segment Migration** — Export, cleanse, import, segment rebuild, tag/property mapping
- **Flow & Automation Build** — Recreate or build new flows (welcome, abandoned cart, re-engagement, etc.)
- **Template Design** — Email templates, landing pages, forms (count × complexity)
- **Integration** — Connect to CRM, ecommerce, data warehouse

#### Phone/VoIP Workstreams
- **System Selection & Setup** — Vendor evaluation, number porting, IVR/routing design
- **CRM Integration** — Call logging, click-to-call, contact sync, activity tracking
- **Training** — Admin + end-user training, call scripts, escalation procedures

#### Data/BI Workstreams
- **Dashboard Design** — Requirements gathering, wireframe, build per dashboard
- **Data Source Connection** — Per source: connect, model, validate
- **Calculated Fields & Logic** — Custom metrics, derived fields, business logic

#### Cross-Cutting Workstreams
- **Project Management** — Kickoff, weekly syncs, status updates, change management (typically 10-15% of total hours)
- **Data Migration** — Per-source: audit, map, cleanse, test load, validate, cutover
- **User Acceptance Testing (UAT)** — Test scripts, user testing sessions, bug fixes, sign-off
- **Documentation & SOPs** — Process docs, admin guides, training materials
- **Go-Live & Hypercare** — Cutover plan, go-live support, 2-week post-launch monitoring

### Step 3: Estimate Hours

For each workstream, provide **min / max / median** hour estimates.

**Estimation Framework:**

| Complexity Factor | Low (min) | Medium (median) | High (max) |
|-------------------|-----------|------------------|------------|
| Users: 1-5 | Base hours | — | — |
| Users: 6-15 | +10-15% | — | — |
| Users: 16-50 | +20-30% | — | — |
| Users: 50+ | +40%+ | — | — |
| Data sources: 1 | Base | — | — |
| Data sources: 2-3 | +15-25% | — | — |
| Data sources: 4+ | +30-50% | — | — |
| Custom objects: 0-2 | Base | — | — |
| Custom objects: 3-5 | +10-20% | — | — |
| Custom objects: 6+ | +25%+ | — | — |
| Data quality: Clean | Base | — | — |
| Data quality: Moderate issues | +15-25% | — | — |
| Data quality: Significant issues/dedup | +30-50% | — | — |
| Multi-entity/brand | +20-40% per entity | — | — |
| ERP involvement | +25-50% complexity premium | — | — |

**Hour Ranges by Workstream (CRM baseline — adjust for platform and complexity):**

| Workstream | Small (1-5 users, simple) | Medium (6-15 users, moderate) | Large (16+ users, complex) |
|------------|---------------------------|-------------------------------|----------------------------|
| CRM Architecture | 4-8 hrs | 8-16 hrs | 16-24 hrs |
| Pipeline & Deals | 4-8 hrs | 8-14 hrs | 14-24 hrs |
| Contact/Company Mgmt | 4-8 hrs | 8-16 hrs | 16-28 hrs |
| Automations | 6-12 hrs | 12-24 hrs | 24-40 hrs |
| Email & Comms | 4-8 hrs | 8-14 hrs | 14-20 hrs |
| Reporting | 4-8 hrs | 8-16 hrs | 16-28 hrs |
| Integration (each) | 6-12 hrs | 12-24 hrs | 24-40 hrs |
| Training (per group) | 4-6 hrs | 6-10 hrs | 10-16 hrs |
| Data Migration (per source) | 8-16 hrs | 16-32 hrs | 32-60 hrs |
| Project Management | 8-12 hrs | 12-20 hrs | 20-32 hrs |

**ERP workstreams typically run 1.5-2x CRM equivalents** due to financial data sensitivity and reconciliation requirements.

**Always calculate:**
- Total min / max / median hours
- Rate modeling at $150/hr (or user's stated rate — ask if not known)
- Total cost range: min×rate through max×rate

### Step 4: Build Risk Register

For every project, generate a risk register. Each risk gets:

| Field | Description |
|-------|-------------|
| **Risk** | What could go wrong |
| **Severity** | 🔴 High / 🟡 Medium / 🟢 Low |
| **Likelihood** | High / Medium / Low |
| **Impact** | What happens if it materializes |
| **Mitigation** | How to prevent or reduce impact |
| **Owner** | Who is responsible (client, consultant, vendor, TBD) |

**Standard risks to always evaluate:**

1. **Data Quality Risk** — Source data is messy, duplicated, or incomplete
2. **Scope Creep** — Client requests additions mid-project without adjusting timeline/budget
3. **Stakeholder Availability** — Key decision-makers unavailable for reviews/approvals
4. **Third-Party Dependency** — Vendor delays, API limitations, export fees, licensing changes
5. **Integration Complexity** — API limitations, rate limits, data format mismatches
6. **Adoption Risk** — Users resist new system, revert to old workflows
7. **Data Migration Risk** — Data loss, corruption, or mapping errors during migration
8. **Timeline Risk** — Dependencies create sequential bottlenecks
9. **Budget Risk** — Unknowns (licensing, vendor fees, add-ons) inflate costs
10. **Resource Contention** — Internal IT bandwidth, shared resources, competing priorities

**Flag high-severity risks prominently.** If any risk is 🔴 High severity AND High likelihood, recommend a mitigation plan or phased approach to isolate the risk.

### Step 5: Generate Approach Comparison (When Applicable)

If the project involves multiple systems or has significant dependency risks, generate a comparison of approaches:

**Approach A: Concurrent (All systems at once)**
- Pros: Faster total timeline, single cutover, one training push
- Cons: Higher risk, more resources needed simultaneously, complex dependencies
- Best when: Systems are tightly coupled, client has strong internal IT, timeline pressure

**Approach B: Phased (System by system)**
- Pros: Lower risk per phase, learnings carry forward, easier change management
- Cons: Longer total timeline, multiple cutover events, temporary manual bridges
- Best when: Data quality concerns, limited internal resources, budget constraints, ERP involvement

**Comparison Matrix Format:**

| Dimension | Approach A | Approach B |
|-----------|-----------|-----------|
| Total Hours | X-Y | Phase 1: A-B + Phase 2: C-D |
| Total Cost | $X-$Y | Phase 1: $A-$B + Phase 2: $C-$D |
| Timeline | X weeks | Phase 1: Y weeks + Phase 2: Z weeks |
| Risk Level | High/Med/Low | High/Med/Low per phase |
| Dependencies | List | List per phase |
| Recommendation | When to choose this | When to choose this |

**Always include a recommendation** with reasoning tied to the client's specific risk factors.

### Step 6: Generate Excel Deliverables

**Before generating any Excel:** Load the Sayer brand spec AND the xlsx mechanics skill in that order.

1. **Brand spec (authoritative):** `skills/sayer-brand-guidelines/SKILL.md` (bundled in this repo) — colors, typography, application rules. If this doc and the bullets below ever conflict, the brand skill wins.
2. **Mechanics:** `skills/scope-project/references/excel-formatting.md` — sheet specs, openpyxl patterns (freeze panes, print areas, formulas), and the `brand_styles` import pattern.
3. **Shared style module (this repo):** `scripts/brand_styles.py` — the single source of truth for every generator in this repo. Import from it; never hard-code hex values. Add a `sys.path.insert` shim at the top of any new generator so it can `from brand_styles import ...`. Per-client generators (kept locally in each client folder) follow this pattern.

**Output one or more Excel workbooks with these sheets:**

#### Workbook: `{ClientName}_Scoping_Estimate.xlsx`

**Sheet 1: "Scoping Estimate"**
- Columns: Workstream | Description | Min Hours | Max Hours | Median Hours | Rate | Min Cost | Max Cost | Median Cost | Notes/Assumptions | Actual Hours | Actual Cost | Variance
- Totals row at bottom
- Rate modeling section (configurable rate cell with Cool Grey fill to signal user input)
- Forecast columns use the **primary header** (Sayer Yellow + black text). Actuals columns (Actual Hours / Actual Cost / Variance) use the **secondary header** (Grey 700 + white text). Two-tier hierarchy = forecast vs reality.

**Sheet 2: "Risk Register"**
- Columns: # | Risk | Severity | Likelihood | Impact | Mitigation | Owner | Status
- Severity fills (semantic — imported from `brand_styles.severity_fill()`): Red for High, **Sayer Yellow (#FEC700)** for Medium, Green for Low
- Filter-ready headers

**Sheet 3: "Assumptions & Exclusions"**
- Section 1: Scope Assumptions (what's included)
- Section 2: Out of Scope (explicit exclusions)
- Section 3: Client Responsibilities (what client must provide)
- Section 4: Open Items (unresolved questions that could affect scope)

**Sheet 4: "Approach Comparison" (if applicable)**
- Side-by-side comparison matrix
- "Option X only" rows use a light-yellow tint (`#FFF3B3`) as a semantic marker — brand-compliant kin of Sayer Yellow
- Recommendation section at bottom

**Formatting Standards (Sayer brand — enforced via `scripts/brand_styles.py`):**
- Font: **Calibri** 11pt body, Semibold 14pt title, Semibold 11pt headers. Rethink Sans is the Sayer brand font but does not survive xlsx conversion — Calibri is the sanctioned fallback (the same Calibri-fallback rule applies to docx).
- Primary header row: **Sayer Yellow (#FEC700) fill, black text (#000000), bold**
- Secondary header row (Actuals columns): **Grey 700 (#2E2E2E) fill, white text, bold**
- Alternating row shading: **Grey 300 (#E3E3E3)**
- Input cells (rate, actuals entry): **Cool Grey (#D6D6D6) fill** — one unified input affordance
- Borders: **Grey 500 (#BCBCBC) thin borders** on data cells
- Currency format: $#,##0
- Column widths: auto-fit with padding
- Freeze panes: top row + first column
- Print area set on all sheets
- Charts (if any): **Sayer Yellow primary series, Grey 500/600 for secondary series** — no non-brand colors

### Step 7: Generate Client-Ready Summary

Create a concise summary suitable for Slack, email, or SOW insertion. Format:

```
**{Client Name} — Implementation Scope Summary**

**Systems in Scope:** {list}
**Approach:** {Concurrent / Phased / TBD}
**Estimated Hours:** {min}–{max} hrs (median: {median})
**Estimated Investment:** ${min_cost}–${max_cost} (at ${rate}/hr)
**Estimated Timeline:** {X} weeks

**Workstream Breakdown:**
{Top-level workstream list with median hours each}

**Key Risks:**
{Top 3 risks with severity}

**Assumptions:**
{Top 3-5 critical assumptions}

**Outstanding Items (Need from Client):**
{List of open items/decisions needed}

**Recommendation:**
{1-2 sentences on recommended approach and why}
```

## Important Rules

1. **Never pad estimates.** Use honest ranges. The min/max spread IS the buffer.
2. **Always flag unknowns.** An unknown that isn't flagged becomes a scope bomb. Surface it.
3. **Separate what you know from what you're assuming.** Label assumptions explicitly.
4. **Rate is configurable.** Default to $150/hr but always ask or use the user's stated rate.
5. **One workstream per integration.** Don't lump integrations together — each has unique complexity.
6. **Data migration is per-source.** Each data source gets its own estimate.
7. **Training is per-audience.** Admin training ≠ end-user training ≠ executive training.
8. **ERP adds a complexity premium.** Financial data is unforgiving — always add buffer for reconciliation.
9. **Cap custom properties.** State the assumed cap (e.g., "up to 30 custom properties") — overages are change orders.
10. **Project management hours scale with project size.** Use 10-15% of total estimated hours.

## Deliverable Checklist

Before presenting to the user, verify all deliverables include:

- [ ] Workstream-level hour estimates (min/max/median)
- [ ] Rate modeling with configurable rate
- [ ] Risk register with severity ratings
- [ ] Assumptions and exclusions list
- [ ] Client responsibilities / what's needed from them
- [ ] Open items / unresolved questions
- [ ] Approach comparison (if multi-system or complex)
- [ ] Client-ready summary (Slack/email format)
- [ ] Excel workbook with consistent formatting

## Example Input → Output

**Input (Discovery Notes):**
> "Met with Acme Corp. 15-person team, currently using spreadsheets and QuickBooks. Want HubSpot CRM for sales pipeline, need to migrate 5,000 contacts from Mailchimp and integrate with QuickBooks for invoice sync. Also need Aircall for phone system integrated with HubSpot. Timeline: want live in 8 weeks."

**Output Structure:**
- 7 workstreams identified (CRM Setup, Pipeline, Contact Mgmt, Automations, Reporting, QB Integration, Aircall Integration, Mailchimp Migration, Training, PM)
- Hour range: 88-156 hrs (median ~122)
- 6 risks flagged (data quality from spreadsheets, QB API limitations, 8-week timeline tight, Mailchimp list health unknown, phone number porting timeline, adoption risk)
- Recommended approach: Phased — CRM + Mailchimp migration first (Weeks 1-5), then QB integration + Aircall (Weeks 4-8, overlapping)
- Excel workbook with 4 sheets
- Client summary ready for Slack/email
