# Top Down Auto -- ERP Clarifying Questions

**Purpose:** Resolve these questions on the follow-up call before finalizing scope and SOW.
**Call participants:** Alexis (IT/dev), Terry & Shafi (ERP experts), Stephanie, Billy Leigh, Ismail, sales manager

---

## Legacy System (Intuitive) Extraction
*Route to: Alexis (IT/dev)*

1. What data entities live exclusively in Intuitive that you still need access to? (Warranty records, old POs, product specs, customer history -- which are actively referenced today, and how often?)
2. Is Intuitive hosted/cloud or on-prem? Has Alexis confirmed he can export structured data (CSV/SQL dump), or is the back-end access read-only/limited?
3. What's the monthly license cost for Intuitive? (Helps build the business case: break-even on the $25K export fee.)
4. Are warranty claims currently being processed against Intuitive data? If so, how frequently?

---

## NetSuite Current State
*Route to: Alexis + sales manager*

5. How many subsidiaries are set up in NetSuite, and which brands do they map to?
6. What NetSuite edition and modules are you on? (SuiteAnalytics, SuiteTalk/REST API access, etc.)
7. How would you rate data quality inside NetSuite today? Are customer records deduplicated across subsidiaries? Are product records complete and current?
8. Who is the day-to-day NetSuite admin, and what's their availability for a project like this?

---

## Atlas / CalTrend
*Route to: Stephanie*

9. What exactly is Atlas? (Custom-built app, database, SaaS tool?) What data does it hold that NetSuite doesn't?
10. What's blocking the Atlas-to-NetSuite migration -- technical complexity, resources, or just priority?

---

## Product Catalog and SKUs
*Route to: Alexis + sales manager*

11. Roughly how many active SKUs exist across all brands/subsidiaries in NetSuite today?
12. Is there an existing cross-reference table that maps equivalent SKUs across brands, or do reps just know from memory?
13. Where does fitment data (year-make-model) live today? NetSuite item records, separate database, or paper catalogs only?
14. For the legacy paper catalogs -- roughly how many pages/catalogs are we talking about?

---

## Data Architecture and Integration
*Route to: Billy Leigh + Ismail*

15. Has any decision been made on data warehouse vs. direct point-to-point integrations? What's Billy's current leaning?
16. What tools does Ismail use today for BI/reporting? (SQL Server, Excel, Tableau, Power BI, NetSuite saved searches?)
17. What middleware connects your web stores (Magento/WooCommerce) to NetSuite today? (Custom code, Celigo, Boomi, something else?)

---

## CRM-ERP Integration Specifics
*Route to: Stephanie + sales manager*

18. For the CRM, what data do you need flowing from NetSuite into HubSpot? (Customer records, order history, open quotes, product catalog, inventory levels -- rank by priority.)
19. Does order entry need to happen in HubSpot, or will reps continue entering orders in NetSuite? (Read-only vs. bidirectional integration.)
20. How should customer records map between HubSpot and NetSuite? One HubSpot company = one subsidiary customer, or one company = parent account across all subsidiaries?

---

## Scoping and Prioritization
*Route to: Stephanie + Billy*

21. If ERP data cleanup takes longer than expected, what's the minimum viable CRM you'd want to launch with?
22. What's your realistic timeline expectation for having ERP data in a "good enough" state to integrate with a CRM?

---

## Question Routing Summary

| Questions | Route To |
|---|---|
| 1-4 (Intuitive) | Alexis (IT/dev) |
| 5-8 (NetSuite) | Alexis + sales manager |
| 9-10 (Atlas) | Stephanie |
| 11-14 (SKUs/Catalog) | Alexis + sales manager |
| 15-17 (Architecture) | Billy Leigh + Ismail |
| 18-20 (Integration) | Stephanie + sales manager |
| 21-22 (Prioritization) | Stephanie + Billy |
