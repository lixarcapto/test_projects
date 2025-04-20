


from ....btpy_random.mod.random_choice.random_choice import*
from ..read_xlsx_dict_list.read_xlsx_dict_list import*

COUNTRY_DICT = {}
EXCEL_ROUTE = "btpy/res/country_data.xlsx"

def random_country(region_key:str = "")->str:
    """
     Función que generan nombres de 
     países aleatorios en ingles según 
     el continente indicado; las claves de
     continente son:
    north_america,
    europe,
    africa,
    south_america,
    central_asia,
    middle_east,
    south_asia,
    far_asia,
    oceania.

    """
    global COUNTRY_DICT
    if(COUNTRY_DICT == {}):
        COUNTRY_DICT \
            = read_xlsx_dict_list(
                EXCEL_ROUTE)
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
    
    