# Project Scoping & Delivery Tool

Sayer's pre-sale **scoping** toolkit (and post-sale delivery workflow) for systems
implementation engagements — primarily HubSpot CRM, plus ERP, marketing automation,
VoIP, data migrations, and integrations. It produces workstream-based hour estimates,
risk registers, approach comparisons, and formatted Excel scope packages, and learns
from past projects through a calibration loop.

This repo is also a **Claude Code plugin + marketplace**, so the scoping skills can be
installed by any teammate with one command.

---

## New here? Start with the setup runbook

**Teammates: read [`SETUP-FOR-TEAM.md`](SETUP-FOR-TEAM.md).** It walks you from clone
to first scope package in ~10 minutes (clone → deps → your own HubSpot/Fireflies creds
→ install the plugin).

Quick version once you've cloned and installed deps:

```bash
# in Claude Code, launched from inside this repo
/plugin marketplace add Sayer-Strategy-Group/project-scoping-tool
/plugin install project-scoping@sayer-scoping
```

You'll get `/client-intake`, `/scope-project`, and `/sayer-rates`.

> **Always launch Claude Code from inside your clone of this repo.** The skills read
> shared calibration data and templates relative to the repo, and write client folders
> into it. They self-check the working directory and will tell you to `cd` in.

---

## What's in here

| Path | What it is |
|------|------------|
| `skills/` | The plugin's scoping skills (`scope-project`, `client-intake`, `sayer-rates`). Auto-discovered when the plugin is installed. |
| `.claude-plugin/` | Plugin + marketplace manifests (`plugin.json`, `marketplace.json`). |
| `calibration/` | **Shared learning loop** — estimate baselines and adjustments from past projects. Single source of truth; read before scoping, append after closing one. |
| `templates/` | Scope summary, decisions log, estimate, discovery prep, delivery, and retro templates. |
| `scripts/` | Python automation — `intake.py` (HubSpot/Fireflies → client folder), credential loader, Excel/proposal helpers. See [`scripts/README.md`](scripts/README.md). |
| `wiki/` | Synthesized, cross-linked knowledge base — read `wiki/clients/{slug}.md` before cold-reading a client's raw folder. |
| `{Client Name}/` | Per-engagement folders: discovery materials, scope summary, decisions, `STATE.md`. |
| `CLAUDE.md` | The full operating guide for working in this repo (session protocol, scoping workflow, calibration, delivery skills). |

---

## Scope of the plugin (current)

**Pre-sale scoping only** — `client-intake`, `scope-project`, `sayer-rates`. The
delivery skills (Linear project setup, Google Sheets, calendar/decks, retros) are part
of the repo's workflow but are **not yet bundled in the plugin** — they carry
credentials that aren't wired for team distribution. Adding them is a future phase.

## Credentials

Scripts resolve secrets in order **macOS Keychain → env var → repo-local `.env`**. The
Keychain account is overridable per machine via `SAYER_KEYCHAIN_ACCOUNT` (default
`harbuckconsulting`). The `/client-intake` skill instead uses the HubSpot / Fireflies /
Gmail **MCP connectors** under each user's own account. Full details in
[`SETUP-FOR-TEAM.md`](SETUP-FOR-TEAM.md) and [`scripts/README.md`](scripts/README.md).

## Requirements

- macOS, Python 3.9+, Claude Code.
- `pip3 install -r requirements.txt`.
