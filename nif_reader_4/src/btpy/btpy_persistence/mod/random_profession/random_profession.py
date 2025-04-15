


from typing import Callable
import random

PROFESSION_CACHE:dict = {}
DEVELOPMENT_KEYS \
    = ("medieval", "victorian", "digital")

def random_profession(
        READ_EXCEL_DICT,
        PROFESSION_PATH,
        development_level:int)->str:
    """
    development level must be:
    "medieval", "victorian", "digital"
    """
    global PROFESSION_CACHE
    global DEVELOPMENT_KEYS
    if(not development_level \
            in DEVELOPMENT_KEYS):
        print(f"<!>Error: development_level \"{development_level}\" does not exist, must be {DEVELOPMENT_KEYS}")
        return ""
    if(PROFESSION_CACHE == {}):
        PROFESSION_CACHE \
            = READ_EXCEL_DICT(
                PROFESSION_PATH)
    return random_level(development_level)

def random_level(level):
    global PROFESSION_CACHE
    final_list = []
    final_list \
            = PROFESSION_CACHE["primitive"]
    if(level == "primitive"):
        return random.choice(final_list)
    final_list \
            = final_list \
            + PROFESSION_CACHE["medieval"]
    if(level == "medieval"):
        return random.choice(final_list)
    final_list \
            = final_list \
            + PROFESSION_CACHE["victorian"]
    if(level == "victorian"):
        return random.choice(final_list)
    final_list \
            = final_list \
            + PROFESSION_CACHE["digital"]
    return random.choice(final_list)
    
