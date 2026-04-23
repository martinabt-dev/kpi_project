import pandas as pd
import streamlit as st


retailers_df = pd.read_csv('C:/Users/User/Desktop/WBS/project_3/raw/retailers.csv', decimal=',')
methods_df = pd.read_csv('raw/methods.csv', decimal=',')
daily_sales_df = pd.read_csv('raw/daily_sales.csv', decimal=',')
products_df = pd.read_csv('raw/products.csv', decimal=',')

goexplore_df = daily_sales_df.merge(retailers_df, on='Retailer code', how='left')
goexplore_df = goexplore_df.merge(methods_df, on='Order method code', how='left')
goexplore_df = goexplore_df.merge(products_df, on='Product number', how='left')
st.write(goexplore_df)

# Revenue per Month
goexplore_df['Date'] = pd.to_datetime(goexplore_df['Date'], dayfirst=True)
result = goexplore_df.groupby(goexplore_df['Date'].dt.to_period('M'))['Unit price_x'].sum()
result.index = result.index.to_timestamp()
st.write("Revenue / month -> Unit price_x")
st.line_chart(result)

result = goexplore_df.groupby(goexplore_df['Date'].dt.to_period('M'))['Unit sale price'].sum()
result.index = result.index.to_timestamp()
st.write("Revenue / month -> Unit sale price")
st.line_chart(result)

# Most popular product categories
st.write("Most popular product categories")
pop_product_cat = goexplore_df.groupby(goexplore_df['Product type'])["Quantity"].sum()
st.write(pop_product_cat.sort_values(ascending=False))

# Countries with the highest return rates
st.write("Countries with the highest return rates")

# Countries with most orders
st.write("Countries with most orders")
pop_product_cat = goexplore_df.groupby(goexplore_df['Country'])["Product number"].count()
st.write(pop_product_cat.sort_values(ascending=False))

st.write(f"Number of Retailer: {goexplore_df['Retailer code'].nunique()}")
