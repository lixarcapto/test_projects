

from .Go import Go

class GoVegetable(Go):

    def __init__(self, id) -> None:
        super().__init__(id)
        self.src_image \
            = "../res/image/vegetable_100x100_icon.png"

    def update(self):
        super().update()
        