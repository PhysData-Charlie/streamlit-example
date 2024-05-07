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

df = pd.DataFrame({'Code-Req.': [i for i in range(0,100)], 
                   'Prioridad': np.random.randint(1,3,size=100),
                  'Impacto': np.random.randint(1,3,size=100)})

df['Prioridad'] = df['Prioridad'].replace({0: 'Baja', 1: 'Media', 2: 'Alta'})
df['Impacto'] = df['Impacto'].replace({0: 'Una Persona', 1: 'Un Departamento', 2: 'Un Servicio'})


def home_page():
    st.title('PRIORIZACIÓN DE TICKETS')
    st.header('Dataset')
    st.write(df.head(10)

def stats_page():
    st.title('ESTADISTICAS')
    stats_df = df.describe()
    st.write(stats_df)

def graphs_page():
    set.title('DISTRIBUCION DE TICKETS')
    bar_df = df.groupby('Prioridad')['Code-Req'].count()
    st.bar_chart(bar_df, use_container_width=True)

if __name __ == '__main__':
    selected_page = st.sidebar.selectbox(
        'Seleccionar página',
        ('Principal', 'Estadistica', 'Graficos)
    )

    if selected_page == 'Principal':
        home_page()
    elif selected_page == 'Estadistica':
        graphs_page()
    elif selected_page == 'Graficos':
        stats_page()

# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices

# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })

# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))
