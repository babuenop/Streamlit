import streamlit as st
import numpy as np
st.write('Hello World')

binom_dist = np.random.binomial(1,.5,100)
st.write(np.mean(binom_dist))