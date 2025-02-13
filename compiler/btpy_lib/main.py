


from btpy.src.btpy.Btpy import Btpy

if __name__ == "__main__":
    print("init...")
    r = None
    #---------------------------------------

    r = Btpy.has_between("el negro jose", "el",
            "jox")

    #---------------------------------------
    print(r)