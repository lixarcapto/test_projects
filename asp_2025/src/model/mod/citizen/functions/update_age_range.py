

from btpy.Btpy import Btpy
from ..citizen_constants import*

def update_age_range(citizen_data):
    """
    Funcion que actualiza el rango de 
    edad del ciudadano segun el 
    age_range_depot.
    """
    year = citizen_data.date_asp.get_year()
    if(year > MAX_AGE):
        year = MAX_AGE
    age_range_dict = citizen_data\
        .age_range_depot.age_range_dict
    list_ = Btpy.whats_range(
        age_range_dict,
        year
    )
    citizen_data.set_age_range_key(
        list_[0]
    )
    return citizen_data