

from persistence.Persistence import Persistence
from .RegionalGroupItem import RegionalGroupItem

class RegionalGroupDepot:

    def __init__(self):
        self.__item_dict:dict = {}
        self.init_item_dict()

    def get_item(self, KEY:str)\
            ->RegionalGroupItem:
        return self.__item_dict[KEY]

    def get_keys(self)->list:
        return list(
            self.__item_dict.keys()
        )

    def init_item_dict(self):
        nested_dict = Persistence\
            .read_regional_group_nested_dict()
        item = None
        for k in nested_dict:
            item = RegionalGroupItem(
                nested_dict[k])
            self.__item_dict[k] = item