---
layer: Org
owner: team
created_at: 2026-07-06
access_level: internal
name: draft-csa-sow
description: >
  Draft a Sayer Consulting Services Agreement (CSA) and Statement of Work (SOW)
  for a client engagement. Starts with a mandatory interview to collect every
  Sayer-side input (pricing model, rate card staffing, timeline, expense
  handling, out-of-scope items) before any document is generated, so
  clarifications happen before drafting instead of as placeholders after.
  Use when the user asks to draft a CSA, draft a SOW, put together a contract,
  or prepare a T&M/fixed-fee agreement for a client.
  Trigger: "draft a CSA for [Client]", "draft a SOW for [Client]", "put
  together a contract for [Client]", "we need an agreement for [Client]"
argument-hint: "[ClientName]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob, mcp__claude_ai_Google_Drive__*
---

# Draft CSA / SOW Skill

Draft a client-ready Consulting Services Agreement and Statement of Work, front-loading every Sayer-side decision into one interview instead of leaving placeholders to chase down after the documents exist.

This skill exists because of a real failure mode: drafting from local precedent files in old client folders (NAKS, GSS Supply, Strive, etc.) instead of the canonical master template. Those files had drifted — an abandoned "Exhibit B" reference, the wrong legal entity name (`BHS Consulting LLC, dba Sayer` instead of `Sayer Strategy Group`), and an inconsistent "LITE" single-phase SOW format — and every one of those had to be caught and corrected after the fact. Always draft from the canonical source below, never from another client's old draft.

## Preflight

