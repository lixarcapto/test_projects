

"""
    funcion que tome todo el string que siguen despues
    de un string hasta llegar al caracter indicado
"""
# return string
def take_string_between(\
        texto, delimitador_inicio,
        delimitador_fin
        ):
    """
    Función que extrae el texto entre dos delimitadores especificados.
    Args:
      texto: El texto del cual se desea extraer la parte deseada.
      delimitador_inicio: El delimitador que marca el inicio del texto a extraer.
      delimitador_fin: El delimitador que marca el final del texto a extraer.
    Returns:
      El texto extraído entre los delimitadores, o una cadena vacía si no se encuentra el texto.
    """
    posicion_inicio = texto.find(delimitador_inicio)
    if posicion_inicio == -1:
      return ""
    posicion_fin = texto.find(delimitador_fin, posicion_inicio + len(delimitador_inicio))
    if posicion_fin == -1:
      return ""
    texto_extraido = texto[posicion_inicio + len(delimitador_inicio):posicion_fin]
    return texto_extraido
