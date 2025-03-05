

from btpy.Btpy import Btpy
import sys


def main():
    print("init...")
    r = None
    # -------------------------------------
    
    Btpy.set_profession_path(
        "./btpy/res/profession_data.xlsx")
    r = Btpy.random_profession("medieval")



    #---------------------------------
    print(r)

main() 