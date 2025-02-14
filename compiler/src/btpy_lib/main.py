


from btpy.src.btpy.Btpy import Btpy

if __name__ == "__main__":
    print("init...")
    r = None
    #---------------------------------------

    three = Btpy.Three()
    three.set_in_node("vegetal")
    three.set_in_node("verdura", "vegetal")
    three.set_in_node("fruta", "vegetal")
    three.set_in_node("lechuga", "verdura")
    three.set_in_node("sandia", "fruta")
    print(three.write())
    print(three.create_keys_list())

    #---------------------------------------
    print(r)