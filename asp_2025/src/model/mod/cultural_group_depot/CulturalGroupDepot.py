

from .CulturalGroupItem import CulturalGroupItem
from persistence.Persistence import Persistence

class CulturalGroupDepot:

    def __init__(self):
        self.__item_dict:dict = {}
        self.__init_items()

    def get_key_list(self)->list:
        return list(
            self.__item_dict.keys())

    def get_item(self, KEY:str)->str:
        return self.__item_dict[KEY]

    def __init_items(self):
        nested_dict:dict = Persistence\
            .read_cultural_nested_dict()
        dict_:dict = {}
        item:CulturalGroupItem = None
        for k in nested_dict:
            dict_ = nested_dict[k]
            print("KEY", k)
            item = CulturalGroupItem(dict_)
            self.__item_dict[k] = item
