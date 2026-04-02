# Project Scoping Tool - CLAUDE.md

## Project Purpose
This repo contains discovery notes, scoping estimates, and proposals for Harbuck Consulting / Sayer systems implementation projects (primarily HubSpot CRM). It also maintains a calibration system that learns from past projects to improve future estimates.

## How This Project Works
1. Cameron Taggart runs discovery calls with clients, produces transcripts and summary notes
2. Kyle and Claude analyze discovery materials and generate scoping packages
3. Scoping packages include: Excel estimate (4 sheets + actuals columns), scope summary (markdown), risk register, approach comparison
4. After project closes, Claude walks Kyle through a conversational retro and records actuals for calibration

## Key Files
- `scoping-skill.md` -- The scoping skill definition (workstream templates, estimation framework, risk register standards, Excel format spec)
- `calibration/calibration.md` -- **READ FIRST before every scoping session.** Calibration data from past projects, estimation adjustments, and cross-project patterns.
- `templates/post-project-retro.md` -- Post-project retrospective template
- `Sayer_Proposal_examples/` -- Reference proposals for format/tone

## Folder Convention
- Each client gets a folder: `{Client Name}/`
- Client folders contain: discovery .md, recording .md/.mp3, Scoping Estimate .xlsx, Scope Summary .md
- `{Client}_decisions.md` -- Key scoping decisions and reasoning captured during the session
- `{Client}_final_estimate.md` -- Which version/file went to client, at what price, and when
- After project closes: completed retro .md, actuals entered in Excel, learnings extracted to calibration.md

## Scoping Workflow
1. **Read `calibration/calibration.md`** -- Check for similar past projects and estimation adjustments
2. Read discovery notes and transcript thoroughly
3. Parse per the scoping skill: client profile, current state, desired future state, complexity indicators, unknowns
4. Ask Kyle clarifying questions one at a time before generating estimates
5. Generate Excel workbook (4 sheets + actuals columns) and scope summary markdown
6. Flag open items, gotchas, and questions to go back to client with
7. Always recommend specific HubSpot tier with reasoning (not generic "TBD")
8. **Log key decisions** in the client's `_decisions.md` during the session
9. **After scoping is complete:** Ask Kyle which version is the final delivery, record in `_final_estimate.md`, and add a new Project Baseline entry to `calibration/calibration.md`

## Learning System
Claude maintains a feedback loop between estimates and outcomes:

- **Before scoping:** Always read `calibration/calibration.md` for patterns and adjustments from past projects
- **During scoping:** Capture decisions and reasoning in `{Client}_decisions.md` -- especially when deviating from baseline ranges and why
- **After scoping:** Add the project to calibration.md under Project Baselines
- **When a project closes:** Offer to walk Kyle through the retro template conversationally (Claude asks questions, Kyle answers, Claude fills out the retro and extracts calibration entries)
- **Never silently adjust estimates** -- When calibration data influences an estimate, cite the source project (e.g., "Adjusting data migration up based on Strive experience with uncoded legacy data")

## Estimation Defaults
- Rate: $150/hr (configurable in Excel cell B1)
- Baseline ranges come from the scoping skill workstream tables, **adjusted by calibration data**
- PE/finance clients: add FINRA compliance considerations, no call recording, manual NDA tracking
- Always include actuals columns (green cells) in Excel for post-project calibration

## Relationship Context
- Some clients have close personal relationships with Sayer/Harbuck (shared office, referrals, subleasing)
- Flag scope creep risk explicitly when relationship is close
- Ensure SOW is signed by budget authority, not just the champion who attended discovery

## Current Active Projects
- **Top Down Auto** -- Scoped, pending follow-up call for ERP clarification. See `Top Down Auto/`
- **Arkview Capital** -- Scoped, pending SOW delivery. See `Arkview Capital/`
- **Milestone Group** -- Proposal delivered. See `MilestoneSoW/`
- **Strive Global** -- Proposal in progress, A/B options presented. See `Strive_Global/`
- **American Bedding** -- CPQ discussion only, not a full scope. See `American Bedding - CPQ Discussion/`
