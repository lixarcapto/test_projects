



class Description:

    """
    Clase que sirve para almacenar
    datos de descripciones como un 
    mensaje.
    """

    def __init__(self):
        self.character_presentation = ""
        self.date = ""
        self.society_characters = ""
        self.character_states = ""
        self.character_relations = ""
        self.region_text = ""

    def write_all(self)->str:
        return ""\
        + f"{self.region_text}.\n"\
        + f"{self.date}."\
        + f"{self.society_characters}.\n"\
        + f"{self.character_presentation}.\n"\
        + f"{self.character_states}.\n"\
        + f"{self.character_relations}.\n"