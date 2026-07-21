import streamlit as st
import main

st.set_page_config(layout="wide")


#DataFrame ↓

filtros = main.f_ex__filtros_df()

region = st.sidebar.selectbox(
    "Selecciona la region",
    ["Todas las Regiones"] + filtros["t_r"]
)

cliente = st.sidebar.selectbox(
    "Selecciona cliente",
    ["Todos los Clientes"] + filtros["t_c"]
)

st.sidebar.divider()

df_data = main.f_ex__df_data(region, cliente)

st.dataframe(df_data)


#Boton descarga ↓

xlsx = main.f_ex__df_descargar(df_data)

st.sidebar.download_button(
    label="Descargar Excel",
    data=xlsx,
    file_name="datos.xlsx",
    mime="pplication/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    icon=":material/download:"
)