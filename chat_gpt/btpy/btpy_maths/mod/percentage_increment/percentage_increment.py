


def percentage_increment(NUMBER:int|float, 
        INCREMENT:int|float)->float:
    """
    function that increases a number 
    by a given percentage.
    """
    return NUMBER * (1+(INCREMENT / 100))