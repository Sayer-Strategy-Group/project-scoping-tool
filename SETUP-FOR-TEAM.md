# Team Setup — Sayer Scoping Toolkit

This repo is three things at once:

1. A **working repo** — you clone it and run Claude Code *from inside it*. Client
   folders, the shared `calibration/` learning data, and `templates/` all live here.
2. A **Claude Code plugin** (`project-scoping`) — bundles the scoping skills
   (`/client-intake`, `/scope-project`, `/sayer-rates`) so they show up as slash
   commands in Claude Code.
3. A **plugin marketplace** (`sayer-scoping`) — so you install the plugin with one
   command and update it with another.

You need **both** the clone (for data + workspace) and the plugin (for the commands).
This guide gets you from zero to producing a scope package.

> Scope of this release: **pre-sale scoping only** — `client-intake`, `scope-project`,
> `sayer-rates`. The delivery skills (Linear project setup, Google Sheets, calendars,
> retros) are **not** bundled yet; they carry credentials that aren't wired for the team.

---

## Prerequisites

- **macOS** with **Claude Code** installed.
- **Python 3.9+** (`python3 --version`). Scripts target 3.9 for compatibility.
- Your **own Sayer credentials**:
  - **HubSpot** Private App token with `crm.objects.{owners,companies,contacts,deals}.read` scopes.
  - **Fireflies** API key.
  - These are used by `scripts/intake.py`. The `/client-intake` *skill* uses the
    HubSpot/Fireflies/Gmail **MCP connectors** instead — connect those in Claude Code
    (`/mcp`) under your own account.
- GitHub access to `Sayer-Strategy-Group/project-scoping-tool` (your org membership).

---

## One-time setup

### 1. Clone the repo and install Python deps

```bash
git clone https://github.com/Sayer-Strategy-Group/project-scoping-tool.git
cd project-scoping-tool
pip3 install -r requirements.txt
```

### 2. Provide your credentials

Pick **one** of three ways (the scripts try them in this order: Keychain → env → `.env`):

**Option A — macOS Keychain (recommended).** Point the lookup at your own account:

```bash
export SAYER_KEYCHAIN_ACCOUNT="$(whoami)"          # add this to your ~/.zshrc to persist
security add-generic-password -a "$SAYER_KEYCHAIN_ACCOUNT" -s HUBSPOT_API_KEY   -w 'pat-na1-...'
security add-generic-password -a "$SAYER_KEYCHAIN_ACCOUNT" -s FIREFLIES_API_KEY -w '...'
```

**Option B — environment variables:**

```bash
export HUBSPOT_API_KEY='pat-na1-...'
export FIREFLIES_API_KEY='...'
```

**Option C — a repo-local `.env`** (already gitignored — never commit it):

```
HUBSPOT_API_KEY=pat-na1-...
FIREFLIES_API_KEY=...
```

### 3. Verify credentials work (no writes, no fetch)

```bash
python3 scripts/intake.py --test-only
```

Expect `OK` for both HubSpot and Fireflies. If you see `FAIL`, the token or scopes
are wrong — fix before continuing.

### 4. Install the plugin

In Claude Code:

```
/plugin marketplace add Sayer-Strategy-Group/project-scoping-tool
/plugin install project-scoping@sayer-scoping
```

You'll now have `/client-intake`, `/scope-project`, and `/sayer-rates`.

---

## Daily use

**Always launch Claude Code from inside your `project-scoping-tool` clone.** The
skills are repo-bound — they read `calibration/` and write client folders relative
to the working directory. Each skill runs a preflight check and will tell you to
`cd` in if you're somewhere else.

```bash
cd ~/path/to/project-scoping-tool
git pull            # get the latest shared calibration + any new clients
claude
```

Then, typically:

1. `/client-intake AcmeCorp` — pulls Fireflies/Gmail/HubSpot discovery into `AcmeCorp/`.
2. `/scope-project AcmeCorp/discovery/...` — generates the workstream estimate, risk
   register, and the `AcmeCorp_Scoping_Estimate.xlsx` package.
3. `/sayer-rates` is consulted automatically for the rate card; invoke it directly to
   review tiers or the pricing-negotiation protocol.

> **No Obsidian vault?** Fine. `client-intake` and `intake.py` mirror to a SayerBrain
> vault *only if one exists*; otherwise they skip the mirror with a notice and the repo
> folder is the source of truth.

---

## Keeping things in sync

- **Plugin updates** (new/changed skills): `/plugin update project-scoping`.
- **Repo updates** (new calibration, templates, clients): `git pull` in your clone.
- Calibration is a **shared learning loop** — there is exactly one `calibration/`,
  here in the repo. When you close a scope, add the baseline here and push, so the
  whole team's estimates improve. Don't fork or copy it.

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Skill says "NOT in repo root" | `cd` into your `project-scoping-tool` clone before running it. |
| `intake.py --test-only` → `FAIL` | Token missing/expired or wrong scopes. Re-add per step 2; HubSpot needs the four `crm.objects.*.read` scopes. |
| `Secret 'X' not found` | No credential resolved. Check `SAYER_KEYCHAIN_ACCOUNT`, your env vars, or `.env`. |
| `/scope-project` not found after install | Run `/plugin marketplace update` then `/plugin install project-scoping@sayer-scoping` again. |
| `[vault] skipped` notice | Expected if you have no Obsidian vault — not an error. |
