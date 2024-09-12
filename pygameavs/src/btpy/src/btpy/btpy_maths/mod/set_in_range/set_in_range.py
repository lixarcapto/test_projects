



def set_in_range(value: int, 
        range_arr: list)->int:
    """
    Funcion que ajusta un valor en el 
    rango limite enviado.
    """
    if value > range_arr[1]: 
        return range_arr[1]
    if value < range_arr[0]: 
        return range_arr[0]
    return value