# HelloSpoke — ClickUp ↔ HubSpot Integration Workstream Addendum

> **⚠️ SUPERSEDED 2026-05-05.** Entire workstream stripped from v3 scope. On the 5/4 walkthrough call, Jeremy confirmed he has already built the basic ClickUp deal-won → task automation himself in his sandbox; the v3 rescope no longer carries a ClickUp integration workstream. The ClickUp work that survives in v3 is workflow refinement (correctness, gating, who-does-what) — not integration build, form replacement, or middleware. This document is retained for historical context only. See `HelloSpoke_decisions.md` 2026-05-04 entry and the v2 patch document for current scope.

---


**Date:** 2026-04-23
**Author:** Kyle / Sayer
**Basis:** 4/23 ops discovery call (Fireflies: `01KPRXJ0AX07VPYY4T9EEBGZJD`) + `/deep-research` agent report on ClickUp↔HubSpot native integration + ClickUp/HubSpot forms
**Purpose:** Targeted addendum to the existing HelloSpoke scope. Replaces the loosely-worded "post-sales ops / ClickUp integration" line in the current proposal with a specified workstream that Jeremy can pick from three concrete architecture tiers. Not a full re-scope — only this workstream is being detailed.

---

## Context

The 2026-04-21 proposal committed Sayer to "native HubSpot↔ClickUp connector + light workflows" with specifics deferred pending the 4/23 ops discovery. That discovery surfaced four client asks:

1. Bidirectional ClickUp↔HubSpot sync with a simple status indicator on HubSpot deal/contact for sales visibility.
2. Replace the "form-returns-as-PDF" problem so onboarding data is queryable in HubSpot.
3. Mandatory field gating at two handoffs (sales→implementation, implementation→billing) so records can't advance without required data.
4. Sales deal-aging triggers ("60 days in demo mode" — Sarah Hines).

Only items 1 and 2 belong in this workstream. Item 3 is a process-redesign line item surfaced separately below. Item 4 is sales-process automation, handled in the CRM Automations workstream of the existing scope — not re-opened here.

---

## Load-Bearing Research Finding (Single Sentence)

**The native ClickUp↔HubSpot integration cannot push HubSpot form submissions into ClickUp custom fields without middleware.** This determines the architecture choice, and therefore the hours. See `/deep-research` report, Topic 1 + Topic 3.

Supporting facts:
- Native integration is maintained by ClickUp, listed in both marketplaces, 2.0/5 rating (69 reviews, 43% one-star).
- "Bidirectional" marketing is misleading — only ClickUp tasks are truly 2-way. Other objects (contacts, companies, deals, tickets) are event-driven trigger→action.
- Custom-field mapping from HubSpot workflows → ClickUp **is not supported** in the native integration.
- HubSpot custom objects are invisible to the native integration.
- ClickUp form submissions DO populate ClickUp custom fields directly (queryable, filterable). The "returns as PDF" complaint is almost certainly a form misconfiguration at HelloSpoke (questions bound to task description instead of typed custom fields), not a product default.

---

## Three Architecture Tiers

Each tier is a complete deliverable, not a partial build. Client chooses based on the balance of architectural cleanliness vs. hours.

### Tier A — Native integration + existing form audit

**What Sayer delivers:**
- Install and configure the native ClickUp↔HubSpot integration end-to-end.
- Two HubSpot workflows: deal-stage → ClickUp task creation, and ClickUp task-status → HubSpot deal-property update for sales visibility.
- Audit HelloSpoke's existing ClickUp implementation form; rebind questions from task-description dump to typed ClickUp custom fields so responses become queryable in ClickUp.
- Sync one "onboarding phase" enum property on the HubSpot deal reflecting ClickUp status.
- One sales-facing HubSpot dashboard card showing onboarding-phase distribution.
- Test matrix + documentation + 30-day hypercare.

**What's deferred:**
- HubSpot-form-as-SoR (client keeps their ClickUp form).
- Custom-field round-trip between systems.
- Mandatory field gating (separately scoped below).

**Hours:** 18–24 (median 21)

**Sayer recommendation:** Viable only if HelloSpoke is willing to accept that onboarding data captured at form submission lives in ClickUp first and is summarized (not fully replicated) in HubSpot. If the sales team needs to filter or report on onboarding form values, Tier A doesn't clear the bar.

---

### Tier B — HubSpot form + Make middleware + native integration (RECOMMENDED)

