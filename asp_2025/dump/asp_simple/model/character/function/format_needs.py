

from ..CharacterData import CharacterData

def format_needs(data)->CharacterData:
    data.set_has_water(False)
    data.set_has_food(False)
    data.set_has_fun(False)
    data.set_has_dress(False)
    data.set_has_sanitation(False)
    data.set_has_relationships(False)
    return data