# Project Scoping & Delivery Tool - CLAUDE.md

## Project Purpose
This repo contains the full consulting engagement lifecycle for Sayer systems implementation projects (primarily HubSpot CRM). It covers scoping (pre-sale), delivery management (post-sale), and calibration (learning from outcomes). Two calibration systems learn from past projects: one for scoping accuracy, one for delivery effectiveness.

## Bundled Plugin Skills (what teammates get)

This repo doubles as the `project-scoping` Claude Code plugin (marketplace `sayer-scoping`). Installing it provides:

| Skill | Purpose |
|-------|---------|
| `/client-intake` | Scaffold client folder; pull Fireflies/Gmail/HubSpot discovery; mirror to the Notion "Client Engagements" database |
| `/scope-project` | Generate workstream estimates, risk register, branded 5-sheet Excel package |
| `/sayer-rates` | Rate card, blended rates, staffing bios |
| `sayer-brand-guidelines` | Brand specs (colors, typography, logo) — auto-read before any client-facing artifact |

Setup runbook: `SETUP-FOR-TEAM.md`. Delivery skills are NOT bundled — see the Delivery Skills section below.

## How This Project Works
1. Cameron Taggart runs discovery calls with clients, produces transcripts and summary notes
2. Kyle and Claude analyze discovery materials and generate scoping packages
3. Scoping packages include: Excel estimate (5 sheets + actuals columns), scope summary (markdown), risk register, approach comparison
4. After project closes, Claude walks Kyle through a conversational retro and records actuals for calibration

## Session Start Protocol

At the start of every session in this repo:
1. Read `PROJECT-STATE.md` — get a quick orientation on all active projects
2. If working on a specific client, **read `wiki/clients/{client-slug}.md` first** (synthesized one-pager), then `{Client}/STATE.md` for raw current state
3. STATE.md is the in-repo source of truth for session handoff — do not rely on memory alone
4. Update `{Client}/STATE.md` and `PROJECT-STATE.md` at the end of every session via `/wrap-up`

## Wiki Protocol

A synthesized knowledge wiki lives in `wiki/`. It compresses raw client folders into dense, cross-linked pages. Claude reads and maintains it — raw source files stay immutable.

**Read the wiki first:**
- Starting a client session → `wiki/clients/{client-slug}.md` (richer than cold-reading 8 raw files)
- Scoping a new engagement → `wiki/patterns/` + `wiki/methodology/workstream-estimates.md`
- Looking for a pattern or lesson → `wiki/index.md` then the relevant pattern page

**Update the wiki after every substantive session:**
- After working on a client → update `wiki/clients/{client-slug}.md` (status, new decisions, open items)
- After any calibration update → update the relevant `wiki/patterns/` page
- Always append a line to `wiki/log.md`: `YYYY-MM-DD | update | pages affected | source`

**Ingest new clients:**
- When a new client folder appears → create `wiki/clients/{slug}.md` from STATE.md + scope summary + decisions log
- Run `python3 scripts/wiki_tool.py sources` to see any un-wikified folders

**Weekly maintenance:**
- `python3 scripts/wiki_tool.py lint` — flags STALE pages (30d default, 14d for active delivery), BROKEN cross-links, INCOMPLETE stubs
- `python3 scripts/wiki_tool.py list` — full page inventory with ages

**The wiki can be wrong.** When in doubt, read the raw source. The wiki is a session-start accelerant, not the legal source of truth.

**STATE.md convention:**
- Every active client folder has a `STATE.md` tracking current phase, open items, and next session focus
- Template: `templates/client-state-template.md`
- These files are committed to git — they are version-controlled session handoffs, not scratch notes

## Key Files

### Scoping
- `skills/scope-project/SKILL.md` -- The scoping skill definition (workstream templates, estimation framework, risk register standards, Excel format spec). Decomposed into `skills/scope-project/references/` (workstream-catalog, hour-ranges, risk-register-template, excel-formatting, example-scope). **Authoritative source of truth** — the former root `scoping-skill.md` monolith was retired 2026-06-12.
- `templates/scoping-schema.json` -- JSON Schema for `scope.json`, the structured estimate record `scope-project` emits per engagement (phase/task x hours x rate x cost). Calibration data source + AIVA invoke contract.
- `calibration/calibration.md` -- **READ FIRST before every scoping session.** Calibration data from past projects, estimation adjustments, and cross-project patterns.
- `templates/scope-summary-template.md` -- Post-discovery scope writeup (tier recommendation, workstreams, risks, assumptions, outstanding items)
- `templates/decisions-template.md` -- Scoping decisions log with worked examples (D1-D3 format)
- `templates/final-estimate-template.md` -- What was sent to client, final price, pricing history, deviations
- `templates/discovery-prep-template.md` -- Data discovery questionnaire for first working session
- `templates/post-project-retro.md` -- Post-project retrospective template
- `Sayer Proposal Examples/` -- Reference proposals for format/tone
- `scripts/intake.py` -- **Client intake automation.** Given a HubSpot record URL, pulls company/deal/contacts/engagements from HubSpot, matches Fireflies transcripts by attendee email, and scaffolds the `{Client Name}/` folder per the convention below. Read `scripts/README.md` for usage.

