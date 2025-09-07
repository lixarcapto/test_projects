


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
def char_in_same_index(string_primal,
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
