

import random

class CharacterProfile:

    def __init__(self, culture):
        self.name = ""
        self.lastname = ""
        self.second_lastname = ""
        self.nickname = ""
        self.culture = culture
        self.geo_adress = None
        self.profession = ""
        self.development_level = "digital"
        self.gender = ""
        self.random_gender()

    def random_gender(self):
        if(random.randint(0, 1) == 1):
            self.gender = "female"
        else:
            self.gender = "male"

    def write(self):
        return ""\
        + f"{self.name} "\
        + f"{self.lastname} "\
        + f"{self.second_lastname} "\
        + f"{self.nickname} "\
        + f"{self.culture} "\
        + f"{self.gender} "\
        + f"{self.profession} "\
        + f"{self.geo_adress.write()}"

    def random_gender(self):
        if(random.randint(0, 1) == 1):
            self.gender = "female"
        else:
            self.gender = "male"
        
        