


import re
"""
    Funcion que divide un string por los 
    string enviados en el array. Utiliza 
    la libreria re
"""
# return string_array
def split_by(text, delimiters):
    pattern = f"|".join(re.escape(d) for d in delimiters)
    array_words = re.split(pattern, text)
    # limpia arrays de espacios y vacios
    for i in range(len(array_words) -1):
        array_words[i] = array_words[i].strip()
        if(array_words[i] == ""):
            del(array_words[i])
    return array_words