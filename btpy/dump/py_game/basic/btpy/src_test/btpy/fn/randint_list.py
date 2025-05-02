


import random

# return int_array
def randint_list(size: int, 
        range_array: list) -> list:
    array = []
    for i in range(size):
        array.append(random.randint(range_array[0],
            range_array[1]))
    return array