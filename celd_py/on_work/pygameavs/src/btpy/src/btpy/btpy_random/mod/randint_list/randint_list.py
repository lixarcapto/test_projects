


import random

def randint_list(size: int, 
        range_array: list[int]) \
        -> list[int]:
    array = []
    for i in range(size):
        array.append(
            random.randint(
                range_array[0],
                range_array[1])
        )
    return array