


"""
    Funcion que suma los elementos de un
    array.
"""
# return element
def sum_array(array):
    if(not type([]) == type(array)):
        raise Exception("is not array")
    if(type("") == type(array[0])):
        result = ""
    elif(type(array[0] == int)
    or type(array[0]) == float):
        result = 0
    for i in range(len(array)):
        result += array[i]
    return result