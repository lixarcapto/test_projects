

from .world.World import World
import random

class Model:

    """
    Es el componente que representa el manejo
    de datos en memoria y las principales
    funciones del programa.
    """

    def __init__(self):
        self.world = None
        self.focus_id = 0
        # es el focus del character actual

    def create_world(self):
        print("create_world")
        self.world = World()
        self.focus_random()

    def advance_one_day(self):
        self.world.advance_one_day()

    def focus_random(self):
        self.focus_id = self.world\
            .randomize_person_id()

    def talk(self, text:str):
        print("talk")
        self.advance_one_day()
        desc = self.world.get_description(
            self.focus_id)
        return desc.write_all()
