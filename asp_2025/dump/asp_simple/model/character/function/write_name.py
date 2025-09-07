


from ..CharacterData import CharacterData

def write_name(data:CharacterData)->str:
    return data.get_name() + " " \
    + data.get_second_name() + " " \
    + data.get_lastname() + " " \
    + data.get_second_lastname() + " "