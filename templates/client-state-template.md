# {Client Name} — Session State

> **Status:** `Active Delivery` | `Pre-Sale` | `On Hold` | `Complete`
> **Last updated:** YYYY-MM-DD
> **One-liner:** [What this engagement is and where it stands in one sentence]

---

## Current Position

| Field | Value |
|-------|-------|
| Phase | Phase X — {name} |
| Week | Wk X of Y |
| Phase end date | YYYY-MM-DD |
| On track? | Yes / At risk / Blocked |

---

## Done Last Session

- [ item completed ]
- [ item completed ]

---

## Open Items

### Sayer Owes
- [ ] item

### Client Owes
- [ ] item (deadline: YYYY-MM-DD)

---

## Next Session Focus

1. [Primary task]
2. [Secondary task]
3. [If applicable]

---

## Key Artifacts

| File | Purpose |
|------|---------|
| `plan.json` | Source of truth for all phases and tasks |
| `delivery-state.json` | Lifecycle ledger — canonical Drive / Notion / Slack / Linear / Sheets artifact IDs (see below) |

---

## Launch Artifacts

The one-time artifacts every skill reuses. `delivery-state.json` is the machine-readable
source; this table is the human-readable mirror. **Never create a second one of these —
skills read the IDs from `delivery-state.json` and write into the existing artifact.**

| Artifact | ID / Link |
|----------|-----------|
| Drive project folder | `driveFolderId` — [link]() |
| Drive `Deliverables/` folder | `driveDeliverablesFolderId` — client-facing sheets/decks land here |
| Notion engagement page | `notionPageId` — [link]() |
| Slack channel | `#project-{slug}` — `slackChannelId` |
| Linear project | `linear.projectId` — [link]() |

---

## Key Decisions

- **[Decision topic]:** [What was decided and why]

---

## Standing Context

[Anything Claude should know at every session start — team structure,
platform quirks, relationship sensitivities, scope boundaries, etc.
Keep this lean. Full detail lives in discovery notes and plan.json.]
