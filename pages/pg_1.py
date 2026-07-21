import streamlit as st
import plotly.express as px
import main
import kpi_script as kpi_s

st.set_page_config(layout="wide")

st.title("Dashboard 11")

st.divider()


#KPI's ↓

kpi_data = main.f_ex__kpi_data()

c1, c2, c3, c4 = st.columns(4)

with (c1):
    kpi_s.f_ex__kpi_script_data(
        data={
            "Ventas Totales" : {
                "v" : kpi_data["v_t"],
                "f" : "$",
                "c" : "#6AFF74"
            }
        }
    )
with (c2):
    kpi_s.f_ex__kpi_script_data(
        data={
            "Productos Vendidos" : {
                "v" : kpi_data["p_v"],
                "c" : "#FFB76A"
            }
        }
    )
with (c3):
    kpi_s.f_ex__kpi_script_data(
        data={
            "Pedidos" : {
                "v" : kpi_data["n_pe"],
                "c" : "#6AFF74"
            }
        }
    )
with (c4):
    kpi_s.f_ex__kpi_script_data(
        data={
            "Ticket Promedio" : {
                "v" : kpi_data["t_pro"],
                "f" : "$",
                "c" : "#FFB76A"
            }
        }
    )

st.divider()


#Grafica 1 ↓

c1, c2 = st.columns(2)

with (c1):
    periodo = st.selectbox(
        "Selecciona periodo",
        ["Mes", "Dia de la Semana"]
    )

periodo = (("D") if (periodo == "Dia de la Semana") else ("M"))

grf_1_data = main.f_ex__grf_1_data(periodo)

grf_1 = px.line(
    grf_1_data[0],
    x=(("Mes") if (periodo == "M") else ("Dia de la Semana")),
    y="Ventas",
    markers=True,
    title=f"Ventas por {("Mes") if (periodo == "M") else ("Dia de la Semana")}"
)
grf_1.update_traces(
    line_color="#6AFF74",
    marker=dict(
        color="#000000"
    )
)
grf_1.add_hline(
    y=grf_1_data[1],
    line_color="#FFFFFF",
    annotation=dict(
        text=f"Promedio de ventas del periodo {grf_1_data[1]:,.2f}"
    ),
    line=dict(
        dash="dash"
    )
)

print(grf_1_data, periodo)

with (c1):
    st.plotly_chart(grf_1)


#Grafica 2 ↓

grf_2_data = main.f_ex__grf_2_data()

grf_2 = px.pie(
    grf_2_data,
    names="Region",
    values="Ventas",
    title="Distribucion de ventas por Regiones"
)
grf_2.update_traces(
    textinfo="label+value"
)

with (c2):
    st.plotly_chart(grf_2)