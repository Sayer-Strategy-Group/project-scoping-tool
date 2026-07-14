---
layer: Org
owner: team
created_at: 2026-06-30
access_level: internal
name: scope-project
description: >
  Generate professional implementation scoping packages from discovery notes.
  Use when the user shares discovery call notes, client requirements, or asks
  to scope a systems implementation. Covers CRM, ERP, marketing automation,
  phone/VoIP, data migrations, integrations, and multi-system projects.
  Outputs workstream-based hour estimates, risk registers, approach comparisons,
  formatted Excel deliverables, and client-ready summaries.
argument-hint: "[path-to-discovery-notes or paste notes inline]"
disable-model-invocation: true
allowed-tools: Read, Write, Bash, Grep, Glob
---

# Systems Implementation Scoping Skill

Generate complete scoping packages from discovery notes for systems implementation projects.

## Preflight: work from the project-scoping-tool repo

This skill writes deliverables into a client folder and reads shared calibration
data, both of which live in the **project-scoping-tool repo**. Before doing any
work, confirm the current working directory is a clone of that repo — check that
`calibration/` and `templates/` exist in the cwd:

```bash
test -d calibration && test -d templates && echo "repo OK" || echo "NOT in repo root"
```

If it reports `NOT in repo root`, tell the user to `cd` into their
`project-scoping-tool` clone before continuing (the scoping workflow is
repo-bound — client folders, calibration, and templates all live there).

`${CLAUDE_SKILL_DIR}` below resolves to this skill's own directory (inside the
installed plugin), so reference files are found regardless of the cwd.

## Input Handling

**Parse `$ARGUMENTS` as follows:**

1. **File path provided** — Read the file and use its contents as discovery notes
2. **Inline text provided** — Use the text directly as discovery notes
3. **Empty / no arguments** — Ask the user to provide discovery notes (paste inline or give a file path). Ask ONE question at a time.

## Workflow

### Step 1: Parse Discovery Notes

Extract structured information from the raw notes:

1. **Client Profile** — Company name, industry, size, current systems, stakeholders, internal IT resources
2. **Current State / Pain Points** — What's broken or manual, data fragmentation, process gaps, compliance requirements
3. **Desired Future State** — Target systems, key outcomes, timeline expectations, budget signals
4. **Complexity Indicators** — Flag these explicitly as they drive hour estimates:
   - Number of users
   - Number of data sources to migrate/integrate
   - Custom object or field requirements
   - Data quality issues (duplicates, incomplete records)
   - Multi-entity or multi-brand structures
   - ERP/accounting involvement (always adds complexity)
   - Vendor lock-in or export fees
   - Stakeholder alignment concerns
5. **Unknowns and Blockers** — Missing info, third-party dependencies, unresolved decisions, cost blockers

**If discovery notes are sparse:** Ask the user ONE question at a time to fill critical gaps. Prioritize: system count, user count, data sources, and integration requirements.

### Step 2: Define Workstreams

Break the project into workstreams based on systems involved. Each workstream gets its own hour estimate.

Reference: `${CLAUDE_SKILL_DIR}/references/workstream-catalog.md` for the full catalog of workstreams by system category.

Apply relevant workstreams from the catalog. Every project also gets the cross-cutting workstreams (PM, UAT, documentation, go-live) sized appropriately.

### Step 3: Estimate Hours

For each workstream, provide **min / max / median** hour estimates.

Reference: `${CLAUDE_SKILL_DIR}/references/hour-ranges.md` for base hour tables, complexity multipliers, and rate modeling instructions.

Always calculate:
- Total min / max / median hours
- Rate modeling (use the `sayer-rates` skill for the current rate card and blended-rate model; default to the Associate rate of $150/hr if no tier mix is specified; ask if unknown)
- Total cost range: min x rate through max x rate

### Step 4: Build Risk Register

Generate a risk register for every project.

Reference: `${CLAUDE_SKILL_DIR}/references/risk-register-template.md` for field definitions, standard risks, and severity definitions.

Flag high-severity risks prominently. If any risk is HIGH severity AND HIGH likelihood, recommend a mitigation plan or phased approach to isolate it.

### Step 5: Generate Approach Comparison (When Applicable)

If the project involves multiple systems or has significant dependency risks, generate a comparison:

- **Approach A: Concurrent** — All systems at once. Faster timeline, single cutover. Higher risk, more parallel resources needed.
- **Approach B: Phased** — System by system. Lower risk per phase, learnings carry forward. Longer total timeline, temporary manual bridges.

Include a comparison matrix (hours, cost, timeline, risk level, dependencies per approach) and a recommendation tied to the client's specific risk factors.

### Step 6: Emit the Structured Scope Record (`scope.json`)

Before generating any deliverable, write the full estimate as a structured record:
`{ClientFolder}/scope.json`, conforming to `templates/scoping-schema.json` (repo root).
This record is the **single source of truth** — the Excel workbook, the client summary,
and (after the deal closes) the pricing-calibration store all derive from it. Do not
re-derive the same numbers in three places; produce them once, here.

