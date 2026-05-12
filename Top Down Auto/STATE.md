# Top Down Auto — Session State

> **Status:** `Pre-Sale (Active) — SOW Drafting`
> **Last updated:** 2026-05-12
> **One-liner:** Phase 1 scope verbally agreed 5/11 (legacy Intuitive ERP → NetSuite migration, audit-led). SOW drafting this week. Stephanie call 2026-05-12 is the formal scoping + proposal pass.

---

## Current Position

| Field | Value |
|-------|-------|
| Phase | Pre-sale — Stephanie scoping call 2026-05-12; Phase 1 SOW drafting in flight |
| Deal | HubSpot deal #283274309364 — **renamed 2026-05-12** to "Top Down Auto — NetSuite Migration + CRM" |
| Deal stage | `qualifiedtobuy` (default pipeline) — appropriate post-5/11 |
| Deal amount | **$20K Phase 1 anchor** (Phase 2 priced separately after Phase 1 outputs define it) |
| Deal owner | Cameron Taggart (originator: Billy Leigh) |
| Company owner | Billy Leigh |
| On track? | Yes — Phase 1 scope agreed verbally; SOW arrives this week with Stephanie pre-briefed by Ismael |

---

## Done Last Session

### 2026-05-11 — Sayer + Top Down Phase 1 scoping working session
Fireflies: `01KRC6JXCKWR5YNRZP6AEYA62Z`. HubSpot note: #369203261115 (assoc: Company, Deal, Alexis, Ismael).

Full recap: [`2026-05-11_post-call_recap.md`](2026-05-11_post-call_recap.md)

- **Phase 1 scope locked verbally:** legacy Intuitive ERP → NetSuite data migration, driven by user interviews + query capture, with rationalization against the 2022 NetSuite cutover before load.
- **Phase 2 deferred:** NetSuite CRM build = separate SOW, scoped post-Phase 1.
- **Alexis silver-plattered the technical approach:** VM/SQL prep (client-owned), interview method via Enable in Central remote desktop as "Brian" god-user (client-provisioned), rationalization + wrangle in SQL Server, then CSV load to NetSuite (Sayer-owned).
- **12 named interview targets** confirmed across Guy Robins, Easy On, and supply chain.
- **Excluded dataset:** anything migrated in 2022 NetSuite cutover is excluded from this pull (immutable since).
- **Open technical questions** logged for Tim: NetSuite import format spec; conferencing platform with "give control" feature.

---

## Today's Focus — 2026-05-12 Stephanie Scoping Call

This is the formal scoping pass. Use [`2026-05-11_post-call_recap.md`](2026-05-11_post-call_recap.md) as the input.

**Goal of the Stephanie call:** Validate Phase 1 framing in writing, secure SOW-signature path, confirm Phase 1 fixed-fee acceptance.

**Materials to produce after the call:**
1. Phase 1 SOW (markdown + brand-styled doc) — workstream breakdown using Alexis's silver-platter sequence
2. Phase 1 Scoping Estimate (Excel, brand-styled per `scripts/brand_styles.py`)
3. Updated scope summary doc (`Top_Down_Auto_Scope_Summary.md` — currently stale)
4. Risk register + assumptions

**Routing:** Run `/scope-project Top Down Auto` after the call.

---

## Open Items

### Sayer Owes
- [ ] **Send Phase 1 follow-up email to Alexis + Ismael** — drafted in Superhuman (`draft005b7b0ce791b84b`), pending Kyle review/send
- [ ] **Run Stephanie scoping call 2026-05-12** — capture her requirements, sign-off path, Phase 1 expectations
- [ ] **Draft Phase 1 SOW** — target: this week. Uses 5/11 recap as input.
- [ ] **Update HubSpot SOW** — refresh Excel estimate workbook with Phase 1 NetSuite migration scope (the existing workbook is stale)
- [ ] **Confirm NetSuite import format** (Tim) — needed for SOW load-step assumptions
- [ ] **Send Whataburger gift cards** to Alexis + Ismael once mailing addresses arrive (Kyle personal commitment from call)

### Client Owes
- [ ] **Alexis:** Complete VM / SQL Server 2022 / Fortinet firewall provisioning; share readiness date
- [ ] **Alexis:** Confirm interview-target list with divisions; add any missed names
- [ ] **Alexis:** Issue "Brian" god-user credentials to Sayer
- [ ] **Ismael:** Pre-brief Stephanie on Phase 1 framing before SOW lands
- [ ] **Stephanie:** Confirm SOW signature path + Phase 1 decision authority

---

## Next Session Focus

1. **Today (2026-05-12):** Run Stephanie scoping call. Goal = scope confirmed + sign-off path clear.
2. **Today / tomorrow:** Generate Phase 1 SOW + Excel estimate via `/scope-project Top Down Auto`. Brand-style both per Sayer brand guidelines.
3. **This week:** Route SOW through Ismael → Stephanie. Get formal Phase 1 sign-off.
4. **Pre-kickoff:** Coordinate internal Sayer NetSuite/data team for Phase 1 execution staffing.

---

## Key Artifacts

