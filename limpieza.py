# ===============================
# limpieza.py - Funciones de limpieza de texto
# ===============================
# Contiene una única función que normaliza el texto:
# - Convierte a minúsculas
# - Elimina símbolos y signos de puntuación
# - Elimina espacios innecesarios

def limpiar_texto(texto):
    import re  # Usamos expresiones regulares

    texto = texto.lower()  # Convertimos todo a minúsculas

    # Eliminamos caracteres que no sean letras (con tildes y ñ) ni espacios
    texto = re.sub(r'[^a-záéíóúñ\s]', '', texto)

    # Reemplazamos múltiples espacios por uno solo
    texto = re.sub(r'\s+', ' ', texto).strip()

    return texto
