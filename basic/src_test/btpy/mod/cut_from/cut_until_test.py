
from btpy.Btpy import Btpy
from .cut_from import*

@Btpy.printtest
def cut_until_test():
    r = cut_until("correcto/texto", "/")
    if(r == "correcto"):
        print("succes")
    else: 
        print("fail")
    r = cut_until("correcto/correcto/texto", 
                   "/",
                   last_appearance=True)
    if(r == "correcto/correcto"):
        print("succes")
    else: 
        print("fail")