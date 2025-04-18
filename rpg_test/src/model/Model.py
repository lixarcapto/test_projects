

from .Character import Character
from btpy.Btpy import Btpy
from persistence.Persistence import Persistence

class Model:

    def __init__(self):
        self.turn_1 = None
        self.char_1 = None
        self.char_2 = None
        self.load_files()

    def load_files(self):
        Character.blueprint_dict\
            = Persistence\
                .load_character_dict()

    def new_match(self):
        self.turn_1 = Btpy.Switch()
        self.char_1 = Character()
        self.char_2 = Character()

    def get_render(self)->list:
        render_list = [
            self.char_1.get_render(),
            self.char_2.get_render()
        ]
        return render_list

    def advance_turn(self):
        if(self.turn_1.is_true()):
            self.char_1.receive_attack(
                self.char_2)
            if(not self.char_1.is_dead):
                self.char_2.receive_attack(
                    self.char_1)
        else:
            self.char_2.receive_attack(
                self.char_1)
            if(not self.char_2.is_dead):
                self.char_1.receive_attack(
                    self.char_2)
        self.turn_1.switch()
        self.char_1.advance_time()
        self.char_2.advance_time()
        self.clean_deads()

    def clean_deads(self):
        if(self.char_2.is_dead):
            self.char_1.experience +=1
            self.char_2 = Character()
            self.char_2.randomize()
        if(self.char_1.is_dead):
            self.char_2.experience +=1
            self.char_1 = Character()
            self.char_1.randomize()


    