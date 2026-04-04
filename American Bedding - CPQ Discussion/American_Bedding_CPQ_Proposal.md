# American Bedding -- HubSpot CPQ Implementation Proposal

Streamline your quoting process from four systems to one. Automate freight calculations. Give leadership full visibility into every quote.

Prepared by Sayer | Confidential

---

## A Note on This Proposal

Proposals are inherently a starting point -- not a final blueprint. This document reflects our understanding of your challenges from our March 16 and March 23 discovery sessions, a proposed solution, and the resources required to execute successfully.

We recognize that you, as the team that lives with these challenges daily, know details we have yet to uncover. Our goal is to use this as a conversation starter -- to refine, align, and ensure we are solving the right problems in the right order.

If any aspect of the scope, solution, or pricing feels misaligned, let's use that as a basis for further discussion.

### Our Commitment

This proposal is a living document. We are committed to refining the scope, solution, and investment until it is exactly right for American Bedding.

- Transparent communication throughout
- Phased delivery with clear milestones
- ROI-first approach to every decision

---

## Executive Summary

American Bedding is a Vesco portfolio company manufacturing mattresses for camps, educational institutions, and government agencies. With NetSuite launched January 1, 2026 and HubSpot in place for CRM, the infrastructure is ready -- but the quoting process is still fragmented across four systems.

Today, Caleb processes 65 quotes per week by jumping between NetSuite (pricing), Excel spreadsheets (weight calculations), Kuebix TMS (freight rates), and HubSpot (opportunity tracking). Each quote takes 10 minutes to an hour. Sales leadership cannot see quote activity, versions, or edits without logging into NetSuite separately.

This proposal eliminates that fragmentation. We will configure HubSpot CPQ as the single quoting interface, build automated integrations with NetSuite and Kuebix through n8n middleware, and replace the Excel weight calculators with a dynamic calculation engine. When complete, creating a quote -- from product selection through freight calculation to customer delivery -- happens in HubSpot.

### Phase 1: Inside Sales CPQ (Weeks 1-12)

Product catalog sync from NetSuite, automated freight via Kuebix API, dynamic weight calculation, branded quote templates, and full quote-to-order integration.

### Why Phase 1 First?

Inside sales represents 65% of revenue and 65 quotes per week of manual effort. Automating this channel delivers the highest ROI in the shortest time. Government RFP automation (Phase 2) is a fundamentally different workflow that benefits from the CPQ foundation built in Phase 1.

---

## The Problem

After launching NetSuite on January 1, 2026, American Bedding has solid systems in place -- but they are not connected where it matters most: the quoting process.

### 10+ Hours Per Week Lost to System Juggling

Every quote requires four systems in sequence: NetSuite for pricing, Excel for weight calculations, Kuebix for freight rates, then back to NetSuite to assemble the quote. At 65 quotes per week, even 10 minutes of unnecessary work per quote adds up to 10+ hours of wasted time weekly.

### Zero Quote Visibility in HubSpot

Quotes live in NetSuite. HubSpot shows deal stages and amounts -- but not the quotes themselves. Sales leadership cannot see quote details, versions, edits, or approval status without switching systems. Pipeline reporting is incomplete.

### Manual Freight Calculation Is the Bottleneck

Weight and freight class data lives in five Excel spreadsheets maintained on individual desktops -- not in any centralized system. Each freight quote requires manual lookup: find the right spreadsheet, calculate weight based on product specs, enter data into Kuebix, wait for carrier rates, then manually enter the result back into the quote.

### No Protection Against Quoting Blocked Customers

Customer credit holds are tracked manually. There is no automated flag to prevent quoting to customers with overdue payments. The risk is real: a quote goes out, an order ships, and collections discovers the customer already owed money.

This is not a technology problem. The technology exists. It is a connection problem -- four capable systems that do not talk to each other during the most critical revenue operation.

---

## Objectives

Ten clearly defined outcomes -- each tied to a measurable business result.

01 -- Single-Interface Quoting: Sales reps create, edit, and send quotes entirely within HubSpot. No system-jumping for standard inside sales quotes.

02 -- Automated Freight Calculation: Kuebix API integration calculates multi-carrier LTL shipping rates automatically. Cheapest rate auto-selected with manual override option. Eliminates manual weight lookup and freight entry.

03 -- Dynamic Weight Engine: Replaces five Excel spreadsheets with an automated calculation engine that determines product weight and volume from specifications -- size, foam density, cover material, innerspring type, packaging. Handles standard and custom product configurations.

