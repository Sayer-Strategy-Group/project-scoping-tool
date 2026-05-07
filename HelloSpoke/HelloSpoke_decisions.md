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

## 2026-04-24 — Revised Proposal Delivered

**Fireflies:** n/a (async delivery)
**Attendees (recipients):** Jeremy Wiley, Christina Edwards, Sarah Hines (HelloSpoke); cc Cameron Taggart (Sayer)

**Trigger:** Kyle committed on 4/23 ops discovery to deliver revised scope + proposal by AM 4/24. Commitment met.

**Decisions:**
- **Pricing anchor held at $44,000** (not $43,750 sheet-calculated median). Aligned with Cameron. Rationale: HelloSpoke signaled discount intent (Jeremy's 50% joke → Sarah's 45% counter on 4/21). $44k round number absorbs an anticipated discount ask without eroding margin below the $175/hr × 250 hr baseline. Reduced scope option anchored at a corresponding round number.
- **Revised Gamma deck generated** — new URL `https://gamma.app/docs/erumqig7pyx7rhm`. Supersedes prior deck at `9xsb2pq9nvfe8ij`. Prior deck stays live but is deprecated; follow-up email explicitly tells recipients to ignore the old one.
- **ClickUp workstream landed in Phase 2** (not Phase 3) in the final deck and sheet. Nests inside Wk 3-6 migration phase — no timeline change.
- **Legacy ClickUp ↔ Salesforce integration explicitly called out in email** as out of scope. Prevents scope creep ambiguity.

**Delivered:**
- Revised proposal Gamma deck (URL above)
- Google Sheet scope doc updated (authoritative sheet `1Kctr6sIfFQY7PzMY-GAHopI7fOdjl_TEgUi8zSjh1uY`)
- Follow-up email sent from kyle@gosayer.com (Superhuman thread `draft0092144722e8694f`; `kyle@sayer.com` not yet a verified alias — flagged as a Superhuman follow-up)

**Open at end of delivery:**
- **Jeremy**: written approval of full scope ($44k) or reduced scope ($24.5k, Phases 1-2 only with ClickUp included)
- **HelloSpoke**: confirm ClickUp plan tier is Unlimited or higher
- **Christina/Dalton/Haley**: draft canonical onboarding status list (candidates: Waiting for Survey → In Configuration → Training Scheduled → Call Forwarding → Complete with % complete indicators)
- **Sarah**: share sales-stage definitions with Jeremy + Christina
- **Dalton**: send current ClickUp implementation form link
- **Kyle**: standing by for walkthrough call if requested

---

## 2026-05-04 — Scope Walkthrough Call (23 min)

**Fireflies:** https://app.fireflies.ai/view/01KQSVGHKNQ1PM7X5ZPWJ4GJJK
**Attendees:** Jeremy Wiley, Christina Edwards, Sara Hines (HelloSpoke); Cameron Taggart, Kyle Harbuck (Sayer)

**Trigger:** First call after Kyle delivered the revised proposal (4/24). Jeremy walked the proposal and asked to redirect the engagement away from data-plumbing work he has already built himself, toward configuration, automation, UX, and enablement.

**Decisions:**

