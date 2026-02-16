


from .compare_strings import*

def compare_strings_test():
    print("compare_strings_test")
    compare_array = [
        ["hola", "hosa"],
        ["ola", "holas"],
        ["perro", "pego"],
        ["perro", "gato"],
        ["aaaa", "bbbb"],
        ["avion", "camion"],
        ["halcon", "alcon"],
        ["p", "pato"]
    ]
    for e in compare_array:
        r = compare_strings(e[0], e[1])
        print(r, e)
