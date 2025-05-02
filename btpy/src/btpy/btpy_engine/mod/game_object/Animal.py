

from .GameObject import GameObject

class Animal(GameObject):

    def __init__(self, ID = ""):
        super().__init__(ID)
        self.set_animation_list("lion",
            "lion_icon_70x70.png")
        self.set_is_collidable(True)
        self.set_is_solid(True)
        self.set_has_acceleration(True)
        self.set_has_air_resistance(True)
        self.set_is_a_walker(True)