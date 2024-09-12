

from .GObject import GObject
from .GAnimal import GAnimal
from .GPlayer import GPlayer
from .GVegetable import GVegetable

class GoFactory:

    """
    clase de Factory que 
    genera el objeto determinado por 
    la clave enviada
    """

    def __init__(self) -> None:
        self.go_dict = {}
        self.add_go_class("GObject", GObject)
        self.add_go_class("GAnimal", GAnimal)
        self.add_go_class("GPlayer", GPlayer)
        self.add_go_class("GVegetable", GVegetable)

    def add_go_class(self, key, 
            class_reference):
        """
        Función que permite Añadir nuevas 
        referencias a objetos Go en tiempo 
        de ejecución
        """
        self.go_dict[key] = class_reference

    def create(self, key_go:str, id)->GObject:
        if(not key_go in self.go_dict):
            raise Exception(
                f"the {key_go} key does not exist"
            ) 
        return self.go_dict[key_go](id)