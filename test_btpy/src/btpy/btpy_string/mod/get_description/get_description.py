


from ..get_between.get_between import*

def get_description(string:str,
        separator_string:str, 
        range_string_array:str)->list[str]:
    """
    Funcion que extrae de un string 
    una lista de elementos separadas 
    por el separator string; iniciando 
    desde el init_string hasta el 
    end_string.
    """
    init_string = range_string_array[0]
    end_string = range_string_array[1]
    string_description = get_between( \
            string, init_string, end_string)
    array = string_description\
        .split(separator_string)
    # elimina los espacios antes y despues
    for i in range(len(array)):
        array[i] = array[i].strip()
    return array