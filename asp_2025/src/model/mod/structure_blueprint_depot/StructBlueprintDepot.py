

from .StructBlueprint import StructBlueprint
from persistence.Persistence import Persistence

class StructBlueprintDepot:

    def __init__(self):
        self.__struct_bp_dict\
            :dict = {}
        nested_dict:dict[dict] = Persistence\
            .read_structure_nested_dict()
        for k in nested_dict:
            self.add_struct_bp_dict(
                k, nested_dict[k])
            
    def get_struct_bp(self, KEY:str)\
            ->StructBlueprint:
        return self.__struct_bp_dict[KEY]
        
    def add_struct_bp_dict(self, 
            KEY:str, DICT:dict)\
            ->None:
        struct = StructBlueprint()
        print("DICT", DICT)
        struct.set_type_key(
            KEY)
        struct.set_recipe_key(
            DICT["recipe_key"])
        struct.set_life_time(
            DICT["life_time"])
        self.__struct_bp_dict[KEY] = struct

    