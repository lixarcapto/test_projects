

from ..CitizenData import CitizenData
from persistence.Persistence import Persistence

def get_player_path_layout(data:CitizenData)\
                ->list[str]:
    """
    Funcion que crea una lista de 
    claves que representan a los 
    datos mas utiles para
    crear una representacion 
    grafica del ciudadano.
    """
    path = Persistence\
        .get_texture_pack_path()
    list_:list[str] = []
    k = get_skin_layout(data)
    list_.append(k)
    k = get_makeup_layout(data)
    list_.append(k)
    k = get_age_range_layout(data)
    list_.append(k)
    k = get_freckles_layout(data)
    list_.append(k)
    k = get_eyes_layout(data)
    list_.append(k)
    k = get_mouth_layout(data)
    list_.append(k)
    k = get_nose_layout(data)
    list_.append(k)
    if(not data.get_hide_hair()):
        k = get_hair_layout(data)
        list_.append(k)
    k = get_clothes_layout(data)
    list_.append(k)
    k = get_beard_layout(data)
    list_.append(k)
    k = get_profession_layout(data)
    list_.append(k)
    k_list = get_baby_layout(data)
    list_ = list_ + k_list
    k = get_skull_layout(data)
    list_.append(k)
    return list_
    
def get_age_range_layout(data)->str:
    if(data.get_age_range_key() 
            == "dying"):
        return "wrinkles"
    return ""
    
def get_skin_layout(data)->str:
    return "skin_" \
        + data.get_gender_key() + "_"\
        + data.get_skin_color_key()
    
def get_background_layout(data)->str:
    layout_key = ""
    return layout_key
    
def get_freckles_layout(data)->str:
    if(data.get_is_freckled()):
        return "freckled"
    return ""
    
def get_hair_layout(data)->str:
    hair_key = ""
    if(data.get_culture_key() 
            == "arab"
    and data.get_gender_key() 
            == "female"):
        return ""
    hair_key = "hair_" \
        + data.get_hairstyle_key()\
        + "_" \
        + data.get_hair_type_key()\
        + "_" \
        + data.get_hair_color_key()
    return hair_key

def get_eyes_layout(data)->str:
    return "eyes_" \
        + data.get_eye_type_key()\
        + "_" + data.get_eye_color_key()

def get_mouth_layout(data:CitizenData)->str:
    name = "mouth_" \
    + data.get_mouth_type_key() + "_"\
    + data.get_mood_value_key().lower()
    return  name
    
def get_nose_layout(data:CitizenData)->str:
    r = "nose_"\
        + data.get_nose_type_key()
    return r
    
def get_clothes_layout(data)->str: 
    key = "clothes_"\
    + data.get_gender_key()\
    + "_" + data.get_culture_key()
    return key
    
def get_profession_layout(data)->str:
    profession = data\
        .get_profession_key().lower()
    return "profession_" \
        + profession

def get_baby_layout(data)->list:
    if(not data.get_is_a_mother()):
        return []
    leng = len(data.child_in_care_list)
    list_ = []
    color_k_1 = data.child_in_care_list[0]\
        .data.get_skin_color_key()
    if(leng > 1):
        color_k_2 = data.child_in_care_list[1]\
        .data.get_skin_color_key()
        list_.append("baby_" + color_k_1)
        list_.append("baby_2_" + color_k_2)
    else:
        list_.append("baby_" + color_k_1)
    return list_

def get_beard_layout(data:CitizenData)->str:
    beard_k = data\
        .get_current_beard_style()
    return "beard_" + beard_k + "_"\
        + data.get_hair_type_key() + "_"\
        + data.get_hair_color_key()

def get_makeup_layout(data:CitizenData):
    return "makeup_"\
    + data.get_current_makeup_key()

def get_skull_layout(data:CitizenData):
    if(data.get_is_dead()):
        return "skull"
    return ""