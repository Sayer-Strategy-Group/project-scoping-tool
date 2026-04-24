# HelloSpoke — Session State

> **Status:** `Pre-Sale`
> **Last updated:** 2026-04-23
> **One-liner:** $42k HubSpot implementation deal at Decision Maker Bought-In; close date 2026-04-30; ops discovery complete, revised proposal in flight with ClickUp integration workstream now specified.

---

## Current Position

| Field | Value |
|-------|-------|
| Phase | Pre-sale — revising proposal post-ops-discovery |
| Deal stage | Decision Maker Bought-In (`decisionmakerboughtin`) |
| Deal amount | $42,000 (pre-revision) |
| Close date target | 2026-04-30 |
| On track? | On track — Kyle commit: revised proposal EOD 2026-04-23 or AM 2026-04-24 |

---

## Done Last Session

- Ran 2026-04-23 ops discovery with Christina, Jeremy, Sarah, Dalton (Implementation), Haley (Ops) — 32 min
- Logged HubSpot note on company + 4 contacts + deal (note `366016513772`)
- Created two HubSpot tasks on the active deal:
  - `366085682933` — ClickUp↔HubSpot native integration research — due 2026-04-23 6 PM CT
  - `366054473408` — Deliver revised scope + proposal to Jeremy — due 2026-04-24 10 AM CT
- Drafted follow-up email in Superhuman to Jeremy (cc Christina, Sarah, Cameron) — pending manual send
- Drafted Slack post to `#project-hellospoke` (tagged Cameron) — Kyle to edit the tag artifact and send
- Appended 4/23 decisions entry to `HelloSpoke_decisions.md`
- Launched `/deep-research` agent on ClickUp↔HubSpot native integration + forms (running background)

---

## Open Items

