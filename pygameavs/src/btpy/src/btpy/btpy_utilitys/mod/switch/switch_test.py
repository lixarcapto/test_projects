



from .Switch import*

def switch_test():
    print("--> switch_test")
    object = Switch()
    print(object.is_true())
    print(object.is_true() == False)