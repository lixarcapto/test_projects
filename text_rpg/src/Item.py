

class Item:

    ATTRIBUTES_TUPLE:tuple = (
        "ATTACK",
        "DEFENSE",
        "SPEED",
        "DAMAGE_RESISTANCE"
    )

    def __init__(self):
        self.attributes_dict:dict = {}
        for e in Item.ATTRIBUTES_TUPLE:
            self.attributes_dict[e] = 0

    def load_item_dict(self, DICT):
        self.attributes_dict = DICT