import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <a href="https://www.linkedin.com/in/martin-abt" target="_blank">
            <img src="https://media.licdn.com/dms/image/v2/D4D35AQFMM5rjc7GzoQ/profile-framedphoto-shrink_800_800/B4DZ2059PRGwAk-/0/1776856585487?e=1777888800&v=beta&t=co6VJ5BRuxYqUp-SYhvdI1vcJb644dOokgCArYArZmg" width="200">
        </a>
        """,
        unsafe_allow_html=True
    )

    st.write("Martin Abt")

with col2:
    st.markdown(
        """
        <a href="https://www.linkedin.com/in/olaf-sierek-097a1a98/" target="_blank">
            <img src="https://media.licdn.com/dms/image/v2/C4D03AQG5Scks0LiFWg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1633078081416?e=1778716800&v=beta&t=iaS0lApLlSuUVG1r7zXkBt0zj8QmM0V-6IDGfvRz8oI" width="200">
        </a>
        """,
        unsafe_allow_html=True
    )

    st.write("Olaf Sierek")

with col3:
    st.markdown(
        """
        <a href="https://www.linkedin.com/in/liliana-elena-vinitchi-875195198/" target="_blank">
            <img src="https://media.licdn.com/dms/image/v2/D4E35AQGgy5ZPRTXTLg/profile-framedphoto-shrink_800_800/profile-framedphoto-shrink_800_800/0/1716149310893?e=1777892400&v=beta&t=tFQuzZ5-39SF2-8OU5WrgT1PVvhPCP4G5w5t3iL6hjY" width="200">
        </a>
        """,
        unsafe_allow_html=True
    )

    st.write("Liliana Elena Vinitchi")