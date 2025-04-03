

from ....btpy_utilitys.mod.max_key.max_key import max_key, min_key

class CountingDict:

    def __init__(self):
        self.__dict:dict = {}

    def get(self)-> dict:
        return self.__dict
    
    def get_max(self)-> str:
        if(self.__dict == {}):
            return None
        return max_key(self.__dict)
    
    def get_min(self)-> str:
        if(self.__dict == {}):
            return None
        return min_key(self.__dict)
    
    def clean(self)-> None:
        self.__dict = {}

    def count(self, KEY:str)-> None:
        if(not KEY in self.__dict):
            self.__dict[KEY] = 1
        else:
            self.__dict[KEY] += 1