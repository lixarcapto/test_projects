

from .GObject import GObject

class GVegetable(GObject):

    def __init__(self, id="") -> None:
        super().__init__(id)
        self.set_image_route(
            "base", "../res/image/three_bald_70x70.png"
        )
        self.set_is_mortal([0, 100])