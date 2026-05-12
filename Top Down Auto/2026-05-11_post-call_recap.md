# Top Down Auto — Post-Call Recap (2026-05-11)

> **Purpose:** Source-of-truth handoff from the 5/11 2pm CT scoping call into the Phase 1 SOW + Stephanie scoping pass on 2026-05-12.
> **Fireflies transcript:** `01KRC6JXCKWR5YNRZP6AEYA62Z` — https://app.fireflies.ai/view/01KRC6JXCKWR5YNRZP6AEYA62Z
> **HubSpot note:** 369203261115 (associated to Company 312829746899, Deal 283274309364, Contacts 483051411148 + 479134824122)

---

## Call Metadata

- **Date:** 2026-05-11, 2:00 PM CT
- **Duration:** 47 minutes (planned 60; Ismael had a conflict, recovered into a tight 30-min working session)
- **External attendees:** Alexis Molina (Top Down Auto, IT/data), Ismael Cordero (parent-co IT lead, ismael@gahh.com)
- **Sayer attendees:** Kyle Harbuck, Tim Hainey (NetSuite engineer)
- **Notable absences:** Stephanie (budget holder) — not on the call; alignment owed by Ismael

---

## The One Decision That Matters

**Phase 1 = data migration audit + execution. Phase 2 = NetSuite CRM build (separate SOW).**

Phase 1 is approved verbally by Alexis + Ismael. Stephanie has *not* seen this in writing yet. The SOW Sayer drafts this week is both the deliverable and the trigger for Stephanie's formal sign-off.

---

## Phase 1 — The Silver-Plattered Sequence

Alexis walked the entire approach verbally. Capture verbatim so the SOW does not lose anything in translation:

### Step 1 — Infrastructure prep (CLIENT-OWNED, in flight)
- Windows Server 2025 VM stood up on the ProLiant — *done*
- Stand up SQL Server 2022 Standard
- Import Guy Robins + Easy On Intuitive ERP databases into SQL Server 2022 (Alexis handles the 2008 R2 → 2022 migration)
- Provision Sayer access through the Fortinet firewall to the two legacy Intuitive ERP servers
- Issue Sayer a credential set for "Brian Oni" (god-level user) — Alexis will reset the password
- Sayer logs in via Enable in Central remote desktop client and runs the Intuitive ERP client app as if a regular user

### Step 2 — User interviews + query capture (SAYER-OWNED)
- Schedule 1:1 sessions with each named user
- Sayer screen-shares from the Intuitive client → gives the interviewee control
- Interviewee drives their normal workflows; Sayer captures every query they invoke
- Per Alexis: the "give control" feature works in Teams and Zoom, **unverified in Google Meet** — switch platforms if needed
- One query per workflow, rinse and repeat per user, then move on
- Pull captured queries into SQL Server 2022 (Alexis can grant Sayer SQL access OR Sayer hands queries back and Alexis runs them)

### Step 3 — Rationalization audit (SAYER-OWNED)
- Pull the data sets the captured queries return
- Compare against what's already in NetSuite from the 2022 cutover — **exclude duplicates** (immutable since 2022)
- Apply must-have vs. nice-to-have filter per user role:
  - CSRs: must-have (warranty fulfillment, customer history)
  - Supply chain: rationalize hard — "may want it, but don't really need it" is the discount lane
- Output: the **delta** that needs to land in NetSuite

### Step 4 — Data wrangling + NetSuite load (SAYER-OWNED)
- Stage the rationalized data in SQL Server (Alexis recommends a separate table)
- Determine NetSuite import format (CSV / mapping spec) — **open question for Tim**
- Transform / wrangle in SQL Server (mappings, null handling, field renames)
- Load into NetSuite

---

## Users to Interview (Phase 1 Discovery)

Confirmed during call. Alexis will validate + add as he asks around the divisions.

| User | Brand / Role | Source |
|------|--------------|--------|
| Normal Lopez | Guy Robins CSR | Alexis |
| Liz Sanchez | Guy Robins CSR | Alexis |
| John Oganessian | Guy Robins CSR | Alexis |
| Ronnie Mesa | CSR (used as illustrative example in call) | Alexis |
| Veronica Lopez | CSR | Alexis |
| Kim Ritchey | Easy On CSR | Alexis |
| Heidi Davis | Easy On CSR | Alexis |
| Sabrina Roser | Easy On CSR | Alexis |
| Tim Powell | Supply chain | Alexis |
| John Bath | Supply chain (top of food chain) | Alexis |
| Juliana Laroche | Supply chain (middle) | Alexis |
| Tony Jordan | Distributor / trim-shop historical orders + can identify other power users | Alexis |

**Caltran:** none of their CSRs use Intuitive (confirmed by Alexis + Ismael).
**Robins:** the two newest CSRs aren't worth interviewing ("they're five minutes old and don't know anything").

