# 📏 KPI Definitions — ABS Retail Analytics

> Every KPI used in the dashboard, how it is calculated, what a good value looks like, and why it matters.

---

## Revenue KPIs

| KPI | Formula | Good Value | Why It Matters |
|---|---|---|---|
| **Total Revenue** | `SUM(gross_revenue_usd)` | Growing YoY | Top-line health indicator |
| **Gross Profit** | `Revenue - Total Cost` | Positive & growing | True profitability after COGS |
| **Gross Margin %** | `Gross Profit / Revenue` | > 30% for retail | How much of each dollar is profit |
| **Net Revenue** | `Revenue - Shipping Cost` | > Gross Profit target | Revenue after fulfilment costs |
| **Average Order Value** | `Revenue / Order Count` | Growing over time | Proxy for upsell effectiveness |
| **YoY Revenue Growth** | `(This Year - Last Year) / Last Year` | > 0% | Trajectory indicator |

---

## Customer KPIs

| KPI | Formula | Target | Why It Matters |
|---|---|---|---|
| **Repeat Customer Rate** | `Repeat Orders / Total Orders` | ≥ 50% | Retention and loyalty signal |
| **Customer Lifetime Value** | `AOV × Purchase Frequency` | Growing | Long-term revenue potential per customer |
| **Total Unique Customers** | `DISTINCTCOUNT(customer_id)` | Growing | Market penetration |

---

## Operations KPIs

| KPI | Formula | Target | Why It Matters |
|---|---|---|---|
| **Return Rate** | `Returned Orders / Total Orders` | < 5.0% | Cost and satisfaction signal |
| **Cancel Rate** | `Cancelled Orders / Total Orders` | < 3.0% | UX and inventory signal |
| **Refund Rate** | `Refunded Orders / Total Orders` | < 2.0% | Financial risk indicator |
| **Avg Delivery Days** | `AVERAGE(days_to_deliver)` | < 3 days | Customer satisfaction driver |
| **Delivery Success Rate** | `Delivered Orders / Total Orders` | > 90% | Fulfilment reliability |

---

## Channel KPIs

| KPI | Formula | Goal | Why It Matters |
|---|---|---|---|
| **Revenue by Channel** | `SUM(revenue) per channel` | Diversified | Over-reliance on one channel is a risk |
| **Channel Revenue Share** | `Channel Revenue / Total Revenue` | No channel > 40% | Healthy channel mix |
| **AOV by Channel** | `Channel Revenue / Channel Orders` | Higher = better | Channel quality indicator |

---

## Geographic KPIs

| KPI | Formula | Goal | Why It Matters |
|---|---|---|---|
| **Revenue by Continent** | `SUM(revenue) per continent` | Balanced | Geographic concentration risk |
| **Revenue by Country** | `SUM(revenue) per country` | Growing in top 10 | Market penetration |
| **AOV by Country** | `Country Revenue / Country Orders` | Identifies premium markets | Informs investment decisions |

---

## Forecast KPIs

| KPI | Description | ABS 2025 Target |
|---|---|---|
| **Baseline Forecast** | Linear regression projection | $660,000 |
| **CAGR Forecast** | Compound annual growth applied | $705,000 |
| **Optimistic Forecast** | Baseline + 12% with initiatives | $739,000 |
| **Conservative Forecast** | Baseline - 8% headwinds | $607,000 |
| **Recommended Target** | Internal planning figure | $705,000 – $720,000 |
