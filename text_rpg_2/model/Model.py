

from .Scenario import Scenario

class Model:

    def __init__(self):
        self.scenario = Scenario()

    def request(self, ORDER_DICT):
        order = ORDER_DICT["ORDER"]
        if(order == "move"):
            idx = ORDER_DICT["INDEX"]
            self.scenario.move_player(idx)
        elif(order == "attack"):
            id_ = ORDER_DICT["ID"]
            self.scenario.attack_pj(
                self.scenario.player_id, 
                id_
            )

    def render(self)->dict:
        dict_ = {
            "PLAYER":self.scenario\
                .write_player()
        }
        self.scenario.update()
        return dict_