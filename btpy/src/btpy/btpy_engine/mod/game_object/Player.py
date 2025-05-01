

from .GameObject import GameObject

class Player(GameObject):

    def __init__(self, ID = ""):
        super().__init__(ID)
        self.set_is_collidable(False)
        self.set_is_solid(False)
        self.set_has_gravity(True)
        self.set_has_cam_focus(True)
        self.set_has_acceleration(True)
    