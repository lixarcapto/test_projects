
from is_hex_color import*

def main():
    #
    r = is_hex_color("#2596be")
    print(r == True)
    #
    r = is_hex_color("#873e23")
    print(r == True)
    #
    r = is_hex_color("#993300")
    print(r == True)
    #
    r = is_hex_color("")
    print(r == False)
    #
    r = is_hex_color("993300")
    print(r == False)
    #

main()