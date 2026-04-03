# American Bedding / Sayer - HubSpot CPQ Follow-up

March 23, 2026, 02:15 pm

## General Summary

- **Current Quoting Process:** Reviewed workflow; 65 quotes handled last week—60% by email, 20% phone, 20-25% website forms.  
- **Data Entry Issues:** Manual lookup in Cubics and Excel leads to quoting delays; processing takes 10 minutes to an hour.  
- **Integration Gaps:** HubSpot syncs opportunity stages but lacks quote visibility; pricing updates only after deal closure.  
- **Government Bidding Complexity:** RFP processes require detailed proposals; tracking currently done via spreadsheets with planned improvements.  
- **Phased Improvement Approach:** Initial focus on inside sales quoting; later phases to explore external integrations post-stabilization.  
- **Sales Team Challenges:** Many customers lack product knowledge; sales processes complicated by multiple systems requiring manual data entry.

## Action items

##### **Caleb**
- Provide copy of the Excel spreadsheet used for weight and freight calculations for review (46:40)
- Continue supporting quote creation and provide sample quoting data sets from HubSpot and NetSuite for scoping (40:00)
##### **Don Reynolds**
- Provide sample files and solicitation examples for government RFP process to help define system needs (34:00)
- Track and organize government bidding information into a customer file for better forecasting and process streamlining (37:30)
- Monitor credit applications and PO status with customers like Anderson University and Case Western, providing regular updates (54:00)
##### **Sarah-Beth Knight**
- Assist in gathering product data and HubSpot NetSuite integration status, clarify quote data syncing capabilities (08:10)
- Support catalog updates for government contracts in collaboration with third-party contractors (37:30)
##### **Kyle Harbuck**
- Lead coordination on solution scoping based on sample data and current workflow understanding (40:00)
- Facilitate discussion of phased approach starting with inside sales quoting before government RFPs (44:30)
##### **Billy Leigh**
- Provide input on recovery of missed meeting content and support phased project approach strategy (45:40)
##### **Cameron Taggart**
- Review Cubics API and explore automation possibilities for freight calculation and integration (46:30)
- Request access to freight weight spreadsheet and other reference materials for technical assessment (46:40)

## Notes

### **Current Quoting Process**
- The team reviewed the existing quote-to-order workflow to identify pain points and integration gaps blocking efficiency.
- **Overview of Quote Generation Workflow** highlighted by Caleb’s experience of handling **65 quotes last week** with **60% via email**, **20% phone**, and **20-25% website form submissions** (05:48)  
    - Quotes start from customer contact info and product interest captured in HubSpot forms or calls.  
    - Sales reps create opportunities in HubSpot, which sync bi-directionally with NetSuite deal stages but do not sync quote documents or PDFs.  
    - Multiple quotes tied to one opportunity are common, especially for customer comparisons during grant submissions.  
    - Quote adjustments mostly happen by editing existing quotes rather than generating new ones.  
- **Manual Data Entry and System Fragmentation** cause delays and inefficiencies (18:13)  
    - Freight and transportation costs come from a separate TMS system called **Cubics**, which requires manual data lookup and entry.  
    - Weight, dimensions, and freight class info live in Excel spreadsheets maintained internally, not in NetSuite.  
    - This fragmentation forces manual cross-checking between systems, adding time to the quoting process, which varies from **10 minutes to an hour** depending on complexity.  
- **Payment and Order Fulfillment Flow** clarified for order processing after quote acceptance (27:17)  
    - Payment terms vary: prepay, net 30, net 60 depending on customer and deal.  
    - Once a quote is signed, sales reps convert it to a sales order in NetSuite, which triggers production work orders and shipping preparation.  
    - Cancellations are rare and mostly due to stock or payment issues.  
    - Manual hold procedures exist for customers with overdue payments, preventing new quotes until resolved.  
- **SKU and Product Complexity** discussed with over **700 SKUs** but a focus on roughly **40-60 core SKUs** for quoting efficiency (13:17)  
    - Customers often don’t know exact product specs, increasing complexity for inside sales to guide them.  
    - There is a need to simplify SKU selection and provide decision support tools for customers to reduce sales effort and quoting time.  
### **HubSpot and NetSuite Integration Challenges**
- The integration between HubSpot and NetSuite supports opportunity syncing but falls short on quote visibility and automation.
- **Two-Way Sync Limits** restrict quote details to deal stages without transferring quote documents or line items (09:39)  
    - HubSpot shows opportunity stages but not the actual quotes or quote edits created in NetSuite.  
    - Pricing and quote amounts sync only after deal closure, limiting sales team visibility during quoting.  
- **Potential for Enhanced Front-End Interface** to guide customers through product and quote selection (12:30)  
    - Since most customers lack clear product specs, a front-end guided interface could gather required info and reduce sales effort.  
    - Mike Taylor emphasized reducing salesperson time by automating customer input and integrating it with HubSpot workflows (15:00).  
    - This would also reduce errors from manual data entry and improve quote accuracy.  
- **Discussion of HubSpot CPQ Capability and Limitations** (16:23)  
    - HubSpot has quoting features but may require third-party integrations to fully handle complex SKU and custom line items.  
    - No existing SKU upload to HubSpot yet; conversations are just starting to explore this capability.  
