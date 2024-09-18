

from btpy.src.btpy.btpy_utilitys\
    .mod.gobject.GObject import GObject

class Card(GObject):

    def __init__(self) -> None:
        super().__init__()
        self.route = "../res/cat_woman.png"
        self.attack = 1
        self.armor = 6
        self.magic = 3
        self.shield = 1
        self.cost = 1
        self.name = "none"