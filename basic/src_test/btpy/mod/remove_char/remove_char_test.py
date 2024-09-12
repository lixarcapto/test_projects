

from .remove_char import*
from btpy.Btpy import Btpy

@Btpy.printtest
def remove_char_test():
    r = remove_char("hola mundo", 2)
    if(not "l" in r): print("succes")
    else: print("fail")