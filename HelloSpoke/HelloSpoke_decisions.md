# HelloSpoke -- Scoping Decisions

**Scoped by:** Kyle + Claude
**Date:** 2026-04-16
**Industry:** VoIP / Telecom (multifamily real estate vertical)
**Systems:** HubSpot CRM (existing instance reconfig), Salesforce (migration source), Rev IO (billing), QuickBooks Online (accounting), QuotaPath (commissions)

---

## Decisions Log

### D1: Exclude Elastic/ALN database integration from initial scope
- **Category:** scope-boundary
- **Decision:** Elastic and ALN integrations are out of initial scope; noted as future phase opportunity
- **Alternatives considered:** Include Elastic/ALN as workstream -- rejected, Jeremy explicitly de-scoped in March 26 call ("at some point we probably want to pull some data from that" / "truly to start with, there aren't that many systems")
- **Rationale:** Jeremy self-identified these as aspirational, not immediate. Data replication architecture (Fivetran/Airbyte) would add 12-24+ hrs and introduce a data warehousing dependency that isn't needed for the core CRM + integrations value.
- **Assumption:** HelloSpoke doesn't need multifamily data enrichment from ALN for the initial HubSpot rollout
- **Invalidation trigger:** Client requests multifamily data automation before go-live
- **Estimate impact:** -12-24 hrs removed from scope
- **Calibration source:** none -- first occurrence
- **Confidence:** high

### D2: Exclude Campfire ERP integration
- **Category:** scope-boundary
- **Decision:** Campfire ERP evaluation is TBD on HelloSpoke's side; excluded from this engagement
- **Alternatives considered:** Include ERP adjacency workstream -- rejected per Kyle's direction after confirming with Cameron
- **Rationale:** ERP selection is still in progress. Including it would add the 1.25-1.5x ERP complexity premium and tie the engagement timeline to an external vendor decision.
- **Assumption:** HelloSpoke's ERP evaluation proceeds independently
- **Invalidation trigger:** Cameron confirms ERP integration is required for the CRM engagement
- **Estimate impact:** Avoids 25-50% complexity premium on integration workstreams
- **Calibration source:** Top Down Auto (ERP involvement pattern), American Bedding (ERP adjacency vs build)
- **Confidence:** high

### D3: Exclude ClickUp sync
- **Category:** scope-boundary
- **Decision:** ClickUp-to-HubSpot visibility sync removed from scope per Kyle
- **Alternatives considered:** Keep as lightweight workstream -- rejected, Kyle directed removal
- **Rationale:** Short-term sync between project management tools is low-value relative to core CRM + integration work
- **Assumption:** HelloSpoke manages ClickUp independently
- **Invalidation trigger:** Sales team can't track implementation status without ClickUp data in HubSpot
- **Estimate impact:** -6-12 hrs removed
- **Calibration source:** none
- **Confidence:** high

### D4: ~~Combine QuotaPath and CPQ into single workstream, QuotaPath-primary~~ -- **INVALIDATED 2026-04-16**
- **Category:** scope-boundary
- **Status:** Superseded by D10 on same day after re-reviewing the SF>HS Implementation Discovery transcript
- **Original reasoning (incorrect):** Assumed QuotaPath covered quoting-adjacent functionality and CPQ could be fallback-only
- **Why invalidated:** QuotaPath is strictly commission tracking / rep management -- it does not handle quoting. CPQ is a distinct, mandatory workstream per Jeremy ("the CPQ process is absolutely part of it") and Billy ("we're just going to use HubSpot CPQ for that because they have the AI CPQ"). See D10 for the revised approach.
- **Estimate impact (reversed):** +34 median hrs added back via D10

### D5: Apply first-time integration premium to Rev IO and QuickBooks
- **Category:** estimation
- **Decision:** Bump integration estimates above baseline ranges to account for Sayer's first implementation of both systems
- **Alternatives considered:** Use standard baseline ranges -- rejected, no prior Sayer experience with either platform creates discovery overhead
- **Rationale:** Rev IO has no native HubSpot marketplace app (requires custom API work via REST + Basic Auth). QuickBooks native HubSpot integration doesn't cover revenue actuals sync (one-way only, no deal-to-invoice matching). Both need custom development. American Bedding's NetSuite integration (also first-time) ran 40-60 hrs.
- **Assumption:** Rev IO API documentation is accessible and sandbox available for testing; QuickBooks OAuth2 setup and webhook configuration are manageable within estimate
- **Invalidation trigger:** Rev IO API turns out to be poorly documented or requires partner-level access; QuickBooks rate limits (500 req/min) become blocking
- **Estimate impact:** Rev IO: +10 hrs median (22 -> 32); QuickBooks: +6 hrs median (12 -> 18)
- **Calibration source:** American Bedding (first-time NetSuite integration, 40-60 hrs)
- **Confidence:** medium

