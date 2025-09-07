

import random

class RandomIndexTK:

    def inner(self, maximum):
        number = random.randint(0, maximum)
        if(number == maximum):
            number -= 1
        return number
