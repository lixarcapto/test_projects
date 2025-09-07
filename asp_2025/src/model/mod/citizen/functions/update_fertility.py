



def update_fertility(citizen_data):
    age_key = citizen_data\
        .get_age_range_key()
    fertility = citizen_data\
        .get_fertility_by_age_range()
    citizen_data.fertility_percent \
        = fertility
    return citizen_data