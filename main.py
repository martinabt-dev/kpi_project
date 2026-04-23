import pandas as pd
import streamlit as st

# import csv files as df
retailers_df = pd.read_csv('raw/retailers.csv', decimal=',')
methods_df = pd.read_csv('raw/methods.csv', decimal=',')
daily_sales_df = pd.read_csv('raw/daily_sales.csv', decimal=',')
products_df = pd.read_csv('raw/products.csv', decimal=',')

goexplore_df = daily_sales_df.merge(retailers_df, on='Retailer code', how='left')
goexplore_df = goexplore_df.merge(methods_df, on='Order method code', how='left')
goexplore_df = goexplore_df.merge(products_df, on='Product number', how='left')
goexplore_df['Date'] = pd.to_datetime(goexplore_df['Date'], dayfirst=True)
# st.write(goexplore_df)

st.set_page_config(layout="wide")
col1, col2, col3 = st.columns(3)
group = {
    "Month" : goexplore_df['Date'].dt.to_period('M'),
    "Quarter" : goexplore_df['Date'].dt.to_period('Q'),
    "Year" : goexplore_df['Date'].dt.to_period('Y'),
    "Country" : "Country",
    "Retailer" : "Retailer name",
    "Retailer Type" : "Type",
    "Product" : "Product",
    "Product type" : "Product type"
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
    "Unit sale price" : "Unit sale price"
}

with col1:
    group_choice = st.selectbox("Group", group)

with col2:
    agg_choice = st.selectbox("Aggregation", agg)

with col3:
    column_choice = st.selectbox("Column", columns)

result = goexplore_df.groupby(group[group_choice]).agg(choice = (columns[column_choice], agg[agg_choice]))
st.write(result)

if group_choice in ["Month", "Year", "Quarter"]:
    result.index = result.index.to_timestamp()
    st.line_chart(result)
