
from btpy.Btpy import Btpy
from Character import Character

class CharacterStore:

    def __init__(self):
        self.character_dict:dict = {}
        self.init()

    def init(self):
        nested_dict = Btpy\
            .read_xlsx_nested_dict_row(
                "./res/characters.xlsx"
            )
        dict_ = {}
        chara = None
        for k in nested_dict:
            dict_ = nested_dict[k]
            chara = Character()
            chara.load_character_dict(
                dict_
            )

    def get_character(self, KEY:str):
        return self.character_dict[KEY]
    
