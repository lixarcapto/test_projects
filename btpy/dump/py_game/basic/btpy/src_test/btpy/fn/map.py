

"""
    Funcion mapper mejorada para permitir
    el recorrido de arrays y diccionarios
    de cualquier profundidad.
"""
# return array or dict
def map(array, function):
    if(type(array) == type({})):
        array = __mapper_dict(array, function)
    elif(type(array) == type([])):
        array = __mapper_array(array, function)
    else:
        raise Exception("isnt an array or dict")
    return array

def __mapper_array(array, function):
    for i in range(len(array)):
        if(type(array[i]) == type([])):
            array[i] = __mapper_array(array[i], function)
        elif(type(array[i]) == type({})):
            array[i] = __mapper_dict(array[i], function)
        else:
            array[i] = function(array[i])
    return array

def __mapper_dict(dict, function):
    for k in dict:
        if(type(dict[k]) == type({})):
            dict[k] = __mapper_dict(dict[k], function)
        elif(type(dict[k]) == type([])):
            dict[k] = __mapper_array(dict[i], function)
        else:
            dict[k] = function(dict[k])
    return dict
