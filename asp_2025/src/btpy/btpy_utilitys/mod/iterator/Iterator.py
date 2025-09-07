

from ....btpy_checkers.mod.is_index.is_index import*

class Iterator:

    """
    Clase iterador para representar
    un recorredor de arrays que 
    almacena los indices tras cada 
    iteracion. para usarlo solo deben 
    llamarse a su metodo next dentro 
    del condicional del bucle y tomar 
    sus elementos con get.
    """

    def __init__(self, array = [],
                 IS_CYCLE = False):
        self.__is_cycle:bool = IS_CYCLE
        self.__is_reverse:bool = False
        self.__list:list = array
        self.__index:int = 0
        self.set_list(array)
        self.set_is_cycle(IS_CYCLE)

    def get_size(self)->int:
        return len(self.__list)

    def set_is_reverse(self, 
            IS_REVERSE:bool)->None:
        """
        Funcion que indica si el iterador
        avansara en la lista en reversa.
        """
        self.__is_reverse = IS_REVERSE
    
    def set_is_cycle(self, IS_CYCLE:bool)\
            ->None:
        """
        Funcion que indica si el iterador
        se reiniciara al llegar a su 
        limite.
        """
        if(not type(self.__is_cycle) == bool):
            raise Exception(
                "The IS_CYCLE parameter must be a boolean type."
            )
        self.__is_cycle = IS_CYCLE

    def has_next(self)->bool:
        """
        Funcion que retorna si el iterador
        todavia tiene elementos sin 
        recorrer.
        """
        leng = len(self.__list)
        if(self.__is_reverse):
            if(self.__index >= 0):
                return True
            return False
        else:
            if(self.__index < leng -1):
                return True
            return False

    def set_list(self, LIST:list)->None:
        """
        Asigna una lista de cualquier
        tipo a como lista de elementos
        a recorrer.
        """
        # validators
        if(not type(LIST) == type([])
        and not type(LIST) == type(())):
            raise Exception(
                "LIST is not an array"
            )
        self.__index = 0
        self.__list = LIST

    def get_list(self)->list:
        """
        Funcion que retorna la lista
        almacenada en el iterador.
        """
        return self.__list
    
    # return element
    def next(self)->None:
        """
        Funcion que indica al objeto 
        que sume uno a su indice
        avansando en la iteracion.
        """
        leng = len(self.__list)
        if(not self.__is_reverse):
            if (self.__index < leng):
                self.__index += 1
            if(self.__is_cycle):
                if (self.__index >= leng):
                    self.__index = 0
        if(self.__is_reverse):
            if (self.__index >= 0):
                self.__index -= 1
            if(self.__is_cycle):
                if (self.__index <= 0):
                    self.__index = leng

    def get(self):
        print("index", self.__index)
        return self.__list[self.__index]
    
    def reset(self):
        """
        Resetea el indice al inicio
        de la lista.
        """
        if(self.__is_reverse):
            self.__index = 0
        else:
            self.__index = len(self.__list)

    def set_index(self, INDEX:int)->bool:
        is_index:bool = is_index(INDEX, 
                self.__list)
        if(not is_index):
            raise Exception(
                f"The index sent is not a valid index for the stored list; its size is ({len(self.__list)})."
            )
        self.__index = INDEX

    def destroy(self):
        self.__list.clean()
        self.__list = None

    def set(self, ELEMENT:any)->None:
        """
        Funcion que remplaza el elemento
        del array en el indice indicado.
        """
        self.__list[self.__index] \
            = ELEMENT

    def remove(self)->None:
        """
        Funcion que elimina el elemento
        actual del iterador.
        """
        element = self.__list[self.__index]
        del(self.__list[self.__index])

    def extract(self)->any:
        """
        Funcion que extrae el elemento
        actual de la lista; usarlo 
        con precaucion.
        """
        element = self.__list[self.__index]
        del(self.__list[self.__index])
        return element