from mi_libreria_texto import limpiar_texto, contar_palabras, frecuencia_palabras

if __name__ == "__main__":
    texto = "¡Hola Mundo! Esto es un ejemplo."
    texto_limpio = limpiar_texto(texto)

    print(f"Texto limpio: {texto_limpio}")
    print(f"Cantidad de palabras: {contar_palabras(texto_limpio)}")
    print(f"Frecuencia de palabras: {frecuencia_palabras(texto_limpio)}")

