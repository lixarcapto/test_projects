


class MatrixIterator:

    """
    Iterador para navegar atraves de 
    matrizes de datos de dos dimensiones.
    Las principales funcione son:
    * get: obtiene el actual elemento.
    * set: modifica el actual elemento.
    * next: avansa al siguiente elemento.
    """

    def __init__(self, matrix2d) -> None:
        self.__y:int = 0
        self.__x:int = 0
        self.__matrix2d:list[list] = [[]]
        self.set_matrix2d(matrix2d)

    # PUBLIC ----------------------------

    def set_matrix2d(self, matrix:list[list]):
        self.__matrix2d = matrix 

    def next(self)->bool:
        size_x = len(
            self.__matrix2d[self.__y])
        size_y = len(self.__matrix2d)
        if(size_x -1 > self.__x):
            self.__x += 1
        else:
            self.__x = 0
            if(size_y -1 > self.__y):
                self.__y += 1
            else:
                return False
        return True
        

    def reset(self):
        self.__x = 0
        self.__y = 0
        
    def get(self):
        return self.__matrix2d\
            [self.__y][self.__x]
    
    def set(self, element):
        self.__matrix2d\
            [self.__y][self.__x]\
                = element
        
    def get_matrix2d(self):
        return self.__matrix2d
    
    def write(self):
        txt = ""
        txt += f"{self.__x=}\n"
        txt += f"{self.__y=}\n"
        return txt
    
    def __str__(self):
        return self.write()