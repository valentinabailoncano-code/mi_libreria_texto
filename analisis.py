# ===============================
# analisis.py - Funciones de análisis de texto
# ===============================
# Este archivo incluye funciones para analizar texto limpio:
# - contar_palabras: número total de palabras
# - frecuencia_palabras: cuántas veces aparece cada palabra
# - eliminar_stopwords: elimina palabras vacías como "el", "de", "y" (usando nltk)
# - detectar_idioma: intenta detectar automáticamente el idioma del texto

import nltk
from collections import Counter
from langdetect import detect

# Asegura que el paquete de stopwords esté disponible
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def contar_palabras(texto):
    palabras = texto.split()  # Divide el texto por espacios
    return len(palabras)  # Devuelve cuántas palabras hay

def frecuencia_palabras(texto):
    palabras = texto.split()  # Divide el texto en palabras
    return Counter(palabras)  # Devuelve diccionario con frecuencia de cada palabra

def eliminar_stopwords(texto, idioma='spanish'):
    """
    Elimina palabras vacías (como "de", "el", "y") según el idioma.
    Usa las stopwords definidas por la librería nltk.
    """
    from nltk.corpus import stopwords

    palabras = texto.split()
    stop_words = set(stopwords.words(idioma))
    filtradas = [palabra for palabra in palabras if palabra not in stop_words]
    return ' '.join(filtradas)

def detectar_idioma(texto):
    """
    Detecta automáticamente el idioma de un texto usando langdetect.
    Devuelve un código de idioma como 'es', 'en', etc.
    """
    return detect(texto)
