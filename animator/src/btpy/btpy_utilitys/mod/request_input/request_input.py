



def request_input(request_dict:list[str])\
        -> dict:
    """
    iterador con un dict que 
    solicita una serie de datos 
    utilizando un bucle indefinido 
    con un input para retornar un dict
    """
    dict = {}
    user_input = ""
    type_key = ""
    map_function = {
        "str":lambda e:e,
        "int":lambda e:int(e),
        "list":lambda e:list(e),
        "float":lambda e:float(e)
    }
    for request_key in request_dict:
        type_key = request_dict[request_key]
        user_input = input(f"{request_key}: ")
        user_input = map_function[type_key]\
            (user_input)
        dict[request_key] = user_input
    return dict