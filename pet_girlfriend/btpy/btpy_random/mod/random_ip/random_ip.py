

from ..random_int_list.random_int_list import*


def random_ip()->str:
    quantity = 4
    array = random_int_list(quantity, 
        [0, 255])
    for i in range(len(array)):
        array[i] = str(array[i])
    text = ".".join(array)
    return text