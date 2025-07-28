
from btpy.Btpy import Btpy

class PjSelector:

    def __init__(self):
        self.character_select = ""
        self.is_ready = False
        self.character_list = []

    def write(self):
        txt = ""
        txt += self.select_your_character()
        return txt
    
    def receibe_input(self, TEXT):
        list_ = self.character_list
        idx = int(TEXT)
        print("idx", idx, "len(list_)", len(list_))
        if(len(list_) > idx 
        and idx >= 0):
            self.is_ready = True
            self.character_select\
                = list_[idx]

    def select_your_character(self):
        txt = ""
        list_ = self.character_list
        txt += "select your character\n" 
        for i in range(len(list_)):
            txt += f"{i}) {list_[i]}\n"
        return txt