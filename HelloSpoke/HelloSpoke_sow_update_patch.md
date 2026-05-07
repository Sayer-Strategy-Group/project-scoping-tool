# HelloSpoke — SOW / Proposal Update Patch

> **⚠️ SUPERSEDED 2026-05-05.** This v2 patch was built to incorporate the 4/23 ClickUp integration findings into the 4/24 proposal. On the 5/4 walkthrough call Jeremy asked to redirect the engagement away from the integration build entirely (he built it himself). A v3 patch document supersedes this one — see `HelloSpoke_sow_update_patch_v2.md` (in progress) and the 2026-05-04 entry in `HelloSpoke_decisions.md`. Retained for historical context.

---

**Date:** 2026-04-23
**Author:** Kyle / Sayer
**Purpose:** Four-document sync patch to incorporate the 2026-04-23 ops discovery findings and the ClickUp ↔ HubSpot native integration research. Apply this patch once; all four HelloSpoke client-facing artifacts converge.

## Documents in Scope of This Patch

| Doc | Drive ID | Current State |
|---|---|---|
| `HelloSpoke_HubSpot_CRM_Proposal.md` | `1u8gNE_vlHN0ioIP_tWpQggnGHlvmF_YW` | 10 workstreams · $35,100 median · no ClickUp |
| `HelloSpoke_Scope_Summary.md` | `1a94F3sheVaemIEj3dsnjxMq84O9vuPWj` | 12 workstreams · ClickUp in "Systems Out of Scope" + "Phase 2 Deferred" |
| `Hello Spoke SOW` (authoritative sheet) | `1Kctr6sIfFQY7PzMY-GAHopI7fOdjl_TEgUi8zSjh1uY` | ClickUp-to-HubSpot sync in OUT OF SCOPE |
| `Copy of Hello Spoke SOW` (working copy) | `1JahJZ6tBuii1KyeE_D1SpMUk9NJtZClhwQHq5f-BcFs` | Same state as authoritative |

**Local reference:** `HelloSpoke/HelloSpoke_clickup_workstream.md` (this repo) — contains the three-tier architecture analysis this patch is built from.

---

## 1. Proposal Markdown Patches (`HelloSpoke_HubSpot_CRM_Proposal.md`)

### 1a. Section 2 — Objectives — ADD bullet

Add at the end of the current Objectives list:

> - **Integrate ClickUp for onboarding operations handoff** — replace the PDF-based implementation form with a HubSpot form that captures onboarding data natively, pushes structured task records to ClickUp for the implementation team, and returns task status to HubSpot for sales-team visibility.

### 1b. Section 3 — Scope of Work — ADD Workstream 11

Insert after Workstream 10 (Training & Adoption):

