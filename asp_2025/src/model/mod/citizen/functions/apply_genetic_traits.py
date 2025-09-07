


def apply_genetic_traits(citizen_data):
    citizen_data = apply_albinism(
        citizen_data)
    return citizen_data

def apply_albinism(citizen_data):
    is_albino = citizen_data.genes_self\
        .data.get_is_albino()
    if(not is_albino):
        return citizen_data
    citizen_data.set_skin_color_key("pale")
    citizen_data.set_eye_color_key("red")
    citizen_data.set_hair_color_key(
        "white")
    return citizen_data