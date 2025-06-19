# ===============================
# __init__.py - Punto de entrada del paquete
# ===============================
# Este archivo permite importar directamente las funciones
# principales desde el paquete "mi_libreria_texto".
#
# Así, al hacer:
#     from mi_libreria_texto import limpiar_texto, contar_palabras...
# automáticamente se accederá a estas funciones definidas en
# limpieza.py y analisis.py

from .limpieza import limpiar_texto  # Importa función para limpieza básica del texto
from .analisis import contar_palabras, frecuencia_palabras  # Importa funciones de análisis léxico
