

from ..person_cache.PersonCache import PersonCache
from ..memory.Memory import Memory
from .DESICION_KEYS import*

class PersonData:

    """
     Clase para descomponer interfaz 
     de persona dividiendo el 
     almacenamiento de datos del 
     comportamiento
    """

    LAST_CODE = 0
    cache = PersonCache()

    def __init__(self) -> None:
        # identity
        self.id = ""
        self.name = ""
        self.second_name = ""
        self.lastname = ""
        self.second_lastname = ""
        self.nickname = ""
        self.gender = ""
        self.culture = ""
        self.race = ""
        self.team = "neutral"
        #
        # place
        self.region_code = ""
        self.territory_code = ""
        #
        # temporal memory
        self.memory = ""
        self.perception_list = []
        self.description_dict = {}
        #
        # appearance
        self.skin_color = ""
        self.age_range = 0
        self.hair_color = ""
        self.hair_type = ""
        self.hair_style = ""
        self.eye_color = ""
        self.eye_type = ""
        self.actual_height = 0
        self.maximum_height = 0
        self.cloth_outfit = ""
        #
        # states
        self.life_time = 0
        self.health = 100
        self.event_buffer = []
        self.desicion = ""
        self.focus_id = ""
        # location
        self.is_outside = True
        # description
        self.region_description = ""
        self.object_description = []
        #
        # memoria actual
        self.memory = Memory()