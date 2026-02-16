

# TODO: organizar esto
def write(data:dict, 
        margin:int = 0)-> str:
    txt = ""
    if(type(data) == dict):
        txt += write_dict(data)
    elif(type(data) == list):
        txt += write_list(data)
    return txt

def write_dict(data, margin = 1):
    margin_str = " " * margin
    txt = f"{margin_str}" + "{\n"
    v = None
    n = 0
    MARGIN_SIZE = 2
    type_key = None
    for k in data:
        v = data[k]
        type_key = type(v)
        # obtiene el valor
        if(type_key == dict):
            txt += write_dict(v, 
                margin + MARGIN_SIZE)
        elif(type_key == list):
            txt += write_list(v, 
                margin + MARGIN_SIZE)
        else:
            # escribe una clave valor
            txt += f"{margin_str} \'{k}\' : {v}"
        if(n < len(data) -1):
            txt += ","
        txt += f" # {k}\n"
        n += 1
    txt += margin_str + "}"
    return txt

def write_list(data, margin = 1):
    margin_str = " " * margin
    txt = f"{margin_str}[\n"
    v = None
    n = 0
    MARGIN_SIZE = 2
    for e in data:
        # obtiene el valor
        if(type(e) == dict):
            txt += write_dict(e, 
                margin + MARGIN_SIZE)
        elif(type(e) == list):
            txt += write_list(e, 
                margin + MARGIN_SIZE)
        else:
            # escribe una clave valor
            txt += f"{margin_str}{e}"
        if(n < len(data) -1):
            txt += ","
        txt += f" # {n}\n"
        n += 1
    txt += f"{margin_str}]"
    return txt