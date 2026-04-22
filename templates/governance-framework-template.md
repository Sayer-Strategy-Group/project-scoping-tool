# {Client Name} -- Project Governance Framework

**Effective:** {Start Date}
**Project:** {Project Type} Implementation
**Duration:** {Timeline}

---

## Working Agreement

This document establishes how Sayer and {Client Name} will work together during the engagement. It covers communication, decision-making, scope management, and escalation -- so everyone knows the rules before we start building.

---

## Team & Roles

| Role | Name | Responsibilities |
|------|------|------------------|
| **Project Lead** (Sayer) | | Day-to-day execution, technical decisions, configuration |
| **Project Manager** (Sayer) | | Timeline, resource coordination, status reporting |
| **Account Manager** (Sayer) | | Relationship, commercial decisions, escalation |
| **Project Sponsor** ({Client}) | | Budget authority, strategic decisions, executive escalation |
| **Day-to-Day Contact** ({Client}) | | Requirements clarification, data access, internal coordination |
| **End Users** ({Client}) | | UAT participation, feedback, adoption |

---

## Communication Plan

| Channel | Cadence | Purpose | Attendees |
|---------|---------|---------|-----------|
| Weekly standup | {Day} {Time} {TZ} | Progress, blockers, decisions | Project lead + PM + client day-to-day |
| Phase review | End of each phase | Sign-off, demo, retrospective | Full team |
| Ad-hoc Slack/email | As needed | Day-to-day questions | Anyone |
| Escalation call | As needed | Blockers > 48hrs unresolved | PM + Sponsor |

**Response time expectations:**
- Sayer responds to client questions within 1 business day
- Client responds to data/access requests within 2 business days
- Blockers flagged same-day via Slack or email

---

## Decision-Making

| Decision Type | Who Decides | Examples |
|--------------|-------------|---------|
| **Technical** | Sayer Project Lead | Property naming, workflow logic, integration approach |
| **Business logic** | Client Day-to-Day | Stage definitions, field values, process rules |
| **Scope changes** | Joint (PM + Sponsor) | New workstreams, timeline shifts, budget impact |
| **Commercial** | Sayer Account Manager + Client Sponsor | Change orders, additional phases, pricing |

**Decision log:** All significant decisions are captured in `{Client}_decisions.md` during the engagement.

---

## Scope Management

**What's in scope:** As defined in the signed proposal/SOW.

**Change request process:**
1. Either party identifies a potential change
2. Sayer documents the change: what, why, hour/cost impact
3. Client sponsor approves or declines
4. If approved, Sayer updates plan.json and timeline
5. Change is logged in decisions file

**Scope creep signals:** Sayer will proactively flag when requests are trending outside the original SOW. Common triggers:
- "Can we also..." during working sessions
- New integrations or data sources not in discovery
- Additional user roles or permission structures
- Reporting requests beyond the agreed count

---

## Data & Access Requirements

| Item | Owner | Due By | Status |
|------|-------|--------|--------|
| HubSpot admin access | Client | Kickoff | |
| Data exports (contacts, deals) | Client | End of Week 1 | |
| Integration credentials | Client | Before integration phase | |
| Test accounts for UAT | Client | Before UAT phase | |

**Data quality responsibility:** Client provides data; Sayer advises on cleanup and deduplication strategy. Sayer does not guarantee data quality for records imported as-is.

---

## Deliverables & Sign-Off

| Phase | Deliverable | Sign-Off By |
|-------|-------------|------------|
| Phase 1 | {Description} | Client Day-to-Day |
| Phase 2 | {Description} | Client Day-to-Day |
| Phase 3 | {Description} | Client Sponsor |
| Final | Documentation + training handoff | Client Sponsor |

**Sign-off process:** At phase review, Sayer demos completed work against success criteria. Client confirms acceptance or flags items. Unresolved items carry forward with documented timeline.

---

## Escalation Path

| Level | Trigger | Who | Timeline |
|-------|---------|-----|----------|
| 1 | Day-to-day blocker | Project Lead + Client Contact | Same day |
| 2 | Blocker > 48hrs or scope dispute | PM + Client Sponsor | Within 2 business days |
| 3 | Commercial or relationship issue | Account Manager + Sponsor | Within 1 week |

---

## Confidentiality

- Sayer treats all client data as confidential
- No client data is shared outside the project team
- Integration credentials are stored securely (macOS Keychain, not in code)
- Client data is not used for training, benchmarking, or marketing without written consent

---

## Post-Project

- Documentation and admin guide delivered before final sign-off
- 30-day support window for questions after go-live (included in engagement)
- Ongoing support available via separate retainer agreement
- Retrospective conducted within 2 weeks of go-live to capture learnings
