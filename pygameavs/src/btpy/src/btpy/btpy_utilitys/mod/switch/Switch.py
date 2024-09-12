


class Switch:

    """
    Clase interruptor para realizar 
    cambios automaticos a variables 
    boolean con cada llamada. Para 
    usarla solo debe crearse un 
    objeto con un nombre estilo
    boolean y comprobarlo con 
    is_true().
    **NOTE**
    La variable rcy es una variable 
    reciclada, para evitar creaciones 
    constantes en los bucles.
    """

    def __init__(self, state_boolean = True):
        self.__boolean = state_boolean
        self.__boolean_rcy = state_boolean

    def is_true(self):
        self.__boolean_rcy = self.__boolean
        if(self.__boolean): self.__boolean = False
        else: self.__boolean = True
        return self.__boolean_rcy