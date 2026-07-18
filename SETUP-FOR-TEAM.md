# Team Setup — Sayer Scoping Toolkit

This repo is three things at once:

1. A **working repo** — you clone it and run Claude Code *from inside it*. Client
   folders, the shared `calibration/` learning data, and `templates/` all live here.
2. A **Claude Code plugin** (`project-scoping`) — bundles the scoping + contract skills
   (`/client-intake`, `/scope-project`, `/sayer-rates`, `/draft-csa-sow`) plus the
   `sayer-brand-guidelines` reference skill (applied automatically to Excel/docx
   output — no slash command needed) so they show up in Claude Code.
3. A **plugin marketplace** (`sayer-scoping`) — so you install the plugin with one
   command and update it with another.

You need **both** the clone (for data + workspace) and the plugin (for the commands).
This guide gets you from zero to producing a scope package.

> Scope of this release: **scoping + contract drafting** — `client-intake`,
> `scope-project`, `sayer-rates`, and `draft-csa-sow` (CSA/SOW drafting with shared
> Contracts-store logging — see "Contracts store" below). The post-signing delivery
> skills (Linear project setup, Google Sheets, calendars, retros) are **not** bundled
> yet; they carry credentials that aren't wired for the team.

---

## Prerequisites

- **macOS or Windows** with **Claude Code** installed.
- **Python 3.9+** (`python3 --version`). Scripts target 3.9 for compatibility.
- **1Password** — the Sayer account, desktop app, and CLI. The shared Fireflies and
  HubSpot API keys live in the Sayer `Shared` vault; **you do not need your own API
  keys.** Setup in step 2 below.
- **MCP connectors** — the skills use these **MCP connectors** under your own account,
  connected in Claude Code (`/mcp`): HubSpot / Fireflies / Gmail / Notion (for
  `/client-intake`), and **Google Drive + Notion** (for `/draft-csa-sow` — it fetches the
  canonical CSA/SOW master from Drive and logs each contract to the Notion Contracts DB).
  (The 1Password keys cover the Python scripts like `intake.py`.)
- GitHub access to `Sayer-Strategy-Group/project-scoping-tool` (your org membership).
- *Optional:* the **Rethink Sans** Google Font for decks — Excel/docx output falls
  back to Calibri automatically, so this is never blocking.

> **Windows users:** Skip the macOS Keychain step in Step 2. The credential
> resolver catches the missing `security` command silently and falls through to
> env var → `.env` → 1Password automatically. Just create a `.env` file in the
> repo root using `.env.example` as a template, or use the 1Password CLI path
> (works cross-platform). Everything else in this guide applies as-is.

---

## One-time setup

### 1. Clone the repo and install Python deps

```bash
git clone https://github.com/Sayer-Strategy-Group/project-scoping-tool.git
cd project-scoping-tool
pip3 install -r requirements.txt
```

### 2. Connect to the shared credentials (1Password)

The scripts resolve secrets in this order: **Keychain → env → `.env` → 1Password**.
The team default is 1Password — the shared keys are already in the Sayer `Shared`
vault, so this is sign-in, not key management:

```bash
brew install 1password-cli
```

Then in the **1Password desktop app**: sign in to the Sayer account →
Settings → Developer → **Integrate with 1Password CLI**. Verify:

```bash
op read "op://Shared/FIREFLIES_API_KEY/credential"
op read "op://Shared/HUBSPOT_API_KEY/credential"
```

Both should print a token. If you get a vault/item error, ask Kyle for access to
the `Shared` vault. (A different vault name can be set via `SAYER_OP_VAULT`.)

**Obsidian vault (optional).** If you maintain a SayerBrain Obsidian vault,
set `SAYER_VAULT_PATH` to mirror client intake folders there automatically.
If not set, intake skips the mirror silently — no action needed:

```bash
export SAYER_VAULT_PATH="$HOME/Obsidian/SayerBrain"   # add to ~/.zshrc to persist
```

