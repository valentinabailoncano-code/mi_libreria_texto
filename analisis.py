# ===============================
# analisis.py - Funciones de análisis de texto
# ===============================
# Este archivo incluye funciones para analizar texto limpio:
# - contar_palabras: número total de palabras
# - frecuencia_palabras: cuántas veces aparece cada palabra

def contar_palabras(texto):
    palabras = texto.split()  # Divide el texto por espacios
    return len(palabras)  # Devuelve cuántas palabras hay

def frecuencia_palabras(texto):
    from collections import Counter  # Clase para contar elementos rápidamente
    palabras = texto.split()  # Divide el texto en palabras
    return Counter(palabras)  # Devuelve diccionario con frecuencia de cada palabra
