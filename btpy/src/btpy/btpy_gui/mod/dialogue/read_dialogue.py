


from ....btpy_persistence.mod.read_txt.read_txt import read_txt
from ....btpy_list.mod.clean_voids.clean_voids import *
from ....btpy_string.mod.normalize.normalize import*

def read_dialogue(PATH:str):
    """
    Lee un archivo en formato de dialogo
    donde cada dialogo inicia con una
    palabra antes de dos puntos y finaliza
    en un salto de linea.
    """
    text = read_txt(PATH)
    paragraph_list = text.split("\n\n")
    dialogue_dict = {}
    dialogue_list = []
    dialogue_dict_list = []
    paragraph_list = clean_voids(
        paragraph_list)
    for e in paragraph_list:
        dialogue_dict = {}
        dialogue_list = e.split(":")
        dialogue_dict["title"] \
            = dialogue_list[0]
        dialogue_dict["description"] \
            = dialogue_list[1]
        dialogue_dict_list.append(
            dialogue_dict
        )
    return dialogue_dict_list
    