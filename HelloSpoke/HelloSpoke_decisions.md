# HelloSpoke — Scoping Decisions Log

Running log of scoping decisions and reasoning. Update during every substantive call or scope change.

---

## 2026-04-14 — Sales Dashboards Discovery (36 min)

**Fireflies:** https://app.fireflies.ai/view/01KNT5ZFCGEYFFWTBZYS196RC7
**Attendees:** Jeremy Wiley, Ryan Sweeney, Christina Edwards, Sarah Hines (HelloSpoke); Cameron Taggart, Kyle Harbuck (Sayer)

**Decisions:**
- **CRM migration target: Salesforce → HubSpot.** Primary driver is sales-process alignment and dashboard adoption (current Salesforce usage is inconsistent).
- **Migration approach: phased / progressive.** Move active + complete customer accounts first, current pipeline second, leads third, archive outdated data.
- **Reporting tier strategy.** Different reports for different roles; dashboards align to how sales reps actually work (identified via shadowing reps, starting with Ryan).
- **Integrations to evaluate.** QuickBooks for revenue-actuals reporting. QuotaPath for commission reporting.
- **Marketing workflow out of scope for initial phase** but Cameron to coordinate with Bridget / John on lead-generation alignment.

**Open at end of call:** Full scope document not yet drafted — Kyle to begin.

---

## 2026-04-21 — Next Steps / Scope Review (17 min)

**Fireflies:** https://app.fireflies.ai/view/01KPRWATCQDV6NF29TWWHMKA1C
**Attendees:** Jeremy Wiley, Ryan Sweeney, Christina Edwards, Sarah Hines (HelloSpoke); Cameron Taggart, Kyle Harbuck (Sayer)

**Trigger:** Jeremy flagged that the written proposal didn't surface post-sales ops / ClickUp integration clearly enough.

**Decisions:**
- **Post-sales ops onboarding + ClickUp integration are in scope** — confirmed on the call. Cameron: "From a technical perspective I've got zero concerns about making that work."
  - Native HubSpot↔ClickUp connector is the starting point.
  - Light workflows in HubSpot to signal order→ops kickoff.
  - Custom properties/workflows only added if Thursday discovery surfaces them.
  - No material scope change expected; scope doc wording needed tightening, not re-scoping.
- **Priority order within scope:** customer-journey automations (lead→account→quote→order→kickoff) > dashboards. Ryan explicitly agreed dashboards can come in a later phase.
- **Stage-visibility requirement accepted** (Christina's ask). Form TBD after Thursday walkthrough — most likely a HubSpot custom property or integration field reflecting current ClickUp stage, not a full ticket pipeline.
- **Ops discovery walkthrough scheduled:** Thursday 2026-04-23 @ 3pm Central. Christina to add Haley (+ possibly Dalton).
- **Price reference for future revisions:** Jeremy joked about a 50% discount; Sarah countered with 45%. Not a formal request, but a signal to anticipate in the next proposal version.

**Open at end of call:**
- Thursday walkthrough to confirm MVP scope for the order-kickoff workflow
- Jeremy to email any outstanding scope questions before Thursday

---

## 2026-04-23 — Ops Discovery for HubSpot (32 min)

**Fireflies:** https://app.fireflies.ai/view/01KPRXJ0AX07VPYY4T9EEBGZJD
**Attendees:** Jeremy Wiley, Christina Edwards, Sarah Hines, Dalton Palmer (Implementation), Haley R (Ops) (HelloSpoke); Kyle Harbuck, Cameron Taggart (Sayer)

**Trigger:** Scheduled walkthrough of current ClickUp onboarding flow to finalize MVP scope for the ClickUp↔HubSpot integration workstream committed to on the 4/21 call.

**Decisions:**
- **ClickUp integration workstream sharpened, not expanded.** The 4/21 decision to include "native HubSpot↔ClickUp connector + light workflows" in scope still holds. Today's discovery filled in specifics — the hours and task list are being detailed; no new workstream is being added.
- **Status model: client-drafted, Sayer-facilitated.** Christina, Dalton, and Haley will propose the canonical status list (candidates from the call: Waiting for Survey → In Configuration → Training Scheduled → Call Forwarding → Complete) with % complete indicators for sales-team visibility. Sarah Hines will run a litmus test with sales reps once drafted.
- **Propose HubSpot form as replacement for ClickUp implementation form (new recommendation).** Capture onboarding data directly in HubSpot via a HubSpot form that then pushes into ClickUp as a task with mapped fields. Eliminates the PDF-output problem Jeremy flagged, makes the data queryable in HubSpot immediately, and simplifies the reverse-sync requirement. Contingent on research confirming the native integration supports this flow.
- **Mandatory field gating flagged but not committed.** Jeremy wants required fields at two handoffs (sales→implementation, implementation→billing) so records can't advance phases without them. This is process redesign, not integration — separate call-out in the revised scope with explicit in/out decision, not folded silently into integration hours.
- **Legacy ClickUp↔Salesforce integration is explicitly out of scope.** Dalton confirmed it "broke along the way." Scope language must clarify Sayer is building net-new against HubSpot, not debugging legacy plumbing.
- **10DLC training tracked separately.** Decoupled from the standard onboarding status flow per Dalton. Won't be in the integration status model.
- **"Win properties" separate survey — 80/20 decision pending.** Dalton mentioned a special survey for Win-branded properties. Kyle's position: solve for 80/20 first; Win-specific flow is an in/out decision for the revised proposal.
- **No billing-system changes scoped today.** Billing record creation was discussed but tied to the separate Rev IO / QuickBooks workstream (Apr 9 call). Not in this integration workstream.

**Open at end of call:**
- Sayer — ClickUp↔HubSpot native integration research (EOD 2026-04-23, Kyle)
- Sayer — revised scope + proposal to Jeremy (AM 2026-04-24, Kyle)
- HelloSpoke — Sarah Hines shares sales-stage definitions with Jeremy + Christina
- HelloSpoke — Dalton sends Kyle the ClickUp implementation form link
- HelloSpoke — Christina / Dalton / Haley draft canonical status list (post-research, for workshop)

---

## Template — Add Each Call Below

### YYYY-MM-DD — {Call Title} ({duration})

**Fireflies:** {link}
**Attendees:**

**Decisions:**
-

**Open at end of call:**
-
