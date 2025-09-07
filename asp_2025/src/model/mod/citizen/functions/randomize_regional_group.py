

from ..CitizenData import CitizenData
from btpy.Btpy import Btpy

def randomize_regional_group(
            data:CitizenData):
        item = data\
            .get_cultural_group_item()
        list_ = item\
            .get_regional_group_list()
        key = Btpy.random_choice(list_)
        data.set_regional_group_key(key)
        return data