04 -- Product Catalog in HubSpot: All 700 SKUs synced from NetSuite with pricing, specifications, and custom attributes. Ongoing automated sync ensures HubSpot always reflects current NetSuite pricing.

05 -- Quote-to-Order Automation: Accepted quotes automatically create Estimates in NetSuite. Approved estimates convert to Sales Orders, triggering production work orders. No manual re-entry.

06 -- Branded Quote Templates: Professional quote PDFs matching your current format -- line items, volume discounts, state-based tax, freight, terms and conditions, customer acceptance. Ready for customer delivery.

07 -- Credit Hold Visibility: Customer credit status from NetSuite surfaces in HubSpot before quote creation. Sales reps see hold flags before investing time in a quote for a blocked customer.

08 -- Volume Discount and Tax Automation: 10% volume discount logic and state-based tax calculation built into the quoting workflow. Consistent pricing across all reps.

09 -- Multi-Warehouse Freight Routing: Freight quotes automatically use the correct origin warehouse based on product and order characteristics. No manual warehouse selection for standard orders.

10 -- Full Quote Visibility for Leadership: Quote activity, versions, edits, approvals, and cancellations visible in HubSpot dashboards. Pipeline reporting includes quote data, not just deal stages.

---

## Solution Overview

### Architecture

HubSpot CPQ is the quoting interface. n8n middleware orchestrates data flow between three systems. NetSuite remains the ERP source of truth.

**How a quote gets built (future state):**

1. Rep opens a deal in HubSpot and starts a new quote
2. Selects products from the synced product catalog (filtered by type, size, material)
3. n8n calculates total weight and volume from product specifications
4. n8n determines the correct shipping origin warehouse
5. n8n calls Kuebix API with weight, dimensions, freight class, and addresses
6. Kuebix returns multi-carrier rates -- cheapest is auto-applied as a freight line item
7. Discount and tax logic auto-calculate based on order value and destination
8. Rep reviews, adjusts if needed, and sends the quote to the customer
9. Customer accepts via clickwrap or e-signature
10. n8n creates an Estimate in NetSuite, which converts to a Sales Order on approval

**Total time per quote: under 5 minutes for standard orders.**

### Technology Stack

- **HubSpot** Sales Hub Professional + Commerce Hub Professional (existing)
- **HubSpot** Operations Hub Professional (recommended addition -- enables custom code actions)
- **NetSuite** ERP (existing -- REST API with OAuth 2.0 M2M authentication)
- **Kuebix** TMS (existing -- Shipment API with Basic Auth)
- **n8n** workflow automation (middleware -- processes data between all three systems)

---

## What We Deliver

### Foundation (Weeks 1-4)

HubSpot CPQ configuration, product catalog migration, and NetSuite integration setup.

**CPQ Architecture and Configuration**

Commerce Hub CPQ module activation, custom deal/quote/line item properties, quote approval workflows, quote numbering, payment terms configuration. The foundation that everything else builds on.

**Product Catalog Sync**

All 700 SKUs extracted from NetSuite via SuiteQL and loaded into HubSpot with custom properties: weight components, freight class, dimensions, cover type, foam series, and construction type. Automated n8n sync keeps HubSpot pricing current with NetSuite changes.

**NetSuite Integration**

OAuth 2.0 M2M authentication. Customer data sync including credit status and payment terms. Price level synchronization. This is the data backbone connecting your ERP to your quoting interface.

### Integration (Weeks 5-8)

Freight automation, weight calculation engine, and quote template design.

**Kuebix Freight Integration**

n8n workflow connects HubSpot quotes to Kuebix's multi-carrier LTL rate shopping API. For each quote, the system collects product weights and dimensions, determines the correct shipping origin, requests rates from all configured carriers, and writes the best rate as a freight line item. Manual override available for truckload or special situations.

**Dynamic Weight Calculation Engine**

Replaces five Excel spreadsheets with automated n8n logic. Calculates shipping weight and cube volume from product specifications: panel dimensions, fabric weight by cover type (Anti-Bac Vinyl, SoFlux OX, Pinstripe Cloth), foam weight by density and thickness, innerspring weight by size, cotton batting, insulator pads, and packaging. Handles both standard and custom product configurations.

**Quote Template Design**

Custom HubSpot quote template matching your current NetSuite format. Line item table with quantity, item number, description, unit price, and amount. Subtotal, volume discount, state-based tax, shipping, and total. Damaged freight policy terms. Delivery instructions. Customer acceptance flow.

**Discount, Tax, and Payment Terms**

Volume discount automation, state-based tax calculation, payment terms workflow (prepay, net 10, net 30, net 60), and credit hold integration from NetSuite accounts receivable.

