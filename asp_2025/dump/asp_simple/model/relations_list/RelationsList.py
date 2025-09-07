


from .Relation import Relation

class RelationsList:

    """
    Clase que sirve para facilitar las
    relaciones entre personajes.
    """

    """
    Estas son las claves para identificar
    cada tipo de relacion: 
    FAMILY: es la relacion de familia
    FRIEND: es la relacion de amistad
    LOVER: es la relacion de noviasgo
    STRANGER: es la relacion basica
    """
    TYPE_KEYS = [
        "FAMILY",
        "FRIEND",
        "LOVER",
        "STRANGER"
    ]

    MAXIMUM_VALUE = 5

    def __init__(self):
        self.relation_arr:list = []

    def size(self)->int:
        return len(self.relation_arr)

    def write_relations(self)->str:
        """
        Escribe las relaciones del personaje
        como si narrara sus conocidos.
        """
        if(self.size() == 0):
            return "i don't know anyone"
        txt = "i know "
        leng = len(self.relation_arr)
        for i, e in enumerate(self.relation_arr):
            txt += f"my {e.type} "\
            + e.name_character
            if(not i == leng -1):
                txt += ", "
        return txt

    def add_relation(self, FULL_NAME:str,
            ID:int, TYPE:str):
        """
        Añade una nueva relacion.
        """
        relation = Relation()
        relation.id_character = ID
        relation.type = TYPE
        relation.name_character = FULL_NAME
        self.relation_arr.append(relation)

    def has_relation(self, ID)->False:
        """
        Retorna True si tiene la relacion
        con el ID indicado.
        """
        for e in self.relation_arr:
            if(e.id_character == ID):
                return True
        return False
    
    def sum_relation(self, ID, VALUE:int):
        """
        Suma el valor int a la relacion 
        actual.
        """
        value:int = 0
        e:Relation = None
        for i, e in enumerate(self.relation_arr):
            if(not e.id_character == ID): 
                continue
            value = self.relation_arr[i]\
                .value
            value += VALUE
            # ajusta el valor maximo
            if(value > self.MAXIMUM_VALUE):
                value = self.MAXIMUM_VALUE
            self.relation_arr[i]\
                .value = value
            break

    def set_relation(self, FULL_NAME:str,
            ID:int, TYPE:str = "STRANGER"):
        """
        Añade o modifica una relacion
        actual.
        """
        if(self.has_relation(ID)):
            self.sum_relation(ID, 1)
        else:
            self.add_relation(
                FULL_NAME, ID, TYPE)