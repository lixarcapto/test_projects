

from is_range import*

def main():
    #"es un rango"
    r = is_range([0, 1])
    print(r == True)
    #"no es rango"
    r = is_range([1, 1])
    print(r == False)
    #"no es array"
    r = is_range(2)
    print(r == False)
    #"es texto"
    r = is_range("[0, 1]")
    print(r == False)

main()