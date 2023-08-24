import streamlit as st
from PIL import Image

st.title("Mi primera aplicación")
st.write("by: Susana Gómez Serna")

st.header("En este espacio comienzo a desarrollar mis aplicaciones")
st.write("Esta es una imagen de mi perro")
image = Image.open('IMG_4030.JPG')

st.image(image, caption = 'Jager')

texto = st.text_input('Escribe algo','Este es mi texto')
st.write('El texto escrito es:', texto)

st.subheader("Ahora usemos 2 columnas")
col1.col2 = st.columns(2)

