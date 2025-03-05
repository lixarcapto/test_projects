


from ..random_name.random_name import random_name
from ..random_lastname.random_lastname import random_lastname
from ..random_geo_adress.random_geo_adress import random_geo_adress
from ..random_profession.random_profession import*
from ..read_excel_dict.read_excel_dict import read_excel_dict
import random

class CharacterProfile:

    PATH_NAME_MALE_XLSX = ""
    PATH_NAME_FEMALE_XLSX = ""
    PROFESSION_PATH = ""
    LASTNAMES_PATH = ""

    def __init__(self,
            PATH_NAME_MALE_XLSX,
            PATH_NAME_FEMALE_XLSX,
            LASTNAMES_PATH,
            PROFESSION_PATH,
            culture):
        CharacterProfile\
            .PATH_NAME_MALE_XLSX \
                = PATH_NAME_MALE_XLSX
        CharacterProfile \
            .PATH_NAME_FEMALE_XLSX  \
                = PATH_NAME_FEMALE_XLSX
        CharacterProfile\
            .LASTNAMES_PATH = LASTNAMES_PATH
        CharacterProfile\
            .PROFESSION_PATH = PROFESSION_PATH
        self.name = ""
        self.lastname = ""
        self.second_lastname = ""
        self.nickname = ""
        self.culture = culture
        self.geo_adress = None
        self.profession = ""
        self.development_level = "digital"
        self.gender = ""

    def write(self):
        return ""\
        + f"{self.name} "\
        + f"{self.lastname} "\
        + f"{self.second_lastname} "\
        + f"{self.nickname} "\
        + f"{self.culture} "\
        + f"{self.gender} "\
        + f"{self.profession}"

    def random_gender(self):
        if(random.randint(0, 1) == 1):
            self.gender = "female"
        else:
            self.gender = "male"

    def random_geo_adress(self):
        self.geo_adress \
            = random_geo_adress()

    def random_name(self):
        self.name = random_name(
            read_excel_dict,
            CharacterProfile \
                .PATH_NAME_MALE_XLSX,
            CharacterProfile \
                .PATH_NAME_FEMALE_XLSX, 
            self.culture,
            self.gender
        )

    def random_lastname(self):
        self.lastname = random_lastname(
          read_excel_dict,
          CharacterProfile.LASTNAMES_PATH,
          self.culture
        )
        self.second_lastname = random_lastname(
          read_excel_dict,
          CharacterProfile.LASTNAMES_PATH,
          self.culture
        )

    def random_profession(self):
        self.profession = random_profession(
            read_excel_dict,
            CharacterProfile.PROFESSION_PATH,
            self.development_level
        )

    def randomize(self):
        self.random_gender()
        self.random_name()
        self.random_lastname()
        self.random_profession()
        
        