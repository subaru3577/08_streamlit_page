import streamlit as st
import pandas as pd

data = {
  'Series_1':[1, 3, 4, 5, 7],
  'Series 2':[10, 30, 40, 100, 250]
}

df = pd.DataFrame(data)

st.title("First Streamlit App")
st.subheader("Introducing Streamlit in Automation")
st.write(""" 
         Thank you for visiting.
         This is a sample page with streamlit.
""")
st.write(df)
st.line_chart(df)
st.area_chart(df)
myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)