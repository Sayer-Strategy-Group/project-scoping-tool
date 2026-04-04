# Delivery Calibration Data

Claude MUST read this file before generating any new project plan, meeting schedule,
or client-facing project sheet.

---

## Delivery Adjustments

Patterns from completed deliveries. Each entry includes source project and confidence.
These override `/project-plan` defaults when applicable.

### Phase Duration Adjustments

*(None yet -- populated after first project retro)*

### Meeting Effectiveness Patterns

*(None yet)*

### Scope Change Patterns

*(None yet)*

---

## Project Delivery Baselines

Delivery data from completed projects. Format mirrors scoping calibration.
When a retro is completed, `/delivery-retro` adds an entry here with actuals.

*(None yet)*

---

## Cross-Project Delivery Patterns

Patterns observed across multiple deliveries. Updated after 2+ projects complete.
One data point is an anecdote -- two is the start of a pattern.

*(None yet)*

---

## How to Use This File

1. **Before `/project-plan`:** Check Phase Duration Adjustments for similar project types. Apply adjustments and cite the source.
2. **Before `/meeting-calendar` or meeting scheduling:** Check Meeting Effectiveness Patterns for cadence and format recommendations.
3. **Before `/project-sheet` or client-facing timelines:** Check Scope Change Patterns for contingency buffer recommendations.
4. **After project closes:** Run `/delivery-retro` to record actuals and extract learnings into the sections above.
5. **Do NOT write to this file manually.** All updates come through `/delivery-retro` to maintain consistent format and source citations.
