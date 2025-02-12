


from btpy.src.btpy.Btpy import Btpy
from btpy.src.btpy.btpy_utilitys.mod.three.Three import Three

if __name__ == "__main__":
    print("init...")
    r = None
    #---------------------------------------


    three = Three()
    three.set_in_node("apple")
    three.set_in_node("blueberry", "apple")
    three.set_in_node("watermellon", 
        "blueberry")
    three.set_in_node("lemon")
    three.set_in_node("lime", "lemon")
    three.print()
    print("apple", three.get_nodes("apple"))



    #---------------------------------------
    print(r)