### Launch (Weeks 9-12)

Quote-to-order automation, testing, training, and go-live.

**Quote-to-Order Bridge**

When a customer accepts a quote, n8n creates an Estimate in NetSuite. On approval, the Estimate converts to a Sales Order, triggering production work orders and shipping preparation. No manual re-entry between systems.

**Testing and Validation**

End-to-end integration testing across all three systems. Quote accuracy validated against your five NetSuite example quotes. Weight calculations validated against existing Excel spreadsheets. Freight calculations validated against manual Kuebix lookups. Two UAT sessions with Caleb and Don.

**Training**

Sales team sessions (Caleb, Don): new quoting workflow, product selection, freight review. Admin sessions (Sarah-Beth, Patrick): system management, product catalog updates, sync monitoring. All sessions virtual, recorded for future onboarding. Admin guide and user quick reference card delivered.

**Go-Live and Hypercare**

Go-live cutover with 2-week hypercare period. Monitoring of integration flows, freight accuracy, and quote template rendering. Issue resolution and adjustment support.

---

## Timeline

A 10-12 week implementation with clear milestones and a natural checkpoint at each phase transition.

### Weeks 1-2

Kickoff, NetSuite data audit, product catalog extraction, CPQ module configuration, OAuth 2.0 setup, Kuebix API credential validation.

### Weeks 3-4

Product catalog loaded into HubSpot with custom properties. NetSuite integration active. Customer data sync operational. Quote approval workflows configured. Milestone review with Mike and Patrick.

### Weeks 5-6

Dynamic weight calculation engine built for first 3 product lines. Kuebix freight integration operational. Origin routing configured. Quote template design in progress.

### Weeks 7-8

Weight engine extended to all 5 product lines. Quote template finalized. Discount, tax, and payment terms logic active. Quote-to-order bridge tested. Milestone review with leadership.

### Weeks 9-10

Integration testing complete. UAT sessions with Caleb and Don. Bug fix window. Training sessions delivered.

### Weeks 11-12

Go-live. Hypercare monitoring. Documentation delivered. Project close-out.

---

## Investment

### $34,500

Total project investment -- fixed fee for the complete Phase 1 CPQ implementation. No hourly billing. No overages within the defined scope.

| Component | Model | Fee |
|-----------|-------|-----|
| Phase 1: Inside Sales CPQ (Weeks 1-12) | Fixed Fee | $34,500 |

### Payment Terms

All invoices are Net-15. Payments are structured as equal installments invoiced every 15 days throughout the engagement.

- 5 equal payments of $6,900 invoiced every 15 days

A 5% Technology and Administrative fee is applied to each invoice to offset costs of our technology stack and internal systems.

### Additional License Recommendations

- **Operations Hub Professional** (~$800/month) -- enables custom code actions and data quality automation in HubSpot. Recommended but not required for the core build. If declined, all automation routes through n8n.

---

## Project Governance

### Sayer Responsibilities

- Lead configuration, integration, and implementation across all workstreams
- Build and maintain n8n middleware workflows
- Conduct weekly check-ins and milestone reviews
- Provide documentation, training, and go-live support
- Manage project timeline and proactively communicate risks or blockers
- Deliver admin guide, user guide, and workflow documentation
- 2-week hypercare post go-live

### American Bedding Responsibilities

- Designate 1 primary point of contact (Sarah-Beth recommended)
- Provide Kuebix API credentials (username, API key, Client ID)
- Provide NetSuite admin access or create OAuth 2.0 M2M integration record
- Provide all 5 Excel shipping calculator files for technical review
- Provide complete warehouse address list with routing rules
- Confirm freight class per product line
- Ensure Caleb and Don availability for UAT sessions
- Validate sample quotes against current NetSuite output
- Complete UAT testing within agreed timeline
- Executive sponsorship from Mike Taylor for CRM adoption

---

## Assumptions and Constraints

### In Scope

- HubSpot Sales Hub Professional + Commerce Hub Professional (existing)
- NetSuite ERP integration (REST API, bi-directional)
- Kuebix TMS integration (Shipment API, freight rate automation)
- n8n middleware (hosted by Sayer or client infrastructure)
- Up to 700 products in HubSpot product library
- Dynamic weight calculation for 5 product lines
- Up to 30 custom properties across deals, quotes, and line items
- 1 branded quote template matching current NetSuite format
- 10-12 week implementation timeline
- All work conducted remotely

### Out of Scope

