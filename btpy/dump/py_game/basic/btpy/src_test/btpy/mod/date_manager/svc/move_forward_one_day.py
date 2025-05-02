

NUMBER_DAYS = 7
NUMBER_WEEKS = 4
NUMBER_MONTHS = 12

"""
    Funcion que avansa el tiempo en un date_manager_data
    cambiando dias, semanas y meses.
    FIXME: arreglar el numero de meses.
"""
# return date_date
def move_forward_one_day(date_data):
    day = date_data.get_day()
    week = date_data.get_week()
    month = date_data.get_month()
    year = date_data.get_year()
    day_of_month = date_data.day_of_month
    day_of_week = date_data.day_of_week
    day += 1
    day_of_month += 1
    day_of_week += 1
    if(day > NUMBER_DAYS):
        week += 1
        day = 1
    if(week > 4):
        week = 1
    # añade un nuevo mes
    if(day_of_month > date_data.MONTHS_DAYS_ARRAY[month]):
        day_of_month = 1
        month += 1
    # añade un nuevo año
    if(month > NUMBER_MONTHS):
        month = 1
        year += 1
    date_data.day_of_month = day_of_month
    date_data.day_of_week = day_of_week
    date_data.set_day(day)
    date_data.set_week(week)
    date_data.set_month(month)
    date_data.set_year(year)
    return date_data
