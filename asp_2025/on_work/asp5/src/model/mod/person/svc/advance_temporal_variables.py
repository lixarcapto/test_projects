



"""
    Funcion que avansa un dia para las variables
    temporales del personaje.
"""
def advance_temporal_variables(data):
    data.month_counter += 1
    if(data.day_counter == data.DAY_TIME):
        data.month_counter += 1
        data.day_counter = 0
    if(data.month_counter == data.MONTH_TIME):
        data.month_counter = 0
        data.year_counter += 1
    if(data.year_counter == data.RANGE_AGE_TIME
    and data.age_code < data.AGE_RANGE_LIMIT):
        data.year_counter = 0
        data.age_code += 1
    if(data.age_code == data.AGE_RANGE_LIMIT):
        data.is_death = True
    return data
