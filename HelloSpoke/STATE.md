# HelloSpoke -- Session State

> **Status:** `Pre-Sale`
> **Last updated:** 2026-04-16
> **One-liner:** Salesforce-to-HubSpot migration + HubSpot CPQ build (native) + Rev IO/QuickBooks/QuotaPath integrations for 30-person VoIP company; proposal drafted at $42K fixed fee, pending client review.

---

## Current Position

| Field | Value |
|-------|-------|
| Phase | Scoping -- proposal drafted |
| Week | N/A (pre-engagement) |
| Phase end date | Pending client approval |
| On track? | Yes |

---

## Done Last Session (2026-04-16)

- Ran first live client intake automation (scripts/intake.py) for HelloSpoke from HubSpot URL
- Fixed URL parser to handle regional subdomains (app-na2.hubspot.com)
- Added 1Password CLI as primary credential source in keychain.py
- Parsed 11 Fireflies transcripts + 24 notes + 25 meetings + 25 emails
- Defined 11 workstreams with hour estimates (134-300 hrs, median 200)
- Researched Rev IO and QuickBooks integration paths (neither has plug-and-play HubSpot connector)
- Built risk register (10 risks) and assumptions/exclusions list
- Generated HelloSpoke_Scope_Summary.md (client-facing proposal, fixed fee $35K / $22K reduced)
- Generated HelloSpoke_Scoping_Estimate.xlsx (4-sheet workbook: estimates, risks, assumptions, approach comparison)
- Logged 9 scoping decisions in HelloSpoke_decisions.md
- Added HelloSpoke to calibration/calibration.md with baseline data and 3 new cross-project patterns
- Published proposal to Gamma (https://gamma.app/docs/ugkxebvhkyyidkt) -- **STALE after CPQ correction, do not send**
- **CPQ scope correction (2026-04-16 PM):** Reviewed SF>HS Implementation Discovery transcript after Kyle flagged QuotaPath does not cover CPQ. Invalidated D4; added D10 (dedicated CPQ & Quoting workstream, HubSpot CPQ native per Billy's on-call direction, PandaDoc fallback). Split old WS 5 (QuotaPath & Quoting, 14 hrs med) into new WS 7 (CPQ, 38 hrs med) + new WS 8 (QuotaPath Coordination trimmed, 10 hrs med). New totals: 158/234/346 hrs. Fixed fee revised $35K -> **$42K** ($14K x 3 installments). Added 8 CPQ atomic requirements (CPQ-01..08). Phase 3 extended to weeks 5-11; Phase 4 shifted to weeks 10-14. Risks added (HubSpot AI CPQ instability, bulk quote import edge cases). Regenerated Excel workbook and calibration entry. Regenerated Gamma proposal: **https://gamma.app/docs/9xsb2pq9nvfe8ij** (supersedes the original Gamma URL; 121 credits used, ~3 min generation).

---

## Open Items

### Sayer Owes
- [ ] Review proposal with Cameron before sending to client
- [ ] Confirm pricing ($35K full / $22K reduced) aligns with Cam's expectations
- [ ] Finalize HubSpot tier recommendation after confirming existing instance tier

### Client Owes
- [ ] HubSpot instance tier confirmation (Professional vs Enterprise vs Commerce Hub for AI CPQ)
- [ ] Confirm HubSpot AI CPQ features are enabled on their instance
- [ ] Confirm DocuSign sunset timeline (no parallel run assumed)
- [ ] Rev IO API credentials and sandbox access
- [ ] QuickBooks Online admin access
- [ ] Salesforce admin access for data audit
- [ ] Sample quote CSVs (Ryan) for bulk-import validation harness
- [ ] Detailed dashboard/reporting requirements write-up (Jeremy Wiley -- committed Apr 14)
- [ ] Written approval of proposal to proceed

---

## Next Session Focus

1. Review proposal with Cameron; adjust pricing/scope if needed
2. If approved: generate plan.json for delivery phase using /project-plan skill
3. Begin Salesforce data audit once SF access provided

---

## Key Artifacts

| File | Purpose |
|------|---------|
| `HelloSpoke_Scope_Summary.md` | Client-facing proposal (fixed fee, no hours) |
| `HelloSpoke_Scoping_Estimate.xlsx` | Internal 4-sheet workbook (estimates, risks, assumptions, approach) |
| `HelloSpoke_decisions.md` | Scoping decision audit trail (9 decisions logged) |
| `HelloSpoke Discovery 2026-04-16.md` | HubSpot engagements + Fireflies transcript summaries |
| `HelloSpoke Meeting Recording.md` | Full Fireflies transcripts (11 recordings) |
| Gamma (current) | https://gamma.app/docs/9xsb2pq9nvfe8ij -- v2 proposal with CPQ scope ($42K) |
| Gamma (stale) | https://gamma.app/docs/ugkxebvhkyyidkt -- v1 proposal ($35K, pre-CPQ), do not send |

---

## Key Decisions

- **Scope boundary:** Elastic/ALN, Campfire ERP, ClickUp sync excluded from initial scope
- **CPQ as dedicated workstream (D10, supersedes D4):** HubSpot CPQ native primary (per Billy's on-call direction, "they have the AI CPQ"); PandaDoc as change-order fallback. Covers product library, dual dynamic templates, bulk line-item import up to 300 lines, parent-child property auto-creation with dedup, native e-sig, close-won amount sync. DocuSign being sunsetted.
- **QuotaPath:** HubSpot-side data flow only (commission tracking). They handle their own platform implementation.
- **Integration premium:** First-time Rev IO + QuickBooks integrations + first HubSpot AI CPQ build bumped above baseline ranges (American Bedding NetSuite + HubSpot CPQ patterns)
- **Pricing:** $42K full scope / $22K CRM-only reduced scope. No verbal quote given -- clean slate.
- **Phased migration:** Salesforce data migrated in 3 phases (inactive → active → leads) per discovery call agreement

---

## Standing Context

- **Salesforce contract expires October 2026** -- must complete migration with buffer. 14-week timeline targets August.
- **Existing HubSpot instance** -- tier unknown, provisioned ~Feb 2026 via HubSpot Growth team. Treat as reconfiguration, not greenfield.
- **Key contacts:** Jeremy Wiley (decision-maker, budget-aware), Christina Edwards (Director of Ops, project liaison), Ryan Sweeney (sales), Sara Hines (reporting/CS)
- **Rev IO** is telecom-specific billing platform. REST API, Basic Auth, sandbox available but webhooks don't work in sandbox.
- **QuickBooks** native HubSpot integration insufficient for revenue actuals -- custom build required.
- **Value-based pricing:** proposals use fixed fee only, no hours shown (Cam directive).
- **Payment terms:** equal installments every 15 days, net-15, 5% tech/admin fee.
