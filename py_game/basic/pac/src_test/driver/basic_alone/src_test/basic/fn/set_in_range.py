


"""
    Funcion que ajusta un valor en el 
    rango limite enviado.
"""
# return number
def set_inrange(value: int, range_arr: list):
    if value > range[1]: return range_arr[1]
    if value < range[0]: return range_arr[0]
    return value