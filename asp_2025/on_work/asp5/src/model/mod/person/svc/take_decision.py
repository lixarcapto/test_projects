

import random

"""
    Funcion que toma una decision aleatoria
    para las actividades especiales de ese dia.
"""
def take_decision(data):
    map = __create_desition_map()
    decision_key = random.choice(data.DESITION_KEYS)
    map["key"] = decision_key
    data.decision_map = map
    return data

def __create_desition_map():
    map = {"key": "", "objetive_code": 0}
    return map