**Personal overrides (optional).** Anything found in Keychain, env vars, or a
repo-local `.env` (gitignored — never commit it) wins over 1Password:

```bash
# Keychain (point the lookup at your own account):
export SAYER_KEYCHAIN_ACCOUNT="$(whoami)"          # add to ~/.zshrc to persist
security add-generic-password -a "$SAYER_KEYCHAIN_ACCOUNT" -s HUBSPOT_API_KEY -w 'pat-na1-...'

# Or env vars:
export HUBSPOT_API_KEY='pat-na1-...'
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

You'll now have `/client-intake`, `/scope-project`, `/sayer-rates`, `/draft-csa-sow`,
and the `sayer-brand-guidelines` reference skill (read automatically before
client-facing output — Excel needs no logo; deck/doc covers fetch logos from the Sayer
shared Google Drive when needed).

---

## Daily use

**Launch Claude Code from inside your `project-scoping-tool` clone for the scoping
skills.** `/client-intake` and `/scope-project` are repo-bound — they read `calibration/`
and write client folders relative to the working directory, and their preflight will tell
you to `cd` in if you're somewhere else. **Exception: `/draft-csa-sow` does NOT need a
clone** — it drafts from the canonical Google Doc master and writes to Drive + the Notion
Contracts store, so it runs in **CoWork** (or any directory) with just the Google Drive +
Notion connectors connected.

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

> **Team visibility:** `/client-intake` also creates a page in the shared
> **Client Engagements** Notion database (under Sayer Home) with status, intake date,
> and a discovery digest — connect the Notion connector in `/mcp` to enable it. If
> Notion isn't connected, intake still works; it just skips the mirror with a notice.
> The repo client folder is always the source of truth.
>
> **No Obsidian vault?** Fine — the Obsidian mirror is an optional operator extra;
> it skips silently when no vault exists.

---

## Contracts store (CSA / SOW)

`/draft-csa-sow [Client]` runs a guided interview, drafts the CSA + SOW from the
canonical master, produces branded `.docx` files, and **logs each contract to the shared
Contracts registry** so the team sees every agreement in one place.

- **Registry:** the **Contracts** Notion database under *Sayer Home* — one row per
  CSA/SOW, linked to the client's Client Engagements page. Tracks Type, Status
  (Draft → In Approval → Sent → Signed → Superseded), value, signed date, the Drive doc
  link, and the HubSpot deal.
- **Documents:** the branded `.docx` files live in the confidential **Contracts** Google
  Drive folder (Partners-drive; do not post these links to Slack project channels).
- **Access is restricted** to the contracts team — **Kyle, Greg, Cameron, Billy, Weston,
  Aisha**. If you can't see the Contracts DB or the Drive folder, ask Kyle for access.
- **Approval:** every SOW goes to **Billy Leigh & Greg Dyer** before it's sent to the
  client — the skill flags this, and the registry `Status` reflects it.
- **Requires** the Google Drive and Notion connectors (`/mcp`).

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
| `intake.py --test-only` → `FAIL` | Token missing/expired or wrong scopes. Verify the `op read` commands from step 2 work; if you used a personal override, re-add it. |
| `Secret 'X' not found` | No credential resolved anywhere. Most common: `op` CLI not installed, CLI integration not enabled in the 1Password app, or no access to the `Shared` vault — re-run step 2. |
| `op read` → "isn't a vault" / "no item" | You don't have the Sayer `Shared` vault yet — ask Kyle to grant access in 1Password. |
| `/scope-project` not found after install | Run `/plugin marketplace update sayer-scoping` then `/plugin install project-scoping@sayer-scoping` again. |
| Plugin out of date | `/plugin marketplace update sayer-scoping` then `/plugin update project-scoping`. |
| "Notion mirror skipped" notice | Notion connector not connected in `/mcp` — intake still completed; connect Notion to enable the team-visible index. |
| `[vault] skipped` notice | Expected if you have no Obsidian vault — not an error. |
