# HubSpot Quoting / CPQ — Capability & Licensing Reference

> **Living reference for scoping HubSpot quoting/CPQ engagements.** HubSpot changes product structure, tiers, and pricing frequently — this file is a *dated snapshot*, not gospel. Re-verify the rows relevant to your engagement with a HubSpot rep/SE at the start of every CPQ scope and update the `Last verified` stamp.
>
> **Last verified: 2026-07-15**
> **Sources:** HubSpot public docs research (2026-07-15); HubSpot rep (Scott) + Solutions Engineer feedback on the NEC engagement (2026-07-15).
> **Refresh rule:** at the start of any quoting/CPQ scope, confirm the license structure + the multiplier/pricing mechanism + any custom-object need with the rep/SE, then bump this date and note who confirmed what.

## Why this file exists

Quoting/CPQ capability parity drives the fee more than hours-per-SKU do: whether pricing logic is native, whether a custom object forces Enterprise, and which Hubs must be licensed each swing scope by tens of hours and swing the client's monthly software cost materially. This reference converts one-off rep conversations into durable, team-wide parity knowledge so we don't re-discover it (or scope against stale assumptions) each engagement.

## Product structure (as of 2026-07-15)

- HubSpot renamed **Commerce Hub → Revenue Hub on 2026-06-16**. Revenue Hub is where native quotes/CPQ, product/price books, approvals, e-sign, payments, and the Contracts object live.
- **Native quotes/CPQ require a Revenue Hub license.** *Legacy quotes are no longer available to new customers* — a new client quoting out of HubSpot must buy Revenue Hub. (Confirmed: Scott, 2026-07-15.)
- **Revenue Hub and Sales Hub are separate line items** — Revenue Hub does **not** auto-bundle into Sales Hub Pro/Enterprise. Both appear individually on the HubSpot quote. (Confirmed: Scott, 2026-07-15.)
- Tiers: Sales/Service/Marketing/Content/Operations(Data) Hubs each Starter/Pro/Enterprise; Revenue Hub ships Free/Professional/Enterprise (no Starter as of this check).

## Capability parity

| Capability | Mechanism / tier | Status | Notes |
|---|---|---|---|
| Native quotes / CPQ | **Revenue Hub Pro or Ent** (Sales Hub alone = legacy quotes, unavailable to new customers) | Confirmed (Scott, 2026-07-15) | Rev Hub is a separate line item from Sales Hub |
| **Rules/multiplier pricing** (list price × multiplier by segment/family) | **Price Books (native to Revenue Hub)** | Confirmed by SE (2026-07-15); rep escalating edge cases | SE: "Price Books can do all that logic." Validate that Price Books express complex matrices (many distributors × family overrides + free-text exceptions) in a design spike — this is the row most worth confirming per-engagement. |
| Auto-populate quote + line items + calculations | **Data Hub (Operations Hub) custom-coded workflow actions** | Confirmed (SE, 2026-07-15) | Optional automation layer: rep selects properties → workflow populates line items, runs calculations, creates the quote. Depth depends on how much automation the client wants. Separate license. |
| "Create Quote" guided UX | **CRM Card as a Create-Quote workflow** | Per SE (2026-07-15) | A CRM Card can drive a guided quote-creation flow. |
| Line-item cost + margin | Native line-item properties (`Unit cost` + auto margin fields) | Confirmed (research, 2026-07-15) | Cost/margin per line, rolls up to quote. |
| Quote approvals | **Rev Hub Pro = standard (property-based)**; **Ent = advanced (workflow-built)** | Confirmed (Scott, 2026-07-15) | Pro standard example: "discount % > 20% → route to N approvers, 1-of-N or all-of-N approve." Enterprise adds conditional flexibility. Property-threshold routing (e.g. quote amount > $X → approver) is a Pro capability. |
| Custom objects | **Enterprise only.** Cheapest path: a **Core Enterprise seat (~$75/mo)** unlocks Enterprise CRM (custom objects) — but then **all core seats become Enterprise**. | Confirmed (Scott, 2026-07-15) | **First check whether a custom object is even needed** — Revenue Hub has a **native Contracts object** that customers previously built custom objects for. Prefer native objects to avoid the portal-wide Enterprise jump. (SE, 2026-07-15.) |
| Product library scale | Handles thousands of SKUs; ~1,500–2,000 is well within limits | Confirmed (both, 2026-07-15) | Not a constraint for typical manufacturers. |
| API limits | **650,000 calls/day** across all Professional products | Confirmed (Scott, 2026-07-15) | **API Limit Increase add-on** (requires a paid plan): +1,000,000/day on top of the 650k. Size ERP-sync volume against this. |

## Pricing (list, per seat/month, observed 2026-07-15 — negotiable, changes often)

- Sales Hub Professional ~$90 · Revenue Hub Professional ~$85 · Sales Hub Enterprise ~$150 · Revenue Hub Enterprise ~$140
- **Core Enterprise seat ~$75/mo** — the minimum-footprint way to unlock custom objects (Enterprise CRM), per Scott. Note it forces all core seats to Enterprise.
- Data Hub (Operations Hub) Professional — confirm current price/structure with rep.
- Payments processing is per-transaction, not seat-based.

## Scoping implications (how to use this when estimating)

- **Multiplier/pricing = Price Books (native), not a custom-code engine.** Budget Price Book configuration + product/price data load. Add Data Hub custom-code hours only if the client wants the auto-populate-and-create-quote automation. This is the natural light-vs-heavy lane split.
- **Default to standard objects.** Only scope a custom object (and the resulting Enterprise upgrade) if a concrete need survives checking the native Contracts object first. Treat any Enterprise trigger as a change order with a stated cost delta.
- **Approvals rarely force Enterprise** — property-threshold routing is a Pro capability. Only go Enterprise-for-approvals if conditional/multi-branch routing is required.
- **License stack to price for the client:** Sales Hub Pro (CRM) + Revenue Hub Pro (quoting), each a separate line item; Data Hub Pro if automating quote creation. Client pays licensing; Sayer negotiates.

## Open / escalating (confirm before committing a fixed fee)

- Whether Price Books cleanly express a **complex multiplier matrix** (many segments × per-family overrides + relative/free-text exceptions) natively, or whether some exceptions need Data Hub custom code or a manual override step. (Rep escalating as of 2026-07-15.)
- Exact Data Hub (Operations Hub) Pro pricing/structure.
- Approval-step counts and conditional-routing limits per tier.
