


def seek_one(array:list, condition)\
        ->int|float|str|dict|list:
    """
     Función que busca un elemento por 
     la condición enviada en la lista.
    """
    return next(filter(condition, array), None)
        
def seek_all(array:list, condition)->list:
    """
     función que busca todos los 
     elementos por la condición enviada 
     en la lista.
    """
    return list(filter(condition, array))

def seek_number(array:list, number:int, 
        condition)->list:
    """
     función que busca la cantidad 
     determinada de elementos por la 
     condición enviada en la lista
    """
    result_arr = []
    n = 0
    for i in range(len(array)):
        if(condition(array[i])):
            result_arr.append(array[i])
            if(n == number): 
                return result_arr
            n += 1
    return result_arr