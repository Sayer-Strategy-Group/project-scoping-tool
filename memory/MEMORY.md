# Project Scoping Tool — Durable Knowledge

> Project-scoped knowledge index. Detail lives in linked files.
> For session state, see `PROJECT-STATE.md` at repo root.
> For per-client state, see `{Client}/STATE.md`.

- [Repo restructure plan](../PROJECT-STATE.md#repo-health) — Deferred migration to clients/{kebab}/ with phase subdirs; simple renames done 2026-04-22
- [Git rename commits skip gitignored files](rename-gitignore-trap.md) — When upstream renames a directory, gitignored files (delivery-state.json, .DS_Store, __pycache__) don't move. Manual migration required per client rename.
- [ClickUp ↔ HubSpot native integration — consulting-scope findings](../HelloSpoke/HelloSpoke_clickup_workstream.md) — Native integration is shallow (2.0/5 marketplace rating, task-only 2-way sync, no HubSpot custom object support, no HubSpot→ClickUp custom field mapping). Middleware (Make / n8n) required for HubSpot-form-as-source-of-truth architectures. Three-tier scope framing: 18-24 / 28-36 / 40-48 hrs. First Sayer ClickUp integration scope — add to calibration.md after delivery.
- [Sayer brand guide specs for SOW Excel docs](../HelloSpoke/Hello Spoke SOW.xlsx) — Grey 700 `#2E2E2E` column headers + Sayer Yellow `#FEC700` section banners + Rethink Sans font applied across the HelloSpoke SOW workbook. Original xlsx used scoping-skill.md default (`#1F4E79` + Arial) which is NOT brand — future client SOWs should apply brand from creation.
