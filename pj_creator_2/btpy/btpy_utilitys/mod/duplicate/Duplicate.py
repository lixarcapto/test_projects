


class Duplicate:

    """
    clase utilizada para duplicar 
    referencias de tipos de datos 
    simples en python mediante un objeto.
    """

    def __init__(self, value = None) -> None:
        self.__value = value

    def get(self)->any:
        return self.__value
    
    def set(self, VALUE:any):
        self.__value = VALUE