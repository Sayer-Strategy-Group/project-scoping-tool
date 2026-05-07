# HelloSpoke — Session State

> **Status:** `Pre-Sale — V3 Artifacts Drafted, Cameron Alignment Pending`
> **Last updated:** 2026-05-07
> **One-liner:** v3 patch doc + v3 proposal markdown + v3 scope summary all authored and uploaded to Drive (`hellospoke/` folder). SOW Sheet update spec uploaded as a manual-apply checklist. Pricing locked at $28,700 median ($25,375 – $32,900 range; 164 hrs at $175/hr). Cameron alignment, manual SOW Sheet apply, Gamma deck regen, and v3 follow-up email are the remaining steps before v3 ships to Jeremy.

---

## Current Position

| Field | Value |
|-------|-------|
| Phase | Pre-sale — v3 artifacts drafted; Cameron alignment + manual artifact application pending |
| Deal stage | Decision Maker Bought-In (`decisionmakerboughtin`) |
| Deal amount | **$28,700 median** at $175/hr (164 hrs); range $25,375 – $32,900. Supersedes 4/24 $44,000 / $24,500 anchors. Pending final Cameron sign-off. |
| Close date target | TBD — reset target for week of 2026-05-12 send pending Cameron alignment + Gamma regen |
| On track? | Recovering after rescope; v3 artifact set ready in Drive; ship blocker is Cameron alignment + manual SOW Sheet apply |

---

## Done Last Session (2026-05-07)

- **Authored v3 patch doc** `HelloSpoke_sow_update_patch_v2.md` (530 lines) — full strip-add-keep tables, 10 v3 workstreams + PM + optional QuotaPath, estimate range, hours table, phase reweighting, risk register (10 rows), revised assumptions (14 items), revised out-of-scope, application plan
- **Commerce Hub CPQ research complete** — CSV upload supported (tier-priced products manual); native e-sig is Commerce Hub Professional+ only and quotes-only (caps 25/user/mo Pro, 50/user Enterprise); HubSpot Contracts beta is quote-tied, not a general-contract platform. Tier validation logged as Risk #1 in v3 risk register
- **Pricing math locked** — 164 hrs × $175 = $28,700; 4-month installments of $7,175; range $25,375 – $32,900; lands inside $27–32k target zone. Net change from 4/24 anchor: −$15,300 (savings passed through)
- **v3 proposal markdown delivered to Drive** — `1b2WOhxXmD1BrLI5JU-Xq0H00qR0ZNAT6` (`HelloSpoke_HubSpot_CRM_Proposal_v3.md` in `hellospoke/` Drive folder). 8-section Sayer format; Customer Story framing preserved on every workstream
- **v3 scope summary delivered to Drive** — `1Q8ZnFSV4vW7oHhzz6J9534XiEn0dbyCs` (`HelloSpoke_Scope_Summary_v3.md`). Follows `templates/scope-summary-template.md`
- **SOW Sheet v3 update spec delivered to Drive** — `1LUYTyEvmx2bgngdcy4D0AnN8M4EoHAzk` (`HelloSpoke_SOW_Sheet_v3_Update_Spec.md`). Tab-by-tab manual apply checklist
- **v3 SOW project workbook built locally** — `HelloSpoke/HelloSpoke_v3_SOW_Project_Sheet.xlsx` (10 tabs: Cover & Pricing, Workstream Hours, Task Breakdown, Phase Matrix, Phase Requirements, Phase Success Criteria, Risk Register, Scope Assumptions, Out of Scope, Open Items). 67-task breakdown sums to 164 hrs median; QuotaPath optional adds 14 hrs. **Drive upload pending** (Service account JSON missing from Keychain; gcloud/ADC not installed on this machine. Kyle drags into `hellospoke/` Drive folder OR adds `GOOGLE_SERVICE_ACCOUNT_JSON` to Keychain to enable scripted upload.)
- **Build script** `HelloSpoke/build_v3_sow_sheet.py` — re-runnable; openpyxl-based; brand-aware (Sayer yellow/grey)
- **v3 Gamma deck generation submitted** — generation ID `id7ImQXlMdFQbi7OYghy3` · status https://gamma.app/generations/id7ImQXlMdFQbi7OYghy3 · Sayer Default Theme (`ivv3t2lgbk9anm2`) · 12 slides, 16:9, executive audience, preserve mode. Will supersede `erumqig7pyx7rhm` once live
- **Logged 2026-05-07 entry** in `HelloSpoke_decisions.md` with Commerce Hub research findings, hours math, and v3 artifact decisions