### D6: No verbal quote given -- clean pricing slate
- **Category:** pricing
- **Decision:** Set fixed fee in $32,000-$38,000 range based on median-to-max hour estimates
- **Alternatives considered:** Price at median ($30K) -- too thin given first-time integration risk; price at max ($45K) -- no justification without known blockers
- **Rationale:** No verbal quote from Cameron to anchor against. Integration uncertainty (Rev IO + QuickBooks are both first-time) warrants pricing above median. HelloSpoke has 15-18 users, Salesforce migration, and 3 integration workstreams -- materially more complex than Milestone ($26K) or Arkview ($18K).
- **Assumption:** Fixed fee covers all 11 workstreams as scoped; scope changes are change orders
- **Invalidation trigger:** Cameron has given verbal pricing that contradicts this range
- **Estimate impact:** Pricing decision only, no hour change
- **Calibration source:** Milestone ($26,075 for simpler scope), Strive Option B ($32,400 for similar user count but fewer integrations)
- **Confidence:** medium

### D7: Recommend phased data migration approach
- **Category:** approach
- **Decision:** Migrate Salesforce data in phases: inactive customers first, then active pipeline, then leads
- **Alternatives considered:** Big-bang migration -- rejected, data quality concerns (duplicates confirmed in transcripts); migrate only active data -- rejected, Jeremy wants historical context preserved
- **Rationale:** Phased approach reduces risk per load, allows validation between batches, and was explicitly agreed upon in discovery calls (March 26 + April 2). Jeremy emphasized completing well before October SF contract end.
- **Assumption:** Salesforce data volume is <50K records total; data is exportable in standard formats
- **Invalidation trigger:** Salesforce export reveals >100K records or heavily customized objects that don't map cleanly
- **Estimate impact:** No net change vs big-bang; hours redistribute across 2-3 load cycles with validation between
- **Calibration source:** Strive Global (existing HubSpot reconfig, data quality risk pattern)
- **Confidence:** high

### D8: Existing HubSpot instance -- reconfiguration, not greenfield
- **Category:** estimation
- **Decision:** Account for existing HubSpot instance audit and cleanup in CRM Architecture workstream
- **Alternatives considered:** Treat as greenfield -- rejected, existing instance may have marketing data, settings, or legacy config
- **Rationale:** HubSpot Growth team (Zack Grimm) ran a demo in February. Instance may have been set up with default config or early marketing work. Calibration pattern from Strive: "Reconfiguration is harder than greenfield."
- **Assumption:** Existing instance is relatively clean (recently provisioned); not 10 years of data like Strive
- **Invalidation trigger:** Existing instance has extensive custom config or data that needs migration/cleanup
- **Estimate impact:** CRM Architecture stays at 8-18 hrs (median 12) -- low end if instance is clean, high end if messy
- **Calibration source:** Strive Global (existing instance reconfiguration pattern)
- **Confidence:** medium

### D10: CPQ scoped as dedicated workstream using HubSpot CPQ native (supersedes D4)
- **Category:** scope-boundary
- **Decision:** Add a dedicated CPQ & Quoting workstream (28/38/52 hrs) using HubSpot CPQ native (incl. native e-signature). Trim QuotaPath Coordination to HubSpot-side data flow only (6/10/14 hrs). PandaDoc handled as a change order if HubSpot CPQ AI falls short during build.
- **Alternatives considered:**
  - Keep combined workstream (D4 approach) -- rejected, QuotaPath does not cover quoting
  - Scope CPQ as PandaDoc primary -- rejected, Billy stated on-call "we're just going to use HubSpot CPQ for that because they have the AI CPQ"
  - Present HubSpot CPQ vs PandaDoc as two priced options -- rejected by Kyle 2026-04-16, single proposal cleaner
