# Top Down Auto — Session State

> **Status:** `Pre-Sale (Active)`
> **Last updated:** 2026-05-11
> **One-liner:** CRM platform pivoted HubSpot → NetSuite CRM on 4/29; Phase 1 candidate is now Legacy Intuitive → NetSuite migration audit + CSR discovery, with NetSuite CRM build deferred to Phase 2.

---

## Current Position

| Field | Value |
|-------|-------|
| Phase | Pre-sale — Phase 1 SOW scoping call 2026-05-11 2pm CDT |
| Deal stage | Scoping pivot post-4/29 — Phase 1 fixed-fee target |
| Deal amount | Phase 1 target: ~$15-25K (audit + discovery + migration plan). Phase 2 NetSuite CRM build: TBD after Phase 1 outputs. Original HubSpot range ($28.8-65.1K) superseded by platform pivot. |
| On track? | Yes — 2pm call locks Phase 1 scope; SOW drafted this week |

---

## Done Last Session

- **2026-04-29 — Sayer + Top Down "Topdown data discovery" call** (Tim, Stephanie, Cameron, Ismael@Genesis, Alexis) — Fireflies IDs `01KQD9YQPA4KKX7S106FF0Y1F3` and `01KQA5SA6TJ9K3RMT9ZGRR3N05` (duplicate captures)
  - CRM platform decision shifted from HubSpot Sales Hub Pro to **NetSuite CRM**
  - Genesis (Ismael Cordero, ismael@gahh.com) confirmed as owner of the SQL Server-based PIM that becomes product-data source-of-truth feeding NetSuite — not a Sayer workstream
  - Legacy Intuitive ERP → NetSuite migration confirmed in scope; ~300 complex tables; Alexis providing Hyper-V VM access
  - NetSuite CRM build timeline: "at least 90 days" / "6-12 weeks"
  - Sayer action items: phased audit + migration plan for legacy data; coordinate internal NetSuite/data team; align ETL/NetSuite syncing teams; support CRM-setup timeline alignment
- 2026-05-11 prep work: revised 2pm call agenda + question lines; pre-call email drafted

---

## Open Items

### Sayer Owes
- [ ] Run 2026-05-11 2pm CDT scoping call; lock Phase 1 = migration audit + CSR discovery + migration plan
- [ ] Draft Phase 1 SOW after 2pm call (target: this week)
- [ ] Schedule internal Sayer NetSuite/data team review for migration-query approach
- [ ] Reposition `Top_Down_Auto_Scope_Summary.md` — workstream estimates still valid as templates, but CRM tier rec is stale (HubSpot Sales Hub Pro → NetSuite CRM)
- [ ] Send revised pre-call email by ~1pm CDT (draft: `2026-05-11_pre-call_email_draft.md`)

### Client Owes
- [ ] Stephanie: confirm Phase 1 decision authority / signature path
- [ ] Stephanie + Alexis: confirm Hyper-V VM access landing date (gates Sayer audit start)
- [ ] Stephanie: define "done" for Phase 1 (written plan? process maps? both?)
- [ ] Stephanie: confirm CRM platform decision (NetSuite firm vs. still negotiable)
- [ ] Ismael: PIM progress demo (informational, not blocking Sayer)

---

## Next Session Focus

1. Run 2pm call per revised agenda — lock Phase 1 audit scope
2. Define Phase 1 SOW deliverables + fixed fee
3. Draft SOW and route to Stephanie for signature within the week
4. Begin internal Sayer NetSuite/data team coordination ahead of Phase 1 kickoff

---

## Key Artifacts

