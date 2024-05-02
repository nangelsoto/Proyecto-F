import streamlit as st
from PIL import Image
st.title("Habitación")
import streamlit as st

image = Image.open('Entrada exterior.jpg')

st.image(image)