| File | Purpose | Status |
|------|---------|--------|
| [`2026-05-11_post-call_recap.md`](2026-05-11_post-call_recap.md) | **5/11 call recap — input to Stephanie scoping pass today** | **FRESH (2026-05-12)** |
| `2026-05-11_pre-call_email_draft.md` | Pre-call email drafted before 5/11 call | Archive — superseded by post-call follow-up draft in Superhuman |
| `2026-05-11_call_runsheet.docx` | Runsheet used for 5/11 call | Archive — call complete |
| `Sayer Topdown Discovery Feb 11 2026.md` | Original 2/11 discovery notes | Reference — pre-pivot, historical context only |
| `Sayer Topdown Discovery Meeting Recording.md` | 2/11 transcript | Reference |
| `Top_Down_Auto_Scope_Summary.md` | Pre-4/29 HubSpot scope writeup | **STALE — regenerate post-Stephanie call** |
| `Top_Down_Auto_Scoping_Estimate.xlsx` | Pre-4/29 HubSpot estimate workbook | **STALE — regenerate for Phase 1 NetSuite migration** |
| `Top Down Auto Scope (1).xlsx` | Alternative scope version | **RETIRE — confirm with Cameron** |
| `Top_Down_Auto_ERP_Questions.md` | 22 ERP clarifying questions | Most resolved; cross-check residuals during Stephanie scoping |
| `TopDownAuto_final_estimate.md` | Final delivery tracker | Stub — populate after Phase 1 SOW lands |
| `claude_chat.md` | Old session log | Archive |

---

## Key Decisions

- **2026-05-11 — Phase 1 scope locked verbally:** Legacy Intuitive ERP → NetSuite data migration, user-interview-driven query capture, rationalization vs. 2022 cutover, load via SQL Server staging. Phase 2 (NetSuite CRM) explicitly deferred.
- **2026-05-11 — Discovery method = query capture, not data audit:** Per Alexis, "where do you stop... you'd pull everything and try to find a home for all of it." Capture what users actually run, then rationalize.
- **2026-05-11 — Excluded dataset:** Anything migrated in 2022 NetSuite cutover is out of scope (immutable since 2022).
- **2026-05-11 — Conferencing platform = Teams or Zoom**, not Google Meet (Alexis: Google Meet "give control" feature for query capture is unverified).
- **2026-04-29 — CRM platform pivot:** HubSpot Sales Hub Pro → **NetSuite CRM**. Driver: consolidation around NetSuite as ERP source of truth; HubSpot would have added a third platform to integrate.
- **2026-04-29 — Lane separation (under review):** Originally Genesis owns PIM / Alexis owns server admin / Sayer owns migration + CRM. **Status today:** Ismael (gahh.com) is operating as the parent-co IT lead overseeing migration — not as a Genesis representative. Genesis's current involvement is **ambiguous** and needs clarification before SOW. Open question for Stephanie call.

---

## Standing Context

- **Company:** Top Down Auto — auto-aftermarket group with multiple subsidiaries (Guy Robins, Easy On, Caltran, plus a fourth brand). Parent likely GAHH (per `gahh.com` domain on Ismael's email). Inbound-heavy CSR-driven service motion.
- **Stakeholders:**
  - **Stephanie** — budget holder, SOW signer (likely COO/CFO-equivalent). Hasn't seen 5/11 framing in writing.
  - **Alexis Molina** (amolina@topdownauto.com, HubSpot #483051411148) — Top Down IT/data lead. Champion + technical decision maker. Already standing up the migration infrastructure.
  - **Ismael Cordero** (ismael@gahh.com, HubSpot #479134824122 — *HubSpot has "Ismael Fernando Mata"; reconcile during Stephanie prep*) — parent-co IT lead overseeing migration. Champion + influencer with Stephanie.
  - **Tim Hainey** (Sayer NetSuite engineer) — internal point on NetSuite import spec
  - **Cameron Taggart** (Sayer, deal owner)
  - **Billy Leigh** (Sayer, company owner, deal originator)
- **Tech stack:**
  - NetSuite (ERP, future CRM target)
  - Legacy Intuitive ERP by Aptean — SQL Server 2008 R2, decommission target (security risk per Alexis)
  - SQL Server 2022 Standard on Windows Server 2025 — being stood up by Alexis as staging for migration
  - Fortinet firewall
  - Enable in Central — remote desktop client for Sayer access
  - Magento + WooCommerce ($3-4M/yr e-comm, consolidation 2027-2028)
  - Nextiva phones (replacement targeted but not in scope)
  - Klaviyo (out of scope)
- **No ETL tooling in place** — no Hightouch / Fivetran. Open whether Sayer recommends introducing one.
- **Risk watch:**
  - Stephanie alignment (gating signature)
  - Alexis's infrastructure prep timeline (gating Phase 1 start)
  - Genesis third-party clarification (lane definition for Phase 2)

---

## Cross-Project Pattern (filed in project memory)

Second engagement where a non-Sayer technical actor narrowed Sayer's lane mid-scoping:

- **VestaFreight:** public B2B vendor APIs more mature than baseline assumed; decoupled integration from CRM migration
- **Top Down Auto:** Genesis PIM took over product-data ownership (and the client-side IT bench is more capable than initial scoping assumed — Alexis is running the legacy DB migration himself); Sayer's CRM workstream shrunk and pivoted platforms; Phase 1 now narrowed to data migration audit.

Pattern: Sayer's discovery-driven scope assumes Sayer-built integration; the client's parallel work changes the lane before SOW. Earlier detection ("who else is building toward this outcome already?") shortens scope-pivot cycles. Filed in project memory: [[project_logistics_broker_scoping_pattern]].
