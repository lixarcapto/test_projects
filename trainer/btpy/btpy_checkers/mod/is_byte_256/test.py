


from is_byte_256 import*

def main():
    #
    r = is_byte_256(255)
    print(r == True)
    #
    r = is_byte_256(0)
    print(r == True)
    #
    r = is_byte_256(256)
    print(r == False)
    #
    r = is_byte_256(255.0)
    print(r == False)
    #
    r = is_byte_256("255")
    print(r == False)
    #
    r = is_byte_256(-1)
    print(r == False)
    #

main()