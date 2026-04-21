# Project Scoping Tool — Active Projects

> **Last updated:** 2026-04-21
> Claude: read this file at session start to orient quickly. Each active project links to its own `STATE.md`.

---

## Active Deliveries

| Client | Status | Current Phase | Next Action | STATE.md |
|--------|--------|---------------|-------------|----------|
| **Milestone Group** | Active — Wk 2 | Phase 1: Contacts & Activity | Friday Apr 24 contacts upload; chase M365 creds + Robert's pipeline spreadsheet in today's call | [STATE.md](MilestoneSoW/STATE.md) |
| **Trialta** | Active — Wk 1–2 | Phase 1: CRM Foundation | Check phase progress, schedule discovery call | [STATE.md](Trialta/STATE.md) |

## Pre-Sale Pipeline

| Client | Status | Next Action |
|--------|--------|-------------|
| **Arkview Capital** | Scoped, pending SOW delivery | Deliver SOW |
| **Strive Global** | V3 proposal complete | Schedule review call |
| **Top Down Auto** | Scoped, pending ERP follow-up call | Clarify ERP questions |
| **American Bedding** | CPQ discussion — two-phase proposal sent | Contract review, follow-up answered Apr 10 |

---

## Repo Health

- [ ] **Repo restructure planned** — migrate to `clients/{kebab}/01-discovery → 05-delivery/phase/workstream` structure. Start with Trialta as dry run. See `project_repo-restructure.md` in memory.
- [ ] **Trialta plan.json** — pricing is $0 / TBD, needs update with signed fee
- [ ] **3 files need renaming** in MilestoneSoW (spaces/underscores → kebab-case) — defer to restructure session
- [x] ~~Linear not yet created for Milestone Group~~ — **Done 2026-04-20.** Project live: https://linear.app/gosayer/project/milestone-group-hubspot-crm-implementation-2c60f3bede3a (125 sub-issues, 9 milestones, 42 blockedBy edges)

---

## Conventions (quick ref)

- Client folders: `{Client Name}/` (pre-restructure) → `clients/{kebab-name}/` (post-restructure)
- Delivery source of truth: `plan.json` in each client folder
- Session state: `STATE.md` in each client folder (this system)
- Calibration: `calibration/calibration.md` (read before every scoping session)
- Skills: `~/.claude/skills/` — invoke via `/project-plan`, `/project-sheet`, etc.