### Delivery
- `calibration/delivery-calibration.md` -- **READ FIRST before generating delivery plans.** Delivery patterns from completed projects.
- `templates/plan-schema.json` -- JSON Schema for plan.json (the intermediate delivery format)
- `templates/kickoff-deck-template.md` -- Gamma markdown for client-facing kickoff presentation
- `templates/governance-framework-template.md` -- Working agreement, roles, communication, scope management, escalation
- `templates/standup-template.md` -- Weekly standup structure (since last week, this week, blockers, hours)
- `templates/phase-review-template.md` -- Phase completion review (objectives, hours, risks, next phase)
- `templates/follow-up-email-template.md` -- Post-call follow-up email structure (action items, deliverables, next agenda)
- `templates/delivery-retro.md` -- Delivery retrospective template (9 sections)
- `templates/phase-pulse.md` -- Lightweight phase completion pulse template (2 questions)

## Folder Convention
- Each client gets a folder: `{Client Name}/`
- Client folders contain: discovery .md, recording .md/.mp3, Scoping Estimate .xlsx, Scope Summary .md
- `{Client}_decisions.md` -- Key scoping decisions and reasoning captured during the session
- `{Client}_final_estimate.md` -- Which version/file went to client, at what price, and when
- After project closes: completed retro .md, actuals entered in Excel, learnings extracted to calibration.md
- **Delivery artifacts (post-signing):**
  - `plan.json` -- Structured project plan (intermediate format for all delivery skills)
  - `delivery-state.json` -- Artifact IDs for idempotency (Linear, Google Sheets, Calendar)
  - `create_linear_project.py` -- Generated Linear API script
  - `kickoff-deck.md`, `standup-template.md`, `phase-review-template.md` -- Gamma markdown meeting decks
  - `phase-notes.md` -- Running phase completion pulses
  - `delivery-retro.md` -- Post-project delivery retrospective

## Scoping Workflow
0. **Intake (when starting from a HubSpot record)** -- Run `python3 scripts/intake.py --url <HUBSPOT_URL>` to scaffold the client folder automatically. Verify credentials first with `--test-only`. Skip this step if discovery materials already exist in a client folder.
1. **Read `calibration/calibration.md`** -- Check for similar past projects and estimation adjustments
2. Read discovery notes and transcript thoroughly
3. Parse per the scoping skill: client profile, current state, desired future state, complexity indicators, unknowns
4. Ask Kyle clarifying questions one at a time before generating estimates
5. Generate Excel workbook (4 sheets + actuals columns) and scope summary markdown
6. **Check for stale code:** When updating scoping docs, also check generator scripts (`build_estimate.py`, `generate_proposal.py`) and re-validate any prior analysis. Stale scripts can overwrite current workbooks.
7. Flag open items, gotchas, and questions to go back to client with
8. Always recommend specific HubSpot tier with reasoning (not generic "TBD")
9. **Log key decisions** in the client's `_decisions.md` during the session
10. **After scoping is complete:** Ask Kyle which version is the final delivery, record in `_final_estimate.md`, and add a new Project Baseline entry to `calibration/calibration.md`

## Learning System (Double-Loop Calibration)
Claude maintains two feedback loops:

### Scoping Calibration (estimates → actuals)
- **Before scoping:** Always read `calibration/calibration.md` for patterns and adjustments from past projects
- **During scoping:** Capture decisions and reasoning in `{Client}_decisions.md` -- especially when deviating from baseline ranges and why
- **After scoping:** Add the project to calibration.md under Project Baselines
- **When a project closes:** Run `/delivery-retro` to bridge actual hours back to scoping calibration
- **Never silently adjust estimates** -- When calibration data influences an estimate, cite the source project

### Delivery Calibration (plans → outcomes)
- **Before planning:** Read `calibration/delivery-calibration.md` for phase duration adjustments, meeting patterns, and scope change frequency
- **During delivery:** Phase completion pulses (2 questions, <60s) capture running data in `phase-notes.md`
- **After delivery:** `/delivery-retro` writes to both calibration files -- delivery patterns to `delivery-calibration.md`, actuals back to `calibration.md`
- **Cross-project patterns** extracted after 2+ completed deliveries

## Estimation Defaults
- Rate: $150/hr (configurable in Excel cell B1)
- Baseline ranges come from the scoping skill workstream tables, **adjusted by calibration data**
- PE/finance clients: add FINRA compliance considerations, no call recording, manual NDA tracking
- Always include actuals columns (green cells) in Excel for post-project calibration

