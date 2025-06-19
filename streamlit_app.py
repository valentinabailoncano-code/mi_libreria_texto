# streamlit_app.py - Visualización web para MASTER-EVOLVE-MODULO-2

import streamlit as st
from mi_libreria_texto import limpiar_texto, detectar_idioma, eliminar_stopwords, contar_palabras, frecuencia_palabras
import matplotlib.pyplot as plt

# Configuración inicial de la página
st.set_page_config(page_title="MASTER-EVOLVE-MODULO-2", layout="centered")
st.title("🧹 Análisis de Texto — MASTER-EVOLVE-MODULO-2")

st.markdown("""
Esta aplicación web analiza tu texto ingresado y te muestra:
- Idioma detectado
- Texto limpio
- Texto sin stopwords
- Conteo de palabras
- Frecuencia visualizada
""")

# Entrada de usuario
texto_usuario = st.text_area("Introduce tu texto aquí:", height=200)

if texto_usuario:
    with st.spinner("Procesando texto..."):
        # Detección de idioma
        idioma = detectar_idioma(texto_usuario)
        st.success(f"🌍 Idioma detectado: {idioma}")

        # Limpieza
        texto_limpio = limpiar_texto(texto_usuario)
        st.text_area("🔤 Texto limpio:", texto_limpio, height=100)

        # Stopwords
        texto_filtrado = eliminar_stopwords(texto_limpio, idioma)
        st.text_area("🧹 Texto sin stopwords:", texto_filtrado, height=100)

        # Conteo y frecuencia
        num_palabras = contar_palabras(texto_filtrado)
        st.write(f"🧮 Número total de palabras significativas: `{num_palabras}`")

        frecuencia = frecuencia_palabras(texto_filtrado)

        if frecuencia:
            # Mostrar gráfico
            st.subheader("📊 Frecuencia de palabras")
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.bar(frecuencia.keys(), frecuencia.values(), color="skyblue")
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.info("No se encontraron palabras significativas tras la limpieza y filtrado.")
else:
    st.info("Introduce un texto para comenzar el análisis.")

