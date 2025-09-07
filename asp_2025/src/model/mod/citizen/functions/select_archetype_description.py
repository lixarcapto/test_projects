

from ..CitizenData import CitizenData
from ..citizen_constants import*
from btpy.Btpy import Btpy

def select_archetype_description(
        citizen_data:CitizenData):
    k = citizen_data.get_archetype_key()
    list_ = DESCRIPTION_ARCHETYPE_DICT[k]
    text = Btpy.random_choice(list_)
    return text