# Git Rename Commits Skip Gitignored Files

## The Trap
When upstream pushes a commit that renames a directory (e.g., `MilestoneSoW` → `Milestone Group`), git's rename handling only moves *tracked* files. Anything gitignored sits on disk in the old path and becomes orphaned when the new path is used going forward.

## Why It Matters Here
This repo has several patterns that are gitignored per client folder:
- `**/delivery-state.json` — holds Linear project IDs, Google Sheet IDs, calendar event IDs for idempotency
- `__pycache__/`, `*.pyc` — Python bytecode for generated scripts
- `.DS_Store` — macOS noise
- `Trialta/` — entire client folder (client data)

If any client folder is renamed in the future (common during scope/stage transitions), the `delivery-state.json` for that engagement will NOT move. Downstream delivery skills (`/project-status`, `/meeting-calendar`, `/project-sheet`) looking for it at the new path will either error or duplicate external artifacts.

## The Fix
Post-pull, when a rename is detected:
1. Check the old path for orphaned gitignored files: `ls <old-path>`
2. Move `delivery-state.json` (and any other real state) to the new path: `mv "<old>/delivery-state.json" "<new>/delivery-state.json"`
3. Delete pure crud: `.DS_Store`, `__pycache__/`
4. `rmdir <old-path>`

## Incident Reference
2026-04-23 — Pulled 10 commits including `refactor: rename MilestoneSoW to Milestone Group`. Manual migration preserved Milestone Group's delivery-state.json which held authoritative Linear + Sheets IDs.
