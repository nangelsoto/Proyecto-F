import streamlit as st
from PIL import Image
st.title ("Página Intro")
image = Image.open('imagencasa.jpg')

st.image(image)
