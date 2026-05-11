---
session_number: 11
date: 2026-05-11
type: client-scoping
focus: Top Down Auto 2pm scoping call prep — Phase 1 audit pivot
---

## How This Works
This file is overwritten every session. Git is the history. Read PROJECT-STATE.md for dashboard, client STATE.md files for client-specific context.

## Last Session (11) — Top Down Auto 2pm Call Prep + 4/29 Scope Pivot Capture

Kyle opened with ~90 min until a 2pm CDT Top Down Auto scoping call. Tim Hainey wanted hard MVP requirements to draft a strong SOW for Stephanie. Prep work surfaced a **major scope pivot from the 4/29 call** that hadn't yet been captured in repo state: CRM platform decision shifted from HubSpot Sales Hub Pro to **NetSuite CRM**, Genesis (Ismael Cordero, gahh.com) confirmed as PIM owner, and Phase 1 work is now legacy Intuitive → NetSuite migration audit + CSR discovery, not HubSpot CRM build.

Fireflies surfaced two duplicate captures of the 4/29 "Topdown data discovery" call (IDs `01KQA5SA6TJ9K3RMT9ZGRR3N05` and `01KQD9YQPA4KKX7S106FF0Y1F3`) with Stephanie, Tim, Cameron, Ismael, and Alexis. Action items from that call basically drafted the Phase 1 SOW: phased audit + migration plan + internal NetSuite/data team coordination.

**Shipped (commit 3fc8dc3 on main):**
- `Top Down Auto/STATE.md` — rewritten to reflect 4/29 pivot, new stakeholders, stale-artifact flags
- `Top Down Auto/2026-05-11_pre-call_email_draft.md` — pre-call email for Stephanie/Tim
- `Top Down Auto/2026-05-11_call_runsheet.docx` — 60-min runsheet with strategic posture, agenda, 4 question blocks (A, B, C, D), watch-fors, and Block A.2 with Tim Hainey's 6 Intuitive→NetSuite migration questions

**External actions:**
- Superhuman draft pushed (`draft00a90ad8d2e2d54c`) for Stephanie + Tim, CC Cameron, from kyle@gosayer.com — pre-call email with Phase 1 framing
- Fireflies 4/29 transcripts pulled and synthesized
- Drive uploads attempted (2 stub `text/html` files in `top-down-auto` folder need cleanup)

**Branch hygiene save:** session started on `docs/hellospoke-v3-cameron-alignment` (HelloSpoke PR branch) with stale state — origin/main was 2 commits ahead with HelloSpoke v3 work that landed since the PR was opened. Stashed Top Down work, switched to main, pulled, popped, committed on main cleanly. **The `feedback_pull_origin_before_session.md` memory worked exactly as intended this session.**

## Open (max 3 — new this session)
1. **2pm Top Down call execution.** Email draft in Superhuman ready to send by 1pm. Runsheet docx ready to drag-drop into Drive as Google Doc. Two stub HTML files in Drive need cleanup (`1gHcBVO2NaaOiug_Gdi-1ee7rTmafnz6c`, `15ssRauiyDBW6ESJppUIB8TkbJQHL8dHj`).
2. **Phase 1 SOW draft within 48 hours of 2pm call.** Sized from Block A + A.2 answers. Anchor band $15–25K but may widen — Tim's ETL/field-map questions can push it higher.
3. **Google service account credential gap.** `GOOGLE_SERVICE_ACCOUNT_JSON` is referenced in CLAUDE.md as keychain-stored but is not actually in the keychain. Blocks programmatic Drive uploads via `sayer-gdoc`. See `memory/google_drive_upload_credential_gap.md`.

## Carried forward from earlier today (S10 — HelloSpoke)
- Cameron review feedback on v3 Superhuman draft → then send.
- Jeremy's three open decisions: QuotaPath, DocuSign direction, sandbox access.
- Google Sheet cleanup — remove stale $175/hr rows before client clicks source link.

## Carried forward from S8/S9
- Linear estimate-scale reconfig (Fibonacci snap on hours issue).
- NAKs proposal expiry 2026-06-04.
- Scoping-tool branch push decision (now N/A — landed today's work on main; PR branch still has 2 commits unpushed for HelloSpoke v3).
- Pre-existing repo churn triage (untracked: AmeriPouch/, Rise Run/, Trialta copy/, VestaFreight/, STATE.md at root, AGENTS.md, .cursor/, etc.).
- AmeriPouch S9 kickoff follow-ups.

## Git state
- `main` tip: `3fc8dc3` — 1 unpushed commit (today's Top Down Auto prep)
- `docs/hellospoke-v3-cameron-alignment` — 2 unpushed commits (S10 HelloSpoke v3 work); PR branch never pushed to origin yet
- Repo has substantial untracked churn (8+ client folders/files outside this session's scope) — pre-existing, deferred

## Next Action When Resuming
1. After 2pm call: write Block A + A.2 answers into `Top Down Auto/STATE.md`, draft Phase 1 SOW within 48 hours.
2. Drag-drop runsheet docx to Drive + delete the two stub HTML files (≤1 min).
3. Decide whether to push `docs/hellospoke-v3-cameron-alignment` to origin and open the PR, or rebase onto current main first.
4. Address the Google service account credential — either add `GOOGLE_SERVICE_ACCOUNT_JSON` to Keychain so `sayer-gdoc` can complete the pipeline, or update CLAUDE.md to remove the claim that it's available.