## Relationship Context
- Some clients have close personal relationships with Sayer/Harbuck (shared office, referrals, subleasing)
- Flag scope creep risk explicitly when relationship is close
- Ensure SOW is signed by budget authority, not just the champion who attended discovery

## Delivery Skills (Kyle's machine only — not part of the shared plugin)

These post-sale skills live in Kyle's `~/.claude/skills/` and are NOT distributed with the `project-scoping` plugin — teammates can ignore this section. The delivery templates in `templates/` ARE shared; only the skills are not.

| Skill | Purpose | Trigger |
|-------|---------|---------|
| `/project-plan` | Translate proposal → plan.json + Linear project | "plan [client]", "set up [client]" |
| `/project-sheet` | Generate client-facing Google Sheets | "create sheet for [client]" |
| `/meeting-calendar` | Generate Gamma decks + calendar events | "set up meetings for [client]" |
| `/sayer-project-kickoff` | Orchestrate plan → sheet → meetings | "kick off [client]" |
| `/sayer-project-status` | Pull Linear data, generate status update | "status on [client]", "where are we" |
| `/delivery-retro` | Conversational retro, feed calibration | "retro on [client]", "close out [client]" |

**Data flow:** Proposal/SOW → `/project-plan` → plan.json → downstream skills
**Source of truth:** Proposal is authoritative for scope. Linear becomes operational truth during delivery. Google Sheet is a regenerable snapshot.

**plan.json authoring rules:**
- Always read the signed proposal file (`*Proposal*Signed*`) before generating or updating plan.json
- `_final_estimate.md` is a working doc and may be superseded by the signed proposal -- verify pricing and payment terms against the signed version
- Present phase-by-phase task breakdown and get Kyle's per-phase approval before writing plan.json
- Do not shortcut the review -- write only after all phases are approved

## Credentials

- **Linear API:** macOS Keychain (`security find-generic-password -a "harbuckconsulting" -s "LINEAR_API_KEY" -w`)
- **HubSpot API:** macOS Keychain (`HUBSPOT_API_KEY` -- Private App token with `crm.objects.{owners,companies,contacts,deals}.read` scopes)
- **Fireflies API:** macOS Keychain (`FIREFLIES_API_KEY`)
- **Google Sheets:** Service account JSON via Keychain (`GOOGLE_SERVICE_ACCOUNT_JSON`)
- **Google Calendar:** MCP tools (already authenticated)

Scripts resolve credentials via `scripts/keychain.py` in this order: macOS Keychain → environment variable → repo-local `.env` file → **shared Sayer 1Password vault** (`op read "op://Shared/<KEY_NAME>/credential"`). Never commit `.env`.

**Teammates need no personal API keys for Fireflies/HubSpot scripts** — the 1Password fallback resolves them from the Sayer `Shared` vault once the teammate installs the 1Password CLI and signs into the Sayer account (vault overridable via `SAYER_OP_VAULT`). The Keychain **account** defaults to `harbuckconsulting` but is overridable per machine via the `SAYER_KEYCHAIN_ACCOUNT` env var. See `SETUP-FOR-TEAM.md` for the full teammate onboarding runbook.

## Testing

### Generated Python Scripts
- All generated scripts must pass `python3 -c "import py_compile; py_compile.compile('<path>', doraise=True)"` on Python 3.9
- Use `typing.Optional[X]` instead of `X | None` (3.10+ syntax not supported)
- Use `typing.Tuple[X, Y]` instead of `tuple[X, Y]` for return type hints
- Linear scripts: test with `--dry-run` flag before live execution
- Google Sheets scripts: test with `--refresh` flag on existing sheets before creating new ones

### plan.json Validation
- After generating plan.json, verify hours integrity: sum of all workstream hours (across phases + cross-phase) must equal `engagement.totalHours`
- Validate with: `python3 -c "import json; d=json.load(open('plan.json')); ..."` (see validation script in commit `17ef982`)
- All workstream IDs must follow `PREFIX-NN` pattern (CRM-01, MIG-03, etc.)
- All phases must have at least one workstream and one success criterion

### Skill Smoke Tests
- `/project-plan` with `--skip-linear`: generates plan.json without API dependency
- `/project-sheet` with `--detail`: generates both summary and full export sheets
- `/meeting-calendar` with `--decks-only`: generates Gamma markdown without calendar API
- `/project-status`: requires Linear project to exist (test after Linear workspace setup)
- `/delivery-retro` with `--phase-pulse`: lightweight 2-question mode, no API needed

### Idempotency
- Re-running any skill with existing `delivery-state.json` must not create duplicates
- Test by running a skill twice and verifying artifact counts match

## Current Active Projects

Active client engagements are tracked **locally only** — client folders, `PROJECT-STATE.md`,
and each `{Client}/STATE.md` are gitignored and never committed to this shared repo (they
hold discovery materials, pricing, and live pipeline state). Run `/client-intake` to scaffold
a new client folder locally; consult your local `PROJECT-STATE.md` for the current portfolio.
