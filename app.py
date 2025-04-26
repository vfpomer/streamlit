#primerro importamos las librerias a usar
import streamlit as st
import pandas as pd

#setup de la app
st.set_page_config(
    page_title="My first Streamlit App",
    page_icon=":tada:",
    layout="centered",  
)
#TEXTOS
st.title("My Streamlit App")#tirulo principal

#Encabezados
st.header("This is a header")#encabezado
st.subheader("This is a subheader")#subencabezado

#texto normal
st.text("Hello Wordl")#texto normal

#markdown
st.markdown("## This is a markdown")#markdown

#latex (formula matematica)
st.latex(r"""a^2 + b^2 = c^2""")#latex

#code
st.code("print('Hello World')", language="python")#codigo

#informacion,advertencia y error
st.info("This is an info message")#informacion  
st.warning("This is a warning message")#advertencia
st.error("This is an error message")#errorç
st.success("This is a success message")#exito     
st.exception("This is an exception message")#excepcion
st.help("This is a help message")#ayuda 

#medios y recursos
#imagenes (la ruta puede ser local o una url)
st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit Logo", width=200)#imagen

#audios
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")#audio

#videos
st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")#video

#------------------------------------------------------------
pf = pd.DataFrame({
    "col1": [1, 2, 3],
    "col2": [4, 5, 6],
    "col3": [7, 8, 9]
})

st.dataframe(pf)#dataframe

#-----------------------------------------------