- **Rationale:** Transcript review (SF>HS Implementation Discovery) surfaced that HelloSpoke's CPQ pain is material and independent of commission tracking: (a) Jeremy is a quoting bottleneck -- reps cannot quote unassisted; (b) two product lines (VoIP + Notify SaaS) need dynamic T&Cs per product; (c) property management deals require bulk line-item quotes (5-300 properties per quote); (d) quote auto-creates sub-accounts but currently duplicates them -- needs dedup logic; (e) close-won automation must sync final quoted amount back to deal amount; (f) DocuSign is being sunsetted (vendor tripled rate). HubSpot CPQ (with AI) is HelloSpoke's declared direction.
- **Assumption:** HubSpot Sales Hub Professional (or Commerce Hub) supports required quote customization; HubSpot AI CPQ features are stable enough for production use by go-live (they are currently testing); up to 2 dynamic templates + 1 combined template; up to 50 products in catalog; up to 2 approval tiers; bulk import up to 300 line items
- **Invalidation trigger:** HubSpot CPQ AI features fail to meet bulk-quote or template requirements during build -> PandaDoc change order; DocuSign contract not sunset before go-live (parallel run needed)
- **Estimate impact:** +38 median hrs (new CPQ WS) - 4 median hrs (QuotaPath trim) = +34 hrs net. Pushes total median from 200 -> 234 hrs. Fixed fee moves $35K -> $42K ($14,000 x 3 installments).
- **Calibration source:** American Bedding (first-time HubSpot CPQ build pattern); HelloSpoke transcript primary source (lines 3148, 3674-3705, 3866, 3890-3944, 4411-4417 of HelloSpoke Meeting Recording.md)
- **Confidence:** medium (HubSpot AI CPQ stability is the largest unknown -- HelloSpoke is still testing it)

### D9: HubSpot tier recommendation pending confirmation
- **Category:** tier
- **Decision:** Recommend Sales Hub Professional as minimum tier; confirm existing instance tier with Kyle/Cameron
- **Alternatives considered:** Enterprise -- possibly needed if advanced custom objects or partitioning required, but Professional supports up to 10 custom objects which should suffice
- **Rationale:** HelloSpoke needs custom objects (Rev IO billing, possibly multifamily properties), workflows, custom reporting, and CPQ capability. Professional covers all of these. Enterprise adds advanced permissions, custom objects beyond 10, and predictive lead scoring -- likely overkill initially.
- **Assumption:** 2-3 custom objects sufficient for Rev IO + multifamily needs
- **Invalidation trigger:** Custom object count exceeds Professional tier limits; advanced partitioning needed for multi-brand structure
- **Estimate impact:** No hour impact; tier affects HubSpot licensing cost (client responsibility)
- **Calibration source:** Milestone (Starter/Smart CRM), Arkview (Professional)
- **Confidence:** medium

---

## Internal Hour Estimates (not for client)

**Revised 2026-04-16 after D10 (CPQ split into dedicated workstream).**

| # | Workstream | Min | Med | Max |
|---|-----------|-----|-----|-----|
| 1 | CRM Architecture & Setup | 8 | 12 | 18 |
| 2 | Pipeline & Deal Management | 8 | 12 | 18 |
| 3 | Contact & Company Management | 12 | 16 | 24 |
| 4 | Salesforce Data Migration | 16 | 24 | 36 |
| 5 | Rev IO Integration | 24 | 32 | 44 |
| 6 | QuickBooks Integration | 12 | 20 | 32 |
| 7 | CPQ & Quoting (HubSpot CPQ native) | 28 | 38 | 52 |
| 8 | QuotaPath Coordination | 6 | 10 | 14 |
| 9 | Automations & Workflows | 10 | 16 | 22 |
| 10 | Reporting & Dashboards | 10 | 16 | 22 |
| 11 | Training & Adoption | 10 | 16 | 24 |
| 12 | Project Management | 14 | 22 | 40 |
| | **TOTAL** | **158** | **234** | **346** |

Rate: $150/hr | Range: $23,700 - $51,900 | Median: $35,100
**Fixed fee proposed: $42,000** (premium above median covers first-time HubSpot CPQ AI, Rev IO + QuickBooks integration unknowns, and CPQ complexity factors: dynamic T&C templates, bulk line-item import, parent-child dedup, DocuSign sunset migration)
