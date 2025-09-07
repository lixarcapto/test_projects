


from .take_string_between import*

"""
    Funcion que busca en un string una descripcion
    iniciada por un punto y coma, y separada por comas,
    obtiene la descripcion y separada cada palabra entre
    comas para formar un array de elementos.
"""
# return string_array
def convert_description_to_array(string,
        name_list, init_string, separator_string, end_string):
    string_description = take_string_between( \
            string, init_string, end_string)
    array = string_description.split(separator_string)
    # elimina los espacios antes y despues
    for i in range(len(array)):
        array[i] = array[i].strip()
    return array
