



def in_range(number: int, range_arr: list)\
        -> bool:
    """
    Function to identify if the input 
    number is contained within the 
    sending range.
    Eg:
    code: print(in_range(5, [4, 6]))
    output: True
    """
    if(not type(number) == int
    and not type(number) == float):
        raise Exception(
            f"is not a number {number}"
        )
    if(number >= range_arr[0]
    and number <= range_arr[1]):
        return True
    return False
