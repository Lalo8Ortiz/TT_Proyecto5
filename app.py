import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Análisis de autos usados")
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
scatter_button = st.button('Construir gráfico de dispersión')  # crear un botón
if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación el gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer",y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_boxplot = st.checkbox('Construir un boxplot')

if build_boxplot: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    fig = px.box(car_data, x="fuel", y="condition", title="Condición de los autos según el tipo de combustible",
             labels={"fuel": "Tipo de combustible", "condition": "Condición"})
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
        