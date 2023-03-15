# librerias básicas
import os
import re
import requests
import pandas as pd
import numpy as np

# plotear gráficos y visualización
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import plot
import chart_studio.plotly as py
import plotly.io as pio
import seaborn as sns

# streamlit
import streamlit as st
import streamlit.components.v1 as components
import google 
from PIL import Image
from pyngrok import ngrok
from IPython.display import display
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import urllib.request
import unicodedata
from unicodedata import name

# ---------------CONFIGURACION DE LA PAGINA--------------------
st.set_page_config(page_title='MADRID' , layout='centered' , page_icon="🌆")

# LEEMOS EL DATA FRAME QUE VAMOS A USAR
df = pd.read_csv("madridsinNulls.csv")

#------------------------------------------------------------------------------------COMENZAMOS LA APP -----------------------------------------------------------------------------------------------
# st.image("https://a.cdn-hotels.com/gdcs/production133/d1207/7ad2d7f0-68ce-11e8-8a0f-0242ac11000c.jpg", width=800)
# st.write("Fuente= [https://ar.hoteles.com/go/espana]")
# st.title('AIRBNB: MADRID')

# creamos una side bar y añadimos una barra con una pagina que nos muestra el tiempo en MADRID
st.sidebar.title("El tiempo en Madrid")
st.sidebar.write(f'<iframe src="https://www.accuweather.com/en/es/madrid/308526/weather-forecast/308526" width="" height="600" style="overflow:auto"></iframe>', unsafe_allow_html=True)
url = "https://www.accuweather.com/en/es/madrid/308526/weather-forecast/308526"
st.sidebar.markdown("[Accuweather](%s)" % url)

# creamos las pestañas que van a dividir nuestra app
tabs = st.tabs(['MADRID','EDA',"CONCLUSIONES"])
#------------------------------------------------------------------------FUNCIÓN FONDO DE PANTALLA-------------------------------------------------------------------------------

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.alphacoders.com/111/1112475.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
#Hacemos transparentes los botones
st.markdown(
    f"""
    <style>
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    
    [data-testid="stMarkdownContainer"] {{
    background-color: rgba(0, 0, 0, 0);
    }}

    .st-c6 {{
    background: rgb(0 0 0 / 0%);
    }}

    [data-testid="stSidebar"]{{                 
    background-color: rgba(0, 0, 0, 0);
    border: 0.5px solid #ff4b4b;
        }}

    </style>
    """
 , unsafe_allow_html=True)


#------------------------------------------------------------------------PRIMERA PESTAÑA: MADRID-------------------------------------------------------------------------------
tab_plots = tabs[0]

# añadimos una página para ver los mejores sitios de madrid
with tab_plots:
    st.header('MADRID')
    st.markdown(""" **Capital de España y conocida habitualmente como Villa y Corte, 
                    Madrid es la mayor ciudad del país y la segunda de la Unión Europea, 
                    con una población de más de 3 millones de habitantes (más de 6 en el área metropolitana).**""")

    st.write(f'<iframe src="https://turismomadrid.es/es/" width="800" height="600" style="overflow:auto"></iframe>', unsafe_allow_html=True)
    # components.iframe(src="https://www.traveltrade.esmadridpro.com/")
    url1 = "https://turismomadrid.es/es/"
    st.markdown("[Turismo Madrid](%s)" % url1)

#-------------------------------------------------------------------------------SEGUNDA PESTAÑA: EDA------------------------------------------------------------------------------------
tab_plots = tabs[1]

# mapa de distribucion de los diferentes alojamientos
with tab_plots:
    map = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='neighbourhood_group',
                        size_max=15, zoom=10, height=800, title="Hospedajes por barrio",
                        labels={"neighbourhood_group":"Barrio","longitude":"Lon","latitude":"Lat"})
    map.update_layout(mapbox_style='open-street-map')
    map.update_layout(margin={"r":80,"t":80,"l":80,"b":80})
    map.update_layout(width=900, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    map.update_layout(template="plotly_dark")
    st.plotly_chart(map)

    st.subheader("*Se aplicaron los siguientes filtros para poder hacer un análisis más específico:*")
    st.markdown("**+ Se tomaron solo los grupos de barrio que tenían más de 1000 alojamientos (“Arganzuela”- “Centro”- “Chamberi”- “Salamanca”**")
    st.markdown("**+ Solo los hosts a partir de 400 reviews**")

# Dashboard de power bi interactivo
with tab_plots:
    st.subheader('Dashboard General')
    st.write(f'<iframe src="https://app.powerbi.com/reportEmbed?reportId=f9c5edba-9729-49b3-a55d-3db8886f8465&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64" width="900" height="700" style="overflow:auto" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

#-------------------------------------------------------------------------------TERCERA PESTAÑA: CONCLUSIONES------------------------------------------------------------------------------------
tab_plots = tabs[2]

with tab_plots:
    st.header("Conclusiones:")
    st.subheader('*Según los datos proporcionados:*')
    st.markdown("- **Los hospedajes más caros se encuentran en Goya, Salamanca.**")
    st.markdown("-	**Los más baratos en Arganzuela.**")
    st.markdown("-	**En el centro es donde hay más hospedajes.**")
    st.write("-	**Los precios promedio van de 72 a 168 euros.**")
    st.markdown("- **Hay muy pocas habitaciones compartidas y habitaciones de hotel**")



    