# {Client Name} -- Scoping Decisions

**Scoped by:** {Name}
**Date:** {Date}
**Industry:** {Industry}
**Systems:** {Systems in scope}

---

## Decisions Log

<!-- Claude fills this in during scoping sessions. One entry per meaningful decision.
     Format is key-value for fast LLM parsing in future calibration reads. -->

### D1: {Short decision title}
- **Category:** {estimation | approach | tier | scope-boundary | risk-mitigation | pricing}
- **Decision:** {What was decided, one sentence}
- **Alternatives considered:** {What was rejected and why, semicolon-separated}
- **Rationale:** {Why this path -- cite client context, risk signals, or budget signals}
- **Assumption:** {What must remain true for this decision to hold}
- **Invalidation trigger:** {What would force revisiting this decision}
- **Estimate impact:** {How this moved hours or cost vs. baseline, e.g., "+15% to data migration" or "no change"}
- **Calibration source:** {Past project that informed this, or "none -- first occurrence"}
- **Confidence:** {high | medium | low}

---

## Example Entries (delete after first real use)

### D1: Recommend phased over concurrent delivery
- **Category:** approach
- **Decision:** Phase 1 CRM standalone, Phase 2 ERP integration after follow-up call resolves unknowns
- **Alternatives considered:** Concurrent CRM+ERP -- rejected due to 22 unresolved ERP questions; fixed-fee with ERP contingency -- rejected, too much variance
- **Rationale:** NetSuite data quality unknown, Intuitive extraction feasibility unconfirmed, multi-subsidiary adds API complexity. Phased isolates ERP risk from CRM value delivery.
- **Assumption:** Follow-up call with Alexis/Terry resolves extraction feasibility and data architecture direction
- **Invalidation trigger:** Client insists on single-phase delivery or imposes hard deadline requiring parallel work
- **Estimate impact:** No net hour change but redistributed across two SOWs. PM hours +4 hrs for second kickoff.
- **Calibration source:** none -- first ERP-involved project
- **Confidence:** high

### D2: Price at lower-middle of Cameron's verbal range
- **Category:** pricing
- **Decision:** Target $18,150 median against Cameron's $15K-$30K verbal quote
- **Alternatives considered:** Price at midpoint ($22.5K) -- rejected, Jess is cost-conscious and wasn't in discovery; price at floor ($15K) -- rejected, leaves no margin for real estate pipeline unknowns
- **Rationale:** Jess controls budget but wasn't in detailed discovery. Lower-middle builds trust while leaving $5K+ buffer for scope additions. Frank is champion but not decision-maker.
- **Assumption:** Real estate pipeline discovery with Vijay/Philip doesn't add >20 hrs of work
- **Invalidation trigger:** Real estate pipeline turns out to need custom objects or complex stage logic
- **Estimate impact:** No hour change -- pricing strategy only
- **Calibration source:** none -- first PE firm with split champion/budget authority
- **Confidence:** medium

### D3: AI enrichment pilot before committing full data cleanup hours
- **Category:** risk-mitigation
- **Decision:** Scope a 500-record AI enrichment pilot in Phase 1 before estimating full data normalization
- **Alternatives considered:** Full manual classification of 10-year backlog -- rejected, could be 40-80 hrs with unknown ROI; skip enrichment entirely -- rejected, pipeline reporting is meaningless without classified contacts
- **Rationale:** 10 years of uncoded contact data is the #1 risk. A 500-record pilot validates whether HubSpot Breeze credits can automate classification before committing to manual hours.
- **Assumption:** Client has 5-10K Breeze credits available on current Enterprise plan
- **Invalidation trigger:** Breeze enrichment accuracy below 70% on pilot batch
- **Estimate impact:** Caps initial data work at 18 hrs (median) instead of potentially 40+ if done manually
- **Calibration source:** none -- first project using AI enrichment as estimation hedge
- **Confidence:** medium
