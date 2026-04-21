# Project Scoping Tool — Active Projects

> **Last updated:** 2026-04-21
> Claude: read this file at session start to orient quickly. Each active project links to its own `STATE.md`.
>
> Note: when working in a specific client, read `{Client}/STATE.md` for full context.

---

## Active Deliveries

| Client | Status | Current Phase | Next Action | STATE.md |
|--------|--------|---------------|-------------|----------|
| **Milestone Group** | Active — Wk 2 | Phase 1: Contacts & Activity | Pipeline spec locked (Robert delivered); building properties. Friday contacts upload. M365 creds chase email pending send. | [STATE.md](MilestoneSoW/STATE.md) |
| **Trialta** | Active — Wk 1–2 | Phase 1: CRM Foundation | Check phase progress, schedule discovery call | [STATE.md](Trialta/STATE.md) |

## Pre-Sale Pipeline

| Client | Status | Next Action |
|--------|--------|-------------|
| **HelloSpoke** | $42k deal at Decision Maker Bought-In, close target 2026-04-30 | Thursday 2026-04-23 @ 3pm Central ops discovery walkthrough (Christina, Haley, Jeremy). See [HelloSpoke/STATE.md](HelloSpoke/STATE.md). |
| **Arkview Capital** | Scoped, pending SOW delivery | Deliver SOW |
| **Strive Global** | V3 proposal complete | Schedule review call |
| **Top Down Auto** | Scoped, pending ERP follow-up call | Clarify ERP questions |
| **American Bedding** | CPQ discussion — two-phase proposal sent | SB asked Apr 17 for HubSpot↔NetSuite CPQ client references; reference-follow-up drafted Apr 21 (awaiting internal clearance on contact share). |

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
