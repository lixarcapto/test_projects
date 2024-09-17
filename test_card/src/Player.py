


from btpy.src.btpy.Btpy import Btpy

class Player:

    def __init__(self) -> None:
        self.name = ""
        self.flip_card = []
        self.field_card = []
        self.deck_card = []
        Btpy.point_in_space()