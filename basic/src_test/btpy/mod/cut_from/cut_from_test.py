


from btpy.Btpy import Btpy
from .cut_from import*

@Btpy.printtest
def cut_from_test():
    r = cut_from("a/b/c/b/b/e", "c")
    print(r == "/b/b/e")
    r = cut_from("a/b/c/b/b/e", "e")
    print(r == "")
    r = cut_from("a/b/c/b/b/e", "b", 
                 last_appearance=True)
    print(r)
    print(r == "/e")


