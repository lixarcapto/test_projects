

from .GObject import GObject

class GAnimal(GObject):

    def __init__(self, id="") -> None:
        super().__init__(id)
        self.set_image_route(
            "../res/image/animal_pix_70x70.png"
        )
        self.is_a_walker = True
        self.set_is_mortal([0, 100])