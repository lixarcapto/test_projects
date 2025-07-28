

from Item import Item
from btpy.Btpy import Btpy

class ItemStore:

    def __init__(self):
        self.items_dict:dict = {}
        self.init_items()

    def get_item(self, KEY:str):
        return self.items_dict[KEY]

    def init_items(self):
        nested_dict = Btpy.read_xlsx_nested_dict_row(
            "./res/items.xlsx"
        )
        dict_ = {}
        item = None
        for k in nested_dict:
            dict_ = nested_dict[k]
            item = Item()
            item.load_item_dict(dict_)
            self.items_dict[k] = item