

from ....btpy_random.mod.randint_list.randint_list import*


def random_ip()->str:
    quantity = 4
    array = randint_list(quantity, 
        [0, 255])
    for i in range(len(array)):
        array[i] = str(array[i])
    text = ".".join(array)
    return text