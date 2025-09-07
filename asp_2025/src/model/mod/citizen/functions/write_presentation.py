


from .get_age_range_nickname import*
from .get_full_name import*

def write_presentation(data)->str:
    """
    Funcion que escribe una 
    presentacion en formato texto 
    del personaje.
    """
    return ""\
    + get_full_name(data)\
    + " was an " \
    + data.get_profession_key()\
    + " "\
    + str(data.date_asp.get_year())\
    + " year-old " \
    + " "\
    + data.get_culture_key()\
    + " "\
    + get_age_range_nickname(data)\
    + "."