from select import select
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

st.title ("Palmer's penguin")
st.markdown('Use  this Streamlit app to make your own scatterplot abou penguins!')

selected_species = st.selectbox('What species would you like to visualize?', ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do want the x variable to be?',['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 
'body_mass_g'] )
selected_y_var = st.selectbox('What about the y?',['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 
'body_mass_g'] )

# Uploaded_file 

penguin_file = st.file_uploader('Select your Local Penguins CSV')

# El siguiente codigo usa un condicional if-else con st.stop() en else 
# para prevenir la entrada al app cuando esta corriendo el st.file_uploader() esta sin uso. 

if penguin_file is not None:
    penguins_df = pd.read_csv('penguins.csv')
else: 
    st.stop()

# penguins_df = pd.read_csv('penguins.csv')
# st.write(penguins_df.head())

sns.set_style('darkgrid')
markers = {'Adelie': "X", "Gentoo":"s", "Chinstrap":'o'}

fig, ax = plt.subplots()
ax = sns.scatterplot(x = penguins_df[selected_x_var], y = penguins_df[selected_y_var], hue = penguins_df['species'], markers = markers)
plt.xlabel(selected_x_var)
plt.xlabel(selected_y_var)
plt.title('Scatterplot () Penguins'.format(selected_species))
st.pyplot(fig)