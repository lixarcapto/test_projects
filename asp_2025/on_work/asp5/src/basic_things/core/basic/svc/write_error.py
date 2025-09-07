


"""
    Funcion que escribe un error de forma ordenada y
    limpia en consola.
"""
# return string
def write_error(\
        error,
        file_name,
        function_name,
        data_error = ""
        ):
    text = "=> Error " + error + " "
    text += "in " + file_name + "." + function_name + " "
    # si tiene datos de error los agrega
    if(not data_error == ""):
        text += "with: \n"
        text += "(" + data_error + ") "
    text += "\n"
    return text
