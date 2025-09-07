


"""
    Funcion que convierte un array de texto en una
    lista punteada con el formato indicado, el simbolo y
    el tamaño de margen.
"""
# return string
def write_a_string_array_as_a_dotted_list(\
        array,
        type = "",
        dot_symbol = ">",
        margin_size = 3
        ):
    text = ""
    margin = " " * margin_size
    i = 0
    for e in array:
        if(type == "number"):
            text += margin + str(i) + dot_symbol + " " + e + ".\n"
            i += 1
        else:
            text += margin + dot_symbol + " " + e + ".\n"
    return text
