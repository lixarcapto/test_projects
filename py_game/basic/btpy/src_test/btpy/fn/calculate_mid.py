

"""
Function that calculates the 
average of the numbers in 
the sent array.
"""
def calculate_mid(array:list)->float:
    sum_number:int = 0
    for e in array:
        sum_number += e
    result = sum_number / len(array)
    return result




