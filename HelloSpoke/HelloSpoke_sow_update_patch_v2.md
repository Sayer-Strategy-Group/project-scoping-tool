# HelloSpoke — V3 SOW / Proposal Rescope

**Version:** v3 (rescope, not a patch)
**Date:** 2026-05-07
**Author:** Kyle / Sayer
**Supersedes:**
- `HelloSpoke_sow_update_patch.md` (v2 patch, 2026-04-23)
- `HelloSpoke_clickup_workstream.md` (ClickUp integration addendum, 2026-04-23)
- 4/24 Gamma deck `https://gamma.app/docs/erumqig7pyx7rhm` (will be replaced by new v3 deck)

**Source call:** Fireflies `01KQSVGHKNQ1PM7X5ZPWJ4GJJK` (2026-05-04 walkthrough call, 23 min)
**Decisions log entry:** `HelloSpoke_decisions.md` lines 101–133

---

## Why This Is a Rescope, Not a Patch

On the 2026-05-04 walkthrough call, Jeremy asked to redirect the engagement away from data-plumbing work he has already built himself (Rev IO integration, basic ClickUp deal-won automation, Salesforce data dump, ALN, QuickBooks) and toward the work he can't do himself: **configuration, automation, UX, and enablement.**

The composition of the engagement is changing materially — not just the dollar amount. Five integration build workstreams come out; three new/elevated configuration workstreams come in; hours redistribute across phases. v3 is treated as a new proposal so the client artifacts read coherently rather than as a red-lined v2.

**Pricing direction (confirmed with Kyle 2026-05-05):** pass savings through to client. Target landing zone $27–32k base at $175/hr, ~150–180 hrs. Final number aligned with Cameron before delivery (he is deal owner).

---

## Strip / Add / Keep Summary

### STRIP — out of v3 scope (Jeremy did it himself or said no)

| Was in v2 | Why out of v3 | Source quote |
|---|---|---|
| Rev IO integration build | Already syncing every 30 min; custom objects already created in sandbox | "I have it sinking every half hour... I just created custom objects for it" |
| ClickUp integration build (v2 Workstream 11, $4,800) | Basic deal-won → ClickUp task creation built; native integration already wired | "I built an automation so when a deal is closed won, it creates it in ClickUp" |
| Salesforce → HubSpot data migration build | Already dumped into sandbox; Sayer reduces to QA review only | "I dumped it all... pulled everything from Salesforce and dumped it all into the sandbox" |
| QuickBooks integration | Jeremy says not needed; financial data lives in Rev IO | "I don't think we need to, honestly. Most of the financial data... they're being processed in Rev" |
| ALN integration | Jeremy is finalizing himself this week | "I have the ALN integration going. They're supposed to finalize that this week" |
| Make middleware (v2 Workstream 11) | Eliminated with the ClickUp integration build | n/a |
| HubSpot onboarding form replacing ClickUp form (v2) | Out with the integration build workstream | n/a |
| Mandatory field gating (v2 W11a optional) | Folded into W3 Sales Stage Definitions + Gating in v3 (not a separate optional line) | Carries forward as a baseline workstream task |

### ADD / ELEVATE — new or elevated v3 workstreams

| Workstream | Why | Source quote |
|---|---|---|
| **Data QA + Pre-Production Audit** | Replaces all stripped integration build hours. Sayer reviews sandbox, validates data integrity, object/property mapping, associations, custom-object structure; designs error handling + rollback plan; green-lights production push. | "Just go and do a QA check right before actually thinking about pushing anything in production" |
| **HubSpot Foundational Architecture** | Cameron asked, Jeremy said yes. Objects, pipelines, lead status, lifecycle stages, properties become a named workstream. | Cameron: "Are you still wanting us to go through and... set up all of your objects and looking at pipeline stages, lead status, lifecycle stages?" Jeremy: "I think we're open to it." |
| **Quoting & CPQ Workflow (Commerce Hub)** | Jeremy's #1 named priority. CSV upload pain, validation rules, property mapping, Commerce Hub CPQ. | "The big ones are the quoting like making sure that the reps can quote easily. Right now... they have such a hard time with it [the CSV]" |
| **DocuSign Replacement Evaluation + Setup** | Jeremy is killing DocuSign. Commerce Hub native signature is the leading candidate (recommended by Cameron); PandaDoc is the backup if non-quote document signing is needed. | "I told DocuSign to eat a dick" |
| **Reporting & Dashboards (elevated to named priority)** | Jeremy's "make it useful" pillar. Was secondary in v2; named priority in v3. | "It's not helpful if it's not in the right spot, if the views don't look right" |

