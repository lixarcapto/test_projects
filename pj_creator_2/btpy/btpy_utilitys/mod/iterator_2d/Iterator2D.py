

from ....btpy_checkers.mod.is_index.is_index import*

class Iterator2D:

    """
    Clase iterador para representar
    un recorredor de matrices 2D que 
    almacena los indices tras cada 
    iteracion. para usarlo solo deben 
    llamarse a su metodo next dentro 
    del condicional del bucle y tomar 
    sus elementos con get.
    """

    def __init__(self, matrix_2d = [],
                 IS_CYCLE = False):
        self.__is_cycle:bool = IS_CYCLE
        self.__is_reverse:bool = False
        self.__matrix_2d:list = matrix_2d
        self.__index:int = 0
        self.__index_x:int = 0
        self.__index_y:int = 0
        self.set_matrix_2d(matrix_2d)
        self.set_is_cycle(IS_CYCLE)

    def get_size(self)->int:
        size:int = 0
        for list_ in self.__matrix_2d:
            size += len(list_)
        return size

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
        leng = self.get_size()
        if(self.__is_reverse):
            if(self.__index >= 0):
                return True
            return False
        else:
            if(self.__index < leng -1):
                return True
            return False
        
    def get_index_point(self)->list[int]:
        n = 0
        for y in range(len(self.__matrix_2d)):
            for x in range(
                    len(self.__matrix_2d[y])):
                if(self.__index != n):
                    n += 1
                    continue
                return [x, y]

    def set_matrix_2d(self, LIST:list)->None:
        """
        Asigna una lista de cualquier
        tipo como lista de elementos
        a recorrer.
        """
        # validators
        if(not type(LIST) == type([])
        and not type(LIST) == type(())):
            raise Exception(
                "LIST is not an array"
            )
        self.__index = 0
        self.__index_x = 0
        self.__index_y = 0
        self.__matrix_2d = LIST

    def get_matrix_2d(self)->list:
        """
        Funcion que retorna la lista
        almacenada en el iterador.
        """
        return self.__matrix_2d
    
    # return element
    def next(self)->None:
        """
        Funcion que indica al objeto 
        que sume uno a su indice
        avansando en la iteracion.
        """
        leng = self.get_size()
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

    def get(self)->int:
        n = 0
        for x in range(len(self.__matrix_2d)):
            for y in range(
                    len(self.__matrix_2d[x])):
                if(self.__index != n):
                    n += 1
                    continue
                return self\
                    .__matrix_2d[x][y]
        return None
    
    def reset(self):
        """
        Resetea el indice al inicio
        de la lista.
        """
        if(self.__is_reverse):
            self.__index = 0
        else:
            self.__index = self.get_size()

    def set_index(self, INDEX:int)->bool:
        is_index:bool = False
        if(INDEX > 0
        and INDEX < self.get_size()):
            self.__index = True
        if(not is_index):
            raise Exception(
                f"The index sent is not a valid index for the stored list; its size is ({len(self.__matrix_2d)})."
            )
        point = self.get_index_point()
        self.__index_x = point[0]
        self.__index_y = point[1]
        self.__index = INDEX

    def destroy(self):
        self.__matrix_2d.clean()
        self.__matrix_2d = None

    def set(self, ELEMENT:any)->None:
        """
        Funcion que remplaza el elemento
        del array en el indice indicado.
        """
        n = 0
        for y in range(len(self.__matrix_2d)):
            for x in range(
                    len(self.__matrix_2d[y])):
                if(self.__index != n):
                    n += 1
                    continue
                self.__matrix_2d[x][y] \
                    = ELEMENT
                return None

    def remove(self)->None:
        """
        Funcion que elimina el elemento
        actual del iterador.
        """
        n = 0
        for y in range(len(self.__matrix_2d)):
            for x in range(
                    len(self.__matrix_2d[y])):
                if(self.__index != n):
                    n += 1
                    continue
                del(self.__matrix_2d[x][y])
                return None

    def extract(self)->any:
        """
        Funcion que extrae el elemento
        actual de la lista; usarlo 
        con precaucion.
        """
        element = None
        n = 0
        for y in range(len(self.__matrix_2d)):
            for x in range(
                    len(self.__matrix_2d[y])):
                if(self.__index != n):
                    n += 1
                    continue
                element = self.__matrix_2d\
                    [x][y]
                del(self.__matrix_2d[x][y])
                return element