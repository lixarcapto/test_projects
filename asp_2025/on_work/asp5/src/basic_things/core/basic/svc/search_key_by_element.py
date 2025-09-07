


from ..index import write_error

"""
    Funcion que busca una clave en un diccionario de
    arrays usando un elemento de sus arrays.
"""
# return string
def search_key_by_element(map, searched_element):
    # si searched_element no es string
    if(not type("") == type(searched_element)):
        text = write_error(\
            error = "isn't string",
            file_name = "search_key_by_element",
            function_name = "search_key_by_element",
            data_error = str(searched_element)
        )
        print(text)
        return None
    # si map no es un diccionario
    if(not type({}) == type(map)):
        text = write_error(\
            error = "isn't map",
            file_name = "search_key_by_element",
            function_name = "search_key_by_element",
            data_error = str(map)
        )
        print(text)
        return None
    array = []
    e = None
    for key in map:
        array = map[key]
        for i in range(len(array)):
            e = array[i]
            if(e == searched_element):
                return key
    return ""
