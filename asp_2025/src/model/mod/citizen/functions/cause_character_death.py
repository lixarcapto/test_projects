


from ..CitizenData import CitizenData
from ..citizen_constants import*
from btpy.Btpy import Btpy

def cause_character_death(
        citizen_data:CitizenData,
        CAUSE_DEATH_KEY:str)->None:
    citizen_data.set_is_dead(True)
    citizen_data.set_cause_death_key(
            CAUSE_DEATH_KEY
    )
    if(CAUSE_DEATH_KEY == "work_accident"):
        prof_k = citizen_data\
                .get_profession_key()
        list_ = SPECIFIC_CAUSE_DEATH\
                [prof_k]
        specific = Btpy.random_choice(
            list_)
        citizen_data.specific_cause_death \
                = specific
    if(CAUSE_DEATH_KEY == "natural_causes"):
        specific = Btpy.random_choice(
            NATURAL_CAUSE_DEATH)
        citizen_data.specific_cause_death \
                = specific
    return citizen_data