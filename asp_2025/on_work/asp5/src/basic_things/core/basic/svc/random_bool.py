

from ..dependences import random

def random_bool():
    if(random.randint(0, 1) == 0):
        return False
    return True