### Sayer Owes
- [ ] ClickUp↔HubSpot native integration research (in progress — Kyle / background agent)
- [ ] Revise Google Sheet scope doc to add the ClickUp integration workstream with calibrated hours (pending research)
- [ ] Revise proposal with the form-replacement recommendation + explicit in/out decisions on mandatory field gating and Win-property survey (pending research + scope revision)
- [ ] Send follow-up email in Superhuman (Kyle to review and send manually)
- [ ] Send Slack update to `#project-hellospoke` (Kyle to edit tag + send)
- [ ] Decide whether to update the HubSpot task title + Superhuman draft body from "ClickUp API" to "ClickUp HubSpot native integration" for wording consistency
- [ ] Manual check in HubSpot UI for any orphan Lead objects on Jeremy/Ryan/Christina/Sarah contacts (MCP can't search leads; skipped)

### Client Owes
- [ ] Sarah Hines — share sales-stage definitions with Jeremy + Christina
- [ ] Dalton Palmer — send Kyle the ClickUp implementation form link
- [ ] Christina / Dalton / Haley — draft canonical status list (post-research, for the scoping workshop)
- [ ] Jeremy — review revised proposal when delivered

---

## Next Session Focus

1. Complete ClickUp integration research + draft `HelloSpoke_clickup_workstream.md` addendum
2. Plug calibrated hours into the external Google Sheet scope doc
3. Revise proposal + send to Jeremy
4. Stand by for proposal walkthrough call if Jeremy requests
5. Move deal to `contractsent` once Jeremy confirms the revised scope

---

## Key Artifacts

| File | Purpose |
|------|---------|
| `HelloSpoke_decisions.md` | Decisions captured from 4/14 discovery, 4/21 next-steps, and 4/23 ops discovery calls |
| `HelloSpoke_clickup_workstream.md` | *(pending research)* ClickUp workstream addendum with hour estimates |
| HubSpot Company `307857992394` | https://app.hubspot.com/contacts/46319964/record/0-2/307857992394 |
| HubSpot Deal `306004595439` | $42k, Decision Maker Bought-In — https://app.hubspot.com/contacts/46319964/record/0-3/306004595439 |
| HubSpot Note `366016513772` (4/23 call) | https://app.hubspot.com/contacts/46319964/companies/307857992394?engagement=366016513772 |
| Fireflies 4/14 discovery | https://app.fireflies.ai/view/01KNT5ZFCGEYFFWTBZYS196RC7 |
| Fireflies 4/21 next-steps | https://app.fireflies.ai/view/01KPRWATCQDV6NF29TWWHMKA1C |
| Fireflies 4/23 ops discovery | https://app.fireflies.ai/view/01KPRXJ0AX07VPYY4T9EEBGZJD |
| Slack channel (internal) | `#project-hellospoke` in sayerhq.slack.com |
| External scope doc | Google Sheet (authoritative — Kyle maintains) |

---

## Key Decisions

- **Post-sales ops / ClickUp integration is in scope** (confirmed 4/21, sharpened 4/23). Sayer builds native HubSpot↔ClickUp integration + light workflows to signal order→ops kickoff.
- **Automation priority over dashboards** (confirmed 4/21). Ryan: customer-journey automations first.
- **Status model: client-drafted, Sayer-facilitated** (4/23). Candidate list: Waiting for Survey → In Configuration → Training Scheduled → Call Forwarding → Complete, with % complete indicators. Sarah runs litmus test with sales reps.
- **Propose HubSpot form as replacement for ClickUp implementation form** (new, 4/23). Strategic recommendation contingent on research: capture data in HubSpot first, push to ClickUp. Simplifies sync architecture, solves the PDF-output frustration.
- **Mandatory field gating flagged but not committed** (4/23). Jeremy wants gated handoffs (sales→impl, impl→billing). Process redesign, not integration — explicit in/out line in revised proposal.
- **Legacy ClickUp↔Salesforce integration is out of scope** (4/23). Sayer builds net-new against HubSpot; not debugging the broken legacy flow.
- **10DLC training tracked separately** (4/23). Not in the standard onboarding status model.
- **Win-property separate survey — 80/20 decision pending** (4/23).

---

## Standing Context

**Stakeholder map**

| Person | Role | Read |
|--------|------|------|
| Jeremy Wiley (jwiley@hellospoke.com) | Decision maker — billing + end-to-end flow | Drove 4/23 follow-ups with Sarah. Wants mandatory field gating (scope-creep risk). "Doesn't do me any good if we're not billing." |
| Sarah Hines (shines@hellospoke.com) | Exec sponsor / sales leader | Asks the MVP framing questions; driving sales-stage definition work. |
| Ryan Sweeney (rsweeney@hellospoke.com) | Sales leader | Vote for automation > dashboards (4/21). Absent 4/23 (out of town). |
| Christina Edwards (cedwards@hellospoke.com) | Director of Operations | Champion + scheduler. Real-time sales/ops visibility is her top ask. |
| Dalton Palmer (Implementation) | ClickUp power user | **No HubSpot contact record** — attended 4/23 but not in CRM. Create when emails confirmed. |
| Haley R (Ops) | ClickUp day-to-day operator | **No HubSpot contact record** — attended 4/23 but not in CRM. Create when emails confirmed. |

**Sayer-side ownership**

- Billy Leigh owns HubSpot Company + contacts (`235753646`)
- Cameron Taggart owns the active deal (`78949101`)
- Kyle Harbuck leads scope/proposal; meeting attendee, not CRM owner (`162440209`)

**Watchlist**

- Pricing signal: Jeremy's 50% discount joke → Sarah's 45% counter (4/21). Watch for formal ask in next round.
- Lifecycle mix on active deal: contacts at `opportunity`, `other`, `lead` — HubSpot auto-manages, monitor.
- Lead object: not verified via MCP (tool limitation); manual HubSpot UI check pending.
- Scope-creep radar: Jeremy's mandatory-field-gating ask is process redesign bleeding into an integration workstream. Next proposal must surface this as a separate, explicitly optional line.
