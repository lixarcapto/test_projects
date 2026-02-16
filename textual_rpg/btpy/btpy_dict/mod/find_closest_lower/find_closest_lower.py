


from ..key_of.key_of import*

def find_closest_lower(DICT:dict, 
        NUMBER:int|float)-> any:
    """
    funcion que identifica en un 
    diccionario de numeros que numero 
    es el mas cercano inferior al numero 
    enviado; retornando su clave.
    """
    values_arr = sorted(DICT.values())
    former_number:int|float = 0
    for value in values_arr:
        if(value > NUMBER):
            break
        former_number = value
    key = key_of(DICT, former_number)
    return key


def find_closest_higher(DICT, 
        NUMBER) -> any:
    """
    Función que identifica en un diccionario de números qué número es el más cercano superior al número enviado, retornando su clave.

    Args:
        DICT: Diccionario donde las claves pueden ser de cualquier tipo y los valores deben ser números (int o float).
        NUMBER: Número para el cual se busca el número más cercano superior.

    Returns:
        La clave del número más cercano superior a NUMBER en el diccionario.
        Retorna None si el diccionario está vacío o si no hay números superiores a NUMBER.
    """
    if not DICT:  # Manejo de diccionario vacío
        return None

    values_arr = sorted(DICT.values())
    closest_higher = None

    for value in values_arr:
        if value > NUMBER:
            closest_higher = value
            break  # Detener la búsqueda tan pronto como se encuentra el primero superior

    if closest_higher is None:  # Manejo de no encontrar números superiores
        return None