import pandas as pd
import sqlite3

def load_data():
    df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
    conn = sqlite3.connect("superstore.db")
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()
    return df

def get_connection():
    return sqlite3.connect("superstore.db")

def get_kpis(df):
    total_revenue = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    avg_margin = (df["Profit"] / df["Sales"]).mean() * 100
    total_orders = df["Order ID"].nunique()
    return total_revenue, total_profit, avg_margin, total_orders

def apply_filters(df, regions, categories, years):
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Year"] = df["Order Date"].dt.year
    if regions:
        df = df[df["Region"].isin(regions)]
    if categories:
        df = df[df["Category"].isin(categories)]
    if years:
        df = df[df["Year"].isin(years)]
    return df