### KEEP — carry forward from v2, possibly with adjusted hours

| Workstream | v3 treatment |
|---|---|
| Sales Stage Definitions + Gating | Kept; gating folded in (was v2 W11a optional) |
| Automations & Workflows | Kept; broadened to deal-stage + lifecycle + customer-journey |
| ClickUp workflow | **Pivots from integration build → workflow refinement.** Integration exists; what's needed is workflow correctness, gating, who-does-what. |
| Training & Enablement | Kept; admin + end-user tracks |
| UAT & Go-Live | Kept; test matrix, hypercare |
| Project Management | Kept; ~10% overhead |

### PENDING — Jeremy's decisions by EOW 2026-05-08

- **QuotaPath integration** — surfaced in v3 as an explicit optional checkbox add-on; v3 ships without waiting on Jeremy's answer
- **Signature tool** — Commerce Hub native vs PandaDoc; resolution may eliminate the W5 line entirely if Commerce Hub native covers everything

---

## v3 Workstream Rebuild

### W1: HubSpot Foundational Architecture

**Customer Story:** HelloSpoke is migrating from Salesforce to HubSpot. The CRM only delivers value if its bones — objects, pipelines, lead status, lifecycle stages, properties — are configured to match how HelloSpoke actually sells, implements, and renews. The team needs an opinionated foundation, not a blank canvas.

**Recommended Approach:**
- Confirm HubSpot tier (Sales Hub Professional minimum; Commerce Hub Professional required for W4 quoting)
- Configure standard objects: Companies, Contacts, Deals; review existing custom objects from Jeremy's sandbox build
- Build sales pipeline with the stages Sara delivers (post sales-team validation)
- Configure lead status values + lifecycle stage progression rules
- Property strategy: required vs optional, snake_case naming, group organization, archival of redundant Salesforce-era properties
- Team/permission structure aligned with sales + ops + leadership roles
- Documentation of architecture decisions for the admin playbook

**Assumptions:**
- HelloSpoke is on Sales Hub Professional or Enterprise (validate during kickoff)
- Object/property catalog from Jeremy's sandbox is available for reference
- Sara delivers finalized sales-stage definitions before W1 build starts
- One sales pipeline + one implementation/onboarding pipeline (no multi-currency, no multi-region complexity)

---

### W2: Data QA + Pre-Production Audit

**Customer Story:** Jeremy has already pulled Salesforce data and Rev IO data into the HubSpot sandbox. Before any of it goes to production, HelloSpoke needs an independent QA review — someone who didn't build it — to validate data integrity, association coverage, and that nothing is going to break the moment users start touching records.

**Recommended Approach:**
- Sandbox access + initial inventory (record counts, object coverage, age of data)
- Data integrity audit: completeness, dedupe candidates, formatting consistency, null-rate review on critical fields
- Object/property mapping validation: source-to-target field mapping correctness, no orphaned values, type coercion verified
- Association validation: Contact↔Company↔Deal coverage; custom-object associations verified
- Custom-object structure review: schema correctness, association labels, pipeline alignment
- Error handling + rollback plan: documented cutover sequence, fail-safe checkpoints, rollback procedure if production push fails
- Production-push green-light memo to Jeremy

**Assumptions:**
- Jeremy grants Sayer access to HubSpot sandbox before W2 begins (open item from 5/4)
- Data already loaded into sandbox; Sayer is auditing, not migrating
- Rev IO custom-object schema already built; Sayer validates, doesn't redesign
- Up to 2 rounds of audit findings + remediation; further rounds are change orders
- Sayer is not responsible for the original migration build or for fixing pre-existing data quality issues at the Salesforce source — only for surfacing them and recommending remediation

---

### W3: Sales Stage Definitions + Gating

**Customer Story:** Sales reps need a pipeline that matches how HelloSpoke actually sells, with handoffs to implementation and billing that don't drop information. Jeremy has been clear: required fields enforced at the right gates, so deals can't advance without the data the next team needs.

**Recommended Approach:**
- Workshop with Sara + Christina to lock final sales-stage definitions (Sara is delivering this week, post sales-team validation)
- Build stages in the HubSpot sales pipeline with the agreed names, probabilities, and stage-entry/exit criteria
- Configure required-field gating at two handoffs:
  - Sales → Implementation (closed-won transition): up to 10 required fields
  - Implementation → Billing: up to 10 required fields
- Workflow validation that surfaces the specific missing field to the rep when advance is attempted
- Stuck-deal HubSpot report for leadership showing records blocked at each gate
- Document gating rules in admin playbook

