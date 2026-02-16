



import random

def around(NUMBER, LIMIT)->int:
    return random.randint(
        NUMBER - LIMIT, 
        NUMBER + LIMIT
    )