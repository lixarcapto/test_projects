

from .Go import Go

class GoAnimal(Go):

    def __init__(self, id) -> None:
        super().__init__(id)
        self.src_image \
            = "../res/image/bird_100x100_icon.png"
        self.is_a_walker = True
        self.set_is_mortal(0, 30)

    def update(self):
        super().update()
        