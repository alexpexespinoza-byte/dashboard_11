import streamlit as st

@st.cache_data
def f_ex__kpi_script_data(data=None):

    r_text = """<div style="padding: 15px; border: 1px solid">"""

    for k, v in data.items():
        r_text += f"""<div style="font-size: 15px">{k}</div>"""

        if ("f" in v):
            if (v["f"] == "$"):
                v["v"] = f"$ {v["v"]:,.2f}"
        else:
            None

        if ((not "c" in v) and (not "d" in v)):
            r_text += f"""<div style="font-size: 30px;">{v["v"]}</div>"""

        if ("c" in v):
            color = f"color: {v["c"]}"
            r_text += f"""<div style="font-size: 30px; {color}">{v["v"]}</div>"""

        if ("d" in v):
            delta_color = f"color: {("#00FF00") if (v["d"][0] > 0) else ("#FF0000")}"
            r_text += f"""<div style="font-size: 12px; {delta_color}">{v["d"][1]}</div>"""

        if ("grf" in v):
            r_text += (
                f"""
                    <svg viewbox="0 0 {150} {100}">
                        <path d="{v["grf"]}" fill="none" stroke="#FFFFFF">
                    </svg>
                """
            )

    st.markdown(r_text, unsafe_allow_html=True)

   