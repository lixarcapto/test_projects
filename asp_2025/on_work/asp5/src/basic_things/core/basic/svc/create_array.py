



"""
    Funcion que crea un array string numerico para pruevas
"""
# return string_array
def create_array(size = 27, type = "none"):
    if("none" == type):
        return [None] * size
    elif("number" == type):
        array = []
        for i in range(size):
            array.append(str(i))
        return array
    elif("letter" == type):
        abc_array = [
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                    "g",
                    "h",
                    "i",
                    "j",
                    "k",
                    "l",
                    "m",
                    "n",
                    "ñ",
                    "o",
                    "p",
                    "q",
                    "r",
                    "s",
                    "t",
                    "u",
                    "v",
                    "w",
                    "x",
                    "y",
                    "z"
                    ]
        array = []
        index_abc = 0
        for i in range(size):
            array.append(abc_array[index_abc])
            # itera el abc_array; regresando al inicio si termina
            if(index_abc < len(abc_array) -1):
                index_abc += 1
            else:
                index_abc = 0
    return array
