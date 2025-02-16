



from .Switch import*

def switch_test():
    print("--> switch_test")
    object = Switch()
    print(object.switch())
    print(object.switch() == False)