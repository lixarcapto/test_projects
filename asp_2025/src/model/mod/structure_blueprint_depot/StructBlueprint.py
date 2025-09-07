


class StructBlueprint:

    def __init__(self):
        self.__type_key:str = ""
        self.__recipe_key:str = ""
        self.__life_time:int = 0

    def set_type_key(self, KEY:str):
        self.__type_key = KEY

    def get_type_key(self)->str:
        return self.__type_key
    
    def set_recipe_key(self, KEY:str):
        self.__recipe_key = KEY
    
    def get_recipe_key(self)->str:
        return self.__recipe_key
    
    def set_life_time(self, KEY:str):
        self.__life_time = KEY
    
    def get_life_time(self)->int:
        return self.__life_time