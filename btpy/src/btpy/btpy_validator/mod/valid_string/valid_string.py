


def valid_string(data: str, 
        min_size = -1, /,
        is_strict:bool = False)->None:
    """
    funcion para validar la cadena enviada;
    esto valida si la cadena es una
    cadena, no esta vacia y es mayor
    que el minimo (opcional)
    """
    text = ""
    if(not type(data) == str):
        text = f"Error: data is not "\
        + f"string ({data})"
        if(is_strict):
            raise Exception(text)
        else:
            print(text)
            return None
    if(data == ""):
        text = f"Error: data is void string"
        if(is_strict):
            raise Exception(text)
        else:
            print(text)
            return None
    if(min_size != -1):
        if(len(data) < min_size):
            text = f"Error: data is less "\
            + f"minimum size {len(data)}"
            if(is_strict):
                raise Exception(text)
            else:
                print(text)
                return None