- Every workstream carries `id` (PREFIX-NN), `category` (controlled vocabulary — use the
  schema enum: crm / erp / marketing / voip / data-bi / integration / migration / pm /
  uat / training / documentation / go-live / other — **not** free text; it is the
  calibration join key), `hours {min,max,median}`, `rate`, `cost {min,max,median}`, and `tasks[]`.
- Invariants: `cost = hours × rate`; each workstream's task hours sum to its median
  (this is what the Task Breakdown integrity check enforces in the workbook).
- Capture `client.hubspotUrl` from intake when available — it is the key used to stamp
  won/lost + final amount onto this record later (pricing calibration).
- **Pick the estimate mode** (`engagement.estimateMode`):
  - `ranges` (default) — min/max/median per workstream. The pre-sale discovery scoping
    standard. Requires `workstreams[]` + `budgetSummary`.
  - `committed` — single committed hours/amount per phase, with a tiered staff blend
    (`staffMix`), a Technology & Admin Fee (`techFeePct`), and a `committedSummary`
    (consulting subtotal → tech fee → grand total). The T&M-SOW form.
    Requires `phases[]` (with `committedHours`/`committedAmount`) + `committedSummary`.
    Use a degenerate range (`min=max=median`) for `engagement.totalHours`.
- Validate before proceeding (catches schema drift early):
  ```bash
  python3 scripts/build_estimate.py {ClientFolder}/scope.json --validate-only
  ```
  Fix any reported schema errors before generating the workbook.

### Step 7: Generate Excel Deliverables

Generate the branded workbook **from `scope.json` using the shared generator** — do NOT
hand-write a per-client openpyxl script (that pattern is retired; one generator, driven by data):

```bash
python3 scripts/build_estimate.py {ClientFolder}/scope.json
```

This emits `{ClientName}_Scoping_Estimate.xlsx` with 5 sheets by default (Scoping Estimate;
Task Breakdown with formula-based integrity checks back to Sheet 1; Deliverables & Acceptance;
Risk Register; Assumptions), plus an Approach Comparison sheet when `approaches` are present.
All styling comes from `scripts/brand_styles.py` (Sayer brand) — never hard-code hex. The sheet
spec is documented in `${CLAUDE_SKILL_DIR}/references/excel-formatting.md` and the
`sayer-brand-guidelines` skill — read those to understand or modify the generator, not to
author a workbook by hand.

### Step 8: Generate Client-Ready Summary

Create a concise summary suitable for Slack, email, or SOW insertion:

```
**{Client Name} -- Implementation Scope Summary**

**Systems in Scope:** {list}
**Approach:** {Concurrent / Phased / TBD}
**Estimated Hours:** {min}-{max} hrs (median: {median})
**Estimated Investment:** ${min_cost}-${max_cost} (at ${rate}/hr)
**Estimated Timeline:** {X} weeks

**Workstream Breakdown:**
{Top-level workstream list with median hours each}

**Key Risks:**
{Top 3 risks with severity}

**Assumptions:**
{Top 3-5 critical assumptions}

**Outstanding Items (Need from Client):**
{List of open items/decisions needed}

**Recommendation:**
{1-2 sentences on recommended approach and why}
```

## Important Rules

1. **Never pad estimates.** Use honest ranges. The min/max spread IS the buffer.
2. **Always flag unknowns.** An unknown that isn't flagged becomes a scope bomb. Surface it.
3. **Separate what you know from what you're assuming.** Label assumptions explicitly.
4. **Rate comes from `sayer-rates`.** That skill is the authoritative rate card and blended-rate model — consult it, do not hardcode. Default to the Associate rate ($150/hr) only when no tier mix is specified; ask if the staffing mix is unknown. Record the rate used in `scope.json` (`engagement.defaultRate` + per-workstream `rate`).
5. **One workstream per integration.** Don't lump integrations together -- each has unique complexity.
6. **Data migration is per-source.** Each data source gets its own estimate.
7. **Training is per-audience.** Admin training is not end-user training is not executive training.
8. **ERP adds a complexity premium.** Financial data is unforgiving -- always add buffer for reconciliation.
9. **Cap custom properties.** State the assumed cap (e.g., "up to 30 custom properties") -- overages are change orders.
10. **Project management hours scale with project size.** Use 10-15% of total estimated hours.

## Deliverable Checklist

Before presenting to the user, verify all deliverables include:

- [ ] `scope.json` written and passing `--validate-only` (the structured source of truth)
- [ ] Workstream-level hour estimates (min/max/median)
- [ ] Rate modeling with configurable rate
- [ ] Risk register with severity ratings
- [ ] Assumptions and exclusions list
- [ ] Client responsibilities / what's needed from them
- [ ] Open items / unresolved questions
- [ ] Approach comparison (if multi-system or complex)
- [ ] Client-ready summary (Slack/email format)
- [ ] Excel workbook with consistent formatting
