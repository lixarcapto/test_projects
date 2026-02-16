



def route_in_dict(seek_string:str,
    dict:dict[dict]) ->list[str]:
    """
    Función que busca en profundidad 
    una serie de claves ordenadas 
    por profundidad a través de 
    diccionarios de diccionarios 
    anidados.
    """
    result = __recursive_search(seek_string,
        dict)
    print(f"{result=}")
    return result

"""
Función recursiva privada que se utiliza 
para la funcionalidad de este Script.
"""
def __recursive_search(seek_string:str, 
        dict_send:dict[dict])\
    ->list[str]:
    keys_array = []
    keys_array_nest = []
    for k in dict_send:
        # llamada recursiva si es un dict 
        # anidado
        if(type(dict_send[k]) == dict):
            keys_array_nest \
                = __recursive_search(
                seek_string, dict_send[k])
            # valida si el resultado de la 
            # busqueda recursiva fue correcto
            if(not keys_array_nest == []):
                # almacena la clave de este 
                # dict antes de las claves 
                # anidadas.
                keys_array.append(k)
                # añade las nuevas claves 
                # anidadas encontradas
                keys_array += keys_array_nest
                break
        # si no esta anidado busca el string
        # buscado y almacena la clave si 
        # lo encuentra.
        if(seek_string in dict_send[k]):
            keys_array.append(k)
            break
    return keys_array

        
