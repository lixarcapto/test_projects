


from .randint_list import*
from .sum_array import*

def random_ip():
    quantity = 4
    array = randint_list(quantity, [0, 255])
    text = sum_array(array, ".")
    return text