


class LimitedInt:

    """
        Tipo de dato personalizado para crear numeros int
        con limites marcados.
        Si no recibe un minimo el minimo sera el numero, si
        no recibe maximo el maximo sera el numero.
        TODO: para basic_things
    """
    def __init__(self, number, min = -1, max = -1):
        self.__number = number
        self.__min = 0
        self.__max = 0
        if(min != -1
        and max == -1):
            self.__min = min
            self.__max = number
        elif(min == -1
        and max != -1):
            self.__min = number
            self.__max = max
        elif(min != -1
        and max != -1):
            self.__number = number
            self.__min = min
            self.__max = max
        self.__result_rcy = 0

    def __check_is_in_range(self, quantity):
        if quantity < self.__min: return False
        if quantity > self.__max: return False
        return True

    """
        Suma el numero enviado dentro del rango limite.
    """
    def sum(self, quantity):
        self.__result_rcy = self.__number + quantity
        if(self.__result_rcy < self.__min):
            self.__number = self.__min
            return None
        elif(self.__result_rcy > self.__max):
            self.__number = self.__max
            return None
        self.__number = self.__result_rcy

    """
        Ajusta el numero enviado dentro del rango limite.
    """
    def set(self, quantity):
        if(quantity < self.__min):
            self.__number = self.__min
            return None
        elif(quantity > self.__max):
            self.__number = self.__max
            return None
        self.__number = quantity

    # return int
    def get(self):
        return self.__number
