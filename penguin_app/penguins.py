import streamlit as st 
import pandas as pd

st.title ("Palmer's penguin")

penguins_df = pd.read_csv('penguins.csv')
st.write(penguins_df.head())