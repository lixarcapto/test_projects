

from ...Btpy import Btpy
from .random_bool import random_bool

@Btpy.printtest
def test_random_bool():
    for i in range(10):
        print(random_bool())