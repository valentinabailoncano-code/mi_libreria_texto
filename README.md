# 🧹 mi_libreria_texto

Librería Python desarrollada en el marco del Máster en Data Science & IA de Evolve.  
Ofrece funciones de procesamiento y análisis léxico de texto con visualización de frecuencias, soporte multilenguaje y limpieza avanzada.

---

## 🚀 Funcionalidades principales

- 🔤 **Limpieza del texto**  
  Convierte a minúsculas, elimina símbolos y espacios innecesarios.

- 🌍 **Detección automática del idioma**  
  Identifica si el texto está en español, inglés, etc.

- 🧹 **Eliminación de stopwords**  
  Elimina palabras vacías como “el”, “de”, “and”, etc. según el idioma detectado.

- 🧮 **Conteo de palabras**  
  Calcula el número total de palabras significativas.

- 📊 **Frecuencia de palabras**  
  Calcula cuántas veces aparece cada palabra y las visualiza en un gráfico de barras.

---

## 🧪 Ejemplo de uso

```python
from mi_libreria_texto import (
    limpiar_texto,
    detectar_idioma,
    eliminar_stopwords,
    contar_palabras,
    frecuencia_palabras
)

texto = "¡Hola Mundo! Esto es un ejemplo de texto."

idioma = detectar_idioma(texto)
texto_limpio = limpiar_texto(texto)
texto_filtrado = eliminar_stopwords(texto_limpio, idioma)
conteo = contar_palabras(texto_filtrado)
frecuencias = frecuencia_palabras(texto_filtrado)

print(f"Idioma: {idioma}")
print(f"Texto limpio: {texto_limpio}")
print(f"Texto sin stopwords: {texto_filtrado}")
print(f"Número de palabras: {conteo}")
print(f"Frecuencias: {frecuencias}")
```

---

## 📁 Estructura del proyecto

```
mi_libreria_texto/
├── mi_libreria_texto/
│   ├── __init__.py
│   ├── limpieza.py
│   └── analisis.py
├── tests/
│   ├── test_limpieza.py
│   └── test_analisis.py
├── main.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🔗 Requisitos

- `nltk`
- `langdetect`
- `matplotlib`
- `pytest`

Instala todo fácilmente con:

```bash
pip install -r requirements.txt
```

---

## 👩‍💻 Autora

**Valentina Bailón Cano**  
📎 [LinkedIn](https://www.linkedin.com/in/valentina-bailon-2653b22b7/)  
