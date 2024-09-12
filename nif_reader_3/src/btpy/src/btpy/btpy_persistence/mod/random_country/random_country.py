


from ....btpy_random.mod.random_choice.random_choice import*
from ..read_excel_dict.read_excel_dict import*

COUNTRY_DICT = {}

def random_country(region_key:str = "")->str:
    """
     Función que generan nombres de 
     países aleatorios en ingles según 
     el continente indicado
    """
    global COUNTRY_DICT
    EXCEL_ROUTE = "../res/country_data.xlsx"
    if(COUNTRY_DICT == {}):
        COUNTRY_DICT \
            = read_excel_dict(EXCEL_ROUTE)
    result = ""
    # si region no es definida
    if(region_key == ""):
        keys:str = list(
            COUNTRY_DICT.keys())
        region_key:str = random_choice(keys)
    # obtiene los paises
    country_list = COUNTRY_DICT[region_key]
    # elige un pais
    return random_choice(country_list)
    
    