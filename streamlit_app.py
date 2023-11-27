import streamlit as st
import requests
import csv

st.text('XIY')
url = st.text_input('Enter url')
response = requests.get(url)


