


from .compare_strings import*

"""
    Funcion que busca una palabra similar basado en
    su letras similares y su posicion en la cadena,
    basado en el porcentage enviado.
    # XXX No funciona bien
"""
# return string
def simil_search(array:list, element:str, 
        required_percent:int) -> str:
    r = None
    for i in range(len(array)):
        r =  compare_strings(array[i], element)
        print(f"{element}:{array[i]}:{r}%")
        if(r >= required_percent):
            return array[i]
    print("=> Error nof found string(" + element \
        + ")in: simil_search.simil_search")
    return ""