

from btpy.src.btpy.Btpy import Btpy
from ..person_cache.PersonCache import PersonCache
from ..memory.Memory import Memory
from .PersonData import PersonData
from .fn.narrative_write import*
from .fn.randomize_person import*
from .fn.appearance_description import*

class Person:

    """
     módulo que representa a un 
     personaje con todos sus atributos 
     y comportamientos
    """

    def __init__(self, culture) -> None:
        self.__in = PersonData()
        self.__in.culture = culture
        self.__init()
        #

    def __init(self):
        self.create_id()
        self.randomize(self.__in.culture)

    #-PUBLIC-ACCESORS -------------------------

    def set_desicion(self, DESICION_KEY):
        self.__in.desicion = DESICION_KEY

    def get_desicion(self):
        return self.__in.desicion
    
    def get_focus_id(self):
        return self.__focus_id

    def get_id(self)->str:
        return self.__in.id
    
    def set_region_description(self, TEXT):
        self.__in.region_description = TEXT

    def add_perception_keys(self, 
            KEY, TYPE):
        perception = {"KEY": KEY, 
                      "TYPE":TYPE}
        self.__in.perception_list \
            = perception

    def add_description(self, KEY, 
        DESCRIPTION):
        self.__in.description_dict[KEY]\
            = DESCRIPTION

    def is_outside(self):
        return self.__in.is_outside
    
    def set_object_description(self, list):
        self.__in.object_description = list

    #------------------------------------------

    def pick_events(self):
        event_list = self.__in.event_buffer
        self.__in.event_buffer.clear()
        return event_list

    def receibe_attack(self, value):
        self.__in.health = Btpy.sum_in_range(
            value, [0, 100])
    
    def update(self):
        pass

    def randomize(self, culture):
        self.__in = randomize_person(
            self.__in, culture)

    def create_id(self):
        self.__in.id = str(PersonData.LAST_CODE)
        PersonData.LAST_CODE += 1

    def personality_description(self):
        txt = ""
        return txt
    
    def describe_appearance(self):
        txt = appearance_description(
            self.__in)
        return txt

    def narrative_write(self):
        return narrative_write(self.__in)