- **Desired State for Quote Data in HubSpot** includes visibility into all quote versions, edits, cancellations, and final approvals (17:06)  
    - Sales leadership wants an overview of all quote activity within HubSpot to avoid bouncing between systems.  
    - Pricing master data would remain in NetSuite but be mirrored in HubSpot for unified sales processes.  
### **Operational Dependencies and System Needs**
- Several operational and technical dependencies surfaced that affect quoting and order fulfillment efficiency.
- **Freight and Transportation Data Integration** is a key gap (19:06)  
    - Freight costs are manually entered using Cubics and internal Excel sheets for weights and classifications.  
    - These sheets include complex formulas and vary product weights, requiring manual updates for new products or changes.  
    - Future freight quoting may require dimensional data (length, width, height) to comply with carrier requirements, necessitating system upgrades.  
- **Manual Workflow and Data Maintenance Burden** adds risk and slows quoting (22:26)  
    - Weight and freight class data are not centralized in NetSuite but managed separately in Excel.  
    - Manual entry increases error risk and delays, especially when adding new products or adjusting existing lines.  
- **Integration with Third-Party APIs** like Cubics’ open API is being explored to automate freight quoting and reduce manual steps (46:42)  
    - Cameron Taggart suggested automating back-end calculations and API calls to Cubics to streamline data flow.  
    - This would allow sales reps to input minimal data and have all freight costs auto-calculated and integrated into quotes.  
### **Government Bidding and RFP Process**
- Government contracts present a distinct and more complex quoting and proposal environment.
- **RFP Process is Highly Complex and Manual** involving detailed proposals, contract clauses, and compliance checks (33:14)  
    - Don Reynolds described multiple government solicitation types requiring written proposals, cut sheets, and extensive contract clause checklists.  
    - Missing any clause or document can lead to disqualification, making accuracy critical.  
    - Responses often require custom packaging, shipping instructions, and coordination with multiple partners.  
- **Current Tracking and Forecasting is Spreadsheet-Based** with plans to improve (37:42)  
    - Government bids and teaming partner leads are tracked manually in spreadsheets.  
    - The team aims to create generic customer files to better forecast and manage government contract opportunities.  
- **GSA Contract Management Requires Constant Updates** due to changing platform requirements and market data requests (38:25)  
    - Recent GSA platform changes forced catalog reformatting and new market info submissions.  
    - The team expects ongoing adjustments as government procurement evolves.  
- **Government Sales Seen as Separate Channel with Unique Workflow Needs** requiring dedicated system capabilities (32:38)  
    - The process differs significantly from inside sales quoting and requires specialized handling of compliance and documentation.  
    - Integration and automation opportunities exist but must accommodate strict government standards.  
### **Strategic Direction and Phased Approach**
- The group agreed on a phased, focused approach to improve quoting starting with inside sales before expanding.
- **Prioritize Inside Sales Channel Improvements First** for quicker impact and manageable scope (45:41)  
    - Billy Leigh recommended starting with smaller, high-impact projects to build momentum and avoid complexity overload.  
    - Don Reynolds supported focusing on inside sales quoting before addressing government RFP complexities.  
- **Phased Implementation to Manage Complexity and Resource Load** (44:31)  
    - Starting with core quoting improvements allows time to build confidence and refine workflows before tackling government bids or external sales channels.  
    - Subsequent phases could explore integration with external storefronts like Shopify once quoting is stable.  
- **Data Sharing and Sample Sets for Scoping** will help define project boundaries (40:44)  
    - Kyle Harbuck requested example data sets from NetSuite, Cubics, and existing spreadsheets to map and scope automation efforts.  
    - Sharing the Excel freight weight spreadsheet with the team will help technical planning.  
- **Long-Term Vision Includes a Unified Sales Platform** where sales reps manage everything from HubSpot with automated data flows from NetSuite and freight systems (39:39)  
    - The ideal state is a single interface for managing opportunities, quotes, orders, and customer data without switching systems.  
    - Customer decision support tools will reduce sales time and improve quote accuracy.  
### **Customer and Sales Insights**
- Sales team insights highlighted customer behavior and internal challenges affecting quoting efficiency.
- **Most Customers Lack Clear Product Knowledge** requiring sales guidance (12:30)  
    - Caleb noted majority of customers do not know exact mattress sizes or specs, complicating quoting.  
    - Decision trees or guided front-end tools could educate and qualify customers better upfront.  
- **Multiple Quote Versions Common for Grant or Budgeting Needs** (11:47)  
    - Customers often request several quotes simultaneously to compare options for grant approvals.  
    - Having these visible and manageable in one system is important for sales transparency.  
- **Manual Holds and Payment Issues Impact Sales Pipeline** but are handled with manual communication (30:54)  
    - Customers with unpaid balances are placed on hold manually, preventing new quotes until resolved.  
    - No automated system flags exist currently to prevent quoting to blocked customers.  
- **SKU and Product Variability Require Simplification Efforts** (13:17)  
    - Over 700 SKUs exist but core sales mostly use about 40-60 SKUs regularly.  
    - Narrowing SKUs and creating custom line items for special orders is part of the current workaround.  
- **Sales Team Struggles with Multiple Systems and Manual Data Lookup** (18:45)  
    - The need to jump between NetSuite, Excel, Cubics, and HubSpot increases quoting time and error risk.  
    - Automation and integration are seen as key to reducing workload and speeding response times.

