# Hour Ranges & Complexity Multipliers

## Complexity Factor Multipliers

Apply these multipliers cumulatively to base hour ranges:

| Complexity Factor | Adjustment |
|-------------------|------------|
| Users: 1-5 | Base hours (no adjustment) |
| Users: 6-15 | +10-15% |
| Users: 16-50 | +20-30% |
| Users: 50+ | +40%+ |
| Data sources: 1 | Base (no adjustment) |
| Data sources: 2-3 | +15-25% |
| Data sources: 4+ | +30-50% |
| Custom objects: 0-2 | Base (no adjustment) |
| Custom objects: 3-5 | +10-20% |
| Custom objects: 6+ | +25%+ |
| Data quality: Clean | Base (no adjustment) |
| Data quality: Moderate issues | +15-25% |
| Data quality: Significant issues/dedup | +30-50% |
| Multi-entity/brand | +20-40% per entity |
| ERP involvement | +25-50% complexity premium |

## Base Hour Ranges by Workstream

CRM baseline -- adjust for platform and complexity:

| Workstream | Small (1-5 users, simple) | Medium (6-15 users, moderate) | Large (16+ users, complex) |
|------------|---------------------------|-------------------------------|----------------------------|
| CRM Architecture | 4-8 hrs | 8-16 hrs | 16-24 hrs |
| Pipeline & Deals | 4-8 hrs | 8-14 hrs | 14-24 hrs |
| Contact/Company Mgmt | 4-8 hrs | 8-16 hrs | 16-28 hrs |
| Automations | 6-12 hrs | 12-24 hrs | 24-40 hrs |
| Email & Comms | 4-8 hrs | 8-14 hrs | 14-20 hrs |
| Reporting | 4-8 hrs | 8-16 hrs | 16-28 hrs |
| Integration (each) | 6-12 hrs | 12-24 hrs | 24-40 hrs |
| Training (per group) | 4-6 hrs | 6-10 hrs | 10-16 hrs |
| Data Migration (per source) | 8-16 hrs | 16-32 hrs | 32-60 hrs |
| Project Management | 8-12 hrs | 12-20 hrs | 20-32 hrs |

**ERP workstreams typically run 1.5-2x CRM equivalents** due to financial data sensitivity and reconciliation requirements.

## Rate Modeling

1. **Check** the `sayer-rates` skill for the current rate card and blended-rate model
2. **If no tier mix or rate is specified**, default to the Associate rate of $150/hr
3. **If the user states a different rate**, use their rate
4. **If unsure**, ask the user: "What hourly rate should I use for cost modeling?"

Always calculate:
- Total min hours x rate = min cost
- Total max hours x rate = max cost
- Total median hours x rate = median cost
