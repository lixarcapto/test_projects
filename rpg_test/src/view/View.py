

from btpy.Btpy import Btpy
from model.Model import Model
from .BattleTab import BattleTab

class View:

    def __init__(self):
        self.model = Model()
        self.window = Btpy.Window("RPG")
        self.window.set_size(1000, 700)
        self.battle_tab = BattleTab(
            self.window,
            self.model
        )
        self.battle_tab.pack()
        self.start()
        
    def start(self):
        self.window.start()

    