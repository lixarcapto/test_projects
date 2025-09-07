


import random

def random_probability_float(
        probability:int|float) -> bool:
    r = random.uniform(
        0, 100)
    if(r < probability):
        return True 
    return False

    