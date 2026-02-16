
from .cut_from import*

def cut_until_test():
    print("cut_until_test")
    r = cut_until("correcto/texto", "/")
    print(r == "correcto")
    r = cut_until("correcto/correcto/texto", 
                   "/",
                   last_appearance=True)
    print(r == "correcto/correcto")