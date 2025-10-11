



def remove_between(cadena, inicio, fin):
    """
    Elimina todo el texto entre dos 
    cadenas específicas, incluyendo esas 
    cadenas. Retorna el string original
    si no encuentra el dato.
    """
    # Encontrar el índice inicial de la 
    # sección a eliminar
    indice_inicio = cadena.find(inicio)
    # Si la cadena de inicio no se encuentra,
    #  retornar la cadena original
    if indice_inicio == -1:
        return ""
    # Encontrar el índice final de la 
    # sección a eliminar
    indice_fin = cadena.find(
        fin, indice_inicio + len(inicio))
    # Si la cadena de fin no se encuentra, 
    # retornar la cadena original
    if indice_fin == -1:
        return cadena
    # Construir la nueva cadena eliminando 
    # la sección
    nueva_cadena = cadena[:indice_inicio]\
        + cadena[indice_fin + len(fin):]
    return nueva_cadena