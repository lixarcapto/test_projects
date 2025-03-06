

from btpy.Btpy import Btpy
import sys


def main():
    print("init...")
    r = None
    # -------------------------------------
    
    for i in range(5):
        r = Btpy.random_profile("nordic")
        print(r.write())



    #---------------------------------
    print(r)

main() 