## Done Prior Session (2026-05-05)

- **Pulled and analyzed 5/4 walkthrough call** (Fireflies `01KQSVGHKNQ1PM7X5ZPWJ4GJJK`, 23 min, Jeremy + Christina + Sara + Cameron + Kyle)
- **Built rescope plan** — see `~/.claude/plans/alright-now-i-need-virtual-pudding.md` (strip integration build / add Data QA + audit / pass pricing through)
- **Logged 5/4 decisions** to `HelloSpoke_decisions.md` — strip Rev IO + ClickUp + Salesforce migration + QuickBooks + ALN integration build hours, replace with Data QA + Pre-Production Audit, elevate quoting/CPQ + dashboards + UX
- **Pricing direction confirmed with Kyle** — pass savings through (target $26-32k, ~150-180 hrs at $175/hr); supersedes the 4/24 $44k anchor
- **QuotaPath direction confirmed with Kyle** — surface as explicit optional add-on with 2026-05-08 deadline; do not wait on Jeremy's decision before sending v3

## Done Prior Session (2026-05-05)

- Pulled and analyzed 5/4 walkthrough call (Fireflies `01KQSVGHKNQ1PM7X5ZPWJ4GJJK`, 23 min)
- Built initial rescope plan — `~/.claude/plans/alright-now-i-need-virtual-pudding.md`
- Logged 5/4 decisions to `HelloSpoke_decisions.md`
- Pricing direction confirmed with Kyle (pass savings through, $26-32k target)
- QuotaPath direction confirmed (explicit optional add-on, 5/8 deadline)
- Marked v2 patch and ClickUp workstream addendum as superseded

## Done Prior Session (2026-04-24 AM)

- Delivered revised proposal + scope to Jeremy Wiley (cc Christina, Sarah, Cameron)
- Gamma deck generated — `https://gamma.app/docs/erumqig7pyx7rhm` (slated for replacement in v3)
- Google Sheet scope doc updated; rate set to $175/hr
- Pricing decision locked at $44k — **superseded 2026-05-05**

---

## Open Items

