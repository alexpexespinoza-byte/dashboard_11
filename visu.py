import streamlit as st

#streamlit run "visu.py"

pg_1 = st.Page("pages/pg_1.py", title="Inicio")
pg_2 = st.Page("pages/pg_2.py", title="Analisis Inteligente")
pg_3 = st.Page("pages/pg_3.py", title="DataFrame")

pg_nav = st.navigation([pg_1, pg_2, pg_3])

pg_nav.run()