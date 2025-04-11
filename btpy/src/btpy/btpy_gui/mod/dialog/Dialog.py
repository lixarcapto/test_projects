

from ..simple_card.SimpleCard import SimpleCard
from .read_dialogue import*
from .read_cards_json import*

class Dialog(SimpleCard):

    """
    TODO: 
    * añadir las descripciones al 
    inicio del dialogo.
    * hacer que todo lo que este sin nombre
    sea enviado automaticamente a un
    narrador.
    """

    def __init__(self, window):
        super().__init__(window, 
            "horizontal", 
            True)
        self.card_dict_nested = {}
        self.dialogue_list = []
        self.set_button_text("continue...")
        self.icon_size_list = [100, 100]
        self.index_dialogue = 0
        def fn(e):
            self.next_dialog()
        self.callback = None
        self.add_listener(fn)
        

    def start(self):
        self.update_dialogue()

    def update_dialogue(self):
        dialogue = self.dialogue_list\
            [self.index_dialogue]
        card_dict = self.card_dict_nested[
            dialogue["title"]]
        self.set_title(dialogue["title"])
        self.set_icon(card_dict["path"],
            self.icon_size_list)
        self.set_description(
            dialogue["description"])
        
    def load_json_cards(self, PATH):
        """
        Esta funcion permite cargar
        objetos cards desde un archivo
        json en formato json cards; 
        este formato consiste en escribir
        un list de objetos json
        con los atributos descritpion, 
        title y path.
        {
            "title": "",
            "description": "",
            "path": ""
        }
        """
        self.card_dict_nested \
            = read_cards_json(PATH)
        
    def load_dialogue_txt(self, PATH:str):
        """
        Esta funcion permite cargar un
        archivo TXT con dialogos en 
        el formato indicado para dialogos.
        Este formato consiste en separar
        cada dialogo por un salto de linea,
        la primera seccion se separa por
        dos puntos y representa al titulo
        del personaje y la segunda al
        texto que se muestra debajo como
        descripcion; por ejemplo:

        Monica: Hola!
        Antonia: Buen dia
        Monica: como te va
        Antonia: exelente
        Monica: me alegro
        """
        dialogue_list = read_dialogue(
            PATH)
        self.set_dialog_list(dialogue_list)
        
    def add_end_listener(self, CALLBACK):
        self.callback = CALLBACK

    def next_dialog(self):
        if(self.index_dialogue \
                < len(self.dialogue_list) -1):
            self.index_dialogue += 1
            self.update_dialogue()
        else:
            self.set_button_text("end")
            if(self.callback != None):
                self.callback()

    def set_dialog_list(self, 
            DIALOG_LIST:dict[str]):
        """
        [
            {
                "title": "", 
                "description": ""
            }
        ]
        """
        self.dialogue_list = DIALOG_LIST

    def set_character_card_dict(self, 
            CARD_DICT:dict[str]):
        """
        {
            "title": "",
            "description": "",
            "path": ""
        }
        """
        self.card_dict_nested\
            [CARD_DICT["title"]] = {
                "description":CARD_DICT[
                    "description"],
                "path":CARD_DICT["path"]
            }