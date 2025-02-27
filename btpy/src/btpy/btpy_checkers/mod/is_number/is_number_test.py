

from .is_number import*

def is_number_test():
    array = []
    print("-> is_number_test")
    if(is_number(5)): array.append(True)
    if(is_number(0.5)): array.append(True)
    if(False in array): 
        print(False)
    else: 
        print(True)
