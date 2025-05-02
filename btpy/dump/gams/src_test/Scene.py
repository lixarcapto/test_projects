

from Go import Go

class Scene:

    """
    Clase que simula un escenario de un 
    motor de escenario para la librería 
    GAMS.
    """
    def __init__(self) -> None:
        self.name:str = ""

    def create_go(self) -> Go:
        return Go()
