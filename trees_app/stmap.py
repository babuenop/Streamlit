import streamlit as st
import pandas as pd
import numpy as np

st.title('ST MAP')
st.write('Display a map with points on it.\n'
         '\nThis is a wrapper around st.pydeck_chart to quickly create scatterplot charts on top of a map, with auto-centering and auto-zoom.')
df = pd.DataFrame(
     np.random.randn(50, 2) / [50, 50] + [8.5380, -80.7821],
     columns=['lat', 'lon'])

st.map(df)