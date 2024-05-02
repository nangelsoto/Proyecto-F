import streamlit as st
from PIL import Image
st.title("Habitación")

image = Image.open('Entrada exterior.jpg')

st.image(image)
