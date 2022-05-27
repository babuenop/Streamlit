'''
This app simulates 1000 coins flips and stores those 
values in a list we call binom_dist. 
When the sample (with replacement) 100 from that list, 
take the mean, and stores thatr mean inthe cleverly named list_of_means.
'''

import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt 

st.title('Illustrating the Central Limit Theorem with Streamlit')

perc_heads = st.number_input (label='Chance of coins landing on Heads', min_value = 0.0, max_value = 1.0, value = .25)
graph_title = st.text_input (label='Graph Title')
binom_dist = np.random.binomial(1, perc_heads ,1000)

list_of_means =[]
for i in range (0,1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())

fig, ax = plt.subplots()
ax = plt.hist(list_of_means)
plt.title(graph_title)
st.pyplot(fig)

#fig2, ax2 = plt.subplots()
#ax2 = plt.hist([1,1,1,1])
#st.pyplot(fig2)


