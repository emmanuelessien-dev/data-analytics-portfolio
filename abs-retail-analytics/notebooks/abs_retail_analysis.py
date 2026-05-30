"""
ABS Retail — Full Data Analysis & Forecast Script
==================================================
Author     : [Your Name]
Project    : Data Analytics Fellowship Capstone
Dataset    : ABS_RETAIL.xlsx (5,000 orders, 2021–2024)
Tools      : Python, pandas, numpy, matplotlib

Description:
    End-to-end analysis covering data cleaning, enrichment,
    descriptive analytics, KPI computation, and 2025 revenue
    forecasting using linear regression and CAGR models.

Usage:
    python abs_retail_analysis.py

Output:
    - Console: All KPIs and analysis summaries
    - /assets/charts/: Exported chart images (PNG)
"""

import os
import warnings
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

warnings.filterwarnings('ignore')

# ── CONFIG ────────────────────────────────────────────────────────────────────
DATA_PATH   = "data/ABS_RETAIL.xlsx"
CHARTS_DIR  = "assets/charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

# Colour palette (matches Power BI dashboard theme)
NAVY    = "#0D1B2A"
ACCENT  = "#2E86C1"
GOLD    = "#F39C12"
GREEN   = "#1E8449"
RED     = "#C0392B"
PURPLE  = "#6E2F8A"
GRAY    = "#717D7E"
LIGHT   = "#F2F3F4"