- **Strip integration build hours from scope.** Jeremy has already built (in his sandbox) the Rev IO integration, the basic ClickUp deal-won → task automation, and the Salesforce data dump. He is finalizing the ALN integration himself this week and has decided QuickBooks integration is not needed (financial data lives in Rev). All previously scoped integration build-out comes out of v3.
- **Replace integration build with Data QA + Pre-Production Audit workstream** (confirmed with Kyle 2026-05-05). Sayer reviews the sandbox, validates data integrity / object & property mapping / associations / custom-object structure, designs error handling and a rollback plan, then green-lights the production push. This is the single workstream that absorbs all the audit-style work that used to be split across multiple integration build lines.
- **HubSpot foundational architecture is in scope and elevated.** Cameron asked: "Are you still wanting us to go through and... set up all of your objects and looking at pipeline stages, lead status, lifecycle stages?" Jeremy: "I think we're open to it." This becomes a named workstream in v3.
- **Quoting & CPQ workflow is the #1 named priority.** Jeremy: "The big ones are the quoting like making sure that the reps can quote easily." CSV upload pain, validation rules, property mapping, and the move to Commerce Hub CPQ are all in scope.
- **DocuSign is being killed.** Jeremy: "I told DocuSign to eat a dick." Two replacement candidates: Commerce Hub native signature (Cameron's recommendation — would be bundled with CPQ work and eliminate a separate signature tool) and PandaDoc (HubSpot-native alternative). Decision pending Jeremy.
- **Dashboards, views, and UX elevated.** Jeremy: "It's not helpful if it's not in the right spot, if the views don't look right." This is the "make it useful" pillar of the rescope.
- **ClickUp workstream pivots from integration build to workflow refinement.** The integration exists; what's needed is workflow correctness and gating so the right people use it the right way. Hours come down accordingly.
- **Phase 2 deliberately under-scoped.** Christina: "We just really don't know what we don't know... I'm sure we will have ideas once we live with the new system for a couple weeks." Phase 2 ideas are intentionally deferred to a follow-on engagement; v3 stays focused on Phase 1 essentials.
- **Pricing direction: pass savings through** (confirmed with Kyle 2026-05-05). Target landing zone $26-32k base at $175/hr, ~150-180 hrs. Final number aligned with Cameron before delivery.
- **QuotaPath surfaced as explicit optional add-on with EOW deadline** (confirmed with Kyle 2026-05-05). Jeremy: "I'll have an answer on that probably by the end of this week." v3 ships without waiting; QuotaPath appears as a checkbox line annotated "decision by 2026-05-08." Cameron flagged the implementation cost reality: "There's got to be somebody on your side configuring HubSpot and working through things with the sales engineers."
- **Treat v3 as a new proposal, not a patch.** Composition is changing materially, not just the dollar amount. New Gamma deck supersedes `erumqig7pyx7rhm`; new Google Sheet revision supersedes the 4/24 version.

**Open at end of call:**

- **Sara Hines** — send finalized sales-stage definitions (this week, post sales-team validation)
- **Jeremy Wiley** — grant Sayer access to HubSpot sandbox with Salesforce + Rev IO data
- **Jeremy Wiley** — answer on QuotaPath (in or out) by EOW 2026-05-08
- **Jeremy Wiley** — confirm DocuSign replacement direction (Commerce Hub native vs PandaDoc)
- **Jeremy Wiley** — continue tweaking QuickBooks + ALN integrations himself; ALN expected finalized this week
- **Christina Edwards** — confirm sales-stage definitions align with current ClickUp setup; flag any minor additions for Phase 2 (deferred)
- **Sayer (Kyle)** — review sandbox once shared and adjust scope based on actual sandbox state
- **Sayer (Kyle)** — update proposal + scope of work for v3 (focus on automations, quoting, dashboards, enablement)
- **Sayer (Cameron)** — coordinate on QuotaPath decision; align on final v3 pricing before delivery

---

## 2026-05-07 — V3 Artifact Authoring (async, Sayer-internal)

**Fireflies:** n/a (Sayer-internal authoring session, no client call)
**Attendees:** Kyle Harbuck (Sayer); Claude (assist)

**Trigger:** Execute the rescope direction agreed on 2026-05-05 — author the v3 patch doc, run the Commerce Hub CPQ research blocker, produce v3 client-facing artifacts in Drive, and prepare for Cameron alignment. Driven by the open items list in STATE.md and the rescope plan at `~/.claude/plans/alright-now-i-need-virtual-pudding.md`.

**Decisions:**

- **V3 hours and pricing locked at 164 hrs / $28,700 median** at $175/hr. Range $25,375 – $32,900 (low–high). 4-month installments of $7,175 + 5% tech fee. Pending Cameron sign-off before v3 ships to Jeremy. Lands inside the $27–32k target. Net change from 4/24 anchor: −$15,300.

- **Commerce Hub Professional is required** for the v3 quoting workstream (W4). Validated via web research:
  - **CSV product upload:** Supported via standard product import + bulk-update by product ID. Limitation: tier-priced products can't be bulk-imported (HubSpot platform constraint; surfaced as Risk #9).
  - **Native e-signature:** Powered by Dropbox Sign; lives in **Commerce Hub Professional/Enterprise + Commerce Hub seat**. Caps: 25 sigs/user/mo (Pro), 50/user (Enterprise), pooled across users, monthly reset. Sales Hub Professional alone is **NOT** sufficient — the e-sig feature is Commerce Hub-specific.
  - **Tier required:** Commerce Hub Professional minimum at $95/seat/mo. Tier validation moves to Workstream 1 kickoff and surfaces as Risk #1 in v3 risk register.

- **DocuSign replacement is partial via Commerce Hub native — quote signing only.** Non-quote contracts (SOWs, MSAs, NDAs) need PandaDoc, HubSpot Contracts beta, or keeping DocuSign. W5 (DocuSign Replacement Evaluation + Setup) sized at 6 hrs median assuming Commerce Hub native; runs to 12 hrs at the high end if PandaDoc selected. HubSpot Contracts (Spring 2026 beta) is quote-tied — does NOT sign general contracts and is incompatible with HubSpot Payments + Stripe accounts; not relied on in v3.

- **V3 workstream rebuild:** 10 workstreams + PM + optional QuotaPath:
  - W1: HubSpot Foundational Architecture (18 med)
  - W2: Data QA + Pre-Production Audit (18 med) — replaces all stripped integration build hours
  - W3: Sales Stage Definitions + Gating (10 med)
  - W4: Quoting & CPQ Workflow / Commerce Hub (24 med)
  - W5: DocuSign Replacement Evaluation + Setup (6 med)
  - W6: Automations & Workflows (20 med)
  - W7: Reporting & Dashboards (18 med)
  - W8: ClickUp Workflow Refinement (12 med)
  - W9: Training & Enablement (12 med)
  - W10: UAT & Go-Live (10 med)
  - PM: Project Management (16 med)
  - Optional: QuotaPath (14 med, decision pending Jeremy 5/8)

- **Phase reweighting (12-week timeline):**
  - Phase 1 — Foundation + Audit (Wk 1–4): W1 + W2 + W3 = 46 hrs
  - Phase 2 — Build (Wk 5–9): W4 + W5 + W6 + W7 + W8 = 80 hrs
  - Phase 3 — Enable + Go-Live (Wk 10–12): W9 + W10 = 22 hrs
  - Cross-phase: PM = 16 hrs

- **Treat v3 as a new proposal, not a patch.** Composition is changing materially. v3 client-facing artifacts uploaded to Drive (`hellospoke/` folder, `16VrwmgEqJRSq1YIM3LmDJ0NX61Sq1Ss-`):
  - `HelloSpoke_HubSpot_CRM_Proposal_v3.md` (`1b2WOhxXmD1BrLI5JU-Xq0H00qR0ZNAT6`)
  - `HelloSpoke_Scope_Summary_v3.md` (`1Q8ZnFSV4vW7oHhzz6J9534XiEn0dbyCs`)
  - `HelloSpoke_SOW_Sheet_v3_Update_Spec.md` (`1LUYTyEvmx2bgngdcy4D0AnN8M4EoHAzk`) — manual-apply checklist for the live SOW sheet

- **Authoritative SOW Sheet update is manual.** Google Drive MCP doesn't support Google Sheet cell edits, and a CSV-conversion approach would lose tab structure and formulas. Kyle applies v3 changes manually using the SOW Sheet Update Spec doc.

**Open at end of session:**

- Sayer (Cameron) — pricing alignment on $28,700 median before v3 ships to Jeremy
- Sayer (Kyle) — manual application of v3 changes to authoritative Google Sheet (`1Kctr6sIfFQY7PzMY-GAHopI7fOdjl_TEgUi8zSjh1uY`)
- Sayer (Kyle) — generate new Gamma deck to supersede `erumqig7pyx7rhm`
- Sayer (Kyle) — draft + send v3 follow-up email to Jeremy (cc Christina, Sara, Cameron) from `kyle@gosayer.com`
- HelloSpoke (Jeremy) — QuotaPath in/out by EOW 2026-05-08
- HelloSpoke (Jeremy) — DocuSign replacement direction (Commerce Hub native vs PandaDoc)
- HelloSpoke (Jeremy) — sandbox access for W2 audit
- HelloSpoke (Jeremy) — Commerce Hub Professional licensing confirmation before W4

---

## Template — Add Each Call Below

### YYYY-MM-DD — {Call Title} ({duration})

**Fireflies:** {link}
**Attendees:**

**Decisions:**
-

**Open at end of call:**
-
