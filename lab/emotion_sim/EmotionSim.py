

from btpy.src.btpy.Btpy import Btpy
from emotion_sim.ConceptKey import ConceptKey
from .ROUTES import*

class EmotionSim:

    """
    Clase para simular emociones para 
    npcs y chatbot
    """

    CONCEPT_DICT = {}
    # referencia a la clase conceptkey para
    # importar
    ConceptKey = ConceptKey

    def __init__(self) -> None:
        self.concept = ConceptKey("")
        self.concept_key_dict = {}
        # carga el recurso nesesario
        if(self.CONCEPT_DICT == {}):
            self.__read_concept_dict()
        self.__init_default_keys()

    """
     función que lee de un archivo 
     Excel un  diccionario de listas 
     de String  Qué representa a claves 
     predefinidas y su modificadores.
    """
    def __read_concept_dict(self):
        concept_dict = Btpy.read_xlsx_nested(
            ROUT_CONCEPT)
        concept_dict = Btpy.mapp(
            concept_dict, 
            lambda e:int(e)
        )
        self.CONCEPT_DICT = concept_dict

    def __analize_concept(self, KEY:str)\
            ->None:
        if(not KEY in self.concept_key_dict):
            return None
        concept = self.concept_key_dict[KEY]
        self.concept.sum_concept_key(
            concept)
        
    def advance_time(self):
        self.concept.advance_time()
        
    def analize_concept_list(self, 
            KEY_LIST:list[str]):
        for e in KEY_LIST:
            self.__analize_concept(e)
    
    def get_main_emotion(self)->str:
        return self.concept\
            .get_main_emotion()
    
    def set_concept_key(self, CONCEPT_KEY):
        self.concept_key_dict\
        [CONCEPT_KEY.get_key()] \
            = CONCEPT_KEY

    def write(self):
        return self.concept.write()
    
    def __init_default_keys(self):
        concept = None
        for k in self.CONCEPT_DICT:
            concept = self.ConceptKey(k)
            concept.load_concept_dict(
                self.CONCEPT_DICT[k])
            self.set_concept_key(concept)