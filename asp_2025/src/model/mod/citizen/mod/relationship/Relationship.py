

from .Relation import Relation

class Relationship:

    SUBTYPE_KEY_TUPLE:tuple[str] = (
        "FATHER",
        "MOTHER",
        "BROTHER",
        "CHILDREN",
        "GRANDPARENT",
        "SPOUSE",
        "NONE"
    )

    """
    Esta clase sirve para representar y
    almacenar las relaciones sociales
    de un personaje con otros 
    personajes; almacena su nivel
    de cercania y distancia.
    METODOS:
    * set_relation: funcion que crea
    una nueva relacion o suma una relacion
    ya creada.
    * has_relation: funcion que retorna 
    si tiene o no una relacion.
    * get_relation: funcion que obtiene 
    una relacion y todos sus datos.
    """

    def __init__(self):
        # este dict almacena cada objeto
        # relation con su clave.
        self.__relation_dict\
            :dict[Relation] = {}
        
    def get_relation_dict(self)->Relation:
        return self.__relation_dict
        
    def get_subtype_relations(self, 
            SUBTYPE_KEY:str)\
            ->list[Relation]:
        """
        Funcion que obtiene una lista de
        las relaciones por subtipo.
        """
        relation_list:list = []
        v:Relation = None
        for k in self.__relation_dict:
            v = self.__relation_dict[k]
            if(v.get_subtype_key() 
                    == SUBTYPE_KEY):
                relation_list.append(v)
        return relation_list

    def set_relation(self, id_citizen:int,
            type_key:str, sum_value:int,
            subtype_key:str, 
            passport):
        """
        Funcion que crea o suma una nueva
        relacion segun el caso.
        """
        if(self.has_relation(id_citizen)):
            self.__sum_relation(id_citizen,
                sum_value
            )
        else:
            self.__add_relation(id_citizen,
                type_key, sum_value, 
                subtype_key, passport
            )

    def has_relation(self, id_citizen:int)\
            ->bool:
        """
        Funcion que retorna verdadero
        si tiene una relacion con el 
        citizen del ID enviado.
        """
        if(str(id_citizen) \
                    in self.__relation_dict):
            return True 
        return False
    
    def get_relation(self, 
            id_citizen:int)->str:
        """
        Funcion que obtiene una relacion
        actual almacenada en forma del
        objeto Relation.
        """
        return self.__relation_dict\
            [str(id_citizen)]
    
    # ------------------------------------
    # PRIVATE ----------------------------

    def __sum_relation(self, 
            id_citizen:int,
            sum_value:int):
        """
        Funcion que suma un valor a una
        relacion ya almacenada en el 
        diccionario.
        """
        self.__relation_dict[str(id_citizen)]\
            .sum_value(sum_value)

    def __add_relation(self, 
            id_citizen:int,
            type_key:str, 
            sum_value:int,
            subtype_key:str,
            passport):
        """
        Funcion que agrega una nueva 
        relacion al diccionario.
        """
        relation = Relation()
        relation.set_type_key(type_key)
        relation.sum_value(sum_value)
        relation.passport = passport
        self.__relation_dict[str(id_citizen)]\
            = relation