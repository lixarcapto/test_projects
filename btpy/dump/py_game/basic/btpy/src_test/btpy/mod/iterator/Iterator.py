

class Iterator:

    """
        Clase iterador para representar
        un recorredor de arrays que almacena
        los indices tras cada iteracion.

        para usarlo solo deben llamarse
        a su metodo next dentro del condicional
        del bucle y tomar sus elementos con get.
    """

    def __init__(self, array, 
                 is_cycle = False):
        if(not type(array) == type([])
        and not type(array) == type(())):
            raise Exception("isnt array")
        if(len(array) <= 1):
            raise Exception("it's very small")
        if(not type(is_cycle) == type(True)):
            is_cycle = False
        self.__is_cycle = is_cycle
        self.__array = array
        self.__element_rcy = None
        self.__i = -1

    """
        Funcion que indica al objeto que sume
        uno a su indice avansando en la iteracion
        y ademas retorne el objeto antes de la suma.
    """
    # return element
    def next(self):
        element = None
        if(self.__is_cycle):
            if (self.__i < len(self.__array)-1):
                self.__i += 1
                return True
            else:
                self.__i = -1
                return False
        else:
            if (self.__i < len(self.__array)-1):
                self.__i += 1
                return True
            else:
                return False

    def get(self):
        return self.__array[self.__i]

    def __destroy(self):
        self.__array.clean()
        self.__array = None

    def extract(self):
        array = self.__array.copy()
        self.__destroy()
        return array