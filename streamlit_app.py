import streamlit as st


st.text('XIY')
url = st.text_input('Enter url')
response = requests.get(url)


