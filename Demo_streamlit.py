

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Welcome!")

#display slider in streamlit
st.write('Hi Everyone')
value = st.slider('val')  # this is a widget
st.write(value, 'Squared is', value * value)
st.write(value, 'Cubed is', value * value * value)

#display dataframe in streamlit
st.write("Our first DataFrame")
st.write(pd.DataFrame({'A': [1, 2, 3, 4],'B': [5, 6, 7, 8]}))

#display select box in streamlit
selectbox = st.selectbox("Select yes or no",["Yes", "No"])
st.write(f"You selected {selectbox}")

#display checkbox in streamlit
checkbox_one = st.checkbox("Yes")
checkbox_two = st.checkbox("No")
if checkbox_one:
    value = "Yes"
elif checkbox_two:
    value = "No"
else:
    value = "No value selected"
st.write(f"You selected: {value}")

#display line chart in streamlit
st.write("Line Chart in Streamlit")
# 10 * 2 dimensional data
chart_data = pd.DataFrame(np.random.randn(10, 2),columns=[f"Col{i+1}" for i in range(2)])

st.line_chart(chart_data)

#display seaborn plot in streamlit
st.write('Seaborn Plot in Streamlit!!')
fig,axs=plt.subplots(figsize=(2,2))
sns.countplot(x = 'A', data = pd.DataFrame({'A':['a','a','a','b','b'],'B':[2,3,4,5,6]}))
st.pyplot(fig)

# text input
email_add = st.text_input('Email address')
st.write('Your email is : ', email_add)
desc = st.text_area('Description')
st.write('Provided Description : ', desc)

# file uploader
f1 = st.file_uploader('Upload a photo', type=['txt'])
st.write(f1)