import streamlit as st
import plotly.express as px
import main

st.set_page_config(layout="wide")


#Grafica 3 ↓

grf_3_data = main.f_ex__grf_3_data()

grf_3 = px.scatter(
    grf_3_data["df"],
    x="Precio_Unitario",
    y="Cantidad",
    size="Tamaño_b",
    color="Región"
)

st.plotly_chart(grf_3)

st.divider()


#Grafica 4 ↓

grf_4_data = main.f_ex__grf_4_data()

grf_4 = px.imshow(
    grf_4_data,
    color_continuous_scale="hot",
    aspect="auto",
    title="Distribucion de ventas de Categorias por dia de la semana"
)

st.plotly_chart(grf_4)