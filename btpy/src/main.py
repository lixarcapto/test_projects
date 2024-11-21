

from btpy.Btpy import Btpy
import sys

def main():
    r = "None"
    #--------------------------------

    maximum = 100
    int_str = "c"
    r = 0
    for i in range(1, maximum):
        r = sys.getsizeof(int_str)
        print(f"{r} bits = {i} characters")
        int_str += "c"
    
    #------------------------------
    print(r)

main()