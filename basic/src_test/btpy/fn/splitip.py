



"""
Función que divide un string por palabras, 
lo convierte en un array, elimina los 
espacios extra y las palabras void; 
retornando un array con las palabras 
limpias.
"""
def splitip(text:str, divider:str)\
            ->list[str]:
    new_array = []
    array = []
    # split
    array = text.split(divider)
    # strip
    array = list(map(
        lambda e : e.strip(), 
        array
    ))
    # remove voids
    for e in array:
        if(not e == ""):
            new_array.append(e)
    return new_array