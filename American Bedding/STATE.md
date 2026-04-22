# American Bedding — Session State

> **Status:** `Pre-Sale`
> **Last updated:** 2026-04-22
> **One-liner:** HubSpot CPQ + NetSuite + Kuebix freight integration — two-phase proposal ($30k V1 + $11.5k V2) sent, pending client response after reference request.

---

## Current Position

| Field | Value |
|-------|-------|
| Phase | Pre-sale — proposal delivered, awaiting response |
| Deal stage | Proposal sent |
| Deal amount | ~$41,500 total (Phase 1: ~$30k, Phase 2: ~$11.5k) |
| On track? | Waiting — SB asked Apr 17 for HubSpot↔NetSuite CPQ references; follow-up drafted Apr 21 |

---

## Done Last Session

- Completed D1-D11 decisions log (most detailed in the repo)
- Finalized two-phase pricing after architecture shift (n8n → hybrid HubSpot + Railway)
- Validated all 5 Excel shipping calculators (no VBA, no external refs)
- Dorm Mattress identified as primary complexity driver (180+ calculation paths)

---

## Open Items

### Sayer Owes
- [ ] Get internal clearance on HubSpot↔NetSuite CPQ client references to share with SB
- [ ] Kyle/Cam review proposal before client presentation

### Client Owes
- [ ] Mike/Patrick review and approve proposal
- [ ] SOW signed by budget authority (Patrick, CFO)
- [ ] Clarify "Special Case Check with Delbert" in Dorm Mattress calculator

---

## Next Session Focus

1. Follow up on reference request (resolve internal clearance)
2. Present to Mike/Patrick for approval
3. Move to SOW signing

---

## Key Artifacts

| File | Purpose |
|------|---------|
| `Proposal Details/American_Bedding_CPQ_Proposal.md` | Two-phase proposal markdown |
| `Proposal Details/American_Bedding_CPQ_Estimate.xlsx` | Estimate workbook |
| `Proposal Details/American_Bedding_decisions.md` | D1-D11 scoping decisions (most detailed in repo) |
| `Proposal Details/American_Bedding_final_estimate.md` | Pricing history + architecture shift detail |
| `Proposal Details/discovery-analysis.md` | Discovery analysis writeup |
| `Proposal Details/American_Bedding_Scoping_Estimate.md` | Scope summary |

---

## Key Decisions

- **D1:** Phase 1 = inside sales CPQ only. Government RFP automation deferred to Phase 2.
- **D2:** Sayer owns all development including NetSuite (TPI not involved).
- **D3:** Hybrid architecture — HubSpot custom code + Railway API (revised from n8n).
- **D4:** Dynamic weight calculation with composition architecture (per-product modules, not single template).
- **D5:** Recommend Operations Hub Professional (~$800/mo additional).
- **D6/D11:** Two-phase pricing — V1 HubSpot-native ~$30k, V2 Railway production ~$11.5k.
- **D7:** Flat product catalog (one SKU per combination, ~700 SKUs).
- **D8:** Kuebix quickRate API for automated LTL freight.
- **D9:** NetSuite OAuth 2.0 M2M + SuiteQL for data access.

---

## Standing Context

- Manufacturing: mattresses/bedding for institutional, camps, government
- Systems: HubSpot Sales Hub Pro + Commerce Hub Pro, NetSuite ERP, Kuebix TMS
- 65 quotes/week is the volume driver — 20-30 min savings per quote = $38K-$58K/year ROI
- Billy Leigh verbal anchor: $25K. Phase 1 at $30K is the closest viable number.
- Patrick (CFO) is budget authority but was NOT in detailed discovery. Mike/Sarah-Beth are champions.
- Government sales (35% of revenue) excluded from Phase 1 — continues on manual process.
- Pre-engagement gate cleared Apr 4: all 5 Excel calculators validated, no VBA/macros.
