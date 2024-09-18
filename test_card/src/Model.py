

from Player import Player
from btpy.src.btpy.Btpy import Btpy
from Card import Card

class Model:

    def __init__(self):
        self.player_1 = Player()
        self.player_2 = Player()
        scenario = Btpy.Scenario()

    def render(self):
        message = {
            "field_1": self.player_1.field_card,
            "field_2": self.player_2.field_card,
            "deck_1": self.player_1.deck_card
        }
        return message
        
