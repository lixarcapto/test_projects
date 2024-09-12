


import random

"""
    Funcion wrapper para mejorar choice de 
    random library añadiendo la posibilidad 
    de randomizar elementos de diccionarios.
"""
# return element
def random_choice(array: list):
    # si es array
    if(type(array) == type([])
    or type(array) == type("")):
        return random.choice(array)
    # si es diccionario
    elif(type(array) == type({})):
        key_arr = []
        for k in array:
            key_arr.append(k)
        key = random.choice(key_arr)
        return array[key]
    # si no es ninguno
    else:
        exception(
            "unsupported type",
            array,
            "you shoud send an array")
    
def exception(text, data, correction):
        margin = " " * 3
        raise Exception("\n\n" \
            + f"Error <!>: \n" \
            + f"{margin}Type: {text}\n" \
            + f"{margin}cause by: {data}\n"\
            + f"{margin}how to fix:" + correction\
            + "\n"
        )
