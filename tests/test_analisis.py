from mi_libreria_texto import contar_palabras, frecuencia_palabras

def test_contar_palabras():
    assert contar_palabras("hola mundo") == 2

def test_frecuencia_palabras():
    assert frecuencia_palabras("hola mundo hola") == {"hola": 2, "mundo": 1}
