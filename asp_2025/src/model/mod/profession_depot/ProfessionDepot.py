

from .ProfessionItem import ProfessionItem
from persistence.Persistence import Persistence

class ProfessionDepot:

    def __init__(self):
        self.__profession_item_dict = {}
        self.init_item_dict()

    def get_profession_keys(self)->list:
        list_ = self.__profession_item_dict\
            .keys()
        return list(list_)

    def get_item(self, KEY:str)\
            ->ProfessionItem:
        return self.__profession_item_dict\
            [KEY]

    def init_item_dict(self):
        nested_dict = Persistence\
            .read_profession_nested_dict()
        item = None
        for k in nested_dict:
            item = ProfessionItem(
                nested_dict[k]
            )
            self.__profession_item_dict\
                [k.upper()] = item