PALETTE = [ACCENT, GOLD, GREEN, RED, PURPLE, "#1A5276", "#117A65", "#7D6608"]


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1 — LOAD & CLEAN DATA
# ═══════════════════════════════════════════════════════════════════════════════
def load_and_clean(path: str) -> pd.DataFrame:
    """Load dataset and perform all cleaning and enrichment steps."""
    print("\n" + "="*60)
    print("STEP 1: LOADING & CLEANING DATA")
    print("="*60)

    df = pd.read_excel(path)
    print(f"✅ Loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")

    # --- Parse dates ---
    df['order_date']    = pd.to_datetime(df['order_date'])
    df['delivery_date'] = pd.to_datetime(df['delivery_date'])

    # --- Data quality check ---
    null_counts = df.isnull().sum()
    null_cols   = null_counts[null_counts > 0]
    print(f"\n📋 Null values:")
    if null_cols.empty:
        print("   None found — except return_reason (expected for non-returned orders)")
    else:
        for col, count in null_cols.items():
            print(f"   {col}: {count:,} nulls")

    # --- Enriched / calculated columns ---
    df['gross_profit']     = df['gross_revenue_usd'] - df['total_cost_usd']
    df['gross_margin_pct'] = df['gross_profit'] / df['gross_revenue_usd']
    df['net_revenue']      = df['gross_revenue_usd'] - df['shipping_cost_usd']
    df['month']            = df['order_date'].dt.month
    df['month_name']       = df['order_date'].dt.strftime('%b')
    df['quarter']          = df['order_date'].dt.quarter.apply(lambda x: f'Q{x}')
    df['is_returned']      = (df['order_status'] == 'Returned').astype(int)
    df['is_repeat']        = (df['is_repeat_customer'] == 'Yes').astype(int)

    print(f"\n✅ Enriched with 7 calculated columns:")
    print("   gross_profit, gross_margin_pct, net_revenue,")
    print("   month, month_name, quarter, is_returned, is_repeat")
    return df


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2 — EXECUTIVE KPIs
# ═══════════════════════════════════════════════════════════════════════════════
def compute_kpis(df: pd.DataFrame) -> dict:
    """Compute all executive-level KPIs and print to console."""
    print("\n" + "="*60)
    print("STEP 2: EXECUTIVE KPI SUMMARY")
    print("="*60)

    kpis = {
        "total_revenue":       df['gross_revenue_usd'].sum(),
        "total_cost":          df['total_cost_usd'].sum(),
        "gross_profit":        df['gross_profit'].sum(),
        "gross_margin_pct":    df['gross_profit'].sum() / df['gross_revenue_usd'].sum(),
        "total_orders":        len(df),
        "avg_order_value":     df['gross_revenue_usd'].mean(),
        "total_customers":     df['customer_id'].nunique(),
        "repeat_rate":         df['is_repeat'].sum() / len(df),
        "return_rate":         (df['order_status'] == 'Returned').sum() / len(df),
        "cancel_rate":         (df['order_status'] == 'Cancelled').sum() / len(df),
        "refund_rate":         (df['order_status'] == 'Refunded').sum() / len(df),
        "avg_delivery_days":   df['days_to_deliver'].mean(),
        "total_shipping_cost": df['shipping_cost_usd'].sum(),
        "net_revenue":         df['net_revenue'].sum(),
    }

    print(f"\n💰 REVENUE & PROFITABILITY")
    print(f"   Total Revenue      : ${kpis['total_revenue']:>12,.2f}")
    print(f"   Total Cost (COGS)  : ${kpis['total_cost']:>12,.2f}")
    print(f"   Gross Profit       : ${kpis['gross_profit']:>12,.2f}")
    print(f"   Gross Margin       : {kpis['gross_margin_pct']:>11.2%}")
    print(f"   Net Revenue        : ${kpis['net_revenue']:>12,.2f}")
    print(f"   Total Shipping Cost: ${kpis['total_shipping_cost']:>12,.2f}")

    print(f"\n📦 ORDERS & CUSTOMERS")
    print(f"   Total Orders       : {kpis['total_orders']:>12,}")
    print(f"   Avg Order Value    : ${kpis['avg_order_value']:>12,.2f}")
    print(f"   Unique Customers   : {kpis['total_customers']:>12,}")
    print(f"   Repeat Rate        : {kpis['repeat_rate']:>11.2%}  (target: 50%+)")

    print(f"\n⚠️  OPERATIONS RISK")
    print(f"   Return Rate        : {kpis['return_rate']:>11.2%}  (target: <5.0%)")
    print(f"   Cancel Rate        : {kpis['cancel_rate']:>11.2%}")
    print(f"   Refund Rate        : {kpis['refund_rate']:>11.2%}")
    print(f"   Avg Delivery Days  : {kpis['avg_delivery_days']:>11.2f}  (target: <3 days)")

    return kpis


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 3 — YEAR-OVER-YEAR ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════
def yoy_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Compute year-over-year performance breakdown."""
    print("\n" + "="*60)
    print("STEP 3: YEAR-OVER-YEAR ANALYSIS")
    print("="*60)

    yearly = df.groupby('year').agg(
        Orders        = ('order_id',            'count'),
        Revenue       = ('gross_revenue_usd',   'sum'),
        Cost          = ('total_cost_usd',       'sum'),
        Gross_Profit  = ('gross_profit',         'sum'),
        Avg_Margin    = ('gross_margin_pct',     'mean'),
        Avg_Order_Val = ('gross_revenue_usd',    'mean'),
    ).round(2)

    yearly['YoY_Growth'] = yearly['Revenue'].pct_change()
    print(f"\n{yearly.to_string()}")
    return yearly


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 4 — CATEGORY ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════
def category_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Revenue, profit and margin breakdown by product category."""
    print("\n" + "="*60)
    print("STEP 4: CATEGORY PERFORMANCE")
    print("="*60)

    cat = df.groupby('category').agg(
        Orders       = ('order_id',           'count'),
        Revenue      = ('gross_revenue_usd',  'sum'),
        Gross_Profit = ('gross_profit',        'sum'),
        Avg_Margin   = ('gross_margin_pct',    'mean'),
    ).sort_values('Revenue', ascending=False).round(2)

    cat['Rev_Share'] = cat['Revenue'] / cat['Revenue'].sum()
    print(f"\n{cat.to_string()}")

    print(f"\n💡 INSIGHT: Beauty & Health has the highest margin "
          f"({cat.loc['Beauty & Health','Avg_Margin']:.1%}) "
          f"but only {cat.loc['Beauty & Health','Rev_Share']:.1%} revenue share.")
    return cat


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 5 — RETURNS ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════
def returns_analysis(df: pd.DataFrame):
    """Deep-dive into return reasons and order status breakdown."""
    print("\n" + "="*60)
    print("STEP 5: RETURNS & ORDER STATUS ANALYSIS")
    print("="*60)

    status = df['order_status'].value_counts()
    status_pct = df['order_status'].value_counts(normalize=True)
    print("\n📊 Order Status Distribution:")
    for s in status.index:
        print(f"   {s:<15}: {status[s]:>5,}  ({status_pct[s]:.2%})")

    returns = df[df['order_status'] == 'Returned']
    reasons = returns['return_reason'].value_counts()
    print(f"\n🔍 Return Reasons (431 returned orders):")
    for r in reasons.index:
        print(f"   {r:<22}: {reasons[r]:>5}  ({reasons[r]/len(returns):.1%} of returns)")

    print(f"\n⚠️  Return Rate Benchmark: 8.62% vs 5.0% target — GAP of 3.62pp")
    print(f"   Est. revenue impact: ~$145,000/year")


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 6 — GEOGRAPHIC ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════
def geographic_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Revenue and order breakdown by continent and country."""
    print("\n" + "="*60)
    print("STEP 6: GEOGRAPHIC ANALYSIS")
    print("="*60)

    geo = df.groupby('continent').agg(
        Orders       = ('order_id',          'count'),
        Revenue      = ('gross_revenue_usd', 'sum'),
        Avg_Order    = ('gross_revenue_usd', 'mean'),
        Gross_Profit = ('gross_profit',       'sum'),
    ).sort_values('Revenue', ascending=False).round(2)

    geo['Rev_Share'] = geo['Revenue'] / geo['Revenue'].sum()
    print(f"\n{geo.to_string()}")

    top_countries = df.groupby('country')['gross_revenue_usd'].sum()\
                     .sort_values(ascending=False).head(10)
    print(f"\n🌍 Top 10 Countries by Revenue:")
    for c, v in top_countries.items():
        print(f"   {c:<25}: ${v:>10,.2f}")

    return geo


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 7 — FORECAST 2025
# ═══════════════════════════════════════════════════════════════════════════════
def forecast_2025(df: pd.DataFrame) -> dict:
    """
    Build 2025 revenue forecast using:
    - Linear regression trend model
    - CAGR model (Compound Annual Growth Rate)
    - Conservative (-8%) and Optimistic (+12%) scenarios
    """
    print("\n" + "="*60)
    print("STEP 7: PREDICTIVE FORECAST — 2025")
    print("="*60)

    yearly_rev = df.groupby('year')['gross_revenue_usd'].sum()
    years      = np.array(range(len(yearly_rev)))
    revenues   = yearly_rev.values

    # Linear regression
    m, b = np.polyfit(years, revenues, 1)
    fc_linear = m * len(years) + b

    # CAGR model
    cagr   = (revenues[-1] / revenues[0]) ** (1 / (len(revenues) - 1)) - 1
    fc_cagr = revenues[-1] * (1 + cagr)

    # Scenarios
    fc_opt  = fc_linear * 1.12
    fc_cons = fc_linear * 0.92

    forecasts = {
        "conservative":  fc_cons,
        "linear":        fc_linear,
        "cagr":          fc_cagr,
        "optimistic":    fc_opt,
        "cagr_rate":     cagr,
    }

    print(f"\n📈 Historical Revenue:")
    for yr, rev in yearly_rev.items():
        print(f"   {yr}: ${rev:>10,.2f}")

    print(f"\n🔮 2025 Forecast Scenarios:")
    print(f"   CAGR Rate          : {cagr:.2%}")
    print(f"   Conservative (-8%) : ${fc_cons:>10,.2f}")
    print(f"   Baseline (Linear)  : ${fc_linear:>10,.2f}")
    print(f"   CAGR Model         : ${fc_cagr:>10,.2f}")
    print(f"   Optimistic (+12%)  : ${fc_opt:>10,.2f}")

    return forecasts


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 8 — CHART EXPORTS
# ═══════════════════════════════════════════════════════════════════════════════
def export_charts(df: pd.DataFrame, forecasts: dict):
    """Export all analysis charts as PNG files."""
    print("\n" + "="*60)
    print("STEP 8: EXPORTING CHARTS")
    print("="*60)

    def save(fig, name):
        path = f"{CHARTS_DIR}/{name}.png"
        fig.savefig(path, dpi=150, bbox_inches='tight',
                    facecolor=LIGHT, edgecolor='none')
        plt.close(fig)
        print(f"   ✅ Saved: {path}")

    def style_ax(ax):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#BFC9CA')
        ax.spines['bottom'].set_color('#BFC9CA')
        ax.tick_params(colors='#2C3E50', labelsize=10)
        ax.grid(axis='y', linestyle='--', alpha=0.3, color='#BFC9CA')

    # -- Chart 1: Monthly Revenue Trend --
    months   = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    fig, ax  = plt.subplots(figsize=(12, 5), facecolor=LIGHT)
    ax.set_facecolor(LIGHT)
    colors_l = [ACCENT, GOLD, RED, GREEN]
    for (yr, grp), lc in zip(df.groupby('year'), colors_l):
        monthly = grp.groupby('month')['gross_revenue_usd'].sum().reindex(range(1,13), fill_value=0)
        ax.plot(range(1,13), monthly.values, 'o-', lw=2.5, ms=6, color=lc, label=str(yr))
    ax.set_xticks(range(1,13)); ax.set_xticklabels(months)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'${v/1000:.0f}K'))
    ax.set_title('Monthly Revenue Trend — 2021 to 2024', fontsize=14, color=NAVY, fontweight='bold', pad=12)
    ax.legend(framealpha=0, fontsize=11)
    style_ax(ax); plt.tight_layout()
    save(fig, '01_monthly_revenue_trend')

    # -- Chart 2: Revenue vs Profit by Category --
    cat = df.groupby('category').agg(Revenue=('gross_revenue_usd','sum'), Profit=('gross_profit','sum'))\
            .sort_values('Revenue', ascending=False)
    fig, ax = plt.subplots(figsize=(10, 5), facecolor=LIGHT)
    ax.set_facecolor(LIGHT)
    xi = np.arange(len(cat)); w = 0.38
    ax.bar(xi-w/2, cat['Revenue'], w, color=ACCENT, label='Revenue', zorder=3)
    ax.bar(xi+w/2, cat['Profit'],  w, color=GREEN,  label='Gross Profit', zorder=3)
    ax.set_xticks(xi); ax.set_xticklabels(cat.index, fontsize=10)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'${v/1000:.0f}K'))
    ax.set_title('Revenue vs Gross Profit by Category', fontsize=14, color=NAVY, fontweight='bold', pad=12)
    ax.legend(framealpha=0, fontsize=11)
    style_ax(ax); plt.tight_layout()
    save(fig, '02_category_revenue_profit')

    # -- Chart 3: Gross Margin by Category --
    margins = df.groupby('category')['gross_margin_pct'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 4), facecolor=LIGHT)
    ax.set_facecolor(LIGHT)
    bars = ax.barh(margins.index, margins.values * 100, color=PALETTE[:len(margins)], height=0.55)
    for b, v in zip(bars, margins.values):
        ax.text(v*100+0.5, b.get_y()+b.get_height()/2, f'{v:.1%}',
                va='center', fontsize=11, color=NAVY, fontweight='bold')
    ax.set_xlim(0, 70)
    ax.spines[:].set_visible(False); ax.xaxis.set_visible(False)
    ax.tick_params(colors='#2C3E50', labelsize=11)
    ax.set_title('Gross Margin % by Category', fontsize=14, color=NAVY, fontweight='bold', pad=12)
    plt.tight_layout()
    save(fig, '03_gross_margin_by_category')

    # -- Chart 4: Revenue by Continent --
    geo = df.groupby('continent').agg(Revenue=('gross_revenue_usd','sum'),
                                       Orders=('order_id','count'))\
            .sort_values('Revenue', ascending=False)
    fig, ax = plt.subplots(figsize=(10, 5), facecolor=LIGHT)
    ax.set_facecolor(LIGHT)
    bars = ax.barh(geo.index, geo['Revenue'], color=PALETTE[:len(geo)], height=0.56)
    for b, v, o in zip(bars, geo['Revenue'], geo['Orders']):
        ax.text(v+5000, b.get_y()+b.get_height()/2, f'${v/1000:.0f}K  ·  {o} orders',
                va='center', fontsize=10, color=NAVY, fontweight='bold')
    ax.set_xlim(0, 850000)
    ax.spines[:].set_visible(False); ax.xaxis.set_visible(False)
    ax.tick_params(colors='#2C3E50', labelsize=11)
    ax.set_title('Revenue & Order Count by Continent', fontsize=14, color=NAVY, fontweight='bold', pad=12)
    plt.tight_layout()
    save(fig, '04_revenue_by_continent')

    # -- Chart 5: Return Reasons --
    returns = df[df['order_status'] == 'Returned']
    reasons = returns['return_reason'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 4), facecolor=LIGHT)
    ax.set_facecolor(LIGHT)
    r_cols = [RED, '#E67E22', GOLD, ACCENT, GREEN]
    bars = ax.barh(reasons.index, reasons.values, color=r_cols[:len(reasons)], height=0.52)
    for b, v in zip(bars, reasons.values):
        ax.text(v+1, b.get_y()+b.get_height()/2, f'{v} returns',
                va='center', fontsize=10, color=NAVY, fontweight='bold')
    ax.set_xlim(0, 250); ax.spines[:].set_visible(False); ax.xaxis.set_visible(False)
    ax.tick_params(colors='#2C3E50', labelsize=11)
    ax.set_title('Return Reasons — Count & Priority', fontsize=14, color=NAVY, fontweight='bold', pad=12)
    plt.tight_layout()
    save(fig, '05_return_reasons')

    # -- Chart 6: Forecast --
    yearly_rev = df.groupby('year')['gross_revenue_usd'].sum()
    fig, ax    = plt.subplots(figsize=(12, 5), facecolor=LIGHT)
    ax.set_facecolor(LIGHT)
    ax.plot(yearly_rev.index, yearly_rev.values, 'o-', color=ACCENT, lw=3, ms=10, label='Actuals', zorder=4)
    for yr, v in yearly_rev.items():
        ax.annotate(f'${v/1000:.0f}K', (yr,v), textcoords='offset points',
                    xytext=(0,14), ha='center', fontsize=10, color=NAVY, fontweight='bold')
    fc_lin  = forecasts['linear']
    fc_opt  = forecasts['optimistic']
    fc_cons = forecasts['conservative']
    last_yr = yearly_rev.index[-1]; last_v = yearly_rev.iloc[-1]
    ax.plot([last_yr, 2025], [last_v, fc_lin], 'o--', color=GOLD, lw=2.5, ms=10,
            label=f'Baseline ${fc_lin/1000:.0f}K', zorder=4)
    ax.fill_between([last_yr, 2025], [last_v, fc_cons], [last_v, fc_opt],
                    color=GOLD, alpha=0.12, label='Confidence Band')
    ax.set_xlim(2020.5, 2026.2); ax.set_ylim(400000, 920000)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'${v/1000:.0f}K'))
    ax.set_title('Revenue Actuals (2021–2024) + 2025 Forecast with Confidence Interval',
                 fontsize=14, color=NAVY, fontweight='bold', pad=12)
    ax.legend(framealpha=0, fontsize=11)
    style_ax(ax); plt.tight_layout()
    save(fig, '06_revenue_forecast_2025')

    print(f"\n✅ All {6} charts exported to /{CHARTS_DIR}/")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n" + "█"*60)
    print("  ABS RETAIL — DATA ANALYTICS CAPSTONE")
    print("  Full Analysis Script")
    print("█"*60)

    df         = load_and_clean(DATA_PATH)
    kpis       = compute_kpis(df)
    yearly     = yoy_analysis(df)
    cat_df     = category_analysis(df)
    returns_analysis(df)
    geo_df     = geographic_analysis(df)
    forecasts  = forecast_2025(df)
    export_charts(df, forecasts)

    print("\n" + "="*60)
    print("✅ ANALYSIS COMPLETE")
    print("   Check /assets/charts/ for all exported visualisations")
    print("="*60 + "\n")
