######################################
# Importar librerias
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

#######################################
# Pagina de configuración
st.set_page_config(
    page_title="Siniestros viales en CABA",
    page_icon="🚧",
    layout= "wide",
    initial_sidebar_state="expanded")
alt.themes.enable("dark")

#######################################
# Estilo CSS
st.markdown("""
<style>

[data-testid="block-continer"] {
            paddind-left: 2rem;
            padding-right: 2rem;
            padding-top: 1rem;
            padding-bottom: 0rem;
            margin-bottom: -7rem:
}

[data-testid="stVerticalBlock"]{
            padding-left: 0rem;
            padding-right: 0rem;
}
[data-testid="stMetric"] {
            backgroud-color: #393939;
            text-align: center;
            padding: 25px 0;
}

[data-testid="stMetricLabel"] {
            display: flex;
            justify-content: center;
            aling-items: center;
}
            </style>
""", unsafe_allow_html=True)

#######################################
# Carga de datos

hechos = pd.read_excel('dataset/homicidios.xlsx', sheet_name='HECHOS')
victimas = pd.read_excel('dataset/homicidios.xlsx', sheet_name='VICTIMAS')

#######################################
# Sidebar


#######################################
# Plots



#######################################


st.title("*Siniestros Viales en CABA*")
st.markdown('***')
st.sidebar.markdown('# Barra lateral')