### Sayer Owes
- [ ] **Cameron alignment on $28,700 median pricing** — confirm number + send approval before v3 ships to Jeremy
- [ ] **Upload `HelloSpoke_v3_SOW_Project_Sheet.xlsx` to Drive** (`hellospoke/` folder, Drive ID `16VrwmgEqJRSq1YIM3LmDJ0NX61Sq1Ss-`). Drag-upload from Finder (10 sec); Drive auto-converts xlsx → Google Sheet on import. OR add `GOOGLE_SERVICE_ACCOUNT_JSON` to Keychain (`security add-generic-password -a "harbuckconsulting" -s "GOOGLE_SERVICE_ACCOUNT_JSON" -w '<json>'`) for future scripted uploads
- [ ] **Manually apply v3 changes to authoritative SOW Google Sheet** (`1Kctr6sIfFQY7PzMY-GAHopI7fOdjl_TEgUi8zSjh1uY`) per `HelloSpoke_SOW_Sheet_v3_Update_Spec.md` — OR if you upload the new xlsx as the new authoritative SOW, retire the old sheet and use the v3 workbook directly
- [ ] **Mirror authoritative changes into working copy SOW** (`1JahJZ6tBuii1KyeE_D1SpMUk9NJtZClhwQHq5f-BcFs`) once authoritative is verified
- [ ] **Verify v3 Gamma deck quality** once generation `id7ImQXlMdFQbi7OYghy3` completes (https://gamma.app/generations/id7ImQXlMdFQbi7OYghy3); record the new deck URL here and mark `erumqig7pyx7rhm` deprecated
- [ ] **Draft + send v3 follow-up email** to Jeremy (cc Christina, Sara, Cameron) from `kyle@gosayer.com` after Cameron alignment + Gamma regen
- [ ] Verify `kyle@sayer.com` as Superhuman send-as alias (housekeeping)
- [ ] Manual check in HubSpot UI for orphan Lead objects on Jeremy/Ryan/Christina/Sarah contacts
- [ ] Add v3 Project Baseline entry to `calibration/calibration.md` once final pricing locks

### Client Owes
- [ ] **Jeremy** — answer on QuotaPath in/out by EOW 2026-05-08
- [ ] **Jeremy** — confirm DocuSign replacement direction (Commerce Hub native vs PandaDoc)
- [ ] **Jeremy** — grant Sayer access to HubSpot sandbox (Salesforce + Rev IO data) for W2 audit
- [ ] **Jeremy** — confirm Commerce Hub Professional licensing (or upgrade decision) before W4 begins
- [ ] **Sara Hines** — send finalized sales-stage definitions (week 1 of delivery)
- [ ] **Christina** — confirm sales-stage definitions align with current ClickUp setup; Phase 2 ideas deferred
- [ ] **Jeremy** — finalize ALN + QuickBooks integrations himself this week (informational; not in Sayer scope)

---

## Next Session Focus

1. **Cameron alignment** — share the v3 patch doc + Drive artifacts; lock $28,700 median (or adjust)
2. **Manual SOW Sheet apply** — Kyle works through `HelloSpoke_SOW_Sheet_v3_Update_Spec.md` tab-by-tab against the authoritative sheet
3. **Gamma deck regen** — generate new v3 deck from the v3 proposal markdown content
4. **v3 follow-up email** — draft to Jeremy from `kyle@gosayer.com`; QuotaPath as explicit optional checkbox; deadline reset
5. **Working copy SOW mirror** — apply same updates after authoritative is verified

---

## Key Artifacts

| File | Purpose |
|------|---------|
| `HelloSpoke_decisions.md` | Decisions log: 4/14, 4/21, 4/23, 4/24, 5/4, 5/7 |
| `HelloSpoke_v3_SOW_Project_Sheet.xlsx` | **v3 SOW workbook (10 tabs)** — Cover, Hours, Task Breakdown (67 tasks), Phase Matrix, Requirements, Success Criteria, Risk Register, Assumptions, Out of Scope, Open Items. Pending Drive upload. |
| `build_v3_sow_sheet.py` | Re-runnable workbook builder (openpyxl, Sayer brand colors) |
| `HelloSpoke_sow_update_patch_v2.md` | **v3 patch doc (active)** — strip-add-keep tables, v3 workstreams, hours, risk register, application plan |
| `HelloSpoke_clickup_workstream.md` | **Superseded 2026-05-05** — workstream stripped from v3 |
| `HelloSpoke_sow_update_patch.md` | **Superseded 2026-05-05** — v2 patch (4/24) |
| Rescope plan (Claude) | `~/.claude/plans/alright-now-i-need-virtual-pudding.md` (5/5), `~/.claude/plans/i-need-to-rescope-synchronous-sifakis.md` (5/7 execution plan) |
| Drive: v3 Proposal | `1b2WOhxXmD1BrLI5JU-Xq0H00qR0ZNAT6` — `HelloSpoke_HubSpot_CRM_Proposal_v3.md` |
| Drive: v3 Scope Summary | `1Q8ZnFSV4vW7oHhzz6J9534XiEn0dbyCs` — `HelloSpoke_Scope_Summary_v3.md` |
| Drive: v3 SOW Sheet Update Spec | `1LUYTyEvmx2bgngdcy4D0AnN8M4EoHAzk` — `HelloSpoke_SOW_Sheet_v3_Update_Spec.md` (manual-apply checklist) |
| Drive: Authoritative SOW Sheet | `1Kctr6sIfFQY7PzMY-GAHopI7fOdjl_TEgUi8zSjh1uY` — pending manual v3 apply |
| Drive: Working Copy SOW Sheet | `1JahJZ6tBuii1KyeE_D1SpMUk9NJtZClhwQHq5f-BcFs` — defer until authoritative verified |
| Drive: hellospoke folder | `16VrwmgEqJRSq1YIM3LmDJ0NX61Sq1Ss-` (parent for v3 artifacts) |
| Fireflies 5/4 walkthrough | https://app.fireflies.ai/view/01KQSVGHKNQ1PM7X5ZPWJ4GJJK |
| HubSpot Company `307857992394` | https://app.hubspot.com/contacts/46319964/record/0-2/307857992394 |
| HubSpot Deal `306004595439` | $42k, Decision Maker Bought-In — https://app.hubspot.com/contacts/46319964/record/0-3/306004595439 |
| Fireflies 4/14 discovery | https://app.fireflies.ai/view/01KNT5ZFCGEYFFWTBZYS196RC7 |
| Fireflies 4/21 next-steps | https://app.fireflies.ai/view/01KPRWATCQDV6NF29TWWHMKA1C |
| Fireflies 4/23 ops discovery | https://app.fireflies.ai/view/01KPRXJ0AX07VPYY4T9EEBGZJD |
| Slack channel (internal) | `#project-hellospoke` in sayerhq.slack.com |

---

## Key Decisions

- **V3 pricing locked at $28,700 median** (2026-05-07). 164 hrs at $175/hr; range $25,375 – $32,900; 4-month installments of $7,175 + 5% tech fee. Pending Cameron sign-off before v3 ships to Jeremy. Honors the 4/21 discount signal (Sarah's 45% counter against the original v1 $52,500 target) without needing a separate discount conversation.
- **Commerce Hub Professional is required** for the v3 quoting workstream (W4) (2026-05-07, validated via web research). Native e-signature lives in Commerce Hub specifically — Sales Hub Pro alone is insufficient. Caps: 25 sigs/user/mo (Pro), 50/user (Enterprise), pooled. Tier validation moves to Workstream 1; surfaced as Risk #1 in v3 risk register.
- **DocuSign replacement is partial via Commerce Hub native** — quote signing only (2026-05-07). Non-quote contracts (SOWs, MSAs, NDAs) require PandaDoc, HubSpot Contracts beta (limited; not relied on), or keeping DocuSign. W5 hour range absorbs both paths.
- **V3 rescope direction: strip integration build, add Data QA + audit, pass pricing through** (2026-05-05, post 5/4 call). Jeremy has built Rev IO + ClickUp + Salesforce migration himself; he's finalizing ALN; he doesn't want QuickBooks. Sayer's role on the data side becomes audit + validation before production push, not build.
- **Pricing direction: pass savings through to client** (2026-05-05, confirmed with Kyle). Target $26-32k base at $175/hr, ~150-180 hrs. Final number aligned with Cameron before delivery. Supersedes 4/24 $44,000 / $24,500 anchors.
- **QuotaPath = explicit optional add-on with EOW 2026-05-08 deadline** (2026-05-05, confirmed with Kyle). v3 ships without waiting on Jeremy's decision; QuotaPath appears as a checkbox line item.
- **Quoting & CPQ workflow is the #1 priority** (5/4). Jeremy: "The big ones are the quoting like making sure that the reps can quote easily." CSV upload pain, validation, property mapping, Commerce Hub CPQ.
- **DocuSign is being killed** (5/4). Jeremy: "I told DocuSign to eat a dick." Commerce Hub native signature is the leading replacement (Cameron's recommendation); PandaDoc is the backup.
- **HubSpot foundational architecture in scope and elevated** (5/4). Cameron asked, Jeremy said "I think we're open to it" — objects, pipelines, lead status, lifecycle stages, properties become a named workstream.
- **Phase 2 deliberately under-scoped** (5/4). Christina: "We just really don't know what we don't know." Phase 2 ideas deferred to a follow-on engagement.
- **ClickUp workstream pivots from integration build → workflow refinement** (5/4). Integration exists; what's missing is workflow correctness and gating.
- **Treat v3 as a new proposal, not a patch** (2026-05-05). Composition is changing materially. New Gamma deck supersedes `erumqig7pyx7rhm`; new Google Sheet revision supersedes 4/24.

### Superseded by v3 (kept for trail)

- ~~Pricing locked at $44,000 for full scope~~ (2026-04-24) — replaced by pass-through pricing 2026-05-05
- ~~Reduced scope option = $24,500~~ — no longer the alternative; v3 base is the new floor
- ~~Sayer builds native HubSpot↔ClickUp integration + Make middleware~~ (4/23) — Jeremy built it himself; stripped 5/5
- ~~Propose HubSpot form as replacement for ClickUp implementation form~~ (4/23) — out with the integration workstream
- Status model, mandatory field gating, legacy SF↔ClickUp out-of-scope, 10DLC, Win-property — all carry forward as decisions but no longer drive a dedicated integration workstream

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
