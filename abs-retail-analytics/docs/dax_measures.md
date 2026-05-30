# 📐 DAX Measures Reference — ABS Retail Power BI Dashboard

> All DAX measures used in the Power BI dashboard. Create these in a dedicated `_Measures` table.
> Replace `'Data'` with your actual table name if different.

---

## How to Create a Measures Table

1. Go to **Home → Enter Data**
2. Name the table `_Measures`
3. Click **Load**
4. Click on `_Measures` in the Fields pane
5. Go to **Table tools → New Measure** for each measure below

---

## 📊 Revenue Measures

```dax
// Total Revenue
Total Revenue =
SUM('Data'[gross_revenue_usd])

// Total Cost
Total Cost =
SUM('Data'[total_cost_usd])

// Gross Profit
Gross Profit =
SUM('Data'[gross_revenue_usd]) - SUM('Data'[total_cost_usd])

// Net Revenue (after shipping)
Net Revenue =
SUM('Data'[gross_revenue_usd]) - SUM('Data'[shipping_cost_usd])

// Total Shipping Cost
Total Shipping Cost =
SUM('Data'[shipping_cost_usd])

// Gross Margin %
Gross Margin % =
DIVIDE([Gross Profit], [Total Revenue])

// Average Order Value
Avg Order Value =
DIVIDE([Total Revenue], COUNTROWS('Data'))
```

---

## 📅 Time Intelligence Measures

```dax
// Prior Year Revenue (requires Date table)
YoY Revenue =
CALCULATE(
    [Total Revenue],
    SAMEPERIODLASTYEAR(Date[Date])
)

// YoY Growth Amount
YoY Growth Amount =
[Total Revenue] - [YoY Revenue]

// YoY Growth Percentage
YoY Growth % =
DIVIDE(
    [Total Revenue] - [YoY Revenue],
    [YoY Revenue]
)

// Year-to-Date Revenue
YTD Revenue =
TOTALYTD([Total Revenue], Date[Date])

// Quarter-to-Date Revenue
QTD Revenue =
TOTALQTD([Total Revenue], Date[Date])
```

---

## 👥 Customer Measures

```dax
// Total Unique Customers
Total Customers =
DISTINCTCOUNT('Data'[customer_id])

// Total Orders
Total Orders =
COUNTROWS('Data')

// Repeat Customer Count
Repeat Customers =
COUNTROWS(
    FILTER('Data', 'Data'[is_repeat_customer] = "Yes")
)

// Repeat Customer Rate
Repeat Rate =
DIVIDE(
    COUNTROWS(FILTER('Data', 'Data'[is_repeat_customer] = "Yes")),
    COUNTROWS('Data')
)

// New Customer Count
New Customers =
COUNTROWS(
    FILTER('Data', 'Data'[is_repeat_customer] = "No")
)
```

---

## ⚠️ Operations & Risk Measures

```dax
// Return Count
Return Count =
COUNTROWS(
    FILTER('Data', 'Data'[order_status] = "Returned")
)

// Return Rate
Return Rate =
DIVIDE(
    COUNTROWS(FILTER('Data', 'Data'[order_status] = "Returned")),
    COUNTROWS('Data')
)

// Cancellation Rate
Cancel Rate =
DIVIDE(
    COUNTROWS(FILTER('Data', 'Data'[order_status] = "Cancelled")),
    COUNTROWS('Data')
)

// Refund Rate
Refund Rate =
DIVIDE(
    COUNTROWS(FILTER('Data', 'Data'[order_status] = "Refunded")),
    COUNTROWS('Data')
)

// Delivery Rate (successfully delivered)
Delivery Rate =
DIVIDE(
    COUNTROWS(FILTER('Data', 'Data'[order_status] = "Delivered")),
    COUNTROWS('Data')
)

// Average Delivery Days
Avg Delivery Days =
AVERAGE('Data'[days_to_deliver])

// Return Rate Target (static reference)
Return Rate Target =
0.05

// Return Rate vs Target (positive = over target = bad)
Return Rate Gap =
[Return Rate] - [Return Rate Target]
```

---

## 🎯 Dynamic Titles (for Page Titles)

```dax
// Dynamic page title that updates with slicer selection
Page Title Revenue =
"Revenue Analysis — " &
IF(
    ISFILTERED('Data'[year]),
    SELECTEDVALUE('Data'[year], "All Years"),
    "All Years"
) & " · " &
IF(
    ISFILTERED('Data'[category]),
    SELECTEDVALUE('Data'[category], "All Categories"),
    "All Categories"
)

// Dynamic KPI subtitle
Selected Period Label =
IF(
    ISFILTERED('Data'[year]),
    "Fiscal Year " & SELECTEDVALUE('Data'[year]),
    "Fiscal Years 2021 – 2024"
)
```

---

## 🎨 Conditional Formatting Measures

```dax
// Color for Return Rate card (red if above 5% target)
Return Rate Color =
IF([Return Rate] > 0.05, "#C0392B", "#1E8449")

// Color for YoY Growth (green if positive, red if negative)
YoY Growth Color =
IF([YoY Growth %] >= 0, "#1E8449", "#C0392B")

// Repeat Rate status indicator
Repeat Rate Status =
IF([Repeat Rate] >= 0.50, "On Target ✓",
    IF([Repeat Rate] >= 0.40, "Approaching Target",
        "Below Target ⚠"
    )
)
```

---

## 📅 Date Table (Create This First)

```dax
// Create Date Table in DAX
Date =
ADDCOLUMNS(
    CALENDARAUTO(),
    "Year",        YEAR([Date]),
    "Month Number", MONTH([Date]),
    "Month Name",  FORMAT([Date], "MMM"),
    "Quarter",     "Q" & QUARTER([Date]),
    "Week Number", WEEKNUM([Date]),
    "Day Name",    FORMAT([Date], "DDD"),
    "Is Weekend",  IF(WEEKDAY([Date], 2) > 5, TRUE, FALSE)
)
```

> After creating the Date table, right-click it → **Mark as Date Table** → select the `Date` column.
> Then create a relationship between `Date[Date]` and `Data[order_date]`.

---

## Formatting Reference

| Measure | Format |
|---|---|
| Total Revenue | `$#,##0` |
| Gross Profit | `$#,##0` |
| Gross Margin % | `0.00%` |
| Avg Order Value | `$#,##0.00` |
| Return Rate | `0.00%` |
| YoY Growth % | `+0.00%;-0.00%;0.00%` |
| Avg Delivery Days | `0.0 "days"` |
| Repeat Rate | `0.00%` |
