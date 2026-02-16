

def __count_numbers_in_range(start:int, 
        end:int)->int:
    """
    Counts the number of integers 
    within a given range (inclusive).
    """
    # Handle negative and positive 
    # ranges separately
    if start <= end:
        return end - start + 1
    # Count for negative ranges
    else:
        return (start - end) + 1  

import random

def random_uniques(quantity:int, 
     range_arr:list[int])\
     ->list[int]:
    """
    función que genera una lista de 
    números aleatorios en un rango 
    sin repetir.
    """
    max_quantity = __count_numbers_in_range(
         range_arr[0], range_arr[1])
    if(max_quantity < quantity):
         raise Exception(
              "max quantity is mayor than quantity required"
         )
    number_arr = []
    n = 0
    counter = 0
    while(True):
         n = random.randint(range_arr[0], range_arr[1])
         if(n in number_arr): continue
         number_arr.append(n)
         if(counter == quantity): break
         counter += 1
    return number_arr
