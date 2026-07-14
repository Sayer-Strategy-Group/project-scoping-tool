---
layer: Org
owner: team
created_at: 2026-06-30
access_level: internal
name: client-intake
description: >
  Create a new client folder and pull discovery materials from Fireflies,
  Gmail, and HubSpot. Use when onboarding a new client for scoping.
  Trigger: "intake [ClientName]", "new client [ClientName]", "set up [ClientName]"
argument-hint: "[ClientName]"
allowed-tools: Read, Write, Bash, Glob, Grep, mcp__claude_ai_Fireflies__*, mcp__claude_ai_Gmail__*, mcp__claude_ai_HubSpot__*, mcp__claude_ai_Notion__*
---

# Client Intake Skill

Pull discovery materials from Fireflies, Gmail, and HubSpot into a standardized client folder. This is the first step before running `/scope-project`.

## Preflight

- **Work from the project-scoping-tool repo.** This skill writes a client folder
  into the repo. Confirm the cwd is a clone of it — `calibration/` and `templates/`
  should exist in the current directory. If not, tell the user to `cd` into their
  `project-scoping-tool` clone first.
- **Connectors required.** This skill pulls live data through the Fireflies, Gmail,
  and HubSpot MCP connectors, and mirrors to Notion through the Notion connector.
  Each user authenticates their own connectors in Claude Code — there are no
  shared API tokens here. If a connector isn't connected, report it and continue
  with the others (see Error Handling).

## Input Handling

**Parse `$ARGUMENTS` as follows:**

1. **Client name provided** — Use it directly (e.g., "Acme Corp")
2. **Empty / no arguments** — Ask for the client name. ONE question at a time.

**Then ask for:**
- **Email domain** (e.g., `acme.com`) — required for Gmail search. If obvious from the client name, suggest it and confirm.

**Confirm before proceeding:**
> "Setting up {ClientName} — I'll search Fireflies by company name, Gmail by @{domain}, and HubSpot by company name. Ready?"

Wait for confirmation before creating anything.

## Step 1: Create Folder Structure

**Primary (project repo):** `{ClientName}/` at the repo root (the current working
directory). Use the original client-name casing for the folder (e.g., `Acme Corp`).

**Optional operator vault mirror (Obsidian):** if — and only if — the user
maintains a SayerBrain vault, also mirror to `$SAYER_VAULT_PATH/03-accounts/{client-name}`
(default `~/Obsidian/SayerBrain/03-accounts/`, kebab-case, e.g. `acme`).
**Skip the mirror silently if that path does not exist** — most teammates have no
vault, and the repo folder is the source of truth. The team-visible mirror is
Notion (Step 5), not Obsidian.

Create this structure in the repo folder (and the vault mirror if present):
```
{client-name}/
├── discovery/
├── emails/
├── hubspot/
└── {client-name}_decisions.md
```

For the decisions file, use this content:
```markdown
# {ClientName} -- Scoping Decisions
```

Replace `{ClientName}` with the actual client name.

## Step 2: Pull Fireflies Data

1. Use `fireflies_get_transcripts` with `keyword: "{ClientName}", scope: "title"` to find meetings matching the company name. **Do NOT use `fireflies_search` — it times out reliably.**
2. For each matching meeting:
   a. Use `fireflies_get_transcript` to pull the full transcript
   b. Use `fireflies_get_summary` to pull the AI summary
3. Write one markdown file per meeting into `discovery/` into the repo client folder (and the Obsidian vault mirror if one exists)

**Filename:** `{YYYY-MM-DD}-{slugified-meeting-title}.md`
- Date from the meeting date
- Title lowercased, spaces replaced with hyphens, special characters removed

**File format:**
```markdown
# {ClientName} — {Meeting Title} ({YYYY-MM-DD})

## Summary
{Fireflies AI summary}

## Participants
{attendee list — name and email if available}

## Transcript
{full transcript text}
```

**If no meetings found:** Report it in the summary. Do not fail — continue to the next step.

## Step 3: Pull Gmail Data

1. Use `search_threads` with query `from:@{domain}` to find threads — **cap at 20 most recent**
2. For each thread, use `get_thread` to pull the full content
3. Write one markdown file per thread into `emails/` into the repo client folder (and the Obsidian vault mirror if one exists)

**Filename:** `{YYYY-MM-DD}-{slugified-subject}.md`
- Date from the first message in the thread
- Subject lowercased, spaces replaced with hyphens, special characters removed
- Truncate filename to 80 characters max

**File format:**
```markdown
# {ClientName} — {Subject} ({YYYY-MM-DD})

## Thread Participants
{to/from/cc from the thread}

## Messages
### Message 1 — {Sender Name} ({YYYY-MM-DD})
{message body}

### Message 2 — {Sender Name} ({YYYY-MM-DD})
{reply body}
```

**If no threads found:** Report it in the summary. Do not fail — continue to the next step.

## Step 4: Pull HubSpot Data

