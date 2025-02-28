

from btpy.Btpy import Btpy
import sys


def main():
    print("init...")
    r = None
    # -------------------------------------
    
    def pipe(e):
        return {"mensaje":"funciona"}
    Btpy.create_server_flask(True, 5001,
        pipe)



    #---------------------------------
    print(r)

main() 