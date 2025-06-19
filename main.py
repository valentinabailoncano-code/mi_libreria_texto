# ===============================
# main.py - Script de demostración
# ===============================
# Este archivo sirve para ejecutar manualmente la librería
# y visualizar cómo funcionan las funciones principales.

from mi_libreria_texto import limpiar_texto, contar_palabras, frecuencia_palabras
import matplotlib.pyplot as plt  # Usamos matplotlib para visualizar los datos

if __name__ == "__main__":
    # Texto de entrada que contiene símbolos, mayúsculas y palabras repetidas
    texto = "¡Hola Mundo! Esto es un ejemplo con ejemplo y texto."

    # Aplicamos limpieza: quita símbolos, convierte a minúsculas, normaliza espacios
    texto_limpio = limpiar_texto(texto)

    # Mostramos el texto limpio en consola
    print(f"Texto limpio: {texto_limpio}")

    # Contamos el número total de palabras
    print(f"Cantidad de palabras: {contar_palabras(texto_limpio)}")

    # Obtenemos la frecuencia de cada palabra en el texto
    frecuencias = frecuencia_palabras(texto_limpio)
    print(f"Frecuencia de palabras: {frecuencias}")

    # ===============================
    # Visualización: Gráfico de barras
    # ===============================
    # Convertimos el diccionario de frecuencias en listas separadas
    palabras = list(frecuencias.keys())
    conteos = list(frecuencias.values())

    # Creamos una visualización sencilla con matplotlib
    plt.figure(figsize=(10, 5))  # Tamaño del gráfico
    plt.bar(palabras, conteos, color='skyblue')  # Gráfico de barras
    plt.title('Frecuencia de palabras')
    plt.xlabel('Palabras')
    plt.ylabel('Cantidad')
    plt.tight_layout()  # Ajusta los márgenes automáticamente
    plt.show()