| File | Purpose | Status |
|------|---------|--------|
| `Top_Down_Auto_Scope_Summary.md` | Pre-4/29 HubSpot scope writeup | **STALE for tier rec — workstream estimates still usable as templates** |
| `Top_Down_Auto_Scoping_Estimate.xlsx` | Pre-4/29 HubSpot estimate workbook | **STALE — needs NetSuite-CRM rework before client delivery** |
| `Top_Down_Auto_ERP_Questions.md` | 22 ERP clarifying questions (pre-4/29) | Most resolved on 4/29; flag 3-5 still-open Phase-1 blockers during 2pm call |
| `TopDownAuto_final_estimate.md` | Final delivery tracker | Still TBD pending 2pm + SOW |
| `Top Down Auto Scope (1).xlsx` | Alternative scope version | Likely retire — confirm with Cameron |
| `Sayer Topdown Discovery Feb 11 2026.md` | Original 2/11 discovery notes | Reference — pre-pivot |
| `2026-05-11_pre-call_email_draft.md` | 1pm CDT prep email for Stephanie + Tim | Draft, awaiting Kyle review/send |

---

## Key Decisions

- **2026-04-29 — CRM platform pivot:** HubSpot Sales Hub Pro → **NetSuite CRM**. Driver: consolidation around NetSuite as ERP source of truth + Genesis PIM feeding it; HubSpot would have added a third platform to integrate. Implication: entire CRM workstream sizing needs re-mapping to NetSuite CRM features; HubSpot estimate workbook is stale for client delivery.
- **2026-04-29 — Lane separation:** Genesis owns PIM, Alexis owns legacy server admin, Sayer owns migration audit + CRM rollout. Pre-emptive boundary to prevent scope creep on Sayer's side and avoid Sayer rebuilding what Genesis is doing.
- **2026-05-11 — Phased SOW strategy:** Phase 1 = audit-only (low-risk, fast, fixed-fee). Phase 2 = NetSuite CRM build, priced after Phase 1 outputs define it. Driver: Genesis PIM not ready, CSR processes not mapped — anything Sayer builds today gets refactored. Audit-first earns the right to the bigger Phase 2 SOW.
- **Previously (2026-03-05) — Phased approach:** Still valid in spirit but the platform choice underneath it changed. Phase 1/Phase 2 split survives the pivot.

---

## Standing Context

- Top Down Auto = auto group with multiple subsidiaries/brands (interiors, convertible tops, seat covers); inbound-heavy sales motion handled by CSRs
- **Stakeholders:**
  - Stephanie (client owner — CRM, phones, sales/service tooling; SOW signer per current understanding)
  - Sales manager (7-year tenure, deep NetSuite knowledge, key implementation partner)
  - Alexis Molina (client IT/dev — legacy server, Hyper-V VM access, migration enablement)
  - Ismael Cordero (Genesis / gahh.com — building SQL Server PIM; NOT Sayer scope but adjacent)
  - Billy Leigh (client architecture leaning — data warehouse vs. point-to-point opinions)
  - Terry + Shafi (NetSuite/ERP experts on Top Down side)
- **Tech stack:** NetSuite (ERP + future CRM), Genesis PIM (SQL Server, in-flight), Intuitive legacy ERP (decommissioning target), Magento + WooCommerce ($3-4M/yr e-comm, consolidation 2027-2028), Nextiva phones (replacement targeted but not in scope), Klaviyo (out of scope)
- **Risk watch:** Genesis dependency — if Ismael's PIM slips, NetSuite CRM rollout slips. Phase 1 audit can proceed in parallel, but Phase 2 cannot.
- Two xlsx estimate versions still exist; both are now stale post-platform-pivot.

---

## Cross-Project Pattern (filed in project memory)

This is the **second engagement** where a non-Sayer technical actor narrowed Sayer's lane mid-scoping:
- VestaFreight: public B2B vendor APIs more mature than baseline assumed; decoupled integration from CRM migration
- Top Down Auto: Genesis PIM took over product-data ownership; Sayer's CRM workstream shrunk and pivoted platforms

Pattern: Sayer's discovery-driven scope assumes Sayer-built integration; the client's parallel work changes the lane before SOW. Earlier detection (asking "who else is building toward this outcome already?" during discovery) could shorten scope-pivot cycles.