> ### Workstream 11: ClickUp ↔ HubSpot Onboarding Integration
>
> **Customer Story:** HelloSpoke wants the post-sale onboarding handoff to happen without chasing information across systems. Today, sales closes a deal in HubSpot, implementation captures onboarding data via a ClickUp form (output lands as a PDF, frustrating downstream use), and the sales team has no visibility into onboarding status. HelloSpoke wants one capture point, structured data visible to everyone, and sales reps who can see where an onboarding is at without opening ClickUp.
>
> **Recommended Approach:**
>
> - Build a new HubSpot onboarding form replacing the ClickUp form. Form captures onboarding data directly to HubSpot contact, company, and deal properties (up to 15 mapped fields).
> - Stand up the native ClickUp ↔ HubSpot integration end-to-end with both sides of workflow configuration.
> - Configure Make middleware to push HubSpot form submissions into ClickUp as structured tasks with mapped custom fields. (The native integration does not push HubSpot form data into ClickUp custom fields; middleware is required for this path.)
> - Use the native integration for the return path: ClickUp task-status changes update a HubSpot "onboarding phase" deal property so sales reps see progress without leaving HubSpot.
> - Configure two HubSpot workflows: deal-stage → ClickUp task creation trigger, and ClickUp task-status → HubSpot deal-property sync.
> - Run a 1-hour status-list workshop with HelloSpoke ops (Christina, Dalton, Haley) to lock the canonical onboarding status values (candidates: Waiting for Survey → In Configuration → Training Scheduled → Call Forwarding → Complete) with % complete indicators.
> - Build one sales-facing HubSpot dashboard card showing onboarding-phase distribution across open deals.
> - Full test matrix, field-mapping documentation, and 30-day post-launch hypercare.
>
> **Assumptions:**
>
> - ClickUp plan is Unlimited or higher (required for custom fields plus the native integration).
> - HubSpot Sales Hub Professional or higher (already in scope per Workstream 1).
> - Up to 15 custom fields mapped between systems. Overages are change orders.
> - HelloSpoke (Christina, Dalton, Haley) drafts the canonical status list; Sayer facilitates the 1-hour workshop to lock it.
> - Make subscription is set up under HelloSpoke's account (~$10–30/mo based on operation volume). HelloSpoke owns the billing relationship.
> - No HubSpot custom objects in the integration path (the native integration cannot touch them).
> - Sayer is not responsible for fixing or debugging the broken legacy ClickUp ↔ Salesforce integration.
> - 10DLC training flow is decoupled from the standard onboarding status model (per Dalton, 2026-04-23).
> - "Win-property" separate survey flow is not in scope; the standard form handles the 80% case.
> - **Mandatory field gating across sales → implementation → billing handoffs is a separate optional add-on (see Workstream 11a below).** It is process design, not integration, and is priced independently.

### 1c. Section 3 — OPTIONAL add-on

Insert after Workstream 11:

> ### Workstream 11a (Optional): Pipeline Governance — Mandatory Field Gating
>
> **Customer Story:** Jeremy wants required fields enforced at two handoffs (sales → implementation, implementation → billing) so records cannot advance without the data the downstream team needs.
>
> **Recommended Approach:**
>
> - Configure HubSpot deal pipeline required-fields at sales-to-implementation and implementation-to-billing stage transitions.
> - Build workflow-enforced validation so deals blocked at a stage surface the specific missing field to the rep.
> - Build a "stuck deal" HubSpot report for sales leadership showing records blocked at each gate.
> - Document the governance rules in the admin playbook.
>
> **Assumptions:**
>
> - HelloSpoke defines which fields are mandatory at each gate (Sayer facilitates the decision).
> - Up to 10 required fields per gate, 2 gates total.
> - Client-owned governance decision on whether to hard-block or soft-warn.

### 1d. Section 4 — Deliverables & Milestones — ADD bullets

Insert after "Sales team trained (admin, reps, managers) with recorded sessions and SOPs":

> - HubSpot onboarding form live, replacing the ClickUp form
> - ClickUp ↔ HubSpot integration operational with HubSpot form → ClickUp task push and ClickUp status → HubSpot deal property return
> - Sales-facing onboarding phase visibility (deal property + dashboard card)
> - Canonical status list workshopped and documented

Update `**Timeline:** 12-16 weeks` — no change. ClickUp workstream fits inside existing phase structure (Phase 3 Integration & Quoting Build, Wk 5–11).

### 1e. Section 5 — Engagement Model & Pricing — UPDATE totals

Replace the pricing block with:

> **Model:** Fixed Fee
>
> **Total Cost (Full Scope, Workstreams 1–11):** $39,900
> *(Workstreams 1–10: $35,100 + Workstream 11 ClickUp integration at $4,800 median)*
>
> **Optional Add-On — Workstream 11a Pipeline Governance:** $1,650 (+/- $450)
>
> **Project Timeline:** 12-16 weeks (unchanged — ClickUp work nests inside Phase 3)
>
> **Payment Terms:**
>
> - Equal monthly payments of $9,975 over 4 months (base scope)
> - Net-15 terms on all invoices
> - Add-on invoiced separately upon client selection
>
> **Technology & Administrative Fee:** 5% applied to each invoice (unchanged policy).

