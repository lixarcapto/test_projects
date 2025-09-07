


"""
    Funcion que corta un texto enviado desde el caracter
    indicado; retornando la primera parte del texto.
"""
# return text
def cuts_text_from_character(string, caracter):
    if caracter not in string:
        return ""
    else:
        return string.split(caracter)[0]
