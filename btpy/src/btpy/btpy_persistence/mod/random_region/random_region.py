


import random

def random_region(REGION_DICT:dict, 
        KEY_COUNTRY:str = "")->str:
    if(KEY_COUNTRY == ""):
        KEY_COUNTRY = random.choice(
            list(REGION_DICT.keys()))
    region_list = REGION_DICT[KEY_COUNTRY]
    return random.choice(region_list)