---

## 2. Scope Summary Patches (`HelloSpoke_Scope_Summary.md`)

### 2a. Systems in Scope — ADD bullet

Add to the "Systems in Scope" list:

> - **ClickUp** — Operations task management; native integration + HubSpot form-driven task creation for the implementation team handoff

### 2b. Systems Out of Scope — REMOVE bullet

Delete this line:

> ~~- **ClickUp** -- Short-term visibility tool; deferred to Phase 2 if needed~~

### 2c. Estimate Summary — UPDATE table

Replace with:

> | Metric | Low | Median | High |
> |--------|-----|--------|------|
> | Total Hours | 190 | 266 | 360 |
> | Rate | $150/hr | $150/hr | $150/hr |
> | Investment | $28,500 | $39,900 | $54,000 |

### 2d. Workstream Breakdown — ADD row

Insert as row 12 (PM becomes row 13):

> | 12 | ClickUp ↔ HubSpot Onboarding Integration | 28 | 32 | 36 | Tier B architecture — HubSpot form + Make middleware + native integration |

Update row numbering on PM to 13, adjust total row:

> | | **TOTAL** | **190** | **266** | **360** | |

### 2e. Risk Register — ADD rows

Insert as rows 11–13:

> | 11 | **ClickUp native integration limitations** — marketplace rating 2.0/5, no HubSpot custom object support, custom-field mapping only one direction | Medium | High | Workarounds add hours; some edge cases require middleware | Middleware (Make) scoped from day 1; document known limitations in SOW | Sayer |
> | 12 | **ClickUp HubSpot Integration 2.0 on roadmap but unscheduled** | Low | Low | Minor rework if breaking change ships mid-delivery | Do not scope against unreleased features; revisit if released during delivery | Sayer |
> | 13 | **Status list drafting dependency** — HelloSpoke ops (Christina/Dalton/Haley) must draft canonical status list before integration build | Medium | High | 2-4 hr delivery delay if status list arrives late | Status-list workshop included in kickoff; client commits to draft before build | HelloSpoke |

### 2f. Assumptions — ADD items

Append to numbered assumptions list:

> 12. ClickUp Unlimited plan or higher (required for custom fields + native integration)
> 13. Up to 15 custom fields mapped between ClickUp and HubSpot in the onboarding form flow
> 14. Make subscription (~$10–30/mo) set up under HelloSpoke's account; HelloSpoke owns the billing relationship
> 15. Canonical onboarding status list drafted by HelloSpoke before integration build (Sayer facilitates workshop)

### 2g. Outstanding Items Needed from Client — ADD bullets

Append:

> 8. **HelloSpoke ops (Christina/Dalton/Haley):** Draft canonical onboarding status list + % complete indicators before integration kickoff
> 9. **Sara Hines:** Share sales-stage definitions with Jeremy and Christina (committed 2026-04-23)
> 10. **Dalton Palmer:** Provide ClickUp implementation form link for reference during form redesign

### 2h. Phase 2 Deferred — REMOVE bullet

Delete this line:

> ~~- ClickUp-to-HubSpot implementation status sync~~

---

## 3. Hello Spoke SOW (Authoritative Sheet) Patches

Source: `https://docs.google.com/spreadsheets/d/1Kctr6sIfFQY7PzMY-GAHopI7fOdjl_TEgUi8zSjh1uY`

### 3a. Phase/Workstream Matrix — ADD row in Phase 3

Insert after the "QuotaPath Coordination" row, still within Phase 3:

