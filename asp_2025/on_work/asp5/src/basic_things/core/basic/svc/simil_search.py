


from .compare_strings import*

"""
    Funcion que busca una palabra similar basado en
    su letras similares y su posicion en la cadena,
    basado en el porcentage enviado.
"""
# return string
def simil_search(array, element, required_percent):
    result = None
    for i in range(len(array)):
        result =  compare_strings(array[i], element)
        if(result >= required_percent):
            return array[i]
    print("=> Error nof found string(" + element \
        + ")in: simil_search.simil_search")
    return ""
