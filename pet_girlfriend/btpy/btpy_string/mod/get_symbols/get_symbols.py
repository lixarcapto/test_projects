

from ....btpy_const.mod.ALPHABET_TUPLE import*

def get_symbols(TEXT):
    """
    Obtiene las palabras y los simbolos
    de un texto como un array.
    """
    char = ""
    buffer_text = ""
    symbols_arr = []
    want_letter = True
    if(TEXT[0] in ALPHABET_TUPLE):
        want_letter = True
    else:
        want_letter = False
    for i in range(len(TEXT)):
        char = TEXT[i]
        if(want_letter):
            if(not char in ALPHABET_TUPLE):
                symbols_arr.append(buffer_text)
                buffer_text = ""
                want_letter = False
        if(not want_letter):
            if(char in ALPHABET_TUPLE):
                symbols_arr.append(buffer_text)
                buffer_text = ""
                want_letter = True
        buffer_text += char
    symbols_arr.append(buffer_text)
    return symbols_arr