import streamlit as st
import plotly.express as px
from data_loader import load_data

goexplore_df = load_data()

st.set_page_config(layout="wide")

# st.write(goexplore_df)
st.write(goexplore_df.describe())
st.write(f"Number of different Retailer: {goexplore_df['Retailer name'].nunique()}")
col1, col2, col3, col4 = st.columns(4)
group = {
    "Month" : goexplore_df['Date'].dt.to_period('M'),
    "Quarter" : goexplore_df['Date'].dt.to_period('Q'),
    "Year" : goexplore_df['Date'].dt.to_period('Y'),
    "Country" : "Country",
    "Retailer" : "Retailer name",
    "Retailer Type" : "Type",
    "Product" : "Product",
    "Product type" : "Product type",
    "Order Method" : "Order method type"
}

agg = {
    "Min" : "min",
    "Max" : "max",
    "Count" : "count",
    "Sum" : "sum",
    "Median" : "median",
    "Mean" : "mean"
}

columns = {
    "Quantity" : "Quantity",
    "Unit price" : "Unit price_x",
    "Unit sale price" : "Unit sale price",
    "Unit cost" : "Unit cost",
    "Revenue" : "revenue",
    "Discount" : "discount",
    "Profit" : "profit",
    "Gross Margin" : "gross_margin_%"
}

with col1:
    group_choice = st.selectbox("Group", group)

with col2:
    group["None"] = "none"
    group_choice2 = st.selectbox("Group", group)

with col3:
    agg_choice = st.selectbox("Aggregation", agg)

with col4:
    column_choice = st.selectbox("Column", columns)

if group_choice2 == "None":
    result = goexplore_df.groupby(group[group_choice]).agg(choice = (columns[column_choice], agg[agg_choice]))
    st.write(result)
    if group_choice in ["Month", "Year", "Quarter"]:
        result.index = result.index.to_timestamp()
        st.line_chart(result)
    elif group_choice == "Country":
        result_df = result.reset_index()
        result_df.columns = ["Country", f"{agg_choice} {column_choice}"]
        fig = px.choropleth(
            result_df,
            locations="Country",
            locationmode="country names",
            color=f"{agg_choice} {column_choice}",
            color_continuous_scale="Blues"
        )
        st.plotly_chart(fig)
else:
    result = goexplore_df.groupby([group[group_choice], group[group_choice2]]).agg(choice=(columns[column_choice], agg[agg_choice]))
    st.write(result)