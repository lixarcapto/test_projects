

from .go_instances.Go import Go
from .go_instances.GoAnimal import GoAnimal
from .go_instances.GoVegetable import GoVegetable

class GoFactory:

    """
    clase de Factory que 
    genera el objeto determinado por 
    la clave enviada
    """

    def __init__(self) -> None:
        self.go_dict = {}
        self.add_go_class("Go", Go)
        self.add_go_class(
            "GoVegetable", GoVegetable)
        self.add_go_class(
            "GoAnimal", GoAnimal)

    def add_go_class(self, key, 
            class_reference):
        """
        Función que permite Añadir nuevas 
        referencias a objetos Go en tiempo 
        de ejecución
        """
        self.go_dict[key] = class_reference

    def create(self, key_go:str, id)->Go:
        if(not key_go in self.go_dict):
            raise Exception(
                f"the {key_go} key does not exist"
            ) 
        return self.go_dict[key_go](id)