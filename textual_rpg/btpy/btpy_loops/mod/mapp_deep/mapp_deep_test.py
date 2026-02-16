


from .mapp_deep import*

def mapp_deep_test():
    print("mapp_test")
    r = mapp_deep([0, 0, 0], 
             lambda e:e +1
        )
    print(r == [1, 1, 1])
    r = mapp_deep([[0, 0, 0], [0, 0]], 
             lambda e:e +1
        )
    print(r == [[1, 1, 1], [1, 1]])
    #
    r = mapp_deep({"a":0, "b":0}, 
             lambda e:e +1
        )
    print(r == {"a":1, "b":1})
    #
    r = mapp_deep({"a":[0, 0], "b":[0, 0]}, 
             lambda e:e +1
        )
    print(r == {"a":[1, 1], "b":[1, 1]})
    #
    r = mapp_deep(["aaa", "bbb"], 
             lambda e:e +"c"
        )
    print(r == ["aaac", "bbbc"])