**Assumptions:**
- Sara delivers finalized sales-stage definitions in week 1 of delivery
- Up to 10 required fields per gate, 2 gates total
- Hard-block (workflow-enforced) governance, not soft-warn — confirm with Jeremy at workshop

---

### W4: Quoting & CPQ Workflow (Commerce Hub)

**Customer Story:** Jeremy's #1 named priority. Reps today struggle to build quotes because the product CSV upload is slow and error-prone. HelloSpoke wants Commerce Hub CPQ to absorb the quote-to-cash workflow with native e-signature on quotes — no DocuSign required for the quote-signing step.

**Recommended Approach:**
- Commerce Hub Professional setup + Commerce Hub seat assignment for the quoting team (tier validation in W1; if not on Commerce Hub Pro+, this becomes a licensing decision before build)
- Product library architecture: SKU structure, pricing rules, product groups
- CSV product upload pattern: standard product import workflow + bulk-update pattern via product ID mapping (note: tier-priced products require manual creation per HubSpot constraint)
- Quote template configuration with HelloSpoke branding
- Validation rules + approval workflows for quotes above pricing thresholds
- Native e-signature configuration on quotes (Dropbox Sign-powered; included with Commerce Hub Professional). **Cap awareness:** 25 sigs/user/mo on Pro, 50/user on Enterprise — pooled across users. Validate HelloSpoke's monthly quote volume during W1 to confirm tier sufficiency
- Quote-to-deal workflow automation: quote acceptance triggers deal stage advance + downstream task creation
- Documentation + handoff training (folds into W9)

**Assumptions:**
- HelloSpoke is on (or upgrading to) Commerce Hub Professional minimum
- Quote signature volume fits within pooled Commerce Hub Pro caps (25/user/mo); Enterprise upgrade is a client-side licensing decision if volume exceeds
- Existing product catalog provided in CSV format with consistent SKU + pricing structure
- No multi-currency quotes
- Native HubSpot e-signature replaces DocuSign **for quote signing only**; non-quote contracts (SOWs, MSAs) are addressed in W5

**Research note (logged 2026-05-07):** HubSpot Contracts beta (Spring 2026) extends the contract lifecycle but is still quote-tied — does not sign general contracts. Not compatible with HubSpot Payments + Stripe accounts. Surfaced as informational only; not relied on in v3 scope.

---

### W5: DocuSign Replacement Evaluation + Setup

**Customer Story:** Jeremy is killing DocuSign. The replacement decision hinges on whether HelloSpoke needs to sign anything that isn't a quote. If not, Commerce Hub native signature in W4 is the full answer and W5 absorbs minimal hours. If yes, PandaDoc (HubSpot-native) is the backup for general contracts (SOWs, MSAs, NDAs).

**Recommended Approach:**
- Decision-support workshop with Jeremy: catalog non-quote signing needs (counts/year, document types)
- **If Commerce Hub native suffices** (quote-only signing): extended config beyond W4 — signature delegation rules (Spring 2026 capability), branded signing experience, audit-trail configuration
- **If PandaDoc selected** (non-quote signing required): PandaDoc account setup (client-billed), HubSpot↔PandaDoc native integration installation, template migration for top 5 document types, deal-stage automation linking signed-doc events to HubSpot

**Assumptions:**
- W5 hours sized at the median assuming Commerce Hub native is sufficient. If PandaDoc is selected, W5 hours run higher (high-end of range)
- PandaDoc subscription, if needed, billed under HelloSpoke's account (Sayer doesn't own the billing relationship)
- Up to 5 document templates migrated if PandaDoc path; further templates are change orders

---

### W6: Automations & Workflows

**Customer Story:** Sales reps and ops need the system to do the chasing — not the other way around. Lead-to-account-to-quote-to-order-to-kickoff should run on rails, with notifications, task creation, and ownership routing happening automatically.

**Recommended Approach:**
- Deal-stage automations: notifications, task creation on stage advance, property updates
- Lifecycle stage progression: lead → MQL → SQL → opportunity → customer transitions tied to deal events
- Customer-journey automation: lead capture → company association → quote-ready → order → onboarding kickoff
- Sales-team notifications + ownership routing (round-robin or rule-based)
- Stuck-deal alerts to managers
- Internal email templates + automated send-on-trigger sequences

**Assumptions:**
- Up to 12 workflows in v3; further workflows or branching complexity are change orders
- HubSpot Operations Hub not required for v3 automations (standard Sales Hub workflow tools sufficient)
- No marketing email nurture flows (out of scope per 4/14 decision; covered in a future engagement)

