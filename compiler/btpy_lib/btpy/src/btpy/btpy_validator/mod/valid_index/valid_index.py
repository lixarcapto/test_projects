


def valid_index(index: int, array: list)\
        ->None:
    """
    Funcion estricta de validacion para
    indices de arrays. Envia el array 
    a verificar.
    """
    #
    leng = len(array)
    # si no es int
    if(not type(index) == int):
        raise Exception(
            f"index is not integer({index})"
        )
    # si es negativo
    if(index < 0):
        raise Exception(
            f"negative index{index} \
            to leng {leng}"
        )
    # si es mayor del tamaño
    if(index >= leng):
        raise Exception(
            f"index out of limit\
            {index} to leng {leng}"
        )