| Phase | Workstream | Description | Notes / Assumptions |
|---|---|---|---|
| *(Phase 3 — continued)* | ClickUp ↔ HubSpot Onboarding Integration | HubSpot form replaces ClickUp form; Make middleware pushes submissions to ClickUp custom fields; native integration returns task status to HubSpot deal property | Tier B architecture; up to 15 mapped fields; status list workshop included |

### 3b. Phase 3 Requirements — ADD IDs

Add to Phase 3 Requirements section (after CPQ-08, continuing numbering under new prefix `CLK-`):

| Phase | Req ID | Requirement | Category |
|---|---|---|---|
| Phase 3 | CLK-01 | HubSpot onboarding form built and published, replacing the ClickUp form | Form |
| Phase 3 | CLK-02 | Up to 15 HubSpot custom properties configured for onboarding data capture | Form |
| Phase 3 | CLK-03 | Make middleware connected to HubSpot + ClickUp with credentials vaulted | Middleware |
| Phase 3 | CLK-04 | Form-submission-to-ClickUp-task mapping configured for all 15 fields with type coercion and error handling | Middleware |
| Phase 3 | CLK-05 | Native ClickUp ↔ HubSpot integration installed, authorized, and object sync toggles configured | Integration |
| Phase 3 | CLK-06 | HubSpot workflow: deal-stage trigger → ClickUp task creation | Workflow |
| Phase 3 | CLK-07 | ClickUp automation: task-status change → HubSpot deal "onboarding phase" property update | Workflow |
| Phase 3 | CLK-08 | Status-list workshop conducted; canonical values + % complete indicators locked | Governance |
| Phase 3 | CLK-09 | Sales-facing HubSpot dashboard card for onboarding-phase distribution live | Reporting |
| Phase 3 | CLK-10 | End-to-end test matrix executed; known-limitation workarounds documented | Validation |

### 3c. Phase 3 Success Criteria — ADD bullets

Append to Phase 3 Success Criteria:

> 8. HubSpot form captures onboarding data natively; ClickUp form retired
> 9. Sales reps can see onboarding phase on every deal without opening ClickUp
> 10. Canonical onboarding status list documented and in production

### 3d. Risk Register — ADD rows

Add rows 13–15 (continuing the 12-row register):

| # | Risk | Severity | Likelihood | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| 13 | ClickUp native integration limitations | Medium | High | Workarounds add hours; edge cases require middleware | Middleware scoped from day 1; known-limitation catalog in SOW | Sayer | Open |
| 14 | ClickUp Integration 2.0 unscheduled | Low | Low | Minor rework if breaking change ships mid-delivery | Do not scope against unreleased features | Sayer | Open |
| 15 | Status list drafting dependency on HelloSpoke ops | Medium | High | 2-4 hr delivery delay if late | Status-list workshop in kickoff; client commits to draft before build | HelloSpoke | Open |

### 3e. SCOPE ASSUMPTIONS — ADD lines

Append:

- ClickUp Unlimited plan or higher (required for custom fields + native integration)
- Up to 15 custom fields mapped between ClickUp and HubSpot for onboarding form flow
- Make subscription set up under HelloSpoke's account (~$10–30/mo); HelloSpoke owns the billing relationship
- Canonical onboarding status list drafted by HelloSpoke before integration build

### 3f. OUT OF SCOPE — REMOVE line

Delete this line:

> ~~- ClickUp-to-HubSpot sync~~

### 3g. CLIENT RESPONSIBILITIES — ADD lines

Append:

- Christina / Dalton / Haley: Draft canonical onboarding status list + % complete indicators before integration build
- Sara Hines: Share sales-stage definitions with implementation team (committed 2026-04-23)
- Dalton Palmer: Provide ClickUp implementation form link for reference during form redesign
- Approve Make subscription setup under HelloSpoke billing account

### 3h. OPEN ITEMS — ADD lines

Append:

- Jeremy Wiley: Confirm in/out on the mandatory field gating add-on (Workstream 11a)
- Jeremy Wiley: Confirm Win-property separate survey flow is out of scope (standard flow handles 80/20)
- Confirm ClickUp plan tier is Unlimited or higher

