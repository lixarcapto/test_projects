
from Character import Character
from btpy.Btpy import Btpy
from ItemStore import ItemStore

class Scene:

    def __init__(self):
        self.pj_dict = Btpy\
            .read_xlsx_nested_dict_row(
                "./res/characters.xlsx"
            )
        self.place_key = ""
        self.is_turn_A = True
        self.battle_is_over = False
        self.character_1 = Character()
        self.character_2 = Character()
        self.you_win = False

    def advance_half_turn(self):
        self.character_1.update()
        self.character_2.update()
        self.fight()
        self.check_if_battle_is_over()

    def advance_one_turn(self):
        for i in range(2):
            self.advance_half_turn()

    def check_if_battle_is_over(self):
        if(self.character_1.is_dead
        or self.character_2.is_dead):
            if(self.character_1.is_dead):
                self.you_win = True
            self.battle_is_over = True

    def fight(self):
        pj_AT:Character = None
        pj_DF:Character = None
        if(self.is_turn_A):
            pj_AT = self.character_1
            pj_DF = self.character_2
        else:
            pj_AT = self.character_2
            pj_DF = self.character_1
        
        attack = pj_AT.final_attr["ATTACK"]
        damage_r = pj_AT.final_attr[
            "DAMAGE_RESISTANCE"]
        pj_DF.damage = Btpy.sum_in_range(
            pj_DF.damage, 
            attack,
            [0, 100]
        )

        if(self.is_turn_A):
            self.character_1 = pj_AT
            self.character_2 = pj_DF
            self.is_turn_A = False
        else:
            self.character_2 = pj_AT
            self.character_1 = pj_DF
            self.is_turn_A = True

    def write(self):
        txt = ""
        if(not self.battle_is_over):
            txt += "PJ 1:\n"
            txt += self.character_1.write() + "\n"
            txt += "PJ 2:\n"
            txt += self.character_2.write() + "\n"
        else:
            if(self.you_win):
                txt += "you win"
            else:
                txt += "you lose"
        return txt
    
    def get_character_keys(self):
        return list(self.pj_dict.keys())
        
    def get_character(self, KEY:str):
        return self.pj_dict[KEY]
    
    def receive_character_selected(self, 
            KEY):
        char_dict = self.get_character(KEY)
        character = Character()
        character.load_character_dict(
            KEY, char_dict)
        self.character_1 = character


    