# Project Scoping & Delivery Tool - CLAUDE.md

## Project Purpose
This repo contains the full consulting engagement lifecycle for Harbuck Consulting / Sayer systems implementation projects (primarily HubSpot CRM). It covers scoping (pre-sale), delivery management (post-sale), and calibration (learning from outcomes). Two calibration systems learn from past projects: one for scoping accuracy, one for delivery effectiveness.

## How This Project Works
1. Cameron Taggart runs discovery calls with clients, produces transcripts and summary notes
2. Kyle and Claude analyze discovery materials and generate scoping packages
3. Scoping packages include: Excel estimate (4 sheets + actuals columns), scope summary (markdown), risk register, approach comparison
4. After project closes, Claude walks Kyle through a conversational retro and records actuals for calibration

## Key Files

### Scoping
- `scoping-skill.md` -- The scoping skill definition (workstream templates, estimation framework, risk register standards, Excel format spec)
- `calibration/calibration.md` -- **READ FIRST before every scoping session.** Calibration data from past projects, estimation adjustments, and cross-project patterns.
- `templates/post-project-retro.md` -- Post-project retrospective template
- `Sayer_Proposal_examples/` -- Reference proposals for format/tone

### Delivery
- `calibration/delivery-calibration.md` -- **READ FIRST before generating delivery plans.** Delivery patterns from completed projects.
- `templates/plan-schema.json` -- JSON Schema for plan.json (the intermediate delivery format)
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

## Delivery Skills (6 skills + orchestrator)

Skills live in `~/.claude/skills/` and are invoked as slash commands:

| Skill | Purpose | Trigger |
|-------|---------|---------|
| `/project-plan` | Translate proposal → plan.json + Linear project | "plan [client]", "set up [client]" |
| `/project-sheet` | Generate client-facing Google Sheets | "create sheet for [client]" |
| `/meeting-calendar` | Generate Gamma decks + calendar events | "set up meetings for [client]" |
| `/project-kickoff` | Orchestrate plan → sheet → meetings | "kick off [client]" |
| `/project-status` | Pull Linear data, generate status update | "status on [client]", "where are we" |
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
- **Google Sheets:** Service account JSON via Keychain (`GOOGLE_SERVICE_ACCOUNT_JSON`)
- **Google Calendar:** MCP tools (already authenticated)

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
- **Top Down Auto** -- Scoped, pending follow-up call for ERP clarification. See `Top Down Auto/`
- **Arkview Capital** -- Scoped, pending SOW delivery. See `Arkview Capital/`
- **Trialta** -- **ACTIVE DELIVERY.** Kickoff complete Apr 7, discovery call next. See `Trialta/`
- **Milestone Group** -- **ACTIVE DELIVERY.** Kickoff complete Apr 7, weekly Mon 2pm Central. See `MilestoneSoW/`
- **Strive Global** -- Proposal in progress, A/B options presented. See `Strive_Global/`
- **American Bedding** -- CPQ discussion only, not a full scope. See `American Bedding - CPQ Discussion/`
