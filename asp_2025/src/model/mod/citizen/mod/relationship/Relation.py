


from btpy.Btpy import Btpy

class Relation:

    """
    Clase que representa a cada relacion
    individual de un character; con 
    su nivel de cercania y categoria.
    """

    __RELATION_DICT_RANGE:dict = {
        "COUPLE" : [201, 300],
        "FRIENDSHIP" : [101, 200],
        "STRANGER" : [-101, 100],
        "HATER" : [-201, -100],
        "ENEMY" : [-300, -200]
    }
    __RANGE_RELATION:list[int]= [-300, 300]

    def __init__(self):
        self.__value:int = 0
        self.__type_key:str = ""
        self.__subtype_key:str = ""
        self.__level_key:str = ""
        self.passport = None

    def get_subtype_key(self)->str:
        return self.__subtype_key
    
    def set_subtype_key(self, KEY:str):
        self.__subtype_key = KEY

    def get_level_key(self)->str:
        """
        Funcion que obtiene el nivel de
        relacion actual del personaje.
        Este nivel puede ser:
        * "COUPLE"
        * "FRIENDSHIP"
        * "STRANGER"
        * "HATER"
        * "ENEMY"
        """
        return self.__level_key

    def set_range_relation(
            RANGE_LIST:list[int]):
        """
        Funcion que asigna un rango en 
        formato lista al valor de las
        relaciones. Este rango indica
        el valor maximo y minimo que 
        pueden tener las relaciones.
        """
        Relation.__RANGE_RELATION \
            = RANGE_LIST

    def get_value(self)->int:
        """
        Funcion que obtiene el valor
        de la relacion actual.
        """
        return self.__value
    
    def get_type_key(self)->str:
        """
        Funcion que obtiene la categoria
        de relacion del objeto relacion.
        Esta son:
        * FAMILY
        * DISTANT
        """
        return self.__type_key
    
    def set_type_key(self, KEY:str)->None:
        """
        Funcion que asigna la categoria
        de relacion del objeto relacion.
        Esta son:
        * FAMILY
        * DISTANT
        """
        self.__type_key = KEY

    def sum_value(self, VALUE:int):
        """
        Funcion que suma un valor numerico
        entero a la relacion dentro
        de los limites del rango de
        relaciones.
        """
        self.__value = Btpy.sum_in_range(
            self.__value,
            VALUE,
            Relation.__RANGE_RELATION
        )
        self.__update_relation_level()

    # ------------------------------------
    # PRIVATE ----------------------------

    def __str__(self):
        return ""\
            + f"{self.__type_key=}\n"\
            + f"{self.__value=}\n"\
            + f"{self.__level_key=}\n"
    
    def __update_relation_level(self):
        """
        Funcion que detecta la categoria
        de relacion actual de la relacion.
        """
        dict_ = self.__RELATION_DICT_RANGE
        self.__level_key = Btpy.whats_range(
            dict_, 
            self.__value
        )