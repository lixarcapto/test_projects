


def update_pregnant_time(citizen_data):
    """
    Funcion que actualiza las 
    variables de tiempo embarazada
    del personaje.
    """
    days = citizen_data\
        .get_days_pregnant()
    if(citizen_data.get_is_pregnant()):
        days += 1
    if(citizen_data.get_days_pregnant() 
    >= citizen_data.MONTHS_PREGNANT):
        days = 0
        citizen_data.set_is_pregnant(
            False)
        citizen_data.set_is_a_mother(True)
    citizen_data.set_days_pregnant(
        days
    )
    return citizen_data