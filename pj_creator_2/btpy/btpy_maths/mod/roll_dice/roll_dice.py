

import random

def roll_dice(DICE_NUMER:int, FACES:int)\
        ->int:
    """
    function that simulates the 
    rolling of multiple dice.
    """
    sum_number:int = 0
    for i in range(DICE_NUMER):
        sum_number += random.randint(
            1,
            FACES
        )
    return sum_number