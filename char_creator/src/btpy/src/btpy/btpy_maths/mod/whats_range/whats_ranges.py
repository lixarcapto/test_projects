


from ....btpy_checkers.mod.in_range.in_range import*

def whats_range(ranges_named:dict, 
            number:int)->list[str]:
    """
    Función que analiza En qué Rango 
    del diccionario de rangos enviados 
    se encuentra el número enviado 
    retornando la clave que identifica 
    al Rango
    """
    range_keys_arr:list = []
    result:bool = False
    for k in ranges_named:
        result = in_range(
            number,
            ranges_named[k])
        if(result):
            range_keys_arr.append(k)
    return range_keys_arr