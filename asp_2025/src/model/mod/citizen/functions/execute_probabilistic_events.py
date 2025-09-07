

from ..CitizenData import CitizenData
from .cause_character_death import*
from btpy.Btpy import Btpy
from ..random_probability_float import*


def execute_probabilistic_events(
            citizen_data):
        citizen_data \
            = launch_workplace_death(
                 citizen_data
            )
        citizen_data \
            = launch_natural_death(
                 citizen_data
            )
        return citizen_data

def launch_workplace_death(
          citizen_data:CitizenData):
    item = citizen_data\
        .get_profession_item()
    is_dead = random_probability_float(
        item.get_death_probability()
    )
    if(is_dead):
        citizen_data\
            = cause_character_death(
                citizen_data,
                "work_accident"
            )
    return citizen_data

def launch_natural_death(citizen_data):
    percent = citizen_data\
        .get_age_range_item()\
            .get_death_probability()
    is_dead = random_probability_float(
        percent
    )
    if(is_dead):
        citizen_data\
            = cause_character_death(
                citizen_data,
                "natural_causes"
        )
    return citizen_data