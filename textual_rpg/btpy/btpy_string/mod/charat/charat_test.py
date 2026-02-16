

from .charat import*

def charat_test():
    print("charat_test")
    r = charat("perro ladrando", 3)
    print(r == "r")
    r = charat("perro ladrando", 13)
    print(r == "o")
    r = charat("perro ladrando", 0)
    print(r == "p")
