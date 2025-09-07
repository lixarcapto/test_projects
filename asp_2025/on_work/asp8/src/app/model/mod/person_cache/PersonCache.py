

from ....persistence.Persistence import Persistence

class PersonCache:

    NAMES_MALE_DICT =  Persistence\
            .read_names()
    NAMES_FEMALE_DICT = Persistence\
            .read_female_names()
    RACES_DICT = Persistence.read_races()

    AGE_CODE_ARRAY = [
        "child",
        "teen",
        "young",
        "adult",
        "senior",
        "elder",
        "dying"
    ]

    HEIGHT_CODE_ARRAY = [
        "dwarft",
        "short",
        "middle",
        "tall",
        "giant"
    ]