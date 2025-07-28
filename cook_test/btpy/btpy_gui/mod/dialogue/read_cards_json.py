

from ....btpy_persistence.mod.read_json_object.read_json_object import*

def read_cards_json(PATH:str):
    card_list = read_json_object(PATH)
    card_nested_dict = {}
    key = ""
    for card_dict in card_list:
        key = card_dict["title"]
        card_nested_dict[key] = card_dict
        del(card_nested_dict[key]["title"])
    return card_nested_dict

