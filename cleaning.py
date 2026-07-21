import pandas as pd

df = pd.read_excel("datasets/datos_ventas_sucios_para_dashboard.xlsx", sheet_name="Datos_Brutos_Ventas")

pd.set_option("display.max_rows", None)


df.drop(index=df[df.duplicated(subset=["ID_Pedido"])].index.to_list(), inplace=True)

df["Fecha"] = pd.to_datetime(df["Fecha"], format="mixed")

df["Producto"] = df["Producto"].str.title()

df["Cantidad"] = df["Cantidad"].fillna(0)

h_m_precios = {
    k : (df[df["Producto"] == k]["Precio_Unitario"].mode()[0]) for k in df["Producto"].unique()
}
df["Precio_Unitario"] = (df["Producto"].map(h_m_precios)).fillna(0)

df["Total_Venta"] = (df["Precio_Unitario"] * df["Cantidad"]).fillna(0)

df["Categoría"] = (
    df["Categoría"].str.title().
    str.strip()
)

df["Región"] = df["Región"].str.title()
df["Región"] = df["Región"].fillna("Desconocido")


dias_semana = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}
df["Dia_Semana"] = df["Fecha"].dt.day_name()
df["Dia_Semana"] = df["Dia_Semana"].map(dias_semana)

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
df["Mes"] = df["Fecha"].dt.month_name()
df["Mes"] = df["Mes"].map(meses_año)


df.to_excel("datasets/data_c.xlsx", index=False)

print("Limpio xd")
