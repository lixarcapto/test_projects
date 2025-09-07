


"""
    Funcion que busca un string similar al enviado en
    un array, map o matriz 2D.
"""
# return string
def get_similar_string(collection, searched_value):
    if(type(collection) == type({})):
        return __get_similar_string_in_map(collection,
            searched_value)
    elif(type(collection) == type([])):
        return __get_similar_string_in_array(collection,
            searched_value)
    elif(type(collection) == type([[]])):
        return __get_similar_string_in_matrix(collection,
            searched_value)

def __get_similar_string_in_array(array, searched_value):
    for i in range(len(array)):
        if(searched_value in array[i]):
            return array[i]
    return ""

def __get_similar_string_in_map(map, searched_value):
    for key in map:
        if(searched_value in map[key]):
            return map[key]
    return ""

def __get_similar_string_in_matrix(matrix, searched_value):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if(searched_value in array[y][x]):
                return array[y][x]
    return ""
