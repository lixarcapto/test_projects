


class PersonData:

    UNIQUE_CODE = 0
    FERTILITY_PERCENT = 50
    PREGNANCY_TIME = 12
    RANGE_AGE_TIME = 4
    AGE_RANGE_LIMIT = 0
    BEAUTY_STAT_SUM = None
    DAY_TIME = 3
    NAMES_MALE_MAP = {}
    NAMES_FEMALE_MAP = {}
    LASTNAMES_MAP = {}
    NOBLE_LASTNAMES_MAP = {}
    EMOTION_LIMIT = 7
    MONTH_TIME = 4
    PERSON_CONST = None
    INITIAL_RANGE_AGE = 3
    DESITION_KEYS = [
        "attack",
        "meet_people",
        "rest",
        "walk"
    ]
    LOCATION_KEYS = [
        "inside",
        "out"
    ]

    def __init__(self):
        # identitty
        self.name = ""
        self.second_name = ""
        self.lastname = ""
        self.second_lastname = ""
        self.clan_name = ""
        self.nickname = ""
        self.code = 0
        self.coordinate_array = []
        self.relation_list = None
        self.is_single = True
        self.country_origin = ""
        self.caste = "pleb"
        self.actual_district = 0
        # temporal states
        self.pregnant_time = 0
        self.flu_time = 0
        self.stress_time = 0
        # emotion states
        self.facial_expression = ""
        self.main_emotion = ""
        self.emotion_states_map = {
            "happiness": 0,
            "anger": 0,
            "sadness": 0,
            "disgust": 0,
            "fear": 0
        }
        # objects
        self.decision_map = {}
        # states
        self.is_death = False
        self.has_ETS = False
        self.baby_can_walk = False
        self.decision_taken = "rest"
        self.location = "inside"
        self.its_legendary = False # indica si es original
        # stadistics

        # others
        self.gen_group = "western"
        self.baby_person = None
        self.gen_father = None
        self.gen_mother = None
        self.gen_own = None
        # time variables
        self.age_code = 0
        self.year_counter = 0
        self.day_counter = 0
        self.month_counter = 0
        # appearance
        self.gender = ""
        self.eye_type = ""
        self.skin_color = ""
        self.weight_code = 0
        self.maximum_height_code = 0
        self.actual_height_code = 0
        self.hair_type = ""
        self.hair_color = ""
        self.eye_color = ""
        self.is_bald = False
        self.has_frekkles = False
        self.beauty = 0
        self.butt_size = 0
        self.breast_size = 0
        # propertys
        self.hair_style = ""
        self.hut_outfit = ""
        self.superior_outfit = ""
        self.inferior_outfit = ""
        self.shoes = ""
        # culture
        self.culture = "race_kaz"
        self.ideology = ""
        self.lenguage_array = []
        self.profession = ""
