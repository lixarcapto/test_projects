

from .GObject import GObject

class GPlayer(GObject):

    def __init__(self, id="") -> None:
        super().__init__(id)
        self.set_image_route(
            "../res/image/animal_pix_70x70.png"
        )
        self.is_movile = True
        self.is_player = True
        self.has_focus_cam = True
        self.set_is_mortal([0, 100])
        self.health_limit = 100
        self.health = 100