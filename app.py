import streamlit as st
import pandas as pd
from data_loader import load_data, get_kpis, apply_filters
from charts import revenue_by_region, monthly_sales_trend, profit_by_category, top_products, sales_vs_profit

st.set_page_config(page_title="Superstore KPI Dashboard", page_icon="📊", layout="wide")

st.title("📊 Superstore Business KPI Dashboard")
st.markdown("Interactive dashboard analyzing 10,000+ sales records across revenue, profit, and regional KPIs.")

# Load data
df = load_data()
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Year"] = df["Order Date"].dt.year

# Sidebar filters
st.sidebar.header("🔍 Filters")
regions = st.sidebar.multiselect("Region", df["Region"].unique())
categories = st.sidebar.multiselect("Category", df["Category"].unique())
years = st.sidebar.multiselect("Year", sorted(df["Year"].unique()))

filtered_df = apply_filters(df.copy(), regions, categories, years)

# KPI Cards
st.subheader("Key Performance Indicators")
total_revenue, total_profit, avg_margin, total_orders = get_kpis(filtered_df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
col3.metric("📊 Avg Margin", f"{avg_margin:.1f}%")
col4.metric("🛒 Total Orders", f"{total_orders:,}")

st.divider()

# Charts Row 1
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(revenue_by_region(filtered_df), use_container_width=True)
with col2:
    st.plotly_chart(monthly_sales_trend(filtered_df), use_container_width=True)

# Charts Row 2
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(profit_by_category(filtered_df), use_container_width=True)
with col2:
    st.plotly_chart(top_products(filtered_df), use_container_width=True)

# Charts Row 3
st.plotly_chart(sales_vs_profit(filtered_df), use_container_width=True)

st.divider()

# Data Table
st.subheader("📋 Raw Data Explorer")
st.dataframe(filtered_df[["Order Date", "Region", "Category", "Sub-Category",
                            "Product Name", "Sales", "Profit"]].reset_index(drop=True),
             use_container_width=True)