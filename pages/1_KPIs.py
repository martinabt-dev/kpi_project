import streamlit as st
import plotly.express as px
from data_loader import load_data

goexplore_df = load_data()

col1, col2, col3 = st.columns(3)
with col1:
    st.write("#### 1. Monthly revenue growth rate by country")
    st.write("Target a minimum 5% monthly revenue growth in each new country during the first 12 months post-launch.")
    st.write("Task to do: Reviewed at the end of each calendar month for every country in the expansion plan.")

    st.write("#### 4. Average order value")
    st.write("Increase AOV by 10% in each new country within the first 9 months of operation.")
    st.write("Task to do: Tracked and reported monthly for each country.")

with col2:
    st.write("#### 2. Country profit margin target")
    st.write("Maintain a minimum profit margin of 15% in each country within 6 months of market entry.")
    st.write("Task to do: Calculated and reviewed monthly for each country.")

    st.write("#### 5. Labor cost as a percentage of profit")
    st.write("Maintain labor cost below 30% of total profit in each country within 12 months of expansion.")
    st.write("Task to do: Calculated and reviewed monthly for each country and overall.")

with col3:
    st.write("#### 3. Preferred Order Method Penetration")
    st.write("Achieve at least 50% of all orders through the preferred channel in each country within the first 6 months.")
    st.write("Task to do: Assessed monthly for each country.")

    st.write("#### 6. Revenue and profit comparison between product categories")
    st.write("Ensure that at least 70% of total monthly profit comes from the top 3 product categories within 12 months of expansion.")
    st.write("Task to do: Calculated and reviewed monthly for each product category.")

    fig = px.scatter(
        goexplore_df,
        x="revenue",
        y="profit",
        color="Product type"
    )
    st.plotly_chart(fig)

