def limpiar_texto(texto):
    import re
    texto = texto.lower()
    texto = re.sub(r'[^a-záéíóúñ\s]', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto
