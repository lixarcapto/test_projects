


CACHE_MAP_WORLD = {}

import random

def random_key(dict_)->str:
    return random.choice(
        list(dict_.keys()))

def random_geo_adress(
        read_json_object,
        GeoAdress,
        MAP_WORLD_PATH,
        country_key:str = ""):
    global CACHE_MAP_WORLD
    if(CACHE_MAP_WORLD == {}):
        CACHE_MAP_WORLD = read_json_object(
            MAP_WORLD_PATH)
    if(country_key == ""):
        country_key = random_key(
            CACHE_MAP_WORLD)
    geo_adress = GeoAdress()
    geo_adress.country = country_key
    region_dict:dict = CACHE_MAP_WORLD\
        [country_key]
    geo_adress.region = random_key(
        region_dict)
    MAXIMUM_HIGH = 99999
    geo_adress.parcel_code = str(random\
        .randint(0, MAXIMUM_HIGH))
    return geo_adress