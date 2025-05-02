

"""
    Funcion estricta de validacion para
    indices de arrays. Enva el tamaño
    para no generar una copia inesesaria 
    del array.
"""
# not return
def valid_index(index: int, leng: int):
    # si no es int
    if(not type(index) == int):
        raise Exception(f"index is not integer \
            ({index})")
    # si es negativo
    if(index < 0):
        raise Exception(f"negative index \
            {index} to leng {leng}")
    # si es mayor del tamaño
    if(index >= leng):
        raise Exception(f"index out of limit\
            {index} to leng {leng}")