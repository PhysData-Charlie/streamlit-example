import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

""""
# PRIORIZACIÓN DE TICKETS

La siguiente aplicación permite identiificar la prioridad de tickets 
según sus características utilizando diversos modelos de procesamiento 
de lenguaje natural (NLP).

Desarrollado por: Rodrigo Salazar Malasquez

"""


def home_page():
    st.title('PRIORIZACIÓN DE TICKETS')
    st.header('Dataset')
    st.write(df.head(10))
    if st.button('Actualizar Datos'):
      st.write('Cargando datos...')
      st.write('Datos actualizados!')
    st.button('Cerrar página', type='primary')

def stats_page():
    st.title('ESTADISTICAS')
    st.write('Estadísticas de los datos')
    stats_df = round(df.describe(),2)
    st.write(stats_df)

def graphs_page():
    set.title('DISTRIBUCION DE TICKETS')
    st.write('Visualización de los datos')
    bar_df = df.groupby('Prioridad')['Code-Req.'].count()
    #st.bar_chart(bar_df, use_container_width=True)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)

def theory_page():
    st.title('MARCO TEÓRICO')
    st.write('Explicación de los modelos escogidos')
    st.write('.........')

def update_data():
  # aqui va el codigo para ejecutar el modelo
  print('In progress')
  

if __name__ == '__main__':

    # dataset de prueba
    df = pd.DataFrame({'Code-Req.': [i for i in range(0,100)], 
                   'Prioridad': np.random.randint(0,3,size=100),
                  'Impacto': np.random.randint(0,3,size=100)})

    df['Prioridad'] = df['Prioridad'].replace({0: 'Baja', 1: 'Media', 2: 'Alta'})
    df['Impacto'] = df['Impacto'].replace({0: 'Una Persona', 1: 'Un Departamento', 2: 'Un Servicio'})
  
    selected_page = st.sidebar.selectbox(
        'Seleccionar',
        ('Principal', 'Estadistica', 'Graficos')
    )

    if selected_page == 'Principal':
        home_page()
    elif selected_page == 'Estadistica':
        stats_page()
    elif selected_page == 'Graficos':
        graphs_page()
    elif theory_page == 'Marco Teórico':
        theory_page()

