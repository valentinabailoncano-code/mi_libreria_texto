def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def frecuencia_palabras(texto):
    from collections import Counter
    palabras = texto.split()
    return Counter(palabras)
