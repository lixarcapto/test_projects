


from .Pac import Pac
from btpy.Btpy import Btpy

@Btpy.printtest
def test_pack():
    for i in range(10):
        print(Pac.random_name())