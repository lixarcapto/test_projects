

from in_range import*

def main():
    #
    print("esta en rango")
    r = in_range(3, [0, 5])
    print(r == True)
    #
    print("esta en rango limite min")
    r = in_range(0, [0, 5])
    print(r == True)
    #
    print("esta en rango limite max")
    r = in_range(5, [0, 5])
    print(r == True)
    #
    print("esta en rango corto")
    r = in_range(0, [0, 1])
    print(r == True)
    #
    print("rango no es array")
    r = in_range(5, 5)
    print(r == False)
    #
    print("rango array es mas grande")
    r = in_range(3, [0, 5, 5])
    print(r == False)
    #
    print("rango array es mas pequeño")
    r = in_range(0, [0])
    print(r == False)
    #
    print("numero es string")
    r = in_range("3", [0, 5])
    print(r == False)
    #


main()