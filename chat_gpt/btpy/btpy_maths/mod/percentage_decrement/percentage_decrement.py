


def percentage_decrement(
        NUMBER:int|float,
        DECREMENT:int|float)->int|float:
    """
    function that decreases a number 
    by a given percentage.
    """
    return NUMBER * (
        1 - (DECREMENT / 100))