---

### W7: Reporting & Dashboards

**Customer Story:** Jeremy has been emphatic — the system isn't useful if dashboards don't show the right things in the right places. Three audiences (executive, sales rep, ops) need their own views with the metrics they actually use.

**Recommended Approach:**
- Executive dashboard: revenue, pipeline health, conversion rates, deal velocity
- Sales rep dashboard: my deals, my activity, my targets, stuck-deal alerts
- Ops dashboard: onboarding pipeline view, ClickUp status sync (read-only), customer health
- Custom views + saved filters per role (sales rep, sales leader, ops, exec)
- Report templates + scheduled-export configuration for ELT into other tools if needed

**Assumptions:**
- Up to 3 dashboards (one per audience), 5–8 reports per dashboard
- HubSpot reporting tier sufficient (Sales Hub Pro minimum; Enterprise gives more report slots if needed)
- Custom report builder used; no external BI tool integration in v3
- Sales rep targets/quotas data provided by HelloSpoke (Sayer doesn't define quotas)

---

### W8: ClickUp Workflow Refinement

**Customer Story:** The ClickUp ↔ HubSpot integration already exists — Jeremy built it. What HelloSpoke needs now is workflow correctness: the right people doing the right things at the right time. Status alignment, gating, who-does-what.

**Recommended Approach:**
- Current state review: existing integration + automation Jeremy built (deal-won → ClickUp task)
- Workflow correctness audit: are statuses meaningful, are tasks landing on the right person, is implementation visibility flowing back to sales
- Status alignment: confirm canonical onboarding statuses are mirrored in HubSpot for sales-rep visibility
- Gating + handoff rules: sales → implementation criteria, implementation → ops criteria, completion criteria
- Documentation of who-does-what + SOPs for implementation team
- Hand-off sync configuration tweaks (NOT integration build — this is configuration of what Jeremy already wired)

**Assumptions:**
- ClickUp integration is functional in Jeremy's sandbox at start of W8 (validate during W2 audit)
- ClickUp side: Christina/Dalton/Haley make ClickUp-side changes; Sayer doesn't directly modify ClickUp configuration
- 10DLC training and Win-property surveys remain decoupled per 4/23 decision

---

### W9: Training & Enablement

**Customer Story:** Jeremy and Christina won't get value from the rebuild if the team can't use it. Training has two tracks: admins (Christina + designated HelloSpoke admin) need depth; end users need workflow-specific training tied to what they actually do.

**Recommended Approach:**
- Admin training: 2 sessions covering CRM structure, workflow editing, report building, user management (recorded for future hires)
- End-user training: sales reps — pipeline workflow, quoting in Commerce Hub, dashboard usage (recorded + live Q&A)
- End-user training: ops/implementation team — onboarding workflow, ClickUp ↔ HubSpot status sync, handoff gates
- Documentation/SOPs: admin playbook (architecture decisions, workflow logic, gotchas), end-user quick-reference cards

**Assumptions:**
- Up to 2 admin training sessions and 2 end-user sessions per team
- Sessions delivered live + recorded; recordings hosted on HelloSpoke's side
- 10DLC training tracked separately (per 4/23 decision)

---

### W10: UAT & Go-Live

**Customer Story:** Before flipping the switch, HelloSpoke needs to know it works. Test scenarios cover the high-value workflows; UAT validates that real users can complete real tasks; go-live includes a hypercare window for the bumps that always show up post-launch.

**Recommended Approach:**
- Test scenario design: top 10 sales workflows, top 5 ops workflows, top 5 reporting checks
- Test matrix execution with HelloSpoke: bug logging, severity triage, fix routing
- UAT facilitation with sales + ops users
- Go-live coordination: cutover sequence, communications plan, rollback trigger
- 30-day hypercare: ad-hoc support tickets, weekly check-in, fast-turn fixes for blocking issues

**Assumptions:**
- HelloSpoke participates in UAT (sales + ops representatives)
- Hypercare scope: bugs and clarifications, not net-new feature requests
- 1 cutover event; phased cutovers are change orders

---

### PM: Project Management

- Weekly standup facilitation across 12-week delivery
- Status reporting + governance artifact maintenance (Sayer-side)
- Stakeholder alignment + escalation handling
- Phase reviews (3 phases): kickoff/foundation, build, UAT/go-live

---

### Optional: QuotaPath Integration (decision pending Jeremy 2026-05-08)

**Customer Story:** Jeremy is undecided on QuotaPath. He's mentioned the team has "kind of figured out how to do some of the commission ourselves" and is questioning whether it's worth it. Cameron flagged the implementation reality: configuration on HelloSpoke's side is required regardless of who installs it.

**Recommended Approach (if IN):**
- HubSpot deal/property configuration to feed QuotaPath
- QuotaPath account setup (HelloSpoke-billed) + integration install
- Commission rule definition workshop with sales leadership
- Sales-engineer alignment session per Cameron's caveat: "There's got to be somebody on your side configuring HubSpot and working through things with the sales engineers"
- Validation testing across 1 commission cycle

**Assumptions (if IN):**
- HelloSpoke owns QuotaPath subscription
- Commission rules are well-defined before integration build (Sara/leadership input required)
- Up to 5 commission rule structures; further structures are change orders

**Decision deadline:** EOW 2026-05-08. v3 ships with this as a checkbox; Jeremy's answer triggers either inclusion or formal removal.

---

## Estimate Summary

| Metric | Low | Median | High |
|--------|-----|--------|------|
| Total Hours | 145 | 164 | 188 |
| Rate | $175/hr | $175/hr | $175/hr |
| Investment | **$25,375** | **$28,700** | **$32,900** |

**Optional QuotaPath add-on:** +10–18 hrs ($1,750–$3,150), median +14 hrs ($2,450)

**Net change from v2 anchor ($44,000):** −$15,300 at median (savings passed through)

---

## Workstream Hours Table

| # | Workstream | Low | Median | High |
|---|---|---|---|---|
| W1 | HubSpot Foundational Architecture | 14 | 18 | 22 |
| W2 | Data QA + Pre-Production Audit | 14 | 18 | 22 |
| W3 | Sales Stage Definitions + Gating | 8 | 10 | 14 |
| W4 | Quoting & CPQ Workflow (Commerce Hub) | 20 | 24 | 30 |
| W5 | DocuSign Replacement Evaluation + Setup | 4 | 6 | 12 |
| W6 | Automations & Workflows | 16 | 20 | 26 |
| W7 | Reporting & Dashboards | 14 | 18 | 24 |
| W8 | ClickUp Workflow Refinement | 8 | 12 | 16 |
| W9 | Training & Enablement | 10 | 12 | 16 |
| W10 | UAT & Go-Live | 8 | 10 | 14 |
| PM | Project Management | 12 | 16 | 20 |
| | **TOTAL (base)** | **128** | **164** | **216** |
| | *Effective range used in proposal* | **145** | **164** | **188** |
| Optional | QuotaPath | 10 | 14 | 18 |

*Note on range tightening:* the raw low (sum of low-end estimates) is 128 hrs and the raw high is 216 hrs. The proposal range tightens these to **145–188** to reflect realistic delivery (concurrent dependencies and overhead apply at every workstream's lower bound, and the high end caps at one full standard deviation above median rather than the sum of pessimistic estimates).

---

## Phase Reweighting (Phase 1 / 2 / 3)

v2 used a 3-phase structure (Foundation, Build, Cutover). v3 keeps the structure but reweights:

| Phase | Workstreams | Median Hours |
|---|---|---|
| Phase 1 — Foundation + Audit (Wk 1–4) | W1, W2, W3 | 46 |
| Phase 2 — Build (Wk 5–9) | W4, W5, W6, W7, W8 | 80 |
| Phase 3 — Enable + Go-Live (Wk 10–12) | W9, W10 | 22 |
| Cross-phase | PM | 16 |
| **Timeline** | | **12 weeks** (was 12–16) |

Phase 2 is the heaviest by design — that's where Jeremy's named priorities (quoting, dashboards, automations) live. Phase 1 fast-tracks audit + foundation so the team unblocks Phase 2. Phase 3 is lean by design per Christina: *"We just really don't know what we don't know... I'm sure we will have ideas once we live with the new system for a couple weeks."* Future iterations belong in a follow-on engagement.

---

## Risk Register (revised for v3)

| # | Risk | Severity | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|---|
| 1 | **HubSpot tier insufficient for Commerce Hub CPQ + native signature** — HelloSpoke may need to upgrade to Commerce Hub Professional ($95/seat/mo) before W4 builds | High | Medium | W4 blocks; client-side licensing decision required mid-delivery | Validate tier in W1 kickoff; surface upgrade decision before W4 starts | Sayer |
| 2 | **Sandbox access delay** — Jeremy must grant Sayer access to HubSpot sandbox with Salesforce + Rev IO data before W2 begins | High | Medium | W2 delayed; Phase 1 timeline slips | Open item flagged on 5/4; access requested in v3 follow-up email | HelloSpoke |
| 3 | **Pre-existing data quality issues** in Jeremy-built migration surface during W2 audit | Medium | High | Remediation may exceed 2 audit rounds; further rounds are change orders | W2 limited to 2 audit rounds; surface remediation needs early; client decides remediation scope | HelloSpoke |
| 4 | **Native signature volume exceeds Commerce Hub Pro caps** (25 sigs/user/mo) | Medium | Low | Forces Enterprise upgrade or PandaDoc fallback for non-quote docs | Volume validation in W1; tier decision before W4; PandaDoc as fallback if needed | HelloSpoke |
| 5 | **DocuSign replacement decision delayed** — Jeremy hasn't confirmed Commerce Hub native vs PandaDoc | Medium | Medium | W5 hours land at high end (PandaDoc) vs low end (Commerce Hub native) | Decision deadline aligned with Phase 1 kickoff; v3 hours sized at median assuming Commerce Hub native | HelloSpoke |
| 6 | **Sales-stage definitions delivered late** — Sara is delivering this week post-validation; W3 build depends on it | Medium | Low | W3 starts late, ripples to W6 dependencies | Sara delivers in week 1 of delivery; if late, W3 slides to Phase 1 end | HelloSpoke |
| 7 | **Phase 2 scope creep** — Christina noted future ideas will surface "once we live with the new system" | Medium | Medium | New asks in mid-delivery erode v3 scope | v3 explicitly defers Phase 2 ideas to a follow-on engagement; documented in scope | Sayer |
| 8 | **QuotaPath decision changes scope mid-engagement** | Low | Medium | If Jeremy decides IN after v3 sends, +14 hrs change order | Surface as explicit checkbox with EOW 5/8 deadline; price impact transparent | HelloSpoke |
| 9 | **Tier-priced products incompatible with bulk CSV import** (HubSpot platform constraint) | Low | Low | If HelloSpoke uses tier pricing, products created manually | W4 inventory captures tier-pricing structure; if present, manual creation hours added | Sayer |
| 10 | **Tight 12-week timeline** with Phase 2 carrying 80 hrs | Medium | Medium | Phase 2 risks running long if dependencies slip | Weekly standups; phase-review checkpoints; early flag if Phase 1 deliverables run late | Sayer |

---

## Scope Assumptions (revised for v3)

1. **HubSpot tier:** Sales Hub Professional minimum; Commerce Hub Professional minimum for W4. Tier validation in W1; upgrade decisions are client-side licensing matters
2. **Sandbox access** granted by Jeremy before W2 begins; sandbox contains current Salesforce + Rev IO data
3. **Jeremy completes** Rev IO integration, basic ClickUp deal-won automation, Salesforce data migration, ALN integration. Sayer does NOT build these
4. **QuickBooks integration is OUT** (Jeremy declined; financial data lives in Rev IO)
5. **Sara delivers** finalized sales-stage definitions in week 1 of delivery
6. **Up to 2 rounds** of W2 audit + remediation findings; further rounds are change orders
7. **Up to 10 required fields** per gate, 2 gates total in W3
8. **Up to 12 workflows** in W6; further or higher-complexity workflows are change orders
9. **Up to 3 dashboards** (executive, sales, ops), 5–8 reports per dashboard in W7
10. **Up to 2 admin training sessions** + 2 end-user sessions per team in W9
11. **30-day hypercare** in W10 covers bugs and clarifications, not net-new feature requests
12. **No multi-currency quotes** in W4
13. **No marketing email nurture flows** (out of scope; covered in future engagement per 4/14)
14. **Phase 2 ideas deliberately deferred** to a follow-on engagement (Christina's ask, 5/4)

---

## Out of Scope (revised for v3)

- **Rev IO integration build** — Jeremy completed
- **ClickUp integration build** (deal-won → ClickUp task automation, native integration setup, Make middleware) — Jeremy completed
- **Salesforce → HubSpot data migration build** — Jeremy completed; Sayer audits in W2 only
- **QuickBooks integration** — Jeremy declined (financial data in Rev IO)
- **ALN integration** — Jeremy completing himself this week
- **Legacy ClickUp ↔ Salesforce integration** — explicitly out per 4/23 decision; Sayer not responsible for legacy plumbing
- **Marketing email nurture flows** — out per 4/14
- **Multi-currency quotes** — out
- **External BI tool integration** for reporting — out
- **Net-new HubSpot custom-object schema design** — Sayer validates Jeremy's existing schemas; doesn't design from scratch
- **10DLC training flow** — tracked separately per 4/23
- **Win-property separate survey flow** — out per 4/23 (80/20 standard flow handles)
- **Phase 2 ideas surfaced post-go-live** — deferred to follow-on engagement

---

## Pricing & Payment Terms

> **Model:** Fixed Fee
>
> **Total Cost (Base Scope, Workstreams 1–10 + PM):**
> **$28,700** at median (164 hrs at $175/hr). Range $25,375 – $32,900 reflects scope-execution variance.
>
> *Final number set at $28,700 for proposal delivery, pending Cameron alignment before v3 send.*
>
> **Optional QuotaPath Add-On:** $2,450 median (range $1,750 – $3,150). Decision required by EOW 2026-05-08.
>
> **Project Timeline:** 12 weeks
>
> **Payment Terms:**
> - Equal monthly payments of **$7,175** over 4 months (base scope at median)
> - Net-15 terms on all invoices
> - QuotaPath add-on, if selected, invoiced separately at workstream completion
>
> **Technology & Administrative Fee:** 5% applied to each invoice (unchanged policy)

**Pricing rationale:** v3 hours come down ~34% vs the 4/24 anchor of 250 hrs; investment comes down ~35% from $44,000 to $28,700. Savings are passed through to the client per direction confirmed with Kyle 2026-05-05. The $28,700 median honors Sarah's 4/21 discount signal (45% off the original target, which was $52,500 at full v1 scope) while preserving Sayer margin at the $175/hr blended rate.

---

## Patch Application Plan — Three Client-Facing Artifacts

### Artifact 1 — Proposal Markdown — DELIVERED 2026-05-07

| Item | ID |
|---|---|
| v1/v2 source (history, do not delete) | `1KBQexPfPZvscxObqEy2kDSthMToL69sN` |
| **v3 file (NEW, this session)** | **`1b2WOhxXmD1BrLI5JU-Xq0H00qR0ZNAT6`** |
| Drive folder | `16VrwmgEqJRSq1YIM3LmDJ0NX61Sq1Ss-` (`hellospoke/`) |

Full v3 proposal uploaded as `HelloSpoke_HubSpot_CRM_Proposal_v3.md`. Customer Story framing preserved on every workstream per `reference_sayer_proposal_format` memory. 8-section structure: Executive Summary → Objectives → Scope of Work (W1–W10 + PM + Optional QuotaPath) → Deliverables & Milestones → Engagement Model & Pricing → Project Governance → Assumptions & Constraints → Approval & Next Steps.

### Artifact 2 — Scope Summary — DELIVERED 2026-05-07

| Item | ID |
|---|---|
| v1/v2 source (history, do not delete) | `1cmDN7kiKA16zFco60znTzbzcgywXS6pa` |
| **v3 file (NEW, this session)** | **`1Q8ZnFSV4vW7oHhzz6J9534XiEn0dbyCs`** |
| Drive folder | `16VrwmgEqJRSq1YIM3LmDJ0NX61Sq1Ss-` (`hellospoke/`) |

Full v3 scope summary uploaded as `HelloSpoke_Scope_Summary_v3.md`. Follows `templates/scope-summary-template.md` structure: Recommendation → Systems in/out of Scope → Approach (12-week phased) → Estimate Summary → Workstream Breakdown → Risk Register (8 rows) → Assumptions (15 items) → Outstanding Items → Pricing Context → Phase 2 / Future.

### Artifact 3 — Authoritative SOW Sheet — MANUAL APPLY REQUIRED

**Drive ID:** `1Kctr6sIfFQY7PzMY-GAHopI7fOdjl_TEgUi8zSjh1uY`
**Status:** NOT auto-updated this session. The Google Drive MCP tools do not support cell-level edits on Google Sheets, and a CSV-conversion approach would lose tab structure and formulas. Kyle applies the v3 changes to the live sheet manually using this section as the spec.

**Tabs to update:**

1. **Phase/Workstream Matrix tab:** Replace v2 workstream rows with v3 W1–W10 + PM rows. Phase mapping per "Phase Reweighting" section above
2. **Phase Requirements tab:** Replace v2 requirement IDs with v3 IDs:
   - **ARC-01..ARC-08** (W1 Architecture)
   - **QA-01..QA-07** (W2 Data QA)
   - **STG-01..STG-05** (W3 Sales Stages + Gating)
   - **CPQ-01..CPQ-09** (W4 Quoting/CPQ)
   - **SIG-01..SIG-04** (W5 DocuSign Replacement)
   - **AUT-01..AUT-12** (W6 Automations)
   - **DASH-01..DASH-08** (W7 Dashboards)
   - **CLK-01..CLK-05** (W8 ClickUp Refinement)
   - **TRN-01..TRN-04** (W9 Training)
   - **UAT-01..UAT-05** (W10 UAT/Go-Live)
   - **QP-01..QP-03** (Optional QuotaPath)
3. **Phase Success Criteria tab:** Update per phase per v3 phase definitions
4. **Risk Register tab:** Replace with v3 risk register (10 rows above)
5. **Scope Assumptions tab:** Replace with v3 assumptions (14 items above)
6. **Out of Scope tab:** Replace with v3 out-of-scope list
7. **Open Items tab:** Replace with current open items from STATE.md
8. **Workstream Hours tab:** Replace with v3 workstream hours table (low/median/high per workstream)
9. **Pricing tab:** Update with $28,700 median, $25,375–$32,900 range, $7,175/mo × 4, 5% tech fee, optional QuotaPath line

**Working copy SOW** (`1JahJZ6tBuii1KyeE_D1SpMUk9NJtZClhwQHq5f-BcFs`): not updated this session per plan (deferred; mirror authoritative once verified).

---

## Application Order

1. **Proposal markdown** first — sets the v3 narrative
2. **Scope summary** second — keeps narrative aligned with the executive summary
3. **Authoritative SOW sheet** third — formalizes the requirements + risk register
4. **(Deferred)** Working copy SOW — mirror authoritative
5. **(Deferred)** New Gamma deck — supersedes `erumqig7pyx7rhm` (Gamma can't edit; full regen)
6. **(Deferred)** v3 follow-up email — to Jeremy (cc Christina, Sara, Cameron) from `kyle@gosayer.com`

---

## Brand Notes

Sayer Brand Guide ([Drive link](https://docs.google.com/document/d/1z_c615tZvLyT-Y_h49evrLYIUzHFh2E7lPPsCxCc7og)):
- Colors: Yellow `#FEC700`, Grey 700 `#2E2E2E`, Black `#000000`
- Headline font: Rethink Sans Semibold
- Body font: Rethink Sans Regular
- Positioning line: "Drive growth, unlock potential."
- Tone: direct, candid, no hedging
- Naming: "Sayer" only (no legacy brand references)

---

## Commerce Hub CPQ — Research Note (logged 2026-05-07)

Web research conducted before workstream sizing to validate three blockers:

**1. CSV product upload — SUPPORTED.** Standard product import + bulk-update via product ID mapping work as expected. Limitation: tier-priced products can't be bulk-imported (HubSpot platform constraint). Surfaced as Risk #9; size impact only if HelloSpoke uses tier pricing.

**2. Native e-signature — SUPPORTED for quotes only.** Powered by Dropbox Sign; included with Commerce Hub Professional/Enterprise + Commerce Hub seat. Caps: 25 sigs/user/mo (Pro), 50/user (Enterprise), pooled across users, resets monthly. **Does NOT sign general contracts (SOWs, MSAs, NDAs)** — that's W5's swing.

**3. HubSpot tier required — Commerce Hub Professional ($95/seat/mo) minimum.** Includes custom quote templates, e-signatures, recurring billing, approval workflows. Sales Hub Professional alone is NOT sufficient for native quote signing (per Spring 2026 docs, signature feature lives in Commerce Hub specifically). This is the load-bearing tier validation for Risk #1.

**HubSpot Contracts beta (Spring 2026)** — quote-lifecycle tool only; not a general contract platform. Not relied on in v3 scope. Flagged for awareness.

---

## Verification Checklist (for Cameron review)

- [ ] Hours integrity: workstream-hour sum = total at low/median/high
- [ ] Pricing math: 164 × $175 = $28,700 ✓; $28,700 / 4 = $7,175/mo ✓
- [ ] No residual stripped-workstream references (Rev IO build, QuickBooks, ALN, Make middleware, Salesforce migration build)
- [ ] All 5/4 strip items appear in Out of Scope
- [ ] All 5/4 add/elevate items appear as named workstreams (W1, W2, W4, W5, W7)
- [ ] All 5/4 keep items carry forward (W3, W6, W8, W9, W10, PM)
- [ ] QuotaPath surfaced as optional with 5/8 deadline
- [ ] DocuSign replacement structured to handle both Commerce Hub native and PandaDoc paths (W5 hour range absorbs both)
- [ ] Pricing range lands $25,375 – $32,900; median $28,700 inside $27–32k target
- [ ] Brand/format integrity (8-section proposal structure, 5% tech fee, fixed-fee pricing)
