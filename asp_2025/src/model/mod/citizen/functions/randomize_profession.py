
from btpy.Btpy import Btpy
from ..citizen_constants import*

def randomize_profession(data):
    list_ = list(PROFESSIONS_KEY_TUPLE)
    i = list_.index("TRAINEE")
    del(list_[i])
    KEY = Btpy.random_choice(list_)
    data.set_profession_key(KEY)
    return data