---

## 4. Copy of Hello Spoke SOW (Working Copy) Patches

Source: `https://docs.google.com/spreadsheets/d/1JahJZ6tBuii1KyeE_D1SpMUk9NJtZClhwQHq5f-BcFs`

**Apply identical patches as section 3 above** (the two sheets differ only in that the working copy lacks the Actual Hours / Actual Cost / Variance columns — content patches are the same).

---

## 5. Optional — Field Gating Add-On Patches

Only apply if Jeremy confirms Workstream 11a is IN.

### 5a. Proposal markdown — already covered in 1c above

### 5b. SOW sheet — ADD row to Phase/Workstream matrix

| Phase | Workstream | Description | Notes / Assumptions |
|---|---|---|---|
| Phase 4 | Pipeline Governance — Mandatory Field Gating (Optional Add-On) | Required fields enforced at sales → impl and impl → billing handoffs; workflow validation; stuck-deal report for leadership | Client-owned governance rules; up to 10 required fields per gate; 2 gates |

### 5c. SOW sheet — ADD requirements

| Phase | Req ID | Requirement | Category |
|---|---|---|---|
| Phase 4 | GOV-01 | Required fields configured at sales → impl stage transition | Governance |
| Phase 4 | GOV-02 | Required fields configured at impl → billing stage transition | Governance |
| Phase 4 | GOV-03 | Workflow validation surfaces missing field to the rep on advance attempt | Governance |
| Phase 4 | GOV-04 | Stuck-deal HubSpot report live for sales leadership | Reporting |
| Phase 4 | GOV-05 | Governance rules documented in admin playbook | Documentation |

### 5d. Pricing — UPDATE if add-on selected

> **Total Cost (Full Scope + Governance Add-On):** $41,550
> *(Base $39,900 + Governance $1,650)*
>
> **Monthly payment:** $10,388 over 4 months
>
> Or invoice the add-on separately upon selection (client preference).

---

## Summary of Numbers

| Config | Hours (median) | Investment (median) |
|---|---|---|
| Original (before today) | 234 | $35,100 |
| **Recommended update (Tier B, base only)** | **266** | **$39,900** |
| With Field Gating Add-On (Workstream 11a) | 277 | $41,550 |
| If client picks Tier A (native only + form audit, no HubSpot form replacement) | 255 | $38,250 |
| If client picks Tier C (n8n middleware) | 278 | $41,700 |

**Net change from pre-patch baseline (Tier B recommended):** +$4,800 / +32 hours.

---

## Application Order

1. **Proposal markdown** (`HelloSpoke_HubSpot_CRM_Proposal.md`) first — it's client-facing narrative and sets the tone.
2. **Scope summary** (`HelloSpoke_Scope_Summary.md`) second — keeps the narrative and the estimate summary aligned.
3. **Authoritative SOW sheet** third — lands the formal requirements + risk register + assumptions.
4. **Working copy SOW** last — mirror of authoritative.

After all four are synced, delete or archive `HelloSpoke_clickup_workstream.md` (local addendum) since the content is now merged into the client-facing artifacts.

---

## Brand Guideline Notes

Sayer Brand Guide specs ([Drive link](https://docs.google.com/document/d/1z_c615tZvLyT-Y_h49evrLYIUzHFh2E7lPPsCxCc7og)):
- **Colors** (for any charts/section headers on Gamma/PDF versions): Yellow `#FEC700`, Grey 700 `#2E2E2E`, Black `#000000`
- **Headline font:** Rethink Sans Semibold
- **Body font:** Rethink Sans Regular
- **Positioning line** (if used): "Drive growth, unlock potential."

For this text-only patch, the only brand-compliance concerns are tone (direct, candid, no hedging) and correct naming ("Sayer" not any legacy brand). Both applied above.
