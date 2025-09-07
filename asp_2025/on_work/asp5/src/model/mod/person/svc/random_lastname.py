


import random

# return string
def random_lastname(data):
    names_array = []
    if(data.caste == "noble"):
        names_array = data.LASTNAMES_MAP[data.culture]
    elif(data.caste == "pleb"):
        names_array = data.NOBLE_LASTNAMES_MAP[data.culture]
    return random.choice(names_array)
