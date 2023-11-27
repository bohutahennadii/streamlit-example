import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


num_points = st.selectbox('Select', [1,2,3])
num_turns = st.slider('Slide me', min_value=0, max_value=10)
