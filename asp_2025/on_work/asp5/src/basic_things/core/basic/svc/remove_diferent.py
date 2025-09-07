

from .remove_string import*
from .search_index_different import*
from .charat import*

"""
    Funcion que elimina los string indicados en el
    different_array enviado del string enviado.
"""
# return string_array
def remove_diferent(string,
        different_array):
    index_diferent = 0
    char_to_remove = ""
    limit = 10000
    count_limit = 0
    index_diferent = 0
    while(index_diferent != -1):
        index_diferent = search_index_different(
            string, different_array)
        char_to_remove = charat(string, index_diferent)
        string = remove_string(string, char_to_remove)
        if(count_limit >= limit):
            break
        count_limit += 1
    return string
