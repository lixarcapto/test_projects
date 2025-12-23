
from ..random_uniques.random_uniques import*

def random_unique_choice(
        LIST:list,
        RESULTS_QUANTITY:int)->list:
    """
    Function that selects a list 
    of elements from a sent list 
    in the indicated quantity.
    """
    idx_list = random_uniques(
        RESULTS_QUANTITY,
        [0, len(LIST) -1]
    )
    r_list = []
    for idx in idx_list:
        r_list.append(LIST[idx])
    return r_list