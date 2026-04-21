# Milestone Group — Session State

> **Status:** `Active Delivery`
> **Last updated:** 2026-04-21
> **One-liner:** 8-week HubSpot CRM implementation for PE real estate firm replacing scattered Outlook/Excel/Zoho tracking — Wk 2, pipeline spec locked, properties build in flight.

---

## Current Position

| Field | Value |
|-------|-------|
| Phase | Phase 1 — Contacts & Activity Capture |
| Week | Wk 2 of 8 |
| Phase end date | 2026-05-08 |
| On track? | Yes on property build (Robert delivered spec) — **blocked on M365 admin creds (ENG-83) for activity-capture workstream** |

---

## Done Last Session (2026-04-21)

**Weekly sync call (14:00 CT, 27 min):**
- **Pipeline spec locked** — Robert shared refined active-tab spreadsheet live; focus on **Status column only** (4th column). Priority/Active become optional dropdowns. Closed tab deleted from build scope.
- **Data model confirmed:** Company → Seller (always), Broker (when marketed), Property = Project. Portfolios = multiple properties owned by one seller (Waterton example).
- **Contact ownership: no rules.** All 3 (Jason, Robert, Jim) share. Bulk-import + most-complete-record dedup authorized.
- **Jason delivered contact export** ✓. Dedup in progress. Friday Apr 24 upload target (one day ahead of hard deadline).
- **Team roles named publicly:** Kyle still leads, Weston = day-to-day PM + HubSpot Build Lead. Robert stays day-to-day champion. Jason = exec stakeholder / sign-off.

**Post-call workflow executed (via `/sayer-post-call Milestone`):**
- HubSpot note `365516064504` logged — all 5 associations (Company + 3 Contacts + Milestone-CRM Deal) successful
- HubSpot task `365551655672` created — "Chase Robert Strong for Microsoft 365 admin credentials (ENG-83)" — HIGH priority, due EOD 2026-04-21, owned by Kyle
- Gmail draft #1 (`r-7133084316364069882`) — team recap + Drive link to Jason/Robert/Jim cc Weston/Cam
- Gmail draft #2 (`r-4670589972762499888`) — M365 creds ask to Robert (short/direct)
- Slack post to #milestone (C0AFYB270P8): https://sayerhq.slack.com/archives/C0AFYB270P8/p1776800860557289
- Contact firstname cleanup: Jason Wise (was "Jwise Wise") + Jim Duey (was "Jduey") — HubSpot records now display correctly

**What didn't happen in-call (carried to async):**
- M365 admin creds ask — NOT raised live (critical path miss)
- Drive URL — not announced in-call; recovered via draft #1 email
- Workflow requirements session scheduling (ENG-98) — not scheduled; push to next Tuesday

### Prior session (2026-04-20)

- **Linear project live in Engagement/Support team:** https://linear.app/gosayer/project/milestone-group-hubspot-crm-implementation-2c60f3bede3a
- Created 9 weekly milestones (Apr 18 → Jun 12 target dates) for progress rollup
- Created 3 phase parent issues: ENG-44 (Phase 1), ENG-45 (Phase 2), ENG-46 (Phase 3) with success criteria descriptions
- Created all 125 sub-issues (ENG-47 through ENG-171) covering all 13 workstreams, each with milestone assignment, workstream prefix + owner labels, rounded-integer estimates
- Wired 42 `blockedBy` dependency edges covering gate transitions: properties-workshop → property-creation, migration chain (audit → normalize → dedupe → test-load → review → fix → prod-import), M365-creds fan-out, workflow-session → WF1-5, pipeline/reporting sessions → their outputs, Fireflies-subscription → connect, training sessions → sign-off, UAT chain (scripts → share → session 1 → triage → fix → session 2 → sign-offs → go-live), hypercare Wk1 → Wk2
- Added `DOC` workstream label (reused `CRM`, `MIG`, `INT`, `TRN`, `UAT`, `sayer`, `client`, `shared` from Trialta rebuild)
- Wrote `delivery-state.json` (schema v2.0, mirrors Trialta structure) with all Linear IDs + dependency edge summary

### Prior session (2026-04-14)
- Rebuilt plan.json from signed proposal as source of truth (125 tasks, 13 workstreams, hours verified at 176h median)
- Corrected pricing to $26,000 / 4 × $6,500 every 15 days Net-15 (was $26,075 / 50-50)
- Created client-facing `Milestone_Project_Tracker.xlsx` (4-sheet XLSX, status dropdowns)
- Generated `milestone-project-tracker.csv` (137 rows, Google Sheets-importable)
- Pushed Working Session #1 deck to Gamma: https://gamma.app/docs/b3calyxkhao6z3z
- Drafted + sent pre-meeting message to Jason and team
- Held first weekly standup + working session #1 at 2pm Central
- Fireflies confirmed in scope (signed proposal WS7 — previously listed as TBD)

---

## Open Items

