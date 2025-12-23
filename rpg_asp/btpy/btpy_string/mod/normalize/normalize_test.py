

from .normalize import*

def normalize_test():
    print("normalize_test")
    r = normalize("Abcde")
    print(r == "abcde")
    r = normalize("ábcdé")
    print(r == "abcde")
    r = normalize(" abcd ")
    print(r == "abcd")