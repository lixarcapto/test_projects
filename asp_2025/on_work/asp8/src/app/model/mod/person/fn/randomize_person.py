

from btpy.src.btpy.Btpy import Btpy

def randomize_person(person_data, culture):
    data = person_data
    data.culture = culture
    data.gender = random_gender()
    if(data.gender == "male"):
        data.name = random_male_name(
            data, culture)
    if(data.gender == "female"):
        data.name = random_fem_name(
            data, culture)
    data = randomize_appearance(data)
    return data

def random_male_name(person_data, culture):
    names_dict = person_data.cache\
        .NAMES_MALE_DICT[culture]
    names_list = list(names_dict.keys())
    return Btpy.random_choice(names_list)
    
def random_fem_name(person_data, culture):
    names_dict = person_data.cache\
        .NAMES_MALE_DICT[culture]
    names_list = list(names_dict.keys())
    return Btpy.random_choice(names_list)

def random_gender():
        if(Btpy.random_bool()):
            return "male"
        return "female"

def randomize_appearance(person_data):
    data = person_data
    data.race = "human_west"
    data.hair_color = randomize_hair_color(
        person_data)
    data.skin_color = randomize_skin_color(
        person_data)
    data.eye_color = randomize_eye_color(
        person_data)
    return data
        
def randomize_skin_color(person_data):
    race_dict = person_data.cache\
        .RACES_DICT[person_data.race]
    return Btpy.random_choice(
        race_dict["skin_colors"])
        
def randomize_hair_color(person_data):
    race_dict = person_data.cache\
        .RACES_DICT[person_data.race]
    return Btpy.random_choice(
        race_dict["hair_colors"])
        
def randomize_eye_color(person_data):
    race_dict = person_data.cache\
        .RACES_DICT[person_data.race]
    return Btpy.random_choice(
        race_dict["eye_colors"])