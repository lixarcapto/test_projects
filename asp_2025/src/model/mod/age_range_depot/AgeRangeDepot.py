

from .AgeRangeItem import*
from persistence.Persistence import Persistence

class AgeRangeDepot:

    def __init__(self):
        self.item_dict:dict = {}
        self.age_range_dict:dict = {}
        age_range_dict = Persistence\
            .read_age_range_dict()
        self.load_age_range_dict(
            age_range_dict
        )
        self.create_age_range_list_dict()

    def get_age_range(self, KEY:str)\
            ->AgeRangeItem:
        return self.item_dict[KEY]

    def create_age_range_list_dict(self):
        dict_ = {}
        list_ = []
        for k in self.item_dict:
            list_ = self.item_dict[k]\
                .range_list
            dict_[k] = list_
        self.age_range_dict = dict_

    def load_age_range_dict(self, 
            NESTED_DICT):
        item = None
        for k in NESTED_DICT:
            item = AgeRangeItem(
                NESTED_DICT[k]
            )
            self.item_dict[k] = item
