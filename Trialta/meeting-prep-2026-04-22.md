# Trialta — Discovery Call Meeting Prep
**Date:** 2026-04-22 | **Prepared by:** Claude
**Call type:** Data Discovery — pipeline decisions, contact structure, Phase 1 status check
**Project position:** Week 3, Day 2 — Phase 2 (Data Migration & Pipeline) started yesterday

---

## Fireflies Note
The Fireflies API key is stored in macOS Keychain, which is unavailable in this Linux session. This prep is built from all available source material: the GTM Assessment (full discovery synthesis), kickoff call transcript + summary (Apr 7), plan.json, kickoff deck, and the data discovery template sent to the team.

---

## What We Already Know — Don't Re-Ask This

### Their Business (from GTM Assessment)
- **Transaction Services (TS):** FDD and QoE for PE firms, bankers, and occasionally corporate acquirers. Deals are fast-moving, data-messy, senior-operator-led.
- **CFO/F&A:** Project-based and interim support — close acceleration, post-close integration, audit prep, technical accounting. New service line, Courtney is the primary voice.
- **Revenue model:** 100% referral/relationship dependent. No outbound, no CRM, no nurture. The firm wins when someone remembers them and loses when they don't.
- **The key quote (Sam Rogers):** *"I feel very confident getting from 1 to 5. The trick is getting from 0 to 1 with a client you actually want."*

### Their Data (from Kickoff)
- **Contact lists:** Distributed across personal spreadsheets and Outlook contacts. Austin, Sam, Blake each have their own.
- **Historical opportunities:** Sam confirmed they have a "pretty good database of historical opportunities, not just actual projects but all our opportunities" — can double as master client list.
- **Volume estimate:** ~500–1,000 contacts (3 lists, known dedup risk).
- **Sam owns the most complete deal history. Austin likely owns the most complete contact list.**
- **No PSA tool yet** (BigTime implementation in progress — may have some overlap with HubSpot contact tracking).

### The Sell-Side / Buy-Side Nuance (critical for pipeline design)
- **Buy-side:** PE sponsor brings the deal. The fund is both client and referral source. The portco CFO is day-to-day.
- **Sell-side:** Banker introduces a founder (the actual buyer). The banker is a referral partner, NOT a client. Marketing and CRM treatment must differ — bankers get a separate outreach motion, founders are the deal contacts.
- **Sam's exact words:** "Our marketing efforts on sell-side need to be focused on referral sources, not the direct client."
- **Austin floated** a different split: TS/QoE vs. CFO/F&A as the pipeline differentiator (not buy-side vs. sell-side). This wasn't resolved.

### Their Team & Stack
| Person | Role | HubSpot user? | Notes |
|--------|------|----------------|-------|
| Austin Dragoun | Primary POC, partner | Yes | CRM champion, somewhat AI-cautious |
| Sam Rogers | Partner | Yes | Collateral POC, has historical deal data |
| Blake | Partner | Yes | Was on beach for kickoff |
| 4th user (TBD) | Possible new hire? | Pending | Sam mentioned "hopefully 4 soon" |
| Courtney | CFO/F&A lead | Unknown | LinkedIn voice, mentioned in GTM Assessment |

- **Email:** Office 365 / Outlook
- **Meetings:** Microsoft Teams
- **Time tracking:** Harvest
- **PSA:** BigTime (implementing — may overlap with HubSpot)
- **AI:** Claude Teams (using it for call summaries and sales agendas; Austin described it as "getting there but not very helpful yet for domain-specific work")

### What the GTM Assessment Already Established
- **Key banker outreach failure pattern:** "We didn't follow up with Lincoln." / "We reached out 6 months ago and never followed up." / "Bankers won't remember us unless we're in front of them constantly."
- **Top growth levers identified:** (1) deepening wallet share with existing PE funds — they serve 6–7 portcos at funds with 20+, (2) systematic banker outreach, (3) CFO/F&A cross-sell into existing TS accounts.
- **PE relationship health:** This is the highest-value use case for the CRM — knowing which PE sponsors have gone cold. Austin's target: be able to ask "which PE firms haven't we talked to in 90 days."
- **Pricing sensitivity:** Most common objection is cost. "Small firm = cheaper" perception. Collateral and website don't support premium positioning.

---

## The Big Decisions Still Open

These were discussed in kickoff but NOT resolved. Today's call needs to close them.

