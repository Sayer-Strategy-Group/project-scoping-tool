# Delivery Retrospective: {Client Name}

**Project:** {Engagement name from plan.json or _final_estimate.md}
**System:** {Primary systems in scope}
**Scoping Date:** {Date from calibration.md baseline}
**Project Start:** {Actual start date}
**Go-Live Date:** {Actual go-live date}
**Retro Completed:** {Today's date}
**Conducted by:** Kyle Harbuck
**Linear Project:** {Linear project URL or "N/A"}

---

## 1. Numbers at a Glance

| Metric | Scoped | Actual | Variance |
|--------|--------|--------|----------|
| Total Hours (median) | {median_hrs} | {actual_hrs} | {+/-X hrs (+/-Y%)} |
| Total Cost | ${scoped_cost} | ${actual_cost} | {+/-$X (+/-Y%)} |
| Timeline (weeks) | {scoped_weeks} | {actual_weeks} | {+/-X weeks} |
| Phases | {scoped_phase_count} | {actual_phase_count} | {same / +/-N} |
| Scope Changes | N/A | {count} | {absorbed / change_order / descoped} |
| Change Order Value | N/A | ${change_order_total} | -- |

**Margin:** ${delivered_price} fee - ${actual_cost} cost = ${margin} ({margin_pct}%)

---

## 2. Phase-by-Phase Actuals

| Phase | Scoped Hours | Actual Hours | Variance | Duration (Scoped) | Duration (Actual) | Notes |
|-------|-------------|-------------|----------|-------------------|-------------------|-------|
| {Phase 1 Name} | {min-max (median)} | {actual} | {+/-X%} | {X weeks} | {Y weeks} | {brief note} |
| {Phase 2 Name} | {min-max (median)} | {actual} | {+/-X%} | {X weeks} | {Y weeks} | {brief note} |
| {Phase N Name} | {min-max (median)} | {actual} | {+/-X%} | {X weeks} | {Y weeks} | {brief note} |
| **Cross-Phase (PM)** | {min-max (median)} | {actual} | {+/-X%} | -- | -- | {brief note} |
| **Total** | **{min-max (median)}** | **{actual}** | **{+/-X%}** | **{X weeks}** | **{Y weeks}** | |

---

## 3. Workstream Variance -- Top 3

The workstreams with the largest estimation variance, and what drove it.

### {Workstream 1 Name} ({ID})
- **Estimated:** {min}-{max} hrs (median {median})
- **Actual:** {actual} hrs
- **Variance:** {+/-X hrs, +/-Y%}
- **Why:** {Root cause of the variance. Be specific -- "took longer" is not actionable.}
- **Calibration impact:** {What should change in future estimates for similar workstreams}

### {Workstream 2 Name} ({ID})
- **Estimated:** {min}-{max} hrs (median {median})
- **Actual:** {actual} hrs
- **Variance:** {+/-X hrs, +/-Y%}
- **Why:** {Root cause}
- **Calibration impact:** {What should change}

### {Workstream 3 Name} ({ID})
- **Estimated:** {min}-{max} hrs (median {median})
- **Actual:** {actual} hrs
- **Variance:** {+/-X hrs, +/-Y%}
- **Why:** {Root cause}
- **Calibration impact:** {What should change}

---

## 4. Scope Changes

| # | Description | Source | Handling | Hours Added | Cost Impact |
|---|-------------|--------|----------|-------------|-------------|
| 1 | {What changed} | {Client request / discovery gap / dependency} | {Absorbed / Change order / Descoped} | {+X hrs} | {+$X or absorbed} |
| 2 | {What changed} | {Source} | {Handling} | {+X hrs} | {+$X or absorbed} |

**Total scope change impact:** {+X hrs, +$Y}

**Pattern note:** {Was this predictable? Should future scopes of similar type include a buffer for this category of change?}

---

## 5. Risk Materialization

Checked against the original risk register from plan.json.

| Risk ID | Risk Name | Predicted Severity | Materialized? | Actual Impact | Mitigation Effectiveness |
|---------|-----------|-------------------|---------------|---------------|-------------------------|
| {R-01} | {Risk name} | {HIGH/MED/LOW} | {Yes / No / Partially} | {Description of actual impact, or "N/A"} | {Mitigation worked / partially / failed / not needed} |
| {R-02} | {Risk name} | {severity} | {Yes/No/Partially} | {impact} | {effectiveness} |

**Unregistered risks:** {Risks that materialized but were NOT in the original register. These are scoping blind spots.}

---

## 6. Meeting Effectiveness

**Planned cadence:** {From plan.json -- e.g., "Weekly 30-min standups, phase review at each milestone"}
**Actual cadence:** {What actually happened}

| Meeting Type | Planned | Actual | Effectiveness | Recommendation |
|-------------|---------|--------|--------------|----------------|
| Kickoff | {1x 60 min} | {what happened} | {Effective / Needs change} | {Keep as-is / Adjust to X} |
| Standups | {Weekly 30 min} | {what happened} | {Effective / Needs change} | {Keep as-is / Adjust to X} |
| Phase Reviews | {Per milestone, 45 min} | {what happened} | {Effective / Needs change} | {Keep as-is / Adjust to X} |
| Training | {Per plan} | {what happened} | {Effective / Needs change} | {Keep as-is / Adjust to X} |

**Key takeaway:** {One sentence on what to do differently with meetings for similar projects}

---

## 7. What Was Missing from the Plan

Things that came up during delivery that scoping or planning did not catch.

- **{Gap 1}:** {Description. Why was it missed? How should the scoping or planning process change to catch it?}
- **{Gap 2}:** {Description and recommended process change}
- **{Gap 3}:** {Description and recommended process change}

**Skills to update:**
- `/scope-project`: {Specific change, or "No change needed"}
- `/project-plan`: {Specific change, or "No change needed"}
- `/delivery-retro`: {Specific change to this skill, or "No change needed"}

---

## 8. Client Satisfaction

**Overall signal:** {Strong positive / Positive / Neutral / Negative}
**Reference potential:** {Yes -- willing to be a reference / Maybe -- need to ask / No}

**Direct feedback or signals:**
- {Quote or paraphrased feedback from client}
- {Observable signal -- e.g., "Renewed for Phase 2 without hesitation", "Asked for proposal for second project"}

**What the client valued most:** {Specific deliverable, behavior, or outcome they highlighted}
**What frustrated the client:** {If anything -- be honest. This feeds improvement.}

---

## 9. Delivery Process Improvements

Specific, actionable changes mapped to the skills and processes that would benefit.

### For `/scope-project` (Estimation)
- {Specific estimation change. E.g., "Add 15% buffer to data migration for clients with 5+ years of CRM data"}
- {Or: "No estimation changes needed -- estimates were accurate"}

### For `/project-plan` (Planning)
- {Specific planning change. E.g., "Add a dedicated data audit task in Phase 1 before committing migration hours"}
- {Or: "No planning changes needed"}

### For `/delivery-retro` (This Process)
- {Specific retro process change. E.g., "Add a question about handoff documentation quality"}
- {Or: "No retro process changes needed"}

### For Delivery Process (General)
- {Broader process improvement. E.g., "Require client to provide system access within 5 business days of kickoff or timeline shifts"}

---

## Calibration Extractions

Summary of what was written to calibration files from this retro.

### Added to `calibration/calibration.md`
- **Baseline updated:** {Client} actuals recorded ({actual_hrs} hrs, ${actual_cost}, {actual_weeks} weeks)
- **Estimation adjustment:** {Description, or "None -- estimates were within range"}
- **Cross-project pattern:** {Updated pattern, or "None -- insufficient data points"}

### Added to `calibration/delivery-calibration.md`
- **Delivery baseline:** {Client} delivery data recorded
- **Phase duration adjustment:** {Description, or "None"}
- **Meeting pattern:** {Description, or "None"}
- **Scope change pattern:** {Description, or "None"}
- **Cross-project delivery pattern:** {Description, or "None -- need 2+ completed deliveries"}
