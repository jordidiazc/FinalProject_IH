import streamlit as st
import pandas as pd

# Cargar el archivo CSV
file_path = 'df.csv'  # Asegúrate de colocar el archivo CSV en el mismo directorio
df = pd.read_csv(file_path)

# Título de la aplicación
st.title('Recomendador de Libros para el Verano')

# Entrada del usuario para seleccionar el género
genero_seleccionado = st.selectbox('¿Qué género le gustaría leer este verano?', df['genre_1'].unique())

# Filtrar el DataFrame basado en el género seleccionado
libros_filtrados = df[df['genre_1'] == genero_seleccionado]

# Mostrar el título del libro
if not libros_filtrados.empty:
    titulo_libro = libros_filtrados['title'].values[0]
    st.write(f'Le recomendamos leer: **{titulo_libro}**')
else:
    st.write('No se encontraron libros para el género seleccionado.')
