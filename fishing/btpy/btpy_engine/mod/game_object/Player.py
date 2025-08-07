

from .GameObject import GameObject

class Player(GameObject):

    def __init__(self, ID = ""):
        super().__init__(ID)
        self.set_is_collidable(True)
        self.set_is_solid(True)
        self.set_has_cam_focus(True)
        self.set_has_acceleration(True)
        self.set_has_air_resistance(True)
    