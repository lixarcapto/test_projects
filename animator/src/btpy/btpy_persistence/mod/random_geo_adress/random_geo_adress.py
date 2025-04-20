


from ..geo_adress.GeoAdress import GeoAdress

def random_geo_adress(
            random_region, 
            random_country, 
            key:str = ""
        ):
    geoadress = GeoAdress()
    if(key == ""):
        geoadress.country \
            = random_country()
        geoadress.region \
            = random_region()
    return geoadress

    