- Government RFP automation, compliance tracking, bid management (Phase 2 -- separate engagement)
- Customer-facing product configurator or guided selling interface (Phase 2)
- External storefront build (Shopify or HubSpot Commerce)
- VoIP / call capture system selection or integration
- AI lead enrichment from call transcripts
- NetSuite reimplementation or new module deployment
- Ongoing Kuebix TMS administration or carrier management
- HubSpot Marketing Hub configuration
- Ongoing managed services beyond 2-week hypercare
- HubSpot or NetSuite license procurement (recommendations provided)

Any scope changes require formal approval and may impact cost or timing.

---

## Approval and Next Steps

Please confirm alignment on scope and structure so we can move forward with scheduling a formal kickoff.

### 1. Pre-Engagement Technical Review -- COMPLETE

Sayer has reviewed and validated all 5 Excel shipping calculator files (April 4, 2026). The dynamic weight calculation engine scope is confirmed within the $34,500 fixed fee. No hidden complexity was found -- all calculator logic is deterministic and replicable.

### 2. Written Approval

Provide written approval of this proposal via email, signed by Mike Taylor or Patrick.

### 3. Schedule Kickoff

Project kickoff within 1-2 weeks of written approval.

### 4. Execute MSA

Sayer will issue a Master Services Agreement via DocuSign with this Scope of Work included.

### 5. Begin Implementation

Once the MSA is executed, Sayer will finalize the implementation plan and begin Week 1 activities.

---

## ROI Appendix

---

## The Value for American Bedding

"We process 65 quotes a week, and every one of them requires four systems. NetSuite for pricing, Excel for weight, Kuebix for freight, then back to NetSuite to put it all together. Our sales team spends more time navigating systems than talking to customers.

This investment connects the systems. Phase 1 gives us a single quoting interface in HubSpot with automated freight calculations within 12 weeks. No more Excel lookups. No more manual Kuebix entries. No more switching between four screens to build one quote.

We are not buying new software. We are connecting the software we already own."

---

## Time Savings -- $38,000 to $58,000 per year

Time that Caleb and the sales team get back for revenue-generating activities -- selling, customer relationships, and processing more quotes.

| Activity | Current State | Future State | Annual Savings |
|----------|--------------|--------------|----------------|
| System navigation per quote | 4 systems, 10-60 min per quote | 1 system, under 5 min per quote | $24,000 - $38,000 |
| Manual weight calculation | Excel lookup per product line, per quote | Automated calculation from product specs | $6,000 - $10,000 |
| Manual freight entry | Kuebix manual entry, wait for carrier response | Kuebix API auto-response in seconds | $5,000 - $7,000 |
| Quote re-entry to NetSuite | Manual estimate and sales order creation | Automated quote-to-order bridge | $3,000 - $5,000 |

These are conservative estimates based on current reported time spend (65 quotes/week at 10-60 minutes each). Actual savings may be significantly higher as the team processes more quotes with freed capacity.

---

## The ROI: Investment vs. Return

This engagement pays for itself within 7-9 months through quantifiable savings alone -- before accounting for error reduction, faster turnaround, or increased quote capacity.

### $34,500 -- Total Investment

Fixed fee for the complete Phase 1 CPQ implementation.

### $38,000 to $58,000 -- Year 1 Return

Conservative Year 1 return from time savings alone.

### 7-9 Months -- Payback Period

Using only quantifiable, conservative estimates.

### 10% to 68% -- Year 1 ROI Range

Excluding revenue uplift from faster quote turnaround and increased capacity.

---

## Error Reduction and Risk Mitigation

### Fewer Pricing Mistakes

Manual data entry across four systems introduces transcription errors. Automated product data and pricing sync eliminates the most common error source.

### Credit Hold Protection

Automated flags surface blocked customers before a quote is built -- not after an order ships. This protects margins and reduces collections effort.

### Consistent Freight Quoting

Dynamic weight calculation and automated Kuebix API calls ensure every freight quote uses the correct weight, freight class, and origin warehouse. No more spreadsheet lookup errors.

### Scalability

The current 65 quotes/week process is at capacity with Caleb handling it alone. Automated quoting enables higher volume without proportional headcount increase. This is the foundation for growth.

---

## Phase 2 Readiness

Phase 1 builds the infrastructure that Phase 2 needs. The product catalog, freight integration, and n8n middleware are reusable components for:

- **Government RFP automation** -- Template-based RFP responses, contract clause checklists, teaming partner tracking
- **Customer-facing configurator** -- Guided product selection for buyers who don't know mattress specifications
- **External storefront** -- Shopify or HubSpot Commerce for direct online ordering

Phase 2 scoping begins after Phase 1 demonstrates ROI.
