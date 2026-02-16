
import sys

class Char:

    """
    Esta clase es un tipo de dato character
    para Python. Sirve para reducir el 
    consumo de datos de los string de
    un solo char.
    Consiste en un string global que sirve
    para almacenar chars en cada indice
    del string. Aunque es mas eficiente
    en memoria consume mas prosesamiento.
    Para evitar desplazar los indices
    los indices void se muestran con el
    simbolo EMPTY_SYMBOL que indica que
    son espacios en memoria vacios que 
    pueden utilizarse.
    """

    last_index = 0
    _char_string = ""
    EMPTY_SYMBOL = "|"

    def __init__(self, char:str)\
            ->None:
        self.index = 0
        # revisa si tiene un indice
        # libre para almacenar
        result = self.get_free_index()
        if(result == -1):
            self.create_new_index()
        else:
            self.index = result
        self.set(char)

    def get_size_of():
        return sys.getsizeof(
            Char._char_string)

    def destroy(self):
        self.set(Char.EMPTY_SYMBOL)
        
    def __str__(self):
        return Char._char_string[self.index]

    def create_new_index(self):
        self.index = Char.last_index
        Char.last_index += 1
        Char._char_string += "|"


    def get_free_index(self)->int:
        i = 0
        for char in Char._char_string:
            if(char == Char.EMPTY_SYMBOL):
                return i
            i += 1
        return -1

    def set(self, char:str):
        if(not len(char) == 1):
            raise Exception("<!> Error: Char cannot store strings larger than one")
        array = list(Char._char_string)
        array[self.index] = char
        Char._char_string = "".join(array)
        

    def get(self):
        return Char._char_string[self.index]