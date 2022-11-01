import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

#import the WHO dataset
hd = pd.read_csv ('heart_2020_cleaned_sample.csv')

st.write(hd)

st.sidebar.header("Pick two variables for your scatterplot")

x_val =st.sidebar.selectbox("Pick your x-axis", hd.select_dtypes(include=np.number).columns.to_list())
y_val =st.sidebar.selectbox("Pick your y-axis", hd.select_dtypes(include=np.number).columns.to_list())


scatter = alt.Chart(hd, title= f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val, title= f"{x_val}"),
    alt.Y(y_val, title= f"{y_val}"), 
    tooltip= [x_val,y_val]
)
st.altair_chart(scatter, use_container_width=True)

# Calculate the correlation
corr= round(hd[x_val].corr(hd[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")