

from btpy.src.btpy.Btpy import Btpy

class ConceptKey:

    LIMIT_EMOTION:int = 5
    MIN_LIMIT:int = 2

    def __init__(self, KEY) -> None:
        self.key = ""
        self.sadness = 0
        self.happiness = 0
        self.angry = 0
        self.surprise = 0
        self.disgust = 0
        self.fear = 0
        self.shame = 0
        self.pain = 0
        self.set_key(KEY)

    """
    Funcion que obtiene la emocion principal
    del personaje calculada tras un 
    algoritmo que define si esta aburrido 
    o tiene otra emocion destacable.
    """
    # retorna una clave de emocion
    def get_main_emotion(self)->str:
        dict_result = {
            "happiness":self.happiness,
            "angry":self.angry,
            "surprise":self.surprise, 
            "disgust":self.disgust,
            "fear":self.fear,
            "shame":self.shame,
            "pain":self.pain
        }
        # para basic things has_all
        is_bored = True
        for k in dict_result:
            if(dict_result[k] \
                > self.MIN_LIMIT):
                is_bored = False
                break
        if(is_bored): return "bored"
        return Btpy.max_dict(dict_result)

    def advance_time(self):
        self.sadness = Btpy.sum_in_range(
            self.sadness, -1, 
            [0, self.LIMIT_EMOTION])
        self.happiness = Btpy.sum_in_range(
            self.happiness, -1, 
            [0, self.LIMIT_EMOTION])
        self.angry = Btpy.sum_in_range(
            self.angry, -1, 
            [0, self.LIMIT_EMOTION])
        self.surprise = Btpy.sum_in_range(
            self.surprise, -1, 
            [0, self.LIMIT_EMOTION])
        self.disgust = Btpy.sum_in_range(
            self.disgust, -1, 
            [0, self.LIMIT_EMOTION])
        self.fear = Btpy.sum_in_range(
            self.fear, -1, 
            [0, self.LIMIT_EMOTION])
        self.shame = Btpy.sum_in_range(
            self.shame, -1, 
            [0, self.LIMIT_EMOTION])
        self.pain = Btpy.sum_in_range(
            self.pain, -1, 
            [0, self.LIMIT_EMOTION])

    def write(self):
        txt = f"{self.happiness=}\n"\
        + f"{self.angry=}\n"\
        + f"{self.surprise=}\n"\
        + f"{self.disgust=}\n"\
        + f"{self.fear=}\n"\
        + f"{self.pain=}\n"\
        + f"{self.shame=}"
        return txt
    
    def load_concept_dict(self, 
            concept):
        self.sum_happiness(
            concept["happiness"])
        self.sum_angry(concept["angry"])
        self.sum_surprise(concept["surprise"])
        self.sum_disgust(concept["disgust"])
        self.sum_fear(concept["fear"])
        self.sum_shame(concept["shame"])
        self.sum_shame(concept["pain"])
    
    def set_key(self, KEY):
        self.key = KEY

    def get_key(self):
        return self.key

    def sum_concept_key(self, CONCEPT_KEY):
        self.sum_sadness(CONCEPT_KEY.sadness)
        self.sum_happiness(CONCEPT_KEY.happiness)
        self.sum_angry(CONCEPT_KEY.angry)
        self.sum_surprise(CONCEPT_KEY.surprise)
        self.sum_disgust(CONCEPT_KEY.disgust)
        self.sum_shame(CONCEPT_KEY.shame)
        self.sum_fear(CONCEPT_KEY.fear)
        self.sum_pain(CONCEPT_KEY.pain)

    def sum_sadness(self, NUMBER):
        self.sadness = Btpy.sum_in_range(
            self.sadness, 
            NUMBER, [0, self.LIMIT_EMOTION]
        )

    def sum_fear(self, NUMBER):
        self.fear = Btpy.sum_in_range(
            self.fear, 
            NUMBER, [0, self.LIMIT_EMOTION]
        )

    def sum_happiness(self, NUMBER):
        self.happiness = Btpy.sum_in_range(
            self.happiness, 
            NUMBER, [0, self.LIMIT_EMOTION]
        )

    def sum_angry(self, NUMBER):
        self.angry = Btpy.sum_in_range(
            self.angry, 
            NUMBER, [0, self.LIMIT_EMOTION]
        )

    def sum_surprise(self, NUMBER):
        self.surprise = Btpy.sum_in_range(
            self.surprise, 
            NUMBER, [0, self.LIMIT_EMOTION]
        )

    def sum_disgust(self, NUMBER):
        self.disgust = Btpy.sum_in_range(
            self.disgust, 
            NUMBER, [0, self.LIMIT_EMOTION]
        )

    def sum_shame(self, NUMBER):
        self.shame = Btpy.sum_in_range(
            self.shame, 
            NUMBER, [0, self.LIMIT_EMOTION]
        )

    def sum_pain(self, NUMBER):
        self.pain = Btpy.sum_in_range(
            self.pain, 
            NUMBER, [0, self.LIMIT_EMOTION]
        )