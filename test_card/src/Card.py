

from btpy.src.btpy.btpy_engine\
    .mod.gobject.GObject import GObject

class Card(GObject):

    def __init__(self) -> None:
        super().__init__()
        self.add_image_layout(
            "../res/image/princess_125x225.png")
        self.attack = 1
        self.armor = 6
        self.magic = 3
        self.shield = 1
        self.cost = 1
        self.name = "none"
        self.description = ""
        self.group = ""
        self.set_hitbox_size(125, 225)

    def load_card_dict(self, KEY, CARD_DICT):
        self.attack = int(CARD_DICT["attack"])
        self.armor = int(CARD_DICT["armor"])
        self.shield = int(CARD_DICT["shield"])
        self.magic = int(CARD_DICT["magic"])
        self.cost = int(CARD_DICT["cost"])
        self.name = KEY
        self.description = CARD_DICT["description"]
        self.add_image_layout(CARD_DICT["route"])