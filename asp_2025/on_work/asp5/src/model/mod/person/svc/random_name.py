


import random

# return string
def random_name(data):
    names_array = []
    if(data.gender == "male"):
        names_array = data.NAMES_MALE_MAP[data.culture]
    else:
        names_array = data.NAMES_FEMALE_MAP[data.culture]
    return random.choice(names_array)
