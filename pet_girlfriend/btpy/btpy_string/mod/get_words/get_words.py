



def get_words(text:str)->list[str]:
    """
    Función que divide un texto en 
    palabras separando por puntuación 
    y espacios
    """
    # separar por puntos
    string_arr = text.split(".")
    # separar por comas
    string_arr = __sub_split(",", string_arr)
    # separar por espacios
    string_arr = __sub_split(" ", string_arr)
    # filtrar otros simbolos
    symbol_list = [
        ",",
        ".",
        " ",
        ":",
        ";"
    ]
    for i in range(len(string_arr)):
        for e in symbol_list:
            string_arr[0].replace(e, "")
    # normalizar todo
    return string_arr

def __sub_split(search_str, string_arr):
    new_string_arr = []
    temp_arr = []
    for i in range(len(string_arr)):
        if(search_str in string_arr[i]):
            temp_arr = string_arr[i].split()
            new_string_arr += temp_arr
        else:
            new_string_arr\
             .append(string_arr[i])
    return new_string_arr
    

   