import pandas as pd
import streamlit as st
import io



@st.cache_data()
def f_ex__kpi_data():
    df = pd.read_excel("datasets/data_c.xlsx")

    ventas_totales = df["Total_Venta"].sum()

    productos_vendidos = int(df["Cantidad"].sum())

    numero_pedidos = len(df["ID_Pedido"])

    ticket_promedio = ventas_totales / numero_pedidos

    data = {
        "v_t" : ventas_totales,
        "p_v" : productos_vendidos,
        "n_pe" : numero_pedidos,
        "t_pro" : ticket_promedio
    }

    return (data)


@st.cache_data()
def f_ex__grf_1_data(per="M"):
    df = pd.read_excel("datasets/data_c.xlsx")

    periodo_ventas = df.groupby(
        (df["Mes"] if (per == "M") else (df["Dia_Semana"]))
    )["Total_Venta"].sum()

    periodo_ventas.index = (
        pd.Categorical(
            periodo_ventas.index, (
                (meses_año.values()) if (per == "M")
                else (dias_semana.values())
            )
        )
    )
    periodo_ventas = periodo_ventas.sort_index()

    data = [
            {
            f"{(("Mes") if (per == "M") else ("Dia de la Semana"))}" : list(periodo_ventas.keys()),
            "Ventas" : list(periodo_ventas.values)
        },
        periodo_ventas.mean()
    ]

    return (data)


@st.cache_data()
def f_ex__grf_2_data():
    df = pd.read_excel("datasets/data_c.xlsx")

    region_ventas = df.groupby(df["Región"])["Total_Venta"].sum()

    data = {
        "Region" : list(region_ventas.keys()),
        "Ventas" : list(region_ventas.values)
    }

    return (data)


@st.cache_data()
def f_ex__grf_3_data():
    df = pd.read_excel("datasets/data_c.xlsx")

    df["Tamaño_b"] = df["Total_Venta"] / 15
    df["Tamaño_b"][df["Tamaño_b"] <= 10] = 10

    data = {
        "df" : df
    }

    return (data)


@st.cache_data()
def f_ex__grf_4_data():
    df = pd.read_excel("datasets/data_c.xlsx")

    hash_map_c = {}

    categoria_idx = list(df["Categoría"].unique())

    for e in categoria_idx:
        df_c = df[df["Categoría"] == e]
        historial_v_t = []
        for e_2 in dias_semana.values():
            df_d_s = df_c[df_c["Dia_Semana"] == e_2]

            historial_v_t.append(df_d_s["Total_Venta"].sum())

        hash_map_c[e] = historial_v_t


    data = pd.DataFrame(
        {
            k : v for k, v in hash_map_c.items() 
        },
        index=dias_semana.values()
    )

    return (data)



@st.cache_data
def f_ex__filtros_df():
    df = pd.read_excel("datasets/data_c.xlsx")

    regiones = list(df["Región"].unique())

    clientes = list(df["Cliente"].unique())

    data = {
        "t_r" : regiones,
        "t_c" : clientes
    }

    return (data)



@st.cache_data
def f_ex__df_data(reg="Todas las Regiones", cli="Todos los Clientes"):
    df = pd.read_excel("datasets/data_c.xlsx")

    df = (
        (df) if (reg == "Todas las Regiones") 
        else (df[df["Región"] == reg])
    )

    df = (
        (df) if (cli == "Todos los Clientes") 
        else (df[df["Cliente"] == cli])
    )

    return (df)



def f_ex__df_descargar(df_p):
    out = io.BytesIO()

    with pd.ExcelWriter(out, engine="openpyxl") as w:
        df_p.to_excel(w, index=False)

    return (out.getvalue())


#Varibles globales ↓

dias_semana = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

meses_año = {
    "January": "Enero",
    "February": "Febrero",
    "March": "Marzo",
    "April": "Abril",
    "May": "Mayo",
    "June": "Junio",
    "July": "Julio",
    "August": "Agosto",
    "September": "Septiembre",
    "October": "Octubre",
    "November": "Noviembre",
    "December": "Diciembre"
}