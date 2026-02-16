

from .mapp import*

def mapp_test():
    print("--> mapp")

    r = mapp("aaa", lambda e:e+"b")
    print(r == "ababab")

    print("")