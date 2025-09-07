



def appearance_description(person_data):
    data = person_data
    txt = ""
    if(data.gender == "female"):
        txt += "she "
    else:
        txt += "he "
    txt +=  "was a "
    txt += f"{get_age_range_text(data)} "
    txt += f"{data.race} "
    txt += " with " + data.hair_style
    txt += f"{data.hair_style} hair, "
    txt += f"{data.eye_color} eyes, "
    txt += f"{data.skin_color} skin "
    txt += f"and {get_height_text(data)} "
    txt += "height.\n"
    return txt

def get_age_range_text(person_data):
    return person_data.cache.AGE_CODE_ARRAY[
        person_data.age_range
    ]
    
def get_height_text(person_data):
    return person_data.cache.HEIGHT_CODE_ARRAY[
        person_data.actual_height
    ]