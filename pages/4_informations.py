import streamlit as st

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

with col1:
    is_discount = st.button("Discount", use_container_width=True)
with col2:
    is_gross = st.button("Gross margin", use_container_width=True)
with col3:
    is_profit = st.button("Profit", use_container_width=True)
with col4:
    is_profitmargin = st.button("Profit margin", use_container_width=True)
with col5:
    is_revenue = st.button("Revenue", use_container_width=True)

if is_discount:
    st.subheader("Discount")
    st.write("#### Formula: Discount = Unit price - Unit sale price")
    st.write("A key pricing adjustment metric used to influence demand, conversion rates, and stakeholder optimism.")
    st.write("Represents the gap between perceived value and actual price paid.")
    st.write("Frequently monitored in dashboards to explain why revenue is slightly lower than forecasted but strategically acceptable.")
elif is_gross:
    st.subheader("Gross margin")
    st.write("#### Formula: Gross margin in % = (Unit sale price - Unit cost) / Unit sale price * 100")
    st.write("A core profitability metric that measures how much revenue remains after subtracting the direct cost of goods sold.")
    st.write("It reflects how efficiently a company turns sales into actual earnings before accounting for overhead, marketing, and other operating expenses.")
    st.write("Often used to evaluate pricing power, cost control, and overall business health.")
    st.write("In dashboards, it quietly reveals whether growth is actually profitable or just expensive revenue.")
elif is_profit:
    st.subheader("Profit")
    st.write("#### Formula: Profit = (Unit sale price - Unit cost) * Quantity")
    st.write("The final financial reality check after all revenues, costs, discounts, and ambitions have been accounted for.")
    st.write("It represents what is actually left over when the business stops spending money to make money.")
    st.write("Often used as the ultimate “yes or no” metric for whether a strategy worked or just looked good in slides.")
    st.write("In dashboards, it tells the uncomfortable truth that revenue alone politely avoids mentioning.")
elif is_profitmargin:
    st.subheader("Profit margin")
    st.write("#### Formula: Profit margin = (Unit sale price - Unit cost) / Unit sale price * 100")
    st.write("A key efficiency metric that shows what percentage of revenue actually turns into profit after all costs are accounted for.")
    st.write("It reflects how effectively a business converts sales into real earnings, not just top-line growth.")
    st.write("Often used to compare performance across products, periods, or companies regardless of size.")
    st.write("In dashboards, it quietly answers the question: “Are we making money, or just moving it around?”")
elif is_revenue:
    st.subheader("Revenue")
    st.write("#### Formula: Revenue = Quantity * Unit sale price")
    st.write("The total amount of money generated from sales before costs, discounts, and financial reality begin to interfere.")
    st.write("It represents the top line of the business and is often the first number people celebrate in meetings.")
    st.write("While revenue signals demand and growth, it says very little about how much money is actually being kept.")
    st.write("In dashboards, it is the optimistic headline that profit later edits for accuracy.")



