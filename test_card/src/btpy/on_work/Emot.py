

from btpy.btpy_maths.mod.sum_in_range.sum_in_range import*
from btpy.btpy_list.mod.dict_operation.max_dict import*

class Emot:

    LIMIT = 10
    # limite a los estados
    MID = 3
    # mitad de limit

    def __init__(self) -> None:
        self.__states_dict = {
            "sadness":0,
            "joy":0,
            "disgust":0,
            "fear":0,
            "surprise":0
        }

    def get_state(self):
        return self.calcule_mayor_state()
    
    def advance_time(self):
        self.reduce_states()

    def sum_state(self, state_key, value = 1):
        e = self.__states_dict[state_key]
        e = sum_in_range(e, value, 
                     [0, Emot.LIMIT])
        self.__states_dict[state_key] = e

    def reduce_states(self):
        e = None
        for k in self.__states_dict:
            e = self.__states_dict[k]
            if(k == "surprise"):
                e -= 2
            if e >= 1: e -= 1
            self.__states_dict[k] = e

    def calcule_mayor_state(self):
        all_are_minors = self\
            .__are_all_minors()
        if(all_are_minors):
            return "bored"
        # si no todos son menores
        key = max_dict(
            self.__states_dict)
        return key
        
    """
    verifica si todos son menores
    """
    def __are_all_minors(self):
        e = None
        for k in self.__states_dict:
            e = self.__states_dict[k]
            if(not e <= Emot.MID):
                return False
        return True
        
    