**What Sayer delivers:**
- Everything in Tier A.
- Plus: build a new HubSpot onboarding form replacing the ClickUp form. Form captures onboarding data to HubSpot contact/deal properties (standard and custom).
- Configure Make middleware (ClickUp + HubSpot connectors) to push new HubSpot form submissions into ClickUp as a task with mapped custom fields.
- Use the native integration for the return path (ClickUp task status → HubSpot deal property) so sales sees onboarding progress without custom build.
- Configure field-mapping matrix (estimated 12–15 fields from Jeremy's desired state).
- Failure handling, error notifications, credential vaulting.

**What's deferred:**
- Mandatory field gating (separately scoped below).
- ClickUp-initiated work visibility in HubSpot (e.g., implementation team spawning a new task outside the form path won't appear in HubSpot automatically).

**Hours:** 28–36 (median 32)

**Sayer recommendation: this is the tier to propose.** Cheapest viable architecture that solves Jeremy's actual complaint (queryable onboarding data in HubSpot) and preserves sales visibility. Make is fastest to stand up and has a straightforward non-developer handoff if HelloSpoke later wants to own it.

**Trade-off to flag to client:** Make is a SaaS subscription (~$10–30/mo depending on operation volume). If HelloSpoke prefers no recurring integration cost, Tier C.

---

### Tier C — HubSpot form + n8n middleware + native integration

**What Sayer delivers:**
- Everything in Tier B.
- Plus: replace Make with n8n as middleware. n8n is Sayer's standard integration platform; self-hosted or Sayer-managed cloud instance.
- Includes n8n workflow design, credential management, error handling, and monitoring.

**Why it costs more:** n8n requires more up-front engineering (workflow design, typed field coercion, ClickUp API error handling, retry logic) than a Make scenario, but eliminates the recurring Make subscription and gives HelloSpoke a more flexible long-term integration spine. Ownership transfers cleanly if they want it internally.

**Hours:** 40–48 (median 44)

**Sayer recommendation:** Only choose Tier C if HelloSpoke wants the integration to live on an open platform they can extend themselves, and is willing to spend ~12 additional hours for that architectural freedom.

---

## Optional Add-On (All Tiers) — Mandatory Field Gating

**What it is:** HubSpot deal pipeline required-fields configuration plus workflow-enforced validation so deals can't advance stages (sales→implementation, implementation→billing) without required data. Includes error messaging, field-required UI surfacing, and a "stuck deal" report for sales leadership.

**Why it's separate:** This is process design, not integration. Jeremy's ask ("things mandatory so it can't move through the phases without the first group doing their job") is a governance requirement that exists whether or not the ClickUp integration is built. Bundling it into the integration line would silently pad hours and obscure what the client is buying.

**Hours:** 8–14 (median 11)

**Sayer recommendation:** Worth the ~11 hrs if HelloSpoke wants the governance. Makes every integration tier above more effective because implementation team stops chasing sales for missing info.

---

## Roll-Up Comparison

| Tier | Hours (median) | Cost @ $150/hr (median) | Architecture | Subscription cost | Client impact |
|---|---|---|---|---|---|
| A | 18–24 (21) | $2,700–$3,600 ($3,150) | Native only | None | Minimal — fixes symptom not root cause |
| **B (recommended)** | **28–36 (32)** | **$4,200–$5,400 ($4,800)** | HubSpot form + Make | ~$10–30/mo Make | Solves root cause; light middleware |
| C | 40–48 (44) | $6,000–$7,200 ($6,600) | HubSpot form + n8n | None (self-host) or Sayer-managed | Cleanest long-term; more up-front engineering |
| + Field gating add-on | +8–14 (+11) | +$1,200–$2,100 (+$1,650) | Independent | None | Enforces data discipline cross-team |

**Fits inside the 20–60 hour envelope Sayer targeted.** All three tiers, with or without the field-gating add-on, stay in range.

---

## Risks

| # | Risk | Severity | Likelihood | Impact | Mitigation |
|---|---|---|---|---|---|
| 1 | Native integration 2.0/5 marketplace rating; known bugs (template-due-date inheritance, no custom-object support) | 🟡 Med | High | Sayer owns bug workarounds post-install | Document known limitations in SOW; budget 2-3 hrs hypercare buffer |
| 2 | ClickUp "HubSpot Integration 2.0" on roadmap but unscheduled — scoped capability may change mid-delivery | 🟢 Low | Low | Minor re-work if ClickUp ships a breaking change | Do not scope against unreleased features; revisit only if released during delivery |
| 3 | Middleware subscription cost (Tier B) or self-hosting overhead (Tier C) is a client decision that affects long-term ownership — if client defers decision, hours shift | 🟡 Med | Med | Hours shift between B and C based on choice | Force the architecture choice before contract sign; don't defer |
| 4 | Jeremy's mandatory-field-gating ask may resurface as "already in scope" if the field-gating add-on is declined | 🟡 Med | Med | Scope creep post-sign | Explicit line in proposal with checkbox: in or out |
| 5 | HelloSpoke has not yet drafted the canonical status list — integration workflows cannot be fully specified without it | 🟡 Med | High | 2–4 hr delay during delivery if status list arrives late | Delivery kickoff includes a status-list workshop; client commits to draft before kickoff |
| 6 | Custom fields needed exceed the assumed 12–15 field cap (Tier B/C field-mapping matrix) | 🟢 Low | Med | Additional 2–4 hrs per 5 fields beyond cap | Cap explicit in SOW; overages are change orders |
| 7 | ClickUp-initiated work (implementation team creating tasks outside the form path) won't reflect in HubSpot | 🟢 Low | High | Sales team sees partial picture | Explicit assumption in SOW; optional Phase 2 add-on if full coverage needed |

---

## Assumptions

- HubSpot tier is Sales Hub Professional or higher (required for HubSpot Workflows, which the integration depends on).
- ClickUp plan is Unlimited or higher (required for custom fields + the integration, per ClickUp partner guidance).
- Up to 15 custom fields mapped between systems in Tier B/C. Overages are change orders.
- Status list will be drafted by HelloSpoke (Christina/Dalton/Haley) before integration build begins; Sayer facilitates a 1-hour workshop to lock it.
- "Mandatory field gating" is treated as optional add-on, not included in any tier's base hours.
- No HubSpot custom objects in the integration path (native integration cannot touch them).
- 10DLC training is decoupled from the onboarding status flow per Dalton's 4/23 note.
- "Win-property" separate survey is not in scope; standard form/flow handles 80% of onboardings per Kyle's 4/23 recommendation.
- Sayer is not responsible for fixing or debugging the broken legacy ClickUp↔Salesforce integration.

---

## Client Responsibilities

- Jeremy, Christina, or designee: review and sign off on architecture tier choice before delivery begins.
- Christina / Dalton / Haley: draft canonical status list with % complete indicators (Sayer facilitates workshop).
- Sarah Hines: share sales-stage definitions with implementation team (already committed on 4/23 call).
- HelloSpoke: provide admin access to ClickUp workspace and HubSpot portal for integration setup.
- HelloSpoke: designate a test environment or staging approach (sandbox vs. gated live).
- If Tier B: approve Make subscription setup under HelloSpoke's account (so they own the billing relationship).
- If Tier C: decide self-hosted n8n vs. Sayer-managed; approve hosting cost if Sayer-managed.

---

## Outstanding Items (Unresolved, Affects Final Hours)

1. **Tier selection:** A / B / C. Drives base hours and subscription decisions.
2. **Mandatory field gating:** in or out. +8–14 hrs if in.
3. **Win-property separate survey:** in or out of the status flow. Assumed out above; confirm with Jeremy.
4. **Number of custom fields in the mapping matrix:** assumed up to 15. Confirm with Dalton once implementation form is shared.
5. **Status list ownership:** confirm client owns drafting; confirm Sayer facilitation workshop is included in base hours (currently: yes).
6. **HubSpot tier constraint:** verify current HubSpot tier supports Workflows (Sales Hub Professional minimum).

---

## Scope Language — Ready for Google Sheet / Proposal

**Recommended workstream line for the Google Sheet scope doc:**

> **ClickUp ↔ HubSpot Integration** — Stand up the HubSpot form + native integration + Make middleware to capture onboarding data in HubSpot at the source, push structured records to ClickUp for implementation team execution, and return onboarding phase/status to HubSpot for sales visibility. Includes HubSpot form build, middleware configuration, custom field mapping (up to 15 fields), deal-pipeline status-sync workflows, sales-facing dashboard card, field-mapping documentation, test matrix, and 30-day hypercare. Excludes HubSpot custom objects, mandatory field gating (optional add-on), and 10DLC/win-property separate flows.
>
> **Hours:** 28–36 (median 32) • **Cost:** $4,200–$5,400 (median $4,800) at $150/hr

**If field-gating add-on selected:**

> **Pipeline Governance Add-On — Mandatory Field Gating** — Configure HubSpot deal pipeline required-fields plus workflow-enforced validation so deals cannot advance stages (sales→implementation, implementation→billing) without required data. Includes error messaging, field-required UI surfacing, and a "stuck deal" report for leadership.
>
> **Hours:** 8–14 (median 11) • **Cost:** $1,200–$2,100 (median $1,650) at $150/hr

---

## Cross-References

- Existing proposal / Google Sheet — this addendum replaces the loosely-specified "ClickUp integration" line with the tiered options above.
- `HelloSpoke_decisions.md` — 4/23 entry captures the architectural decisions behind this addendum.
- `STATE.md` — post-4/23 session state.
- `/deep-research` report — delivered via agent `a946f801d55b872bd`; not saved to repo (research output only).
- `calibration/calibration.md` — no prior ClickUp projects baselined; this is Sayer's first. Add to calibration after delivery.
- `scoping-skill.md` line 158 — Integration workstream baseline ranges (Medium: 12–24 hrs). HelloSpoke integration lands at the upper-medium/low-large boundary due to the middleware requirement, consistent with the research's "real consulting effort" bracket.
