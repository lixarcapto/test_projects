


from .char_in_same_index import*
from .calculate_similes_chars import*

"""
    Funcion que calcula las similitudes entre dos strings
    a partir de sus caracteres similares y su posicion
    en la cadena; despues hace una media entre ambos
    porcentajes.
"""
# return int
def compare_strings(strig_primal, string_to_compare):
    percent_1 = char_in_same_index(strig_primal,
        string_to_compare)
    percent_2 = calculate_similes_chars(strig_primal,
        string_to_compare)
    array = [percent_1, percent_2]
    result = calculate_mid(array)
    return result

# return float
def calculate_mid(array):
    sum_number = 0
    for e in array:
        sum_number += e
    result = sum_number / len(array)
    return result
