######################################
# Importar librerias
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import folium

#######################################
# Pagina de configuración
st.set_page_config(
    page_title="Siniestros viales en CABA",
    page_icon="🚧",
    layout= "wide",
    initial_sidebar_state="expanded")
alt.themes.enable("dark")


#######################################
# Carga de datos

hechos = pd.read_csv('dataset/homicidios.csv')
victimas = pd.read_csv('dataset/victimas.csv')
tasa_homicidios = pd.read_csv('dataset/tasahomicidios.csv')
accidentes_moto = pd.read_csv('dataset/accidentes_moto.csv')

#######################################
# Sidebar

años = ['2016', '2017', '2018', '2019', '2020', '2021']
año_seleccionado = st.sidebar.selectbox('Selecciona el año:', años)

# Crear una lista desplegable para el semestre
semestres = ['1', '2']
semestre_seleccionado = st.sidebar.selectbox('Selecciona el semestre:', semestres)

# Puedes usar las variables "año_seleccionado" y "semestre_seleccionado" en tu lógica de procesamiento posterior.


#######################################
# Plots



#######################################


st.title("*Siniestros Viales en CABA*")
st.markdown('***')


########################################
# Datacard
col1, col2 = st.columns(2)
diferencia = int(año_seleccionado) - 2016

if semestre_seleccionado == '1':
    indice = 2*diferencia
else:
    indice = 2*diferencia + 1

# Mostrar la tasa de homicidios
with col1:
    st.metric(label="Tasa de Homicidios", value= str(tasa_homicidios.loc[indice][1]) + '%' , delta= str(tasa_homicidios.loc[0][1] - 10) + '%')

# Mostrar la tasa de acidentes de motocicleta
with col2:
    st.metric(label="Accidentes en Motocicletas", value= str(accidentes_moto['Reduccion_7%'].loc[diferencia]) + '%' , delta= str(7- accidentes_moto['Reduccion_7%'].loc[diferencia]) + '%')


# Agregar un filtro para seleccionar el medio de transporte
selected_transport = st.selectbox('Selecciona un medio de transporte:', hechos['VICTIMA'].unique())

# Filtrar los datos según la selección del usuario
filtered_data = hechos[hechos['VICTIMA'] == selected_transport].groupby(by=['AAAA'])['N_VICTIMAS'].sum()
years = list(filtered_data.keys())

# Dibujar el gráfico con los datos filtrados
plt.figure(figsize=(10, 3))
plt.plot(years, filtered_data, marker='o', label=selected_transport)
plt.title(f'Número de Víctimas por Año ({selected_transport})')
plt.xlabel('Año')
plt.ylabel('Número de Víctimas')
plt.legend()

# Mostrar el gráfico en Streamlit
st.pyplot(plt)

# Mostrar una tabla con los datos filtrados
st.write(filtered_data)

