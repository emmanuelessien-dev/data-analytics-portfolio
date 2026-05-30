# 🛒 ABS Retail — End-to-End Data Analytics Project

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-Analysis-217346?logo=microsoftexcel&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**A complete, production-grade retail analytics project covering descriptive analysis, predictive forecasting, and an interactive Power BI dashboard — built as a Data Analytics Fellowship Capstone.**

[📊 View Dashboard Screenshots](#dashboard-preview) · [📁 Explore Files](#project-structure) · [📈 Key Findings](#key-findings) · [🚀 How to Run](#how-to-run)

</div>

---

## 📌 Project Summary

| Detail | Info |
|---|---|
| **Dataset** | ABS Retail Transactions 2021–2024 |
| **Records** | 5,000 orders · 600 customers · 23 countries |
| **Tools** | Python, Power BI, Excel, DAX |
| **Analysis Type** | Descriptive + Diagnostic + Predictive |
| **Deliverables** | Dashboard · Excel Workbook · Presentation · Forecast |
| **Duration** | Capstone Project — Data Analytics Fellowship |

---

## 🎯 Business Problem

ABS Retail operates across 23 countries and 6 continents. Despite growing order volume, the company faces three critical challenges:

1. **High return rate (8.62%)** against an industry benchmark of 5% — costing an estimated **$145,000/year**
2. **Low repeat customer rate (34.28%)** against a 50% target — representing **$400,000+ in uncaptured annual revenue**
3. **Margin imbalance** — Electronics dominates revenue (56% share) but earns the lowest gross margin (21.9%), while Beauty & Health sits underinvested at a 53.7% margin

This project answers the question: **Where should ABS Retail invest, cut back, and act urgently?**

---

## 📂 Project Structure

```
abs-retail-analytics/
│
├── 📁 data/
│   ├── ABS_RETAIL.xlsx                  # Raw source dataset
│   └── data_dictionary.md               # Field definitions & data types
│
├── 📁 notebooks/
│   └── abs_retail_analysis.py           # Full Python EDA & forecast script
│
├── 📁 dashboard/
│   ├── dashboard_screenshots/           # PNG exports of all 6 dashboard pages
│   └── powerbi_build_guide.md           # Step-by-step Power BI build instructions
│
├── 📁 docs/
│   ├── business_questions.md            # Analytical questions that guided the project
│   ├── data_limitations.md              # Transparency on what the data cannot tell us
│   ├── kpi_definitions.md               # Every KPI formula and business definition
│   ├── dax_measures.md                  # All DAX measures used in Power BI
│   └── recommendations.md              # 6 strategic recommendations with ROI estimates
│
├── 📁 presentation/
│   └── ABS_Retail_Capstone.pptx         # 16-slide stakeholder presentation
│
├── 📁 assets/
│   └── charts/                          # Exported matplotlib chart images
│
├── ABS_Retail_Analysis.xlsx             # Full Excel analysis workbook (8 sheets)
├── README.md                            # This file
└── LICENSE
```

---

## 🔍 Key Findings

### 💰 Revenue & Profitability
- **Total Revenue: $2,637,250** across 5,000 orders over 4 years
- **2024 was the strongest year** at $702,533 — recovering +15.3% after a two-year dip in 2022–2023
- **Gross Margin: 31.74%** portfolio-wide, but ranges from **21.9% (Electronics)** to **53.7% (Beauty & Health)**
- **Average Order Value: $527.45**, highest from In-Store Kiosk channel ($580.21)

### 📉 The 2022–2023 Dip
Revenue declined two consecutive years (-9.3% in 2022, -3.3% in 2023). Diagnostic analysis points to post-pandemic demand normalisation — a pattern consistent with global e-commerce trends in that period.

### 👥 Customer Behaviour
- Only **34.28% repeat customer rate** vs 50%+ industry benchmark
- **Professional segment** holds the highest average order value ($558.49)
- **Mobile App** channel shows the fastest YoY growth trajectory and highest repeat rates

### 🌍 Geography
- **Asia leads** in revenue ($608,549) and orders (1,098)
- **Oceania is an untapped premium market** — fewest orders (445) but highest average order value ($549) of any continent
- **Top 3 countries**: USA ($186K), Japan ($178K), Germany ($166K)

### ⚠️ Operations Risk
| Metric | Current | Target | Gap |
|---|---|---|---|
| Return Rate | 8.62% | 5.00% | **-3.62pp** |
| Cancel Rate | 7.84% | 3.00% | **-4.84pp** |
| Avg Delivery Days | 4.67 | 3.00 | **-1.67 days** |
| Repeat Customer Rate | 34.28% | 50.00% | **-15.72pp** |

**Top return reason:** Changed Mind (200 cases, 46% of all returns) — a preventable category.

---

## 📊 Dashboard Preview

> Built in **Microsoft Power BI** with 6 interactive pages, 20+ visuals, DAX measures, AI Key Influencers, and a 2025 revenue forecast with confidence intervals.

| Page | Focus | Key Visual |
|---|---|---|
| Page 1 | Executive Overview | KPI Cards · Line Trend · World Map |
| Page 2 | Sales Deep Dive | Decomposition Tree · Waterfall · Scatter |
| Page 3 | Customer Analysis | Key Influencers AI · Retention Trend |
| Page 4 | Operations | Return Rate Gauge · Reasons Bar |
| Page 5 | Geographic | Filled Map · Country × Category Matrix |
| Page 6 | Forecast 2025 | Confidence Band · Scenario Cards |

*Screenshots available in `/dashboard/dashboard_screenshots/`*

---

## 🔮 Forecast — 2025 Revenue Projections

Using a **linear regression trend model** and **CAGR model** on 4 years of historical data:

| Scenario | Projected Revenue | vs 2024 |
|---|---|---|
| 🔴 Conservative | $607,000 | -13.6% |
| 🟡 Baseline (Linear) | $660,000 | -6.0% |
| 🔵 CAGR Model | $705,000 | +0.4% |
| 🟢 Optimistic | $739,000 | +5.2% |

> **Recommended target:** $705K–$740K with loyalty program implementation and return rate reduction.

---

## 🛠 Tools & Technologies

| Tool | Purpose |
|---|---|
| **Python (pandas, numpy)** | Data cleaning, EDA, statistical analysis, forecasting |
| **Matplotlib** | Custom chart generation for presentation |
| **Microsoft Power BI** | Interactive 6-page dashboard |
| **DAX** | Calculated measures (Gross Profit, Margin %, YoY Growth, Repeat Rate, Return Rate) |
| **Microsoft Excel** | Analysis workbook with 8 formatted sheets |
| **python-pptx** | Programmatic generation of 16-slide presentation |

---

## ⚡ DAX Measures (Highlights)

```dax
// Gross Profit
Gross Profit = SUM('Data'[gross_revenue_usd]) - SUM('Data'[total_cost_usd])

// Gross Margin %
Gross Margin % = DIVIDE([Gross Profit], SUM('Data'[gross_revenue_usd]))

// YoY Revenue Growth
YoY Growth % = DIVIDE(
    [Total Revenue] - CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(Date[Date])),
    CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(Date[Date]))
)

// Return Rate
Return Rate = DIVIDE(
    COUNTROWS(FILTER('Data', 'Data'[order_status] = "Returned")),
    COUNTROWS('Data')
)

// Repeat Customer Rate
Repeat Rate = DIVIDE(
    COUNTROWS(FILTER('Data', 'Data'[is_repeat_customer] = "Yes")),
    COUNTROWS('Data')
)
```

*Full DAX reference: [`/docs/dax_measures.md`](docs/dax_measures.md)*

---

## 🚀 How to Run

### Python Analysis Script
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/abs-retail-analytics.git
cd abs-retail-analytics

# Install dependencies
pip install pandas numpy matplotlib openpyxl python-pptx

# Run the full analysis
python notebooks/abs_retail_analysis.py
```

### Excel Workbook
Open `ABS_Retail_Analysis.xlsx` — no installation needed. Contains 8 sheets:
- `Clean Data` — enriched dataset with calculated columns
- `Executive KPIs` — colour-coded KPI summary
- `Revenue Trends` — monthly trend data + line chart
- `Category & Channel` — product and channel breakdown
- `Customer & Geography` — segment and continent analysis
- `Returns & Operations` — return reasons and shipping metrics
- `Forecast 2025` — three scenario projections + monthly breakdown
- `PowerBI Guide` — step-by-step dashboard build instructions

---

## 🎯 Strategic Recommendations

| Priority | Recommendation | Est. Impact |
|---|---|---|
| 🔴 URGENT | Reduce return rate: AR try-on, QC audit, better product listings | Save ~$52K/year |
| 🔴 CRITICAL | Launch loyalty program to grow repeat rate from 34% → 50% | +$400K/year potential |
| 🟡 HIGH | Shift marketing budget to Beauty & Health (53% margin) | +6pp portfolio margin |
| 🟡 HIGH | Accelerate Mobile App channel investment | Target 40% revenue share |
| 🟢 MEDIUM | Unlock Oceania premium market (highest AOV at $549) | New revenue stream |
| 🔵 PLAN | Set 2025 baseline target at $705K–$740K | +0.4% to +5.2% YoY |

---

## 📋 Data Dictionary (Summary)

| Field | Type | Description |
|---|---|---|
| `order_id` | String | Unique transaction identifier |
| `order_date` | Date | Date order was placed |
| `delivery_date` | Date | Date order was delivered |
| `customer_segment` | Category | Professional, Individual, Family, Senior, Student |
| `gross_revenue_usd` | Float | Total revenue before costs |
| `total_cost_usd` | Float | COGS for the order |
| `shipping_cost_usd` | Float | Shipping cost allocated |
| `order_status` | Category | Delivered, Returned, Cancelled, Refunded |
| `return_reason` | Category | Reason for return (null if not returned) |
| `is_repeat_customer` | Boolean | Yes if customer has ordered before |
| `Gross Profit` *(calc)* | Float | `gross_revenue_usd - total_cost_usd` |
| `Gross Margin %` *(calc)* | Float | `Gross Profit / gross_revenue_usd` |

*Full dictionary: [`/docs/data_dictionary.md`](docs/data_dictionary.md)*

---

## 🏆 About This Project

This project was developed as a **Data Analytics Fellowship Capstone** with the goal of producing a **production-quality, end-to-end analytics deliverable** — not just exploratory analysis, but a full business intelligence solution with:

- A clean, documented codebase
- An interactive stakeholder dashboard
- Actionable recommendations with quantified ROI
- A professional presentation for non-technical audiences
- Transparent documentation of data limitations

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙋 Connect

If you found this project useful or want to discuss the analysis, feel free to connect:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/YOUR_PROFILE)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/YOUR_USERNAME)

> ⭐ **If this project helped you, please star the repository!**
