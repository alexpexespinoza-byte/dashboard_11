import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")


#Grafica ↓

df = pd.DataFrame(
        {
        "a" : [1, 2, 3],
        "b" : [4, 5, 6],
        "c" : [7, 8, 9]
    },
    index=["Leo", "Nel", "Xd"]
)

grf = px.imshow(
    df
)

st.plotly_chart(grf)