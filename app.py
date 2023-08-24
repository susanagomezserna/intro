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

col1, col2, col3 = st.columns(3)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Mi nombre es Susana")
  respsi = st.checkbox('Sí')
  respno = st.checkbox('No')
  if respsi:
    st.write('Correcto!')
  if respno:
    st.write('Incorrecto :(')

with col2:
  st.subheader("Esta es la segunda columna")
  nombre = st.radio("Como se llama mi perro?", ('Tequila','Ginebra','Jager','Rafa'))
  if nombre == 'Tequila' & 'Ginebra' & 'Rafa':
    st.write("Incorrecto :(")
  if nombre == 'Jager':
    st.write("Correcto!")
    
with col3:
  st.subheader("Esta es la tercera columna")
  gusta = st.slider('Que tanto te gusta Jager?', Poquito, Mucho, Normal)
  st.write("Te gusta:", gusta) 
  
  


  

  
      
    
