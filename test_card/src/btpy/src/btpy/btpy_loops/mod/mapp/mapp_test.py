


from .mapp import*

def mapp_test():
    print("mapp_test")
    r = mapp([0, 0, 0], 
             lambda e:e +1
        )
    print(r == [1, 1, 1])
    r = mapp([[0, 0, 0], [0, 0]], 
             lambda e:e +1
        )
    print(r == [[1, 1, 1], [1, 1]])
    #
    r = mapp({"a":0, "b":0}, 
             lambda e:e +1
        )
    print(r == {"a":1, "b":1})
    #
    r = mapp({"a":[0, 0], "b":[0, 0]}, 
             lambda e:e +1
        )
    print(r == {"a":[1, 1], "b":[1, 1]})
    #
    r = mapp(["aaa", "bbb"], 
             lambda e:e +"c"
        )
    print(r == ["aaac", "bbbc"])

