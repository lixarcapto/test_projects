

from ...fn.percent_from_part import*

class CounterCall:

    """
        Tipo de dato especilizado para contar
        de forma agil un numero de llamadas.
        Se utiliza llamando al metodo is_end en
        un condicional, con cada llamada sumara
        un numero hasta llegar al limite indicado,
        una vez alcanzado el limite se formateara.
    """

    def __init__(self, limit):
        self.__counter = 0
        self.__limit = 0
        self.__set_limit(limit)

    def get_percent(self):
        percent = percent_from_part(
            self.__counter,
            self.__limit
        )
        percent = round(percent)
        r = str(percent) + "%"
        return r

    """
        Funcion que obtiene el numero contador.
    """
    # return int
    def get(self):
        return self.__counter

    def __set_limit(self, integer):
        if not type(0) == type(integer):
            raise Exception("limit isnt integer")
        if integer == 0: raise Exception("limit less minimum")
        self.__limit = integer

    def reset(self, limit = -1):
        if not limit == -1: self.__set_limit(limit)
        self.__counter = 0

    def is_end(self):
        if(self.__limit == self.__counter):
            self.reset()
            return True
        else:
            self.__counter += 1
            return False