Reasonable Phase 1 SOW assumption: **12 user interview sessions** at ~45–60 min each. Sayer to add buffer for screen-share/platform setup time.

---

## Phase 1 Open Technical Questions (for SOW assumptions)

1. **NetSuite import format** — what does NetSuite require for bulk load (CSV / specific column structure / SuiteScript / RESTlet)? Tim to answer.
2. **Conferencing platform for query capture** — Google Meet "give control" feature unverified. Default to Teams or Zoom for the interview sessions.
3. **ETL tooling** — Alexis confirmed Top Down has no Hightouch / Fivetran. Open whether Sayer recommends introducing one or stays with hand-rolled SQL→CSV→NetSuite.
4. **SQL access scope** — Sayer pulls queries directly from SQL Server 2022, or hands the query list to Alexis who runs them? Either works; pick one for the SOW.

---

## Risks / Watch Items

- **Stephanie has not seen the framing in writing.** SOW arrives without primer = high risk of "what is this and why does it cost this." Mitigation: Ismael primes her this week; SOW opens with explicit Phase 1 / Phase 2 framing.
- **Client-side infrastructure prep gates Phase 1 start.** If Alexis's VM / SQL / firewall slips, Sayer can't begin interviews. SOW should make Phase 1 kickoff explicitly contingent on access provisioning (with a flag that delays of >2 weeks may require re-quoting).
- **Phase 1 deliverable is fundamentally audit-driven, not "system built."** Sayer is staffing interviews + analysis + a controlled load — billable hours. The deliverable is a working data foundation, not a finished CRM. Frame this carefully in the SOW so Stephanie's expectations match what she's paying for.
- **Phase 2 (NetSuite CRM) is undefined.** Alexis correctly positioned Phase 2 as the value story. Stephanie's inclusions/exclusions for the CRM feature set are still unspecified. Don't price Phase 2 yet — anchor it as "to be scoped post-Phase 1 based on outcomes Stephanie prioritizes."
- **Genesis third-party.** Mentioned by Kyle in passing; STATE.md previously assumed Ismael's organization was Genesis-the-PIM-vendor, but today's call had Ismael acting as Top Down's IT lead, not as a Genesis representative. Clarify before SOW: is Genesis still in the picture? Are they doing PIM, integration, or nothing?

---

## Pricing Anchor (Working Numbers, Not Final)

From STATE.md target + the silver-platter sequence:

- **Phase 1 fixed-fee target:** ~$20K (current deal anchor in HubSpot) — likely realistic given 12 interviews + audit + load. Validate against rate card: 12 × 2 hrs = 24 hrs interview + capture + write-up; +20 hrs rationalization; +30 hrs wrangle + load + QA. ~74 hrs × Sayer blended rate. Sanity-check during scoping.
- **Phase 2 (NetSuite CRM build):** TBD, intentionally not quoted yet.

---

## Decisions Log — 2026-05-11

| # | Decision | Why | Lock state |
|---|----------|-----|------------|
| D1 | Phase 1 = data migration only; Phase 2 = NetSuite CRM separate SOW | Genesis dependency unresolved + CSR processes not mapped; anything Sayer builds now gets refactored. Audit-first earns the right to Phase 2. | **Locked** (verbal, all parties; written in SOW this week) |
| D2 | Discovery method = user-interview-driven query capture, NOT a blanket data audit | Alexis: "where do you stop... you'd pull everything and try to find a home for all of it. How would you ever finish." | **Locked** |
| D3 | Excluded dataset = anything migrated in 2022 NetSuite cutover (immutable since) | Avoid duplicate-migration trap | **Locked** |
| D4 | Rationalization is a deliverable, not an afterthought | Must-have vs. nice-to-have filter applies before load; supply-chain users get pushback on "might-need" data | **Locked** |
| D5 | Sayer chooses conferencing platform for interviews (Teams / Zoom, not Google Meet) | "Give control" feature must work for query capture | **Locked** |
| D6 | Whataburger gift cards owed to Alexis + Ismael | Kyle committed on call | **Personal commitment** |

---

## Next Actions (next 48 hours)

1. **Sayer — Kyle:** Send follow-up email to Alexis + Ismael (drafted today via Superhuman). [Action]
2. **Sayer — Kyle:** Run Stephanie scoping call today (2026-05-12) → generate Phase 1 SOW + Excel estimate + scope summary using this recap as input.
3. **Sayer — Tim:** Confirm NetSuite import format spec for the SOW's load-step assumptions.
4. **Client — Alexis:** Finalize VM / SQL / firewall access. Confirm interview-target list with divisions. Communicate readiness date.
5. **Client — Ismael:** Pre-brief Stephanie on Phase 1 framing this week.
