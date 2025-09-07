


class Character:

    def __init__(self):
        self.name:str = ""
        self.lastname:str = ""
        self.gender_key = "female"
        self.age_range_key:str = ""
        self.origin_country_key:str = ""
        self.back_story_key:str = ""
        self.young_story_key:str = ""
        self.end_story_key:str = ""
        self.philosophy_key:str = ""
        self.weapon_key:str = ""
        self.races_key:str = ""
        self.years_old:int = 0
        self.profession_key:str = ""
        self.traits_dict:dict = {}
        self.skills_list:list = []
        self.hobby_key:str = ""
        self.rejections_key:str = ""
        self.romantic_experience_k:str = ""
        self.experiences_list:list = []

    def load_character_dict(self, 
            DICT:dict):
        self.name = DICT["NAME"]
        self.lastname = DICT["LASTNAME"]
        self.gender_key\
             = DICT["GENDER_KEY"]
        self.age_range_key \
            = DICT["AGE_RANGE_KEY"]
        self.origin_country_key\
             = DICT["ORIGIN_COUNTRY_KEY"]
        self.back_story_key\
             = DICT["BACK_STORY_KEY"]
        self.young_story_key\
             = DICT["YOUNG_STORY_KEY"]
        self.end_story_key\
             = DICT["END_STORY_KEY"]
        self.philosophy_key\
             = DICT["PHILOSOPHY_KEY"]
        self.weapon_key\
             = DICT["WEAPON_KEY"]
        self.phrase_key\
             = DICT["PHRASE_KEY"]
        self.races_key\
             = DICT["RACES_KEY"]
        self.years_old\
             = DICT["YEARS_OLD"]
        self.profession_key\
             = DICT["PROFESSION_KEY"]

    def create_character_dict(self):
        return {
            "NAME": self.name,
            "LASTNAME": self.lastname,
            "GENDER_KEY": self.gender_key,
            "AGE_RANGE_KEY":self.age_range_key,
            "ORIGIN_COUNTRY_KEY":self.origin_country_key,
            "BACK_STORY_KEY":self.back_story_key,
            "YOUNG_STORY_KEY":self.young_story_key,
            "END_STORY_KEY":self.end_story_key,
            "PHILOSOPHY_KEY":self.philosophy_key,
            "WEAPON_KEY":self.weapon_key,
            "PHRASE_KEY":self.phrase_key,
            "RACES_KEY":self.races_key,
            "YEARS_OLD":self.years_old,
            "PROFESSION_KEY":self.profession_key
        }