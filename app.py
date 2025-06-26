import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Demo Streamlit",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.title("Menú de Navegación")
    option = st.radio(
        "Selecciona una sección:",
        ["Inicio", "Visualización de Datos", "Formularios", "Widgets Interactivos"]
    )
    
    st.divider()
    
    st.write("Sobre esta aplicación")
    st.info("Esta es una demo simple de Streamlit que muestra algunos de sus componentes principales.")
    
    # Añadir un selector de color en la barra lateral
    color = st.color_picker("Elige un color", "#00ABAB")
    
    # Mostrar la hora actual
    st.write("Hora actual:")
    st.write(datetime.now().strftime("%H:%M:%S"))

# Contenido principal
if option == "Inicio":
    st.title("Bienvenido a la Demo de Streamlit")
    st.subheader("Una introducción a los componentes de Streamlit")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### ¿Qué es Streamlit?")
        st.write("""
        Streamlit es una biblioteca de Python que permite crear aplicaciones web 
        interactivas con facilidad. Es ideal para visualización de datos, 
        creación de dashboards y herramientas de machine learning.
        """)
        
        # Expandible con más información
        with st.expander("Ver más información"):
            st.write("""
            Streamlit convierte scripts de Python en aplicaciones web compartibles en minutos.
            Todo está escrito en Python puro, y no se necesita experiencia en frontend.
            """)
            
        # Mostrar código
        st.code("""
import streamlit as st

st.title("Hola Mundo")
st.write("¡Esta es mi primera app de Streamlit!")
        """)
    
    with col2:
        # Imagen de ejemplo
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)
        
        # Progreso
        st.write("### Ejemplo de barra de progreso")
        progress = st.progress(0)
        for i in range(100):
            progress.progress(i + 1)
        
        # Éxito
        st.success("¡Completado!")
        
        # Alerta
        st.warning("Esto es una advertencia")
        
        # Error
        st.error("Esto es un mensaje de error")

elif option == "Visualización de Datos":
    st.title("Visualización de Datos")
    
    # Crear datos de ejemplo
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    tab1, tab2, tab3, tab4 = st.tabs(["Gráfico de líneas", "Gráfico de barras", "Mapa", "Plotly"])
    
    with tab1:
        st.subheader("Gráfico de líneas")
        st.line_chart(chart_data)
        
    with tab2:
        st.subheader("Gráfico de barras")
        st.bar_chart(chart_data)
        
    with tab3:
        st.subheader("Mapa")
        map_data = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon']
        )
        st.map(map_data)
        
    with tab4:
        st.subheader("Gráfico con Plotly")
        fig = px.scatter(
            chart_data, x='A', y='B', size='C', color='C',
            hover_name=chart_data.index,
            title="Gráfico de dispersión interactivo"
        )
        st.plotly_chart(fig)
    
    # Mostrar datos en tabla
    st.subheader("Datos en tabla")
    st.dataframe(chart_data.style.highlight_max(axis=0))
    
elif option == "Formularios":
    st.title("Formularios")
    
    with st.form("formulario_ejemplo"):
        st.write("### Formulario de contacto")
        nombre = st.text_input("Nombre")
        email = st.text_input("Email")
        mensaje = st.text_area("Mensaje")
        
        # Selector de fecha
        fecha = st.date_input("Fecha de contacto")
        
        # Checkbox
        acepta_terminos = st.checkbox("Acepto los términos y condiciones")
        
        # Botón de envío
        submitted = st.form_submit_button("Enviar")
        
        if submitted:
            if nombre and email and mensaje and acepta_terminos:
                st.success(f"¡Gracias por tu mensaje, {nombre}!")
                st.write(f"Email: {email}")
                st.write(f"Fecha: {fecha}")
                st.write(f"Mensaje: {mensaje}")
            else:
                st.error("Por favor completa todos los campos y acepta los términos.")

else:  # Widgets Interactivos
    st.title("Widgets Interactivos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Controles básicos")
        
        # Slider
        numero = st.slider("Selecciona un número", 0, 100, 50)
        st.write(f"Número seleccionado: {numero}")
        
        # Select box
        opcion = st.selectbox(
            "¿Cuál es tu lenguaje de programación favorito?",
            ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
        )
        st.write(f"Has seleccionado: {opcion}")
        
        # Multi select
        opciones = st.multiselect(
            "¿Qué frameworks conoces?",
            ["React", "Angular", "Vue", "Django", "Flask", "FastAPI", "Express"],
            ["Django", "Flask"]
        )
        st.write(f"Has seleccionado: {opciones}")
    
    with col2:
        st.subheader("Más widgets")
        
        # Radio buttons
        genero = st.radio(
            "Género",
            ["Masculino", "Femenino", "No binario", "Prefiero no decirlo"]
        )
        
        # Number input
        edad = st.number_input("Edad", min_value=0, max_value=120, value=25)
        
        # Text area
        bio = st.text_area("Biografía", "Escribe algo sobre ti...")
        
        # Button
        if st.button("Mostrar información"):
            st.write(f"Género: {genero}")
            st.write(f"Edad: {edad}")
            st.write(f"Biografía: {bio}")
    
    # Carga de archivos
    st.subheader("Carga de archivos")
    archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])
    
    if archivo is not None:
        try:
            df = pd.read_csv(archivo)
            st.write("Vista previa de los datos:")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error al leer el archivo: {e}")

# Footer
st.divider()
st.caption("Demo de Streamlit creada como ejemplo para Kodigo Bootcamp")
