


def merge_as_dict(KEYS_LIST:list, 
        VALUES_LIST:list)->dict:
    """
    Funcion que crea un diccionario 
    utilizando dos listas.
    """
    if len(KEYS_LIST) != len(VALUES_LIST):
        raise ValueError(
            "lists have different sizes")
    result_dict = dict(
        zip(KEYS_LIST, VALUES_LIST)
    )
    return result_dict