1. Authenticate via `mcp__claude_ai_HubSpot__authenticate` if not already authenticated
2. Search for the company by name
3. Pull the company record and all associated contacts
4. Write one file into `hubspot/` into the repo client folder (and the Obsidian vault mirror if one exists)

**Filename:** `company-profile.md`

**File format:**
```markdown
# {ClientName} — HubSpot Profile

## Company
| Property | Value |
|----------|-------|
| Name | {company name} |
| Domain | {domain} |
| Industry | {industry} |
| Lifecycle Stage | {lifecycle stage} |
| Owner | {hubspot owner} |
| Create Date | {create date} |

## Contacts

### {Contact Full Name}
| Property | Value |
|----------|-------|
| Title | {job title} |
| Email | {email} |
| Phone | {phone} |
| Lifecycle Stage | {lifecycle stage} |
```

Repeat the contact section for each associated contact.

**If HubSpot auth fails or company not found:** Report it in the summary. Do not fail — the folder and other data are still valuable.

## Step 5: Mirror to Notion (team-visible index)

Create the client's page in the shared **Client Engagements** database in the
Sayer Notion workspace (parent: Sayer Home).

- **Database ID:** `1ee8290de7bc415a8afd62cc22b43fa7`
- **Data source:** `collection://365887c7-a250-40fb-8421-d97a2ecab24b`

1. **Check the ledger, then the database, before creating.** If
   `{ClientName}/delivery-state.json` exists and has `launch.notionPageId`, reuse
   that page — update it, never create a second one. Otherwise search the data
   source for the client name; if a page already exists, update it instead of
   creating a duplicate. Only create a new page when neither the ledger nor the
   database has one.
2. Create (or update) the page with properties:
   - **Client Name:** `{ClientName}`
   - **Status:** `Intake`
   - **Intake Date:** today
   - **HubSpot URL:** the company record URL (if HubSpot pull succeeded)
   - **Owner:** the current user
3. Add two sub-pages under the client page:
   - **Discovery Notes** — a bullet list of the meetings and email threads pulled
     (titles + dates + one-line takeaways). Do NOT paste full transcripts into
     Notion — the repo folder holds the raw material.
   - **Scope Summary** — stub with "Pending — populated after /scope-project."
4. **Status lifecycle** (updated by later skills/sessions, not re-set by intake):
   `Intake → Scoping → Proposal Sent → Signed / Lost`.

**If the Notion connector is not connected or the database is unreachable:**
skip with an explicit notice in the summary ("Notion mirror skipped — connector
not available"). The local repo folder remains the source of truth; never fail
the intake over the mirror.

## Step 6: Seed the lifecycle ledger

Intake is the front of the client lifecycle, so it opens the continuity ledger
that every downstream skill (`/scope-project`, `/project-plan`, `/project-sheet`,
`/meeting-calendar`, `/sayer-project-status`, `/delivery-retro`, and the launch
skill) reads to find already-created artifacts. This is what prevents parallel
Notion pages, duplicate Drive folders, and orphaned local sheets later.

Write `{ClientName}/delivery-state.json` (schema:
`templates/delivery-state-schema.json`). If the file already exists, **merge**
into it — never clobber IDs a later skill already recorded.

- Set `client.name` and `client.slug`.
- Set `launch.notionPageId` and `launch.notionDatabaseId` to the page and database
  from Step 5 (leave `null` if the Notion mirror was skipped).
- Leave the Drive / Slack / Linear launch fields `null` — they are provisioned by
  the launch skill post-signing, which fills them into this same file.
- Append a `history` entry: `{ date, skill: "client-intake", action: "created/reused Notion page" }`.

This file is gitignored (it holds external artifact IDs), so it stays local to the
client folder. Skip this step silently only if the folder could not be created.

## Step 7: Summary Report

Print a summary of everything collected:

```
{ClientName} intake complete:
- {N} Fireflies recordings pulled → discovery/
- {N} Gmail threads pulled → emails/
- 1 company + {N} contacts pulled → hubspot/
- decisions.md template created
- Notion: Client Engagements page created (Status: Intake) — or "skipped, connector not available"
- delivery-state.json seeded (Notion page ID recorded for downstream skills)

Written to:
  Repo:     {ClientName}/   (in the project-scoping-tool repo)
  Ledger:   {ClientName}/delivery-state.json  (lifecycle artifact IDs — reused by all later skills)
  Notion:   Client Engagements → {ClientName}  (team-visible index)
  Obsidian: {vault path}    (only if a SayerBrain vault is present; omit otherwise)

Ready to scope when you are. Run /scope-project with the discovery materials when you want to start.
```

If any source returned 0 results, note it explicitly:
```
- 0 Fireflies recordings found (searched for "{search term}")
```

## Error Handling

- **Do not stop on partial failures.** If one source fails (auth error, no results, API timeout), continue with the others and report what happened in the summary.
- **Never silently skip a source.** Always report 0 results or errors explicitly.
- **Do not commit if the folder is empty** (all 3 sources returned nothing). Ask Kyle to verify the client name and domain.
