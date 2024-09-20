


from btpy.src.btpy.Btpy import Btpy
from Card import Card

class Player:

    def __init__(self) -> None:
        self.name = ""
        self.flip_card = []
        self.field_card = []
        self.deck_card = []

    def add_deck(self, card):
        self.deck_card.append(card)

    def add_field(self, card):
        self.field_card.append(card)