# 📋 Data Dictionary — ABS Retail Dataset

> Full field reference for the ABS_RETAIL.xlsx dataset. All monetary values are in USD.

---

## Source File
- **File:** `ABS_RETAIL.xlsx`
- **Records:** 5,000 rows
- **Fields:** 29 original + 5 calculated
- **Coverage:** Fiscal Years 2021–2024
- **Missing Values:** `return_reason` is null for non-returned orders (expected behaviour)

---

## Original Fields

| # | Field | Data Type | Example | Description |
|---|---|---|---|---|
| 1 | `order_id` | String | ORD-00001 | Unique identifier for each transaction |
| 2 | `order_date` | Date | 2023-04-15 | Date the order was placed by customer |
| 3 | `delivery_date` | Date | 2023-04-20 | Date the order was delivered to customer |
| 4 | `year` | Integer | 2023 | Fiscal year extracted from order_date |
| 5 | `customer_id` | String | CUST-001 | Unique customer identifier |
| 6 | `customer_name` | String | John Doe | Customer full name |
| 7 | `customer_segment` | Category | Professional | One of: Professional, Individual, Family, Senior, Student |
| 8 | `country` | String | Ghana | Country where order was placed |
| 9 | `city` | String | Accra | City of the customer |
| 10 | `continent` | Category | Africa | One of: Africa, Asia, Europe, North America, South America, Oceania |
| 11 | `product_id` | String | PROD-001 | Unique product identifier |
| 12 | `product_name` | String | iPhone 15 Pro | Full product name |
| 13 | `category` | Category | Electronics | One of: Electronics, Home & Living, Beauty & Health, Clothing & Apparel, Books & Media |
| 14 | `sub_category` | String | Smartphones | Product sub-classification within category |
| 15 | `unit_cost_usd` | Float | 450.00 | Cost to ABS Retail per unit |
| 16 | `unit_price_usd` | Float | 899.00 | Selling price per unit before discount |
| 17 | `discount_pct` | Float | 0.10 | Discount applied (0.0 = 0%, 1.0 = 100%) |
| 18 | `quantity` | Integer | 2 | Number of units in the order |
| 19 | `gross_revenue_usd` | Float | 1618.20 | Total revenue: `unit_price * qty * (1 - discount)` |
| 20 | `total_cost_usd` | Float | 900.00 | Total COGS: `unit_cost * quantity` |
| 21 | `shipping_cost_usd` | Float | 12.50 | Shipping cost charged to ABS (not customer) |
| 22 | `shipping_method` | Category | Express | One of: Standard, Express, Economy, Same Day, Click & Collect |
| 23 | `days_to_deliver` | Float | 2.0 | Number of days between order_date and delivery_date |
| 24 | `payment_method` | Category | Credit Card | One of: Credit Card, Debit Card, PayPal, Bank Transfer, Mobile Money, Cryptocurrency |
| 25 | `order_channel` | Category | Website | One of: Website, Mobile App, Social Media, Marketplace, In-Store Kiosk |
| 26 | `order_status` | Category | Delivered | One of: Delivered, Returned, Cancelled, Refunded |
| 27 | `return_reason` | Category | Size Issue | One of: Changed Mind, Size Issue, Defective, Not as Described, Wrong Item — **NULL if not returned** |
| 28 | `is_repeat_customer` | Boolean | Yes | "Yes" if the customer has a prior order in the dataset |

---

## Calculated / Enriched Fields
> Added during data preparation. Not in the original source file.

| Field | Formula | Description |
|---|---|---|
| `Gross Profit` | `gross_revenue_usd - total_cost_usd` | Absolute profit per order before shipping |
| `Gross Margin %` | `Gross Profit / gross_revenue_usd` | Profit as a percentage of revenue |
| `Net Revenue` | `gross_revenue_usd - shipping_cost_usd` | Revenue after deducting shipping cost |
| `Month` | `MONTH(order_date)` | Integer month number (1–12) |
| `Quarter` | `QUARTER(order_date)` | Quarter label (Q1, Q2, Q3, Q4) |

---

## Category Value Distributions

### order_status
| Value | Count | % of Total |
|---|---|---|
| Delivered | 3,936 | 78.72% |
| Returned | 431 | 8.62% |
| Cancelled | 392 | 7.84% |
| Refunded | 241 | 4.82% |

### return_reason (only for Returned orders)
| Value | Count |
|---|---|
| Changed Mind | 200 |
| Size Issue | 149 |
| Defective | 125 |
| Not as Described | 112 |
| Wrong Item | 86 |
| NULL (not returned) | 4,328 |

### shipping_method
| Value | Orders | Avg Days |
|---|---|---|
| Standard | 1,926 | 5.00 |
| Express | 1,274 | 2.01 |
| Economy | 1,012 | 10.41 |
| Same Day | 406 | 0.56 |
| Click & Collect | 382 | 0.99 |

---

## Data Quality Notes

- ✅ No duplicate `order_id` values
- ✅ All date fields are valid and parseable
- ✅ `gross_revenue_usd` is always > 0
- ✅ `return_reason` is NULL for all non-returned orders (expected, not a data error)
- ⚠️ `return_reason` for 241 Refunded orders is also NULL — reason unknown
- ⚠️ `is_repeat_customer` is a static flag — does not track recency or frequency of repeat behaviour
- ⚠️ No marketing spend or customer acquisition cost data is available