- **Work from the project-scoping-tool repo.** Confirm `calibration/` and `templates/` exist in the current directory. If not, tell the user to `cd` into their clone first.
- **Verify the repo is current before drafting.** Run `git fetch origin` and check whether the checked-out branch (or `main`, if not on it) is behind `origin/main`. If behind, fast-forward `main` (only if `main` is not the checked-out branch with uncommitted changes — never discard someone else's in-progress work to do this). Report the finding either way ("repo is current" or "N commits behind, fast-forwarded" or "couldn't safely sync, here's why").
- **Canonical master template:** Google Doc, fileId `19c49b94uvnYf99oEeIMmaCG3ulsld0Mj0rfHC1BvkG4`. **Always re-fetch this fresh** via `mcp__claude_ai_Google_Drive__read_file_content` at the start of every CSA/SOW drafting task — do not rely on any local `.md` copy, including this repo's `templates/Consulting Services Agreement CSA.md`, which can drift out of sync with the live doc (this happened in 2026-07). The doc contains both the master CSA (Articles I–VIII) and, further down, a `#SOW Instructions` block with a fill-in checklist and an illustrative example SOW — read both.
- **Rate card:** current hourly rates live in the `sayer-rates` skill, but that file itself is a cached copy of the **Sayer Proposal Playbook (Notion)** — treat the skill as a fallback, not gospel. If the user states rates that differ from the skill, use the user's stated rates for this engagement and flag the discrepancy back to them rather than silently overriding either source.

## Input Handling

**Parse `$ARGUMENTS` as the client name.** If empty, ask for it.

## Step 1: Grill-Me Interview (mandatory, before drafting)

Invoke the `grill-me` skill (or run an equivalent one-question-at-a-time interview if unavailable) to resolve every item below. Provide a recommended answer for each question, sourced from precedent where possible. Do not proceed to drafting until every applicable item is resolved or explicitly deferred by the user.

1. **Pricing model.** Fixed Fee or Time & Materials? (If T&M, all remaining questions below apply. If Fixed Fee, skip to the fee/payment-structure questions in the master template's Cohesion example.)
2. **Staffing / rate card.** Who is staffed on this engagement, and at what tier/rate? Get names and rates explicitly — do not assume from another engagement's staffing.
3. **Estimate disclosure.** Should the SOW show an hour/dollar estimate at all? Three options exist — ask which:
   - **Per-phase range** (hours × rate per phase, shown) — most transparent, matches most T&M precedent.
   - **No estimate at all** — pure rate card, actual hours billed and totaled at completion. Valid when scope/duration is genuinely unknown upfront (used for NEC's Houston discovery trip, 2026-07).
   - **Committed / hours-hidden** — a single all-in dollar figure with no hours shown, for buyers who'd anchor on an hourly breakdown (e.g., a CPA). Rare; only when the user asks for it.
4. **Timeline.** Key dates — kickoff, on-site visits, phase boundaries. Get exact dates, not "TBD."
5. **Scope phases.** What are the actual phases of work? Default to a **full, multi-phase structure** (see Step 3) — do not default to a single-lump "lite" format unless the user explicitly asks for a lighter document.
6. **Out of scope.** What should be explicitly excluded and deferred to a future SOW? (Common case: a discovery/process-review phase excludes the full implementation it's scoping.)
7. **Expense handling.** Standard language is: pre-approved, billed at cost with no markup, receipts required, no numeric caps (matches every precedent checked — Sayer's actual guidelines don't specify booking-class or per-diem limits). If the engagement is travel-heavy, confirm this is still the desired framing rather than assuming; if the user wants real caps, get the actual numbers — don't invent them.
8. **Client identity fields (legal name, address, signer).** Default: **leave these blank** for the client to complete at signing (this is the actual convention — do not chase down the client's exact legal entity name from the user; it's not a Sayer-side input).

## Step 2: Draft the CSA

- Copy the master template's Articles I–VIII verbatim from the freshly-fetched Google Doc. Do not alter the legal boilerplate.
- Client-identity fields (name, address, signer) stay as plain blank lines (`_______________`), matching the master template's own convention — not bracketed placeholder notes.
- Entity name is **Sayer Strategy Group** (LLC) throughout — this is current as of the live master doc; do not use `BHS Consulting LLC, dba Sayer` from older precedent files.

## Step 3: Draft the SOW

Follow the canonical section order (this matches the master doc's `#SOW Instructions` checklist — the single source of truth for section order; re-fetch it fresh per the Preflight):

1. Masthead / metadata (Client, Prepared by, Start Date, SOW Date)
2. Executive Summary
3. Objectives
4. Scope of Work — **organized into named phases** (Phase 1, Phase 2, ...), each phase containing one or more workstreams with Customer Story / Recommended Approach / Assumptions. Default to full multi-phase detail; only collapse to a single phase if the user asked for a lighter document in Step 1.
5. Out of Scope (explicit, names what's deferred and to where)
6. Deliverables & Milestones
7. Engagement Model & Pricing — pricing model, rate card, estimate disclosure per the Step 1 answer, invoicing cadence + Net terms stated explicitly, tech/admin fee, expense clause
8. Project Governance
9. Assumptions & Constraints
10. Working Agreement — copy verbatim from the master doc's current wording
11. Payment Terms — copy verbatim from the master doc's current wording (billing contact block, late-fee terms, 7-day price-validity clause, etc.)
12. Signature block (Client fields blank; Sayer fields per Step 1 staffing)

**Update all section numbers sequentially** — the master doc's own example has an off-by-one numbering artifact; don't copy it literally, just keep your document's numbers internally consistent.

## Step 4: Generate Branded Docx

1. Invoke `sayer-brand-guidelines`, then the `docx` skill, before generating any file.
2. Write a `build_docx.js` in the client's folder (or reuse/adapt an existing one, e.g. from a prior client folder — the converter logic is generic markdown-to-branded-docx and doesn't need to be rewritten from scratch each time). Output both `{Client}_CSA_draft.docx` and `{Client}_SOW_draft.docx`.
3. Verify the output: `validate.py` may not run on this machine (Python version gap) — fall back to a zip/XML integrity check (`zipfile.testzip()` + `defusedxml.ElementTree.fromstring()` on `word/document.xml` — use `defusedxml`, not stdlib `xml.etree`, even though these are self-generated files) and confirm no unintended `[FILL]`/placeholder text survived into fields that should be resolved.

## Step 5: Decisions Log

Write or append to `{Client}_decisions.md` in the client folder: every pricing/scope/entity decision made in Step 1, plus any open items still needing the user's confirmation.

## Step 6: Summary + Approval Routing

Report what was drafted and remind the user: **the master template's standing instruction is that all SOWs go to Billy Leigh & Greg Dyer for approval before being sent to the client for signature.** Do not imply the documents are ready to send until that approval has happened.

## Error Handling

- If the Google Drive fetch of the canonical master doc fails, do not silently fall back to a local precedent file — report the failure and ask the user for the doc link or to paste the current text.
- If the user's stated rates differ from the `sayer-rates` skill, use the user's rates for this document but flag the discrepancy explicitly rather than resolving it unilaterally.