### Sayer Owes
- [ ] **Kyle: Send Gmail drafts `r-7133084316364069882` (team recap) and `r-4670589972762499888` (M365 ask to Robert)** — both staged, pending review
- [ ] **Kyle: Share Drive folder with jwise@, rstrong@, jduey@ as editors** — promised in draft #1 body
- [ ] **Kyle + Weston: Build HubSpot properties from Robert's active-tab spec** (ENG-57, ENG-58) — by next call 2026-04-28
- [ ] **Kyle: Record Outlook-setup walkthrough video** OR schedule 1:1 setup calls — for next call onboarding
- [ ] Send rules of engagement examples / short video (Jason flagged at kickoff)
- [ ] Rotate `LINEAR_API_KEY` in macOS Keychain — current token returns 401 (OAuth via claude.ai MCP works; direct scripts that need the key do not)
- [ ] Forward Robert's active-tab spreadsheet to Claude for archival to Drive `/03-artifacts/phase-1-build-spec/`

### Client Owes
- [ ] **Microsoft 365 admin credentials (ENG-83)** — **CRITICAL PATH.** Blocks ENG-84, 85, 86, 87, 88, 91 (tracking domain + per-user Outlook inbox + calendar sync). Chased via draft #2 to Robert — awaiting response.
- [x] ~~Outlook contact exports — Jason~~ — **Delivered 2026-04-21.** Dedup in progress for Friday Apr 24 upload. Older team members backfill later (Robert OK'd).
- [x] ~~Robert: refined deal pipeline spreadsheet~~ — **Delivered 2026-04-21 in-call.** Active tab is Phase 1 property-build spec.
- [ ] Zoho CRM export — small team segment (deadline: **2026-04-25**)
- [ ] Confirm Fireflies subscription + API access (required before Phase 3)

---

## Next Session Focus (Tuesday 2026-04-28 @ 2pm CT)

1. **Review built properties** — Kyle + Weston walk through what's in the portal (ENG-57, ENG-58) per Robert's active-tab spec. Robert confirms or redlines.
2. **Kick off user provisioning** (CRM-01 workstream, ENG-47-55) — pending M365 creds resolution.
3. **Outlook integration walkthrough** — video OR 1:1 calls; depends on creds timing.
4. **Confirm Zoho export status + Fireflies API access** — light check-ins, push forward if not resolved.
5. **Schedule workflow requirements session with Jason** (ENG-98) — find a 45-min slot this week or next.

---

## Key Artifacts

| File | Purpose |
|------|---------|
| `plan.json` | Source of truth — 125 tasks, 13 workstreams, 3 phases |
| `Milestone Group HubSpot CRM Proposal - Signed.md` | Signed proposal — authoritative for scope and pricing |
| `Milestone_Project_Tracker.xlsx` | Client-facing 4-sheet tracker |
| `milestone-project-tracker.csv` | Flat CSV for Google Sheets |
| `working-session-1-deck.md` | Working session deck (Gamma: https://gamma.app/docs/b3calyxkhao6z3z) |
| `Data Discovery Template.md` | 23-question blueprint template — answers to be captured |
| `create_linear_project.py` | Older flat-structure script — **superseded by Linear MCP approach Apr 20**, keep as reference only |
| `delivery-state.json` | **New Apr 20** — schema v2.0 state file with Linear project/milestone/phase-parent IDs (mirrors Trialta structure) |

---

## Key Decisions

- **Pipeline spec source (2026-04-21):** Robert's refined active-tab spreadsheet is authoritative. Focus on Status column (4th). Priority/Active become optional dropdowns. Closed tab excluded from build.
- **Data model (2026-04-21):** Company → Seller (always present), Broker (only when marketed), Property = Project. Portfolios = multiple properties under one seller.
- **Contact ownership (2026-04-21):** No ownership rules. All users share. Bulk-import with "most complete record" dedup logic — Robert, Jason, Jim all explicitly OK'd.
- **Calculated properties (2026-04-21):** TMG price per unit = Excel formula. HubSpot API cannot create rollups — must be manually configured in UI after property build.
- **Pricing source of truth:** Signed proposal ($26,000) supersedes `Milestone_final_estimate.md` ($26,075)
- **Fireflies phasing:** Confirmed in scope as Phase 3. Client must provide API access before Phase 3 starts.
- **Outlook sync phasing:** Kept in Phase 1 (INT-02) despite proposal listing it in Phase 3 — Phase 1 success criteria requires calendar sync working
- **Migration approach:** Conservative — start with priority contacts (broker + acquisition target list), Outlook auto-capture handles the rest

---

## Standing Context

- 4 offices: Atlanta, Dallas, Denver, South Florida. 10 users.
- **Roles (as of 2026-04-21):** Robert Strong = day-to-day champion (Milestone). Jason Wise = exec stakeholder / sign-off (Milestone). Kyle Harbuck = Sayer Project Lead. Weston Baker = Sayer PM + HubSpot Build Lead. Cameron Taggart = Sayer Exec Sponsor.
- **HubSpot Portal ID:** 245699062. **Tier:** Sales Hub Professional (1 seat) + Core Seats Professional (19 seats) = 20 total seats. 3,000 HubSpot credits/mo included. Custom 10% discount negotiated ($945/mo billed).
- Microsoft 365 / Outlook only — NOT Google Workspace (corrected at kickoff)
- Prior DealCloud abandonment after 2 months — adoption risk is real. Ages 25–65.
- Robert's smart approach: export Outlook per broker, filter against acquisition target list
- Linear project (live Apr 20): https://linear.app/gosayer/project/milestone-group-hubspot-crm-implementation-2c60f3bede3a
- Shared Drive (live Apr 21): https://drive.google.com/drive/folders/0ABostCjJJ6egUk9PVA
- Weekly standups: Tuesday 2pm Central (confirmed 2026-04-14 Discovery)
