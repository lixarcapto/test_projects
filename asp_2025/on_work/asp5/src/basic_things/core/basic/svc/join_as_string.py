


"""
    Funcion que escribe un array de string como una
    descripcion separadas por comas.
"""
# return string
def join_as_string(string_array,
        divisor_symbol = ","):
    its_string = True
    if(not type("") == type(string_array[0])):
        its_string = False
    text = ""
    i = 0
    limit = len(string_array)
    for e in string_array:
        if(its_string):
            text += e
        else:
            text += str(e)
        if(i != limit -1):
            text += divisor_symbol + " "
        i += 1
    return text
