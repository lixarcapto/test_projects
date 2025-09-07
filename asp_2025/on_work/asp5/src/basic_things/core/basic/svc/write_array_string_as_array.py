


"""
    Funcion que escribe un diccionario de arrays de string
    como un solo diagrama de matriz en formato texto
"""
# return string
def write_array_string_as_array(map_of_string_array):
    # informa errores
    if(not len(map) > 0):
        print("=> Error: void map in LogicFacade.map_of_arrays_to_text.")
        return ""
    array = None
    text =  ""
    is_finish_element = False
    leng = len(map)
    i = 0
    n = 0
    # itera el map
    for key in map:
        array = map[key]
        # itera los arrays
        text += str(i) + "[ "
        for e in array:
            # añade comas a los elementos no finales
            # y a los elementos no iniciales
            if((n < leng -1)
            and (n > 0)):
                text += ", "
            text += e
            n += 1
        # salto de linea al terminar iteracion del map
        # añade corchete final
        text += "]\n"
        i += 1
        n = 0
    return text
