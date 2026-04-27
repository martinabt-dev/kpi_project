import streamlit as st
import plotly.express as px
from data_loader import load_data

goexplore_df = load_data()

col1, col2, col3 = st.columns(3)
with col1:
    fig = px.scatter(
        goexplore_df,
        x="revenue",
        y="profit",
        color="Product type"
    )
    st.plotly_chart(fig)

col5, col6 = st.columns(2)


#st.components.v1.iframe(
#    "https://lookerstudio.google.com/embed/reporting/XXXX/page/XXXX",
#    height=600
#)