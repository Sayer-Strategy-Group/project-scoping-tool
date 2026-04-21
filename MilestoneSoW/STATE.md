# Milestone Group — Session State

> **Status:** `Active Delivery`
> **Last updated:** 2026-04-20
> **One-liner:** 8-week HubSpot CRM implementation for PE real estate firm replacing scattered Outlook/Excel/Zoho tracking — Linear project fully live (125/125 sub-issues + 9 milestones + 3 phase parents + 42 blockedBy edges).

---

## Current Position

| Field | Value |
|-------|-------|
| Phase | Phase 1 — Contacts & Activity Capture |
| Week | Wk 1 of 8 |
| Phase end date | 2026-05-08 |
| On track? | Yes — blocked on client data exports |

---

## Done Last Session (2026-04-20)

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
- [ ] Set up shared Google Drive data room (promised Apr 10)
- [ ] Send rules of engagement examples / short video (Jason flagged at kickoff)
- [ ] Schedule next working session (smaller group: Jason + 1)
- [ ] Rotate `LINEAR_API_KEY` in macOS Keychain — current token returns 401 (OAuth via claude.ai MCP works; direct scripts that need the key do not)

### Client Owes
- [ ] Outlook contact exports — Jason, Robert, David, Rich, Jim (deadline: **2026-04-18** soft / **2026-04-25** hard)
- [ ] Zoho CRM export — small team segment (deadline: **2026-04-25**)
- [ ] Robert: broker contacts vs. acquisition target list (deadline: **2026-04-25**)
- [ ] Confirm Fireflies subscription + API access (required before Phase 3)
- [ ] Complete Data Discovery Template Q1–Q23 (working through live in session today)

---

## Next Session Focus

1. Capture data discovery answers from today's working session into `Data Discovery Template.md`
2. Begin CRM-01 (portal setup, user accounts, roles) — HubSpot access confirmed (ENG-47 through ENG-55)
3. Run properties workshop with Jason Wise (ENG-56) — blocks contact/company property creation
4. Begin repo restructure planning (dedicated session — see `PROJECT-STATE.md`)

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

- **Pricing source of truth:** Signed proposal ($26,000) supersedes `Milestone_final_estimate.md` ($26,075)
- **Fireflies phasing:** Confirmed in scope as Phase 3. Client must provide API access before Phase 3 starts.
- **Outlook sync phasing:** Kept in Phase 1 (INT-02) despite proposal listing it in Phase 3 — Phase 1 success criteria requires calendar sync working
- **Migration approach:** Conservative — start with priority contacts (broker + acquisition target list), Outlook auto-capture handles the rest

---

## Standing Context

- 4 offices: Atlanta, Dallas, Denver, South Florida. 10 users.
- Jason Wise = primary decision contact. Weston Baker = Sayer PM.
- Microsoft 365 / Outlook only — NOT Google Workspace (corrected at kickoff)
- Prior DealCloud abandonment after 2 months — adoption risk is real. Ages 25–65.
- Robert's smart approach: export Outlook per broker, filter against acquisition target list
- Linear project (live Apr 20): https://linear.app/gosayer/project/milestone-group-hubspot-crm-implementation-2c60f3bede3a
- Weekly standups: Monday 2pm Central
