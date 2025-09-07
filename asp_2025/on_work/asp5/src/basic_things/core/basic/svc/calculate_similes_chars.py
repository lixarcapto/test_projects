


from ..index import charat

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
def calculate_similes_chars(string_base,
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
