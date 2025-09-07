


"""
    Funcion que comprueba si existe algo diferente
    al array de referencia enviado en el array
    enviado.
"""
# return int
def search_index_different(array_to_analize,
        array_reference):
    if(not type([]) == type(array_reference)):
        error = "=> Error isnt array "
        error += "("
        error += "/array_reference: " + str(array_reference) + ")"
        error += "in: search_index_different"
        print(error)
        return -1
    for i in range(len(array_to_analize)):
        if(not array_to_analize[i] in array_reference):
            return i
    return -1
