

def sort_numbers_dict_descending(
        diccionario_numeros):
    """
    Ordena las claves de un diccionario 
    de números de mayor a menor, 
    según sus valores.
    Args:
        diccionario_numeros (dict): Un diccionario donde las claves son únicas
            y los valores son números (enteros o flotantes).

    Returns:
        list: Una lista de las claves del diccionario, ordenadas de mayor a menor
            según los valores correspondientes en el diccionario.
            Devuelve una lista vacía si el diccionario de entrada está vacío.
    """
    if not diccionario_numeros:
        return []  # Devuelve una lista vacía si el diccionario está vacío

    # Ordena las claves del diccionario utilizando una lambda function como key.
    # La lambda function toma una clave (k) y devuelve el valor del diccionario
    # correspondiente a esa clave (diccionario_numeros[k]).
    # El argumento reverse=True asegura que el orden sea descendente.
    claves_ordenadas = sorted(
        diccionario_numeros, 
        key=lambda k: 
        diccionario_numeros[k], 
        reverse=False
    )
    return claves_ordenadas