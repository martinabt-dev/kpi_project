import streamlit as st
from PIL import Image

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <a href="https://www.linkedin.com/in/martin-abt" target="_blank">
            <img src="https://media.licdn.com/dms/image/v2/D4D35AQFMM5rjc7GzoQ/profile-framedphoto-shrink_800_800/B4DZ2059PRGwAk-/0/1776856585487?e=1778583600&v=beta&t=KD1xf0Yn6ZHKHMEdc7qr2voWUxSCQ8kMZaMCJPL_gBY" width="200">
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
            <img src="https://media.licdn.com/dms/image/v2/D4E35AQGgy5ZPRTXTLg/profile-framedphoto-shrink_800_800/profile-framedphoto-shrink_800_800/0/1716149310893?e=1778583600&v=beta&t=bRpm2sBvnm05goz0QDhTVFlOwBaUqRs6mZn9FQCNf3A" width="200">
        </a>
        """,
        unsafe_allow_html=True
    )

    st.write("Liliana Elena Vinitchi")

st.divider()
st.write("#### Used tools:")

col4, col5, col6 = st.columns(3)

with col4:
    image = Image.open("python.jpg")
    st.image(image, caption="Python 3", use_container_width=True)
    image = Image.open("streamlit.png")
    st.image(image, caption="Streamlit", use_container_width=True)

with col5:
    image = Image.open("looker.png")
    st.image(image, caption="Looker Studio", use_container_width=True)

with col6:
    image = Image.open("sheets.png")
    st.image(image, caption="Google Sheets", use_container_width=True)
