

from ..citizen_constants import*

def update_age_behaviors(citizen_data):
    if(citizen_data.get_age_range_key() 
                == "child"):
        citizen_data.can_speak = False
    else:
        citizen_data.can_speak = True
    year = citizen_data.date_asp\
        .get_year()
    if(year >= MAX_AGE):
        citizen_data.set_is_dead(True)
        citizen_data\
            .set_cause_death_key(
                "natural_causes"
            )
    return citizen_data