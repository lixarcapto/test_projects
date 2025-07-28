

from Scene import Scene
from btpy.Btpy import Btpy
from Character import Character
from PjSelector import PjSelector

class Model:

    def __init__(self):
        self.is_on = True
        self.scene = Scene()
        self.view_key = "selector"
        self.selector = PjSelector()
        self.selector.character_list\
            = self.scene.get_character_keys()
        pass

    def get_output(self)->str:
        output = ""
        if(self.view_key == "scene"):
            output = self.scene.write()
        if(self.view_key == "selector"):
            output = self.selector.write()
        return output

    def set_input(self, input_text)->str:
        result = ""
        if(input_text == "end"
        or input_text == "f"):
            self.is_on = False
            return result
        if(self.view_key == "scene"):
            self.scene.advance_one_turn()
        if(self.view_key == "selector"):
            self.selector.receibe_input(
                input_text)
            if(self.selector.is_ready):
                self.scene.receive_character_selected(
                    self.selector\
                        .character_select
                )
                self.view_key = "scene"
    
    