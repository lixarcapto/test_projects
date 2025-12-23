

from .scenario.Scenario import Scenario

class Model:

    def __init__(self):
        self.scenario = Scenario()
        self.player_id = 0
        self.scenario.populate_room(0)

    def populate_character(self):

    def advance_time(self):
        self.scenario.advance_time()

    def write_narrative(self):
        player_char = self.scenario\
            .get_character(self.player_id)
        txt = player_char.history
        return txt
