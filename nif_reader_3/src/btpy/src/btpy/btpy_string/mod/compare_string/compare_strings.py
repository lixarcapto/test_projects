





def compare_strings(
        strig_primal:str, 
        string_to_compare:str)\
        ->float|int:
    """
    Funcion que calcula las similitudes
    dos strings a partir de sus caracteres 
    similares y su posicion en la cadena; 
    despues hace una media entre ambos
    porcentajes.
    """
    percent_1 = __char_in_same_index(
        strig_primal,
        string_to_compare
    )
    percent_2 = __calculate_similes_chars(
        strig_primal,
        string_to_compare
    )
    array = [
        percent_1,
        percent_2
    ]
    result = __calculate_mid(array)
    return result

# return float
def __calculate_mid(array):
    sum_number = 0
    for e in array:
        sum_number += e
    result = sum_number / len(array)
    return result

"""
    Funcion que compara las letras similares en dos
    strings diferentes y retorna un porcentaje
    de similitudes.
    Algorithm:
    * recorre el string comparando cada letra en la
    otra palabra.
    * cuando encuentre una letra igual añade un punto y
    sigue con la siguiente hasta completar.
    * calcula un porcentaje basado en el total de puntos y
    los puntos obtenidos.

"""
# return integer
def __calculate_similes_chars(string_base, 
        string_to_compare):
    char = ""
    points = 0
    for i in range(len(string_to_compare)):
        char = string_to_compare[i:i+1]
        if(char in string_base):
            points += 1
            continue
    percentage = points * (100 / len(string_base))
    return percentage


"""
    función que calcule Cuántos caracteres de un string se
    encuentran en el mismo índice de un string enviado,
    y retorna un porcentaje entero de esa cantidad
    ALG:
    * itera sobre ambos string contando los
    caracteres en la misma posicion que son iguales.
    * controla no superar el tamaño.
"""
# return int
def __char_in_same_index(string_primal,
        string_to_compare):
    compare_array = []
    compare_array.append(len(string_primal))
    compare_array.append(len(string_to_compare))
    minimum = min(compare_array)
    char_primal = ""
    char_to_compare = ""
    points_counter = 0
    for i in range(minimum):
        char_primal = string_primal[i]
        char_to_compare = string_to_compare[i]
        # compara ambos chars y suma puntos
        if(char_primal == char_to_compare):
            points_counter += 1
    # calcula un porcentaje
    percent = points_counter * (100 / len(string_primal))
    return percent
