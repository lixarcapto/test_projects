


from btpy.src.btpy.Btpy import Btpy
from Card import Card

class Player:

    def __init__(self) -> None:
        self.name = ""
        self.flip_card = []
        self.field_card = []
        self.deck_card = []
        for i in range(5):
            self.deck_card.append(Card())
        for i in range(5):
            self.field_card.append(Card())