### Decision 1: Pipeline Structure — 1 or 2?
**What we know:** Kyle recommended 1 pipeline to reduce complexity. Austin floated TS/QoE vs. CFO/F&A as a possible split. Sam said the key sell-side difference is the referral source (banker), not the deal type.

**Recommendation to lead with:** 2 pipelines — but NOT buy-side/sell-side. Instead: **TS/Transaction Services** and **CFO/F&A**. These have genuinely different motions:
- TS deals are project-based, time-boxed, driven by deal events, banker-introduced or PE-driven
- CFO/F&A engagements are longer-term, recurring, often cross-sold from TS relationships
- Reporting will need to separate these — PE sponsor deal velocity looks very different from CFO/F&A retention metrics

Handle the banker referral source distinction within deal properties and contact roles, NOT a separate pipeline. That's a contact type + deal property problem.

**Question to confirm:** "Austin, when you mentioned TS/QoE vs. CFO as a possible split — is that what you're thinking? Or are you open to keeping one and using deal type as a property field?"

### Decision 2: Contact Role Taxonomy
Five contact types need to be defined and confirmed. We need Trialta's names for them, not ours.

| Role | What it is | HubSpot treatment |
|------|-----------|-------------------|
| Direct client / buyer | PE fund partner, founder, CFO bringing them work | Deal contact, primary |
| Referral source / Banker | Investment banker who introduces sell-side deals | DO NOT cold-email. Tag separately. Marketing cadence differs. |
| PE sponsor / fund | PE firm at fund level (parent company) | Parent company record; PE health tracking view |
| PortCo executive | CFO or controller at a portfolio company | Associated with PE parent; potential CFO/F&A cross-sell |
| Internal team | Austin, Sam, Blake | Internal users — exclude from marketing |

**Question to confirm:** "For each deal, who do you typically track? Let's walk through a recent buy-side deal and a recent sell-side deal and name the people you'd want to see in HubSpot attached to that deal."

### Decision 3: Pipeline Stage Definitions
The data discovery template was sent but we don't have their responses. Need to get these verbally:

**For TS deals:**
- What stage does a deal enter when you first hear about it?
- What moves it from "interested" to "proposal sent"?
- What's the stage between proposal and active work?
- Do you track "won" and "lost" separately, or just "closed"?

**For CFO/F&A engagements:**
- Are these scoped like TS deals, or are they more ongoing retainer-type?
- How long is the typical cycle from intro to signed engagement?

---

## Phase 1 Status Check — Do This First

Phase 1 ended April 18 (4 days ago). We're now in Phase 2. But STATE.md flagged that no session work had happened since kickoff. **Assume nothing is confirmed done until they say so.**

Work through this checklist verbally:

| Phase 1 Deliverable | Status to confirm |
|--------------------|-------------------|
| HubSpot portal configured, Trialta branding | Done? |
| Custom contact/company properties built (up to 20) | Done? Which ones? |
| PE firm parent-child associations configured | Done? |
| Segmentation views (PE vs. sell-side vs. portco) built | Done? |
| Outlook integration live for Austin | Done? Any issues? |
| Outlook integration live for Sam | Done? Any issues? |
| Outlook integration live for Blake | Done? Reachable? |
| Data import template sent to team | Done (we sent it) |
| Data import template returned by team | **CRITICAL — see below** |

---

## The Critical Risk: Data Submission

**The R-3 risk from the scope:** Client must submit raw data files by end of Week 2 (April 18) or migration timeline slips.

**This is now due. We need to know if it's been delivered.**

Ask directly: "Did you get a chance to send over the contact exports and historical opportunities list? We're starting migration work this week and the data is the input."

**If data has NOT been submitted:**
- Don't panic. Pull forward Phase 2 pipeline configuration work (CRM-09 through CRM-16 don't require data).
- Set a hard new deadline: by April 25 (end of this week).
- Offer a 30-min session to walk them through the Outlook export — the instructions were sent but it's "hidden in a weird way" per Kyle's kickoff comment.
- Prioritize: historical opportunities list from Sam first (existing clients / deal history), then Outlook contacts.

**If data HAS been submitted:**
- Get confirmation of what was sent and where.
- Audit scope: how many records, how many sheets, what's the format?

---

## What to Accomplish in This Call

**Priority order:**

1. **Phase 1 status** — Is it actually done? What's blocked?
2. **Data submission** — Do we have the files? Are we unblocked for migration?
3. **Pipeline decision** — TS/CFO split or single? Need answer to configure Phase 2.
4. **Contact role taxonomy** — Walk through a real deal, map the people.
5. **Pipeline stages** — Get the stage names from them (buy-side/TS first, then CFO/F&A).
6. **HubSpot license status** — 3 or 4 users? Who is the 4th?
7. **Quick wins** — "If HubSpot could show you one thing tomorrow, what would it be?" (Austin said 90-day PE outreach visibility.)

---

## Questions to Ask — Organized by Topic

### Phase 1 & Outlook
- "How's Outlook feeling? Is email and calendar syncing for all three of you, or did anyone hit a snag?"
- "Is Blake now up and running? He was traveling at kickoff."
- "Have you been logging into HubSpot at all this week? What's your first impression of the setup?"

### Data
- "Did you get a chance to send over the spreadsheets? We need those to kick off migration this week."
- [If yes] "Can you walk me through what you sent — formats, how many sheets, roughly how many contacts?"
- [If no] "No worries — let's get that done. Can you commit to getting us the Outlook export and Sam's opportunities list by Friday? I can jump on a quick call to walk you through the export if that helps."
- "Sam — do you have that historical opportunities spreadsheet in a format you could share easily? That's the one we want to use as the master client list baseline."

### Pipeline & Deal Structure
- "Before we build the pipelines, I want to make sure we get this right. Austin, you mentioned TS/QoE vs. CFO as a possible split — is that the direction you want to go, or would you rather keep it as one unified pipeline with a deal type field?"
- "For a typical TS deal — walk me through what stages it goes through from when you first hear about it to when you close the engagement letter. What would you call those stages?"
- "For CFO/F&A — is that a different rhythm? Longer cycle? More of a retainer? How do you know when an opportunity has converted?"

### Contact Roles & Relationships
- "Let's walk through a recent deal. Pick one — buy-side or sell-side. Who are the people you'd want to see in HubSpot attached to that deal, and what's their role?"
- "For bankers who send you sell-side work — do you want to track them as contacts on the deal, or in a separate banker outreach view? Or both?"
- "Are there people in your world you explicitly do NOT want cold-emailed or put into any outreach — existing clients, close relationships, club contacts?"

### HubSpot Licenses & Users
- "Where are we on licenses — still 3 users, or did you get to 4?"
- [If 4] "Who's the 4th — a new hire, or Courtney getting added for CFO/F&A?"

### Quick Wins
- "If HubSpot could show you one thing as of this Friday, what would it be? I want to make sure that's on the build list for this week."

---

## Things NOT to Re-Cover (Already Settled in Kickoff)

- Whether to use HubSpot — done, they're in.
- Whether to integrate Outlook — done, planned for Phase 1.
- Scope of the engagement (CRM only, not GTM phases 2–4) — documented in contract.
- Scope creep risk (collateral, website, demand gen) — excluded and documented.
- The fact that Austin uses Claude Teams — don't re-pitch AI; they know.

---

## Watch For in This Call

**Scope creep signals:**
- Any mention of marketing automation, sequences, or "automatic emails to bankers"
- Requests to build LinkedIn integrations or BigTime integrations
- Collateral or website work surfacing — Sam mentioned in kickoff that the website matters for premium positioning; don't let this drift into scope
- The Weston/Billy AI system ("Ava") — they may want to discuss this; it's out of scope

**Adoption risk signals:**
- If Outlook integration isn't set up yet, that's the canary — if they haven't done the easy thing, migration data submission is also at risk
- If Austin or Sam say "we haven't really logged into HubSpot yet" — flag this directly; Phase 2 data QA requires them to be in the system

**Timeline risk:**
- If data wasn't submitted, Phase 2 migration (MIG-03 through MIG-08) slips and compresses QA + pipeline work into weeks 4–5
- If pipeline decision isn't made today, pipeline configuration (CRM-11 through CRM-16) can't start
- The hard deadline is May 15 (6 weeks from kickoff). With data delays, that becomes very tight.

---

## After the Call — Immediate To-Dos

- [ ] Log pipeline decision in decisions.md
- [ ] Document agreed contact role taxonomy
- [ ] Document pipeline stage definitions (both pipelines)
- [ ] If data received: begin MIG-03 (contact dedup and cleanup)
- [ ] If data not received: pull forward CRM-11 (pipeline configuration) and set hard deadline April 25
- [ ] Update STATE.md with Phase 1 status and Phase 2 blockers
- [ ] Send recap email to Austin confirming decisions and any outstanding items
