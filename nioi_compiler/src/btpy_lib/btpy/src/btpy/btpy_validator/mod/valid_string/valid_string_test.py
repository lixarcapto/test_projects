


from .valid_string import*

def valid_string_test():
    print("valid_string_test")
    #
    # NEGATIVOS
    print("it shoud be error")
    valid_string(1333, 
            3)
    print("it shoud be error")
    valid_string("h", 
            3)
    print("it shoud be error")
    valid_string("ho", 
        3)
    print("it shoud be error")
    valid_string("", 
        0)
    #
    # POSITIVOS
    print("it shoud not be error")
    valid_string("hom", 
        3)
    print("it shoud not be error")
    valid_string("homero", 
        3)
    
    
