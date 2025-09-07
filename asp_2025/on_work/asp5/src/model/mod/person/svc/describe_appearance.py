


"""
    Funcion que describe como texto narrativo
    exclusivamente la apariancia del personaje.
"""
# return string
def describe_appearance(data):
    # identitty
    text = ""
    text += data.PERSON_CONST.BEAUTY_KEYS_ARRAY[data.beauty] + " "
    text += data.gender + " "
    text += data.PERSON_CONST.AGE_RANGE_ARRAY[data.age_code] + " "
    text += " with " + data.facial_expression +  ", "
    text += data.eye_type + " "
    text += data.eye_color + " eyes, "
    text += data.skin_color + " skin, "
    if data.has_frekkles: text += " had frekkles, "
    text += data.hair_type + " "
    text += data.hair_color + " hair, "
    text += data.PERSON_CONST.HEIGHT_ARRAY[data.actual_height_code] + " and "
    text += data.PERSON_CONST.WEIGHT_ARRAY[data.weight_code]
    text += data.relation_list.write()
    return text
