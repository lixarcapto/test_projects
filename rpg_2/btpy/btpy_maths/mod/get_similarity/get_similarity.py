


def get_similarity(LIST_1: list, 
        LIST_2: list) -> int:
    """
    Calcula el número de elementos 
    de una lista que se encuentran 
    en la otra lista.
    Cuenta cada aparición de un elemento 
    en la lista más corta hasta el 
    número de apariciones de ese elemento 
    en la lista más larga.
    """

    # Convierte las listas en diccionarios para contar las ocurrencias de cada elemento.
    conteo1 = {}
    for elemento in LIST_1:
        conteo1[elemento] = conteo1.get(elemento, 0) + 1

    conteo2 = {}
    for elemento in LIST_2:
        conteo2[elemento] = conteo2.get(elemento, 0) + 1

    # Cuenta las similitudes.
    similitudes = 0
    for elemento, cantidad1 in conteo1.items():
        if elemento in conteo2:
            cantidad2 = conteo2[elemento]
            # Suma el mínimo de las apariciones en ambas listas.
            similitudes += min(cantidad1, cantidad2)

    return similitudes
