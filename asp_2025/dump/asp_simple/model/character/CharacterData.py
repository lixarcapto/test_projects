

from ..relations_list.RelationsList \
    import RelationsList
from ..time_sp.TimeSp import TimeSp
from .const.appearance_const import*
from ..genetics.Genetics import Genetics
from .KeysTranslator import KeysTranslator
from .character_const import*

class CharacterData:

    """
    Clase que almacena los datos del
    Character.
    """

    KEYS = KeysTranslator
    ACTION_TUPLE = ACTION_TUPLE

    def __init__(self):
        # IDENTITY --------------------------
        """
        Son todos los datos relacionados
        a la identidad de la persona.
        """
        self.__name:str = "None"
        self.__second_name:str = "None"
        self.__lastname:str = "None"
        self.__second_lastname:str = "None"
        self.__age_range:str = "None"
        self.__id:str = "None"
        self.__district_code:str = "None"
        self.__region_code:str = "None"
        self.__birth_region_code:str = "None"
        self.__country_code:str = "None"
        self.__culture:str = "None"
        self.__gender:str = "None"
        self.__is_ancestral:bool = True
        self.__proffesion:str = "unprofessional"
        #
        # CONEXIONS -------------------------
        self.relations = RelationsList()
        #
        # APPEARANCES ------------------------
        self.__facial_hair:str = ""
        self.__hair_style:str = ""
        self.__actual_height:int = 0
        self.__skin_color:str = ""
        self.__eye_color:str = ""
        self.__eye_type:str = ""
        self.__hair_type:str = ""
        self.__hair_color:str = ""
        self.__maximum_size:int = 0
        #
        # PERSONALITY -----------------------
        """
        Incluye los rasgos de personalidad
        que definen su comportamiento; tienen
        un rango de 0 a 2.
        """
        self.__courage:int = 0
        self.__goodness:int = 0
        self.__self_control:int = 0
        self.__persistence:int = 0
        self.__respect:int = 0
        self.__activity:int = 0
        #
        # TALK DATA -------------------------
        self.__salute:str = ""
        self.__goodbye:str = ""
        #
        # NEEDS ------------------------------
        """
        Son las nesesidades de productos
        y servicios del personaje para
        vivir.
        """
        self.__has_water:bool = True
        self.__has_food:bool = True
        self.__has_fun:bool = True
        self.__has_dress:bool = True
        self.__has_relationships:bool = True
        self.__has_refreshing:bool = True
        self.__has_heating:bool = True
        self.__has_sanitation:bool = True
        self.__has_health:bool = True
        #
        # STATES --------------------------
        """
        Son todos los estados variables
        numericos relacionados al personaje.
        """
        self.__mood_points = 0
        self.__emotion = "normal"
        self.age_time = TimeSp()
        self.genetics:Genetics = Genetics()
        """
        indica si el personaje esta 
        en una casa o en la calle.
        """
        self.__is_outside = True
        self.__action:str = ""
        #

    # IDENTITY ACCESS -----------------------

    def set_name(self, STRING:str):
        self.__name = STRING

    def get_name(self)->str:
        return self.__name

    def set_second_name(self, 
            STRING:str):
        self.__second_name = STRING

    def get_second_name(self)->str:
        return self.__second_name

    def set_lastname(self, STRING:str):
        self.__lastname = STRING

    def get_lastname(self)->str:
        return self.__lastname

    def set_second_lastname(self, STRING:str):
        self.__second_lastname = STRING

    def get_second_lastname(self)->str:
        return self.__second_lastname
    
    def set_age_range(self, AGE_RANGE:str):
        self.__age_range = AGE_RANGE

    def get_age_range(self)-> str:
        return self.__age_range
    
    def set_id(self, ID:str):
        self.__id = ID
    
    def get_id(self)->str:
        return self.__id

    def set_district_code(self, CODE:str):
        self.__district_code = CODE

    def get_district_code(self)-> str:
        """
        Obtiene el codigo del distrito 
        donde esta el personaje.
        """
        return self.__district_code
    
    def set_region_code(self, CODE:str):
        self.__region_code = CODE

    def get_region_code(self)-> str:
        return self.__region_code

    def set_birth_region_code(self, 
            CODE:str):
        self.__birth_region_code = CODE

    def get_birth_region_code(self)->str:
        return self.__birth_region_code

    def set_country_code(self, CODE:str):
        self.__country_code = CODE

    def get_country_code(self)->str:
        return self.__country_code
    
    def set_culture(self, CULTURE:str):
        self.__culture = CULTURE

    def get_culture(self)-> str:
        return self.__culture
    
    def set_gender(self, GENDER:str):
        self.__gender = GENDER

    def get_gender(self)->str:
        return self.__gender
    
    def get_is_ancestral(self)->bool:
        """
        Ancestral indica que el personaje
        es de los creados artificialmente.
        """
        return self.__is_ancestral
    
    def set_is_ancestral(self, BOOL:bool):
        self.__is_ancestral = BOOL

    def set_proffesion(self, PROFFESION:str):
        self.__proffesion = PROFFESION

    def get_proffesion(self)->str:
        return self.__proffesion
    
    # ----------------------------------------
    
    # PERSONALITY ACCESS --------------------

    def set_courage(self, INT:int):
        self.__courage = INT

    def get_courage(self)->int:
        return self.__courage

    def set_goodness(self, INT:int):
        self.__goodness = INT

    def get_goodness(self)->int:
        return self.__goodbye

    def set_self_control(self, INT:int):
        self.__self_control = INT

    def get_self_control(self)->int:
        return self.__self_control

    def set_persistence(self, INT:int):
        self.__persistence = INT

    def get_persistence(self)->int:
        return self.__persistence

    def set_respect(self, INT:int):
        self.__respect = INT

    def get_respect(self)->int:
        return self.__respect

    def set_activity(self, INT:int):
        self.__activity = INT

    def get_activity(self)->int:
        return self.__activity

    # ---------------------------------------
    
    # TALK DATA ACCESSOR --------------------

    def set_salute(self, TEXT:str):
        self.__salute = TEXT

    def get_salute(self)->str:
        """
        Es el saludo que utilizara el 
        personaje en un mensaje.
        """
        return self.__salute
    
    def set_goodbye(self, TEXT:str):
        self.__goodbye = TEXT

    def get_goodbye(self)->str:
        """
        Es la despedida que usara un 
        personaje en un mensaje.
        """
        return self.__goodbye

    # ---------------------------------------

    # NEEDS ACCESSORS ----------------------

    def get_has_water(self)->bool:
        return self.__has_water
    
    def set_has_water(self, BOOL:str):
        self.__has_water = BOOL

    def get_has_food(self)->bool:
        return self.__has_food
    
    def set_has_food(self, BOOL:str):
        self.__has_food = BOOL

    def get_has_fun(self)->bool:
        return self.__has_fun
    
    def set_has_fun(self, BOOL:str):
        self.__has_fun = BOOL

    def get_has_dress(self)->bool:
        return self.__has_dress
    
    def set_has_dress(self, BOOL:str):
        self.__has_dress = BOOL

    def get_has_relationships(self)->bool:
        return self.__has_relationships
    
    def set_has_relationships(self, BOOL:str):
        self.__has_relationships = BOOL

    def get_has_refreshing(self)->bool:
        return self.__has_refreshing
    
    def set_has_refreshing(self, BOOL:str):
        self.__has_refreshing = BOOL

    def get_has_heating(self)->bool:
        return self.__has_heating
    
    def set_has_heating(self, BOOL:str):
        self.__has_heating = BOOL

    def get_has_sanitation(self)->bool:
        return self.__has_sanitation
    
    def set_has_sanitation(self, BOOL:str):
        self.__has_sanitation = BOOL

    def get_has_health(self)->bool:
        return self.__has_health
    
    def set_has_health(self, BOOL:str):
        self.__has_health = BOOL

    # ---------------------------------------

    # STATES ACCESORS------------------------

    def get_mood_points(self)->int:
        return self.__mood_points
    
    def set_mood_points(self, INT:str):
        self.__mood_points = INT

    def sum_mood_points(self, INT:str):
        self.__mood_points += INT

    def get_emotion(self)->str:
        return self.__emotion
    
    def set_emotion(self, EMOTION:str):
        self.__emotion = EMOTION

    def get_is_outside(self)->bool:
        return self.__is_outside
    
    def set_is_outside(self, BOOL:str):
        self.__is_outside = BOOL

    def get_action(self)->str:
        return self.__action
    
    def set_action(self, STRING:str)->None:
        self.__action = STRING

    # --------------------------------------

    # APPEARANCES --------------------------

    def get_facial_hair(self)->str:
        return self.__facial_hair
    
    def set_facial_hair(self, 
            STRING:str):
        if(not STRING in FACIAL_HAIR_TUPLE):
            print(f"Error:{STRING} is not facialhair key")
        self.__facial_hair = STRING

    def get_hair_style(self)->str:
        return self.__hair_style
    
    def set_hair_style(self, HAIR_STYLE:str):
        self.__hair_style = HAIR_STYLE

    def get_actual_height(self)->int:
        return self.__actual_height
    
    def set_actual_height(self, HEIGHT:int):
        self.__actual_height = HEIGHT

    def get_actual_height_key(self)->str:
        return self.KEYS.HEIGHT_KEY\
            [self.__actual_height]

    def get_skin_color(self)->str:
        return self.__skin_color
    
    def set_skin_color(self, SKIN_COLOR:str):
        self.__skin_color = SKIN_COLOR

    def get_eye_color(self)->str:
        return self.__eye_color
    
    def set_eye_color(self, EYE_COLOR:str):
        self.__eye_color = EYE_COLOR

    def get_eye_type(self)->str:
        return self.__eye_type
    
    def set_eye_type(self, EYE_TYPE:str):
        self.__eye_type = EYE_TYPE

    def get_hair_type(self)->str:
        return self.__hair_type
    
    def set_hair_type(self, HAIR_TYPE:str):
        self.__hair_type = HAIR_TYPE

    def get_hair_color(self)->str:
        return self.__hair_color
    
    def set_hair_color(self, HAIR_COLOR:str):
        self.__hair_color = HAIR_COLOR

    def get_maximum_size(self)->int:
        return self.__maximum_size
    
    def set_maximum_size(self,
            MAXIMUM_SIZE:int):
        self.__maximum_size = MAXIMUM_SIZE

    # -------------------------------------