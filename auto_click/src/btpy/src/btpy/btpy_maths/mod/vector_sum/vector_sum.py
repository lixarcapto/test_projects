



def vector_sum(array1:list[int], 
        array2:list[int])->list[int]:
    """
    Función que suma los elementos 
    de dos arrays de números en la 
    misma posición del array.
    """
    #
    new_array = array1.copy()
    for i in range(len(array1)):
        new_array[i] += array2[i]
    return new_array