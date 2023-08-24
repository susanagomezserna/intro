import streamlit as st
from PIL import Image

st.title("Mi primera aplicación")
st.write("by: Susana Gómez Serna")

st.Header("En este espacio comienzo a desarrollar mis aplicaciones")
st.write("Esta es una imagen de mi perro")
image = Image.open('IMG_4030.JPG')

st.image(image, caption = 'Jager')
