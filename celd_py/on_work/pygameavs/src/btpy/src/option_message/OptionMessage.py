

from .Desition import Desition
from btpy.Btpy import Btpy

class OptionMessage:

    def __init__(self) -> None:
        self.desition_dict = {}
        self.actual_key = ""
        self.start_key = ""
        self.has_start_key = False
        self.is_end = False
        self.historic_key_arr = []

    def write_narrative(self):
        txt = ""
        txt += self.get_desition()\
            .write_narrative()
        return txt
    
    def write_historic(self):
        txt = "you chose:\n"
        i = 0
        for e in self.historic_key_arr:
            txt += str(i) + " " *2 + e + "\n"
            i += 1
        return txt

    def new_desition_dict(
        self, desition_dict:dict):
        self.new_desition(
            desition_dict["id"],
            desition_dict["text"],
            desition_dict["option_id_arr"]
        )

    def new_desition(self, id:str, text:str, 
            option_id_arr:list[str])->None:
        if(not self.has_start_key):
            self.start_key = id 
            self.actual_key = id
            self.has_start_key = True
        desition = Desition(id)
        desition.text = text
        desition.option_id = option_id_arr
        self.desition_dict[id] = desition

    def get_desition(self)->Desition:
        return self.desition_dict\
            [self.actual_key]
    
    def set_desition(self, desition):
        self.desition_dict\
            [desition.actual_key] = desition
        
    def has_next(self):
        desition = self.get_desition()
        if(desition.option_id == []):
            return False
        return True

    def next_desition(self, 
            index:int)->None:
        desition = self.get_desition()
        # si no existe la opcion
        if(index < 0 \
           or index > len(desition.option_id)):
            return None
        # si existe
        self.actual_key = desition\
            .option_id[index -1]
        # añade un historico
        self.historic_key_arr\
            .append(self.actual_key)
        
    def start(self):
        user_input = ""
        while(True):
            Btpy.clean_console()
            print(self.write_narrative())
            if(not self.has_next()):break
            user_input = input()
            self.next_desition(int(user_input))
            if(user_input == "f"): break