# Skill Continuity Review — Reuse Launch Artifacts Across the Lifecycle

**Trigger:** A delivery session surfaced that `/project-plan` and `/project-sheet` did not
capture or reuse the engagement's already-created Google Drive folder,
`CRM Implementation/Deliverables/` subfolder, or its Notion engagement page. The draft
project sheet was built locally instead of being dropped into the existing Drive folder,
risking parallel sources of truth.

**Goal:** One set of launch artifacts (Drive folder, Notion page, Slack channel, Linear
project) created once and reused across intake → scoping → planning → delivery → status → retro.

---

## Findings

### 1. Who creates the launch artifacts

| Artifact | Created by | In this repo? |
|----------|-----------|:---:|
| Notion "Client Engagements" page | **`client-intake`** (Step 5) | ✅ bundled skill |
| Google Drive folder + `CRM Implementation/` subfolders | launch skill on Kyle's machine | ❌ not in repo |
| Slack channel (`#project-{slug}`) | launch skill on Kyle's machine | ❌ |
| Linear project/issue | `/project-plan` (per CLAUDE.md) or launch skill | ❌ |

**On the name "/project-launch":** it is not in this repo and not in CLAUDE.md's skill
tables. Drive-folder and Slack-channel creation appear in **none** of the documented
delivery skills (`/project-plan`, `/project-sheet`, `/meeting-calendar`,
`/sayer-project-kickoff`, `/sayer-project-status`, `/delivery-retro`). The launch skill
Kyle referenced is therefore an on-machine skill not yet reflected here — **its exact
name needs confirmation from Kyle's `~/.claude/skills/`.** Most likely `/sayer-project-kickoff`
(documented as the orchestrator) has grown Drive+Slack provisioning, or there is a newer
dedicated launch skill.

### 2. Root cause of parallel/duplicate artifacts

- **Launch-artifact IDs are persisted nowhere discoverable.** `client-intake` creates the
  Notion page but records its ID nowhere — it re-searches by client name each run. Fine for
  intake; useless for downstream skills, which don't repeat that search. Nothing records the
  Drive folder IDs at all.
- **`delivery-state.json` had no schema.** It was referenced in `CLAUDE.md` and
  `templates/client-state-template.md` as holding "Linear / Sheets / Calendar" IDs, but no
  schema defined it and its documented scope **omitted Drive, Notion, and Slack**. Only
  `plan-schema.json` existed.
- Consequence: when `/project-plan` / `/project-sheet` run, they have no anchor to the
  launch-created Drive folder or Notion page, so they build locally / create new artifacts.

### 3. Repo vs. on-machine split

- **Bundled here:** `client-intake`, `scope-project`, `sayer-rates`, `sayer-brand-guidelines`.
- **On Kyle's machine only:** `/project-plan`, `/project-sheet`, `/meeting-calendar`,
  `/sayer-project-kickoff`, `/sayer-project-status`, `/delivery-retro`, and the launch skill.
- The shared **templates + schema** in this repo are the contract those on-machine skills read.

---

## Recommendations — implemented in this repo

1. **`templates/delivery-state-schema.json` (new).** Defines `delivery-state.json` as the
   single lifecycle continuity ledger with a `launch` block (`driveFolderId`,
   `driveDeliverablesFolderId`, `driveWorkingFilesFolderId`, `driveMeetingNotesFolderId`,
   `notionPageId`, `notionDatabaseId`, `slackChannelId`, `slackChannelName`,
   `linear.{projectId, issueIdentifier}`), an `artifacts` block for regenerable IDs (sheet,
   decks, calendar events, Linear issues), and an append-only `history` log.
2. **`client-intake` seeds the ledger at intake** (new Step 6): writes
   `{Client}/delivery-state.json` with `launch.notionPageId` + `notionDatabaseId`, and checks
   the ledger before searching Notion so it reuses the existing page.
3. **`client-state-template.md`** gains a human-readable **Launch Artifacts** table mirroring
   the ledger.
4. **`CLAUDE.md`** documents launch-artifact ownership and a **read-before-create contract**
   for every downstream skill.

---

## Per-skill edit spec — to apply on Kyle's machine (`~/.claude/skills/`)

These skills are not in this repo. Apply the following so scoping and delivery stay anchored
to the same Drive folder + Notion page. All skills should treat `{Client}/delivery-state.json`
as the ledger of record: **read it first, reuse present IDs, write back new ones.**

### Launch skill (confirm name — likely `sayer-project-kickoff` or a dedicated launch skill)
- **Owns** creation of the Drive folder (+ `Deliverables`/`Working Files`/`Meeting Notes`),
  Slack channel, and Linear project.
- Before creating each, read `delivery-state.json`; if the ID is already present, reuse it.
- After creating each, **write the ID into `delivery-state.json`** (`launch.*`) and append a
  `history` entry. Also fill the STATE.md "Launch Artifacts" table.
- Confirm it does not create a *second* Notion page — reuse `launch.notionPageId` from intake.

### `/project-plan`
- Read `delivery-state.json` first. If `launch.linear.projectId` is present, **reuse** it —
  do not create a new Linear project; add issues under it.
- Mirror the launch IDs it depends on into `plan.json` (or reference the ledger), but keep
  `delivery-state.json` as the source of record.
- Write new Linear issue IDs back to `artifacts.linearIssueIds`.

### `/project-sheet`
- **Root cause fix.** Create the Google Sheet with `launch.driveDeliverablesFolderId` as its
  Drive `parent`, so it lands in the existing `CRM Implementation/Deliverables/` folder — not
  locally. If that ID is missing, tell Kyle the launch step hasn't run; do not build a stray
  local/orphaned sheet.
- Record `artifacts.sheetId` + `sheetUrl`; on re-run, update that sheet in place (idempotent).
- Add the sheet link to the existing Notion page (`launch.notionPageId`).

### `/meeting-calendar`
- Store generated decks in the Drive folder (`launch.driveMeetingNotesFolderId` or
  `Deliverables/`) and record `artifacts.gammaDeckIds`.
- Reuse `artifacts.calendarEventIds` for idempotent event updates.
- Link decks/agenda on the existing Notion page and post to the existing Slack channel
  (`launch.slackChannelId`).

### `/sayer-project-status`
- Read Linear via `launch.linear.projectId`.
- Post the status update to the existing Slack channel (`launch.slackChannelId`) and append
  it to the existing Notion page (`launch.notionPageId`) — never a new page/channel.

### `/delivery-retro`
- Attach the retro doc to the existing Drive folder and update the existing Notion page.
- After feeding calibration, append a `history` entry to `delivery-state.json`.

---

## Open item for Kyle

- **Confirm the real launch-skill name** and whether Drive+Slack provisioning already lives in
  `/sayer-project-kickoff` or a separate skill. That determines which on-machine skill owns
  writing the `launch.*` Drive/Slack/Linear IDs into `delivery-state.json`.
