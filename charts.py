import plotly.express as px

def revenue_by_region(df):
    data = df.groupby("Region")["Sales"].sum().reset_index()
    fig = px.bar(data, x="Region", y="Sales", title="Revenue by Region",
                 color="Region", color_discrete_sequence=px.colors.qualitative.Set2)
    return fig

def monthly_sales_trend(df):
    df["Order Date"] = df["Order Date"].astype(str)
    import pandas as pd
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
    data = df.groupby("Month")["Sales"].sum().reset_index()
    fig = px.line(data, x="Month", y="Sales", title="Monthly Sales Trend",
                  markers=True, color_discrete_sequence=["#00CC96"])
    fig.update_xaxes(tickangle=45)
    return fig

def profit_by_category(df):
    data = df.groupby("Category")["Profit"].sum().reset_index()
    fig = px.bar(data, x="Profit", y="Category", orientation="h",
                 title="Profit by Category", color="Category",
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    return fig

def top_products(df):
    data = df.groupby("Sub-Category")["Profit"].sum().reset_index()
    data = data.sort_values("Profit", ascending=False).head(10)
    fig = px.bar(data, x="Profit", y="Sub-Category", orientation="h",
                 title="Top 10 Sub-Categories by Profit",
                 color="Profit", color_continuous_scale="Teal")
    return fig

def sales_vs_profit(df):
    fig = px.scatter(df, x="Sales", y="Profit", color="Category",
                     title="Sales vs Profit", hover_data=["Product Name"],
                     color_discrete_sequence=px.colors.qualitative.Bold)
    return fig