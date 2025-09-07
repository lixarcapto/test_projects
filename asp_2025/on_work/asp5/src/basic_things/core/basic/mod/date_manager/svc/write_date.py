


from ..constants.translates_dates import*

"""
    Funcion que escribe un objeto date_data en
    una fecha escrita en formato string.
    TODO: cambia el texto por claves de traduccion
"""
# return text
def write_date(date_data, lenguage = "english"):
    text = ""
    day_index = date_data.get_day() -1
    day_of_month = date_data.day_of_month
    week_index = date_data.get_week() -1
    month_index = date_data.get_month() -1
    year = date_data.get_year()
    text += DAY_NAMES_MAP[lenguage][day_index -1] + " "
    text += str(day_of_month) + " "
    text += "de la " + WEEK_NAMES_MAP[lenguage][week_index -1] + " semana "
    text += "de " + MONTH_NAMES_MAP[lenguage][month_index -1] + " "
    text += "del año" + " " + str(year)
    return text
