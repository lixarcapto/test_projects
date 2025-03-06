

from is_byte_127 import*

def main():
    print("--> is_byte127_test")
    #
    r = is_byte_127(100)
    print(r == True)
    #
    r = is_byte_127(126)
    print(r == True)
    #
    r = is_byte_127(-126)
    print(r == True)
    #
    r = is_byte_127(127)
    print(r == False)
    #
    r = is_byte_127(-127)
    print(r == False)
    #
    r = is_byte_127(0)
    print(r == True)
    #
    r = is_byte_127(-100)
    print(r == True)
    #
    r = is_byte_127(256)
    print(r == False)
    #
    r = is_byte_127(-256)
    print(r == False)
    #
    r = is_byte_127("100")
    print(r == False)
    #

main()