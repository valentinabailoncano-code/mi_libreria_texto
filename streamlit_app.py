# streamlit_app.py - Visualización web para MASTER-EVOLVE-MODULO-2

import streamlit as st
from mi_libreria_texto import limpiar_texto, detectar_idioma, eliminar_stopwords, contar_palabras, frecuencia_palabras
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configuración inicial de la página
st.set_page_config(page_title="MASTER-EVOLVE-MODULO-2", layout="centered")
st.title("🧹 Análisis de Texto — MASTER-EVOLVE-MODULO-2")

st.markdown("""
Esta aplicación web analiza tu texto ingresado y te muestra:
- Idioma detectado
- Texto limpio
- Texto sin stopwords
- Conteo de palabras
- Visualizaciones interactivas
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
            # Convertir a DataFrame
            df_frec = pd.DataFrame(frecuencia.items(), columns=["Palabra", "Frecuencia"])
            df_frec = df_frec.sort_values(by="Frecuencia", ascending=False)

            # Gráfico de barras
            st.subheader("📊 Frecuencia de palabras (Top 10)")
            fig_bar, ax = plt.subplots(figsize=(10, 4))
            ax.bar(df_frec["Palabra"].head(10), df_frec["Frecuencia"].head(10), color="skyblue")
            ax.set_ylabel("Frecuencia")
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig_bar)

            # Gráfico de dispersión
            st.subheader("🔎 Diagrama de dispersión")
            fig_scatter, ax2 = plt.subplots()
            ax2.scatter(df_frec["Palabra"], df_frec["Frecuencia"], color="purple")
            ax2.set_ylabel("Frecuencia")
            ax2.set_xticklabels(df_frec["Palabra"], rotation=45)
            st.pyplot(fig_scatter)

            # Tabla
            st.subheader("📋 Tabla de frecuencias")
            st.dataframe(df_frec.reset_index(drop=True))

        else:
            st.info("No se encontraron palabras significativas tras la limpieza y filtrado.")
else:
    st.info("Introduce un texto para comenzar el análisis.")


