"""
Superstore 電商營運分析 Dashboard
技術棧：Python + pandas + SQL + Plotly + Streamlit
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sqlite3

st.set_page_config(
    page_title="Superstore 營運分析",
    layout="wide"
)

st.title("Superstore 電商營運分析")
st.caption("資料來源：Sample Superstore | 技術：Python · SQL · Plotly · Streamlit")

@st.cache_data
def load_data():
    df = pd.read_csv("../data/superstore.csv", encoding="latin1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
    df["Profit Margin"] = df["Profit"] / df["Sales"]
    df["Ship Days"] = (df["Ship Date"] - df["Order Date"]).dt.days
    return df

df = load_data()

@st.cache_data
def run_sql(df, query):
    conn = sqlite3.connect(":memory:")
    df.to_sql("orders", conn, index=False, if_exists="replace")
    result = pd.read_sql(query, conn)
    conn.close()
    return result

# 側邊欄篩選器
st.sidebar.header("篩選條件")
selected_years = st.sidebar.multiselect("年份", sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))
selected_cats = st.sidebar.multiselect("品類", df["Category"].unique().tolist(), default=df["Category"].unique().tolist())
selected_regions = st.sidebar.multiselect("地區", df["Region"].unique().tolist(), default=df["Region"].unique().tolist())

filtered = df[
    df["Year"].isin(selected_years) &
    df["Category"].isin(selected_cats) &
    df["Region"].isin(selected_regions)
]

# KPI 指標
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
col1.metric("總銷售額",   f"${filtered['Sales'].sum():,.0f}")
col2.metric("總利潤",     f"${filtered['Profit'].sum():,.0f}")
col3.metric("平均利潤率", f"{filtered['Profit Margin'].mean():.1%}")
col4.metric("訂單數",     f"{filtered['Order ID'].nunique():,}")
st.markdown("---")

# 第一排圖表
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("月度銷售 & 利潤趨勢")
    monthly = run_sql(filtered, """
        SELECT Month,
               ROUND(SUM(Sales), 0) AS Sales,
               ROUND(SUM(Profit), 0) AS Profit
        FROM orders
        GROUP BY Month
        ORDER BY Month
    """)
    fig = go.Figure()
    fig.add_bar(x=monthly["Month"], y=monthly["Sales"], name="Sales", marker_color="#4C9BE8", opacity=0.7)
    fig.add_scatter(x=monthly["Month"], y=monthly["Profit"], name="Profit", mode="lines+markers", line=dict(color="#FF6B6B", width=2))
    fig.update_layout(height=350, margin=dict(t=20))
    st.plotly_chart(fig, use_container_width=True)

with row1_col2:
    st.subheader("子品類利潤率分析")
    cat_data = filtered.groupby(["Category", "Sub-Category"]).agg(
        Sales=("Sales", "sum"),
        AvgMarginPct=("Profit Margin", "mean")
    ).reset_index()
    cat_data["AvgMarginPct"] = cat_data["AvgMarginPct"] * 100
    cat_data = cat_data.sort_values("AvgMarginPct", ascending=True)
    fig2 = px.bar(cat_data, x="AvgMarginPct", y="Sub-Category", color="Category",
                  orientation="h", color_discrete_sequence=px.colors.qualitative.Set2)
    fig2.add_vline(x=0, line_dash="dash", line_color="red")
    fig2.update_layout(height=350, margin=dict(t=20))
    st.plotly_chart(fig2, use_container_width=True)

# 第二排圖表
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("折扣率 vs 利潤率")
    fig3 = px.scatter(filtered, x="Discount", y="Profit Margin", color="Category",
                      opacity=0.5, size="Sales", size_max=15,
                      color_discrete_sequence=px.colors.qualitative.Set1)
    fig3.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="損益兩平")
    fig3.update_layout(height=350, margin=dict(t=20))
    st.plotly_chart(fig3, use_container_width=True)

with row2_col2:
    st.subheader("地區銷售與利潤")
    region_data = filtered.groupby("Region").agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    ).reset_index()
    fig4 = px.bar(region_data, x="Region", y=["Sales", "Profit"],
                  barmode="group", color_discrete_sequence=["#4C9BE8", "#FF6B6B"])
    fig4.update_layout(height=350, margin=dict(t=20))
    st.plotly_chart(fig4, use_container_width=True)

# 商業洞察
st.markdown("---")
st.subheader("商業洞察")

high_disc = filtered[filtered["Discount"] > 0.4]["Profit Margin"].mean()
no_disc = filtered[filtered["Discount"] == 0]["Profit Margin"].mean()
worst_sub = filtered.groupby("Sub-Category")["Profit"].sum().sort_values().index[0]

col_a, col_b, col_c = st.columns(3)
col_a.info(f"**折扣陷阱**\n\n高折扣(>40%)訂單平均利潤率為 {high_disc:.1%}，無折扣訂單為 {no_disc:.1%}，差距顯著。")
col_b.warning(f"**虧損品項**\n\n{worst_sub} 是總利潤最差的子品類，建議檢討定價策略。")
col_c.success("**建議行動**\n\n限制高折扣訂單比例，聚焦高利潤率品類，優化季末促銷策略。")

with st.expander("查看原始資料"):
    st.dataframe(filtered.head(100), use_container_width=True)
