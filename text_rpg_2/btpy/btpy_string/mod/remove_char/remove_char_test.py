

from .remove_char import*

def remove_char_test():
    print("remove_char_test")
    r = remove_char("hola mundo", 2)
    print(not "l" in r)