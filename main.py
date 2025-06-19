# ===============================
# main.py - Script de demostración
# ===============================
# Este archivo sirve para ejecutar manualmente la librería
# y visualizar cómo funcionan las funciones principales.

from mi_libreria_texto import limpiar_texto, contar_palabras, frecuencia_palabras

if __name__ == "__main__":
    # Texto de entrada que contiene símbolos y mayúsculas
    texto = "¡Hola Mundo! Esto es un ejemplo."

    # Limpiar el texto: elimina símbolos, minúsculas, espacios
    texto_limpio = limpiar_texto(texto)

    # Mostrar el texto limpio
    print(f"Texto limpio: {texto_limpio}")

    # Mostrar cuántas palabras contiene
    print(f"Cantidad de palabras: {contar_palabras(texto_limpio)}")

    # Mostrar cuántas veces aparece cada palabra
    print(f"Frecuencia de palabras: {frecuencia_palabras(texto_limpio)}")
