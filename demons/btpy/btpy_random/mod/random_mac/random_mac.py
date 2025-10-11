

import random
from ....btpy_const.mod.HEX_TUPLE import*

def random_mac():
    pair = ""
    QUANTITY_PAIR = 6
    array = []
    for i in range(QUANTITY_PAIR):
        pair = str(
            random.choice(HEX_TUPLE)
            )
        pair += str(
            random.choice(HEX_TUPLE)
            )
        array.append(pair)
    return ":".join(array)