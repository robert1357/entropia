import streamlit as st
import math
from collections import Counter

def leer_archivo(archivo):
    texto = archivo.read().decode("utf-8")
    return texto

def calcular_frecuencias(texto):
    texto = texto.lower() 
    frecuencias = Counter(texto)
    total_caracteres = sum(frecuencias.values())
    for caracter in frecuencias:
        frecuencias[caracter] /= total_caracteres
    return frecuencias

def calcular_entropia(frecuencias):
    entropia = -sum(frecuencia * math.log2(frecuencia) for frecuencia in frecuencias.values() if frecuencia != 0)
    return round(entropia, 2)  # Redondea la entropía a dos decimales

def main():
    st.set_page_config(page_title="Cálculo de Entropía", page_icon="📊", layout="centered")
    
    st.markdown("""
        <style>
        body {
            background-color: #1565c0; /* Fondo azul */
            color: #ffffff; /* Texto blanco */
            font-family: Arial, sans-serif;
        }
        .main {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .title {
            color: #b71c1c; /* Texto rojo oscuro */
            font-family: 'Arial';
            text-align: center;
        }
        .subtitle {
            text-align: center;
            color: #ffffff; /* Texto blanco */
        }
        .upload-box {
            background-color: #ffffff;
            border: 2px dashed #b71c1c; /* Borde rojo oscuro */
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
        }
        .result-box {
            text-align: center;
            background-color: #1565c0; /* Fondo azul */
            color: #ffffff; /* Texto blanco */
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .download-button {
            display: flex;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='title'>Cálculo de Entropía de Letras</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Sube un archivo de texto para calcular la entropía de las letras.</p>", unsafe_allow_html=True)

    st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
    archivo = st.file_uploader('', type=['txt'], key="file_uploader")
    st.markdown("</div>", unsafe_allow_html=True)

    if archivo is not None:
        texto = leer_archivo(archivo)
        frecuencias = calcular_frecuencias(texto)
        entropia = calcular_entropia(frecuencias)
        
        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.markdown("<h3>Resultado</h3>", unsafe_allow_html=True)
        st.write(f'La entropía del texto es: {entropia:.2f}')  # Mostrar entropía con dos decimales
        st.markdown("</div>", unsafe_allow_html=True)

        resultado = f'La entropía del texto es: {entropia:.2f}'
        
        st.markdown("<div class='download-button'>", unsafe_allow_html=True)
        st.download_button(
            label="Descargar Resultado",
            data=resultado,
            file_name="resultado_entropia.txt",
            mime="text/plain"
        )
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='upload-box'><p>Por favor, sube un archivo de texto.</p></div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
