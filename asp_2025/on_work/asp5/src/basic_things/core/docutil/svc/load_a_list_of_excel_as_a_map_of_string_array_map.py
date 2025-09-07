

from .load_an_excel_file_as_a_string_array_dictionary import*

"""
    Funcion que carga una lista de archivos excel como
    un diccionario de diccionarios de arrays strings.
"""
# return map_of_string_array_map
def load_a_list_of_excel_as_a_map_of_string_array_map(\
    direction_folder,
    direction_array
    ):
    dictionary = {}
    direction = ""
    dictionary_2D = {}
    format = ".xlsx"
    # Filtro de array vacio
    if(len(direction_array) == 0):
        print("=> Error void array: in load_a_list_of_excel_as_a_map_of_string_array_map")
        return None
        # detecta si existen los archivos
        for e in direction_array:
            direction = direction_folder + "/" + e + format
            if(not os.path.exist(direction)):
                print("=> Error path dosnt exist in StorageFacade.load_excel_as_dictionary_2D_of_list")
                break
    for e in direction_array:
        direction = direction_folder + "/" + e + format
        dictionary = load_an_excel_file_as_a_string_array_dictionary(\
            direction)
        dictionary_2D[e] = dictionary
    return dictionary_2D
