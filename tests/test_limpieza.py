from mi_libreria_texto import limpiar_texto

def test_limpiar_texto():
    assert limpiar_texto("Hola, Mundo!") == "hola mundo"
    assert limpiar_texto("Prueba123") == "prueba"
