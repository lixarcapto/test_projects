

from .citizen_constants import*
from ..genes.genes_constant import*
from ..genes.Genes import Genes
from ...mod.date_asp.DateAsp import DateAsp
from .mod.relationship.Relationship import Relationship
from ..age_range_depot.AgeRangeDepot import AgeRangeDepot
from ..profession_depot.ProfessionDepot import ProfessionDepot
from ..cultural_group_depot.CulturalGroupDepot import CulturalGroupDepot
from ..cultural_group_depot.CulturalGroupItem import CulturalGroupItem
from btpy.Btpy import Btpy

class CitizenData:

    """
    Esta clase contiene los datos de 
    los genes para separar el 
    almacenamiento de las principales 
    funciones modificadoras de la 
    clase genes.
    """

    last_unique_number:int = 0
    profession_dict = None
    age_range_data_dict:dict[dict] = None
    age_range_list_dict:dict[dict] = None
    age_range_depot = AgeRangeDepot()
    profession_depot = ProfessionDepot()
    MOOD_POINTS_MAX:int = 2
    PREGNANT_PROBABILITY_LIST = [
        ["TWINS", 2],
        ["MULTIPLE", 3],
        ["ONLY", 95]
    ]
    MAX_NUMBER_BABIES:int = 3
    MONTHS_PREGNANT:int = 3

    def __init__(self):
        # -------------------------------
        # IDENTITY
        #
        # Estas variables de identidad
        # sirven para identificar a los
        # personajes mediante claves
        # y codigos.
        #
        self.__name:str = ""
        self.__second_name:str = ""
        self.__lastname:str = ""
        self.__second_lastname:str = ""
        self.__nickname:str = ""
        self.__id_number:int = 0
        self.__i_point_origin_region \
            :list[int] = [0, 0]
        self.__i_point_actual_region \
            :list[int] = [0, 0]
        # ---------------------------------
        # STYLE TRAITS
        #
        self.__beard_style:str = "invisible"
        self.__current_beard_style\
            :str = "invisible"
        self.__clothing_style_number:int = 0
        self.__hairstyle_number:int = 0
        self.__makeup_number:int = 0
        self.__current_makeup_number\
            :int = 0
        # ---------------------------------
        # GENETICS TRAITS 
        #
        self.genes_self = None
        self.genes_dad = None
        self.genes_mom = None
        self.__regional_group_idx:int = 0
        self.__hair_color_actual_n\
            :int = 0
        self.__height_actual_number:int = 0
        self.__age_range_number:int = 0
        self.__eye_color_number:int = 0
        self.__hair_type_number:int = 0
        self.__is_bald:bool = False
        self.__eye_type_number:int = 0
        self.fertility_percent:int = 0
        self.__skin_color_number:int = 0
        self.__nose_type_number:int = 0
        self.__is_freckled:bool = False
        self.__mouth_type_number:int = 0
        # ---------------------------------
        # NEEDS ---------------------------
        self.__have_food:bool = False
        self.__have_water:bool = False
        self.__have_shelter:bool = False
        self.__have_clothes:bool = False
        self.__have_transportation:bool \
            = False
        self.__have_comfort:bool = False
        self.__have_luxuries:bool = False
        self.__have_toilet:bool = False
        self.__have_fun:bool = False
        self.__have_social:bool = False
        self.__have_beauty:bool = False
        self.__have_jov:bool = False
        self.__have_heating:bool = False
        self.__have_lighting:bool = False
        # ---------------------------------
        # OBJECTS 
        #
        self.date_asp = None
        self.relation = None
        self.actual_postcard = None
        self.origin_postcard = None
        # ---------------------------------
        # BEHAVIOR
        #
        self.childhood_overcome = False
        self.adolescence_overcome = False
        self.ambient_temperature:str = ""
        self.is_dead:bool = False
        self.is_pregnant:bool = False
        self.is_giving_birth:bool = False
        self.is_a_mother:bool = False
        self.is_inside:bool = False
        self.is_virgin:bool = True
        self.is_legendary:bool = False
        self.can_speak:bool = True
        self.can_walk:bool = True
        self.can_hear:bool = True
        self.hide_hair:bool = False
        self.child_in_care_list:list = []
        self.__has_infertility:bool = False
        # -------------------------------
        # PERSONALITY
        #
        self.__profession_number:int = 0
        self.days_pregnant:int = 0
        self.child_in_care = None
        self.cause_death_key:str = ""
        self.specific_cause_death:str = ""
        self.__archetype_key:str = ""
        self.__mood_points:int = 0
        self.__mood_value:int = 0
        self.__culture_number:int = 0
        self.__ideology_number:int = 0
        self.__gender_number:int = 0
        # --------------------------------
        # BIOGRAPHY HISTORY
        #
        # Estas variables sirven para
        # contar una historia relacionada
        # al personaje.
        #
        self.childrens_history_code\
            :int = 0
        self.childrens_activities_code = 0
        self.childrens_living_place_code = 0
        self.teens_actities_code = 0
        self.birthdate_date = None
        self.teenage_story_code:int = 0
        self.lastest_work_story_code\
            :int = 0
        self.latest_story_freetime_code\
            :int = 0
        # --------------------------------

    # -------------------------------------
    # PUBLIC ACCESSORS --------------------

    # -----------------------------------
    # IDENTITY

    def get_name(self)->str:
        return self.__name
    
    def set_name(self, NAME:str):
        self.__name = NAME
    
    def set_second_name(self, NAME:str):
        self.__second_name = NAME

    def get_second_name(self)->str:
        return self.__second_name
    
    def set_lastname(self, NAME:str):
        self.__lastname = NAME

    def get_lastname(self)->str:
        return self.__lastname
    
    def set_second_lastname(self, NAME:str):
        self.__second_lastname = NAME

    def get_second_lastname(self)->str:
        return self.__second_lastname
    
    def set_nickname(self, NAME:str):
        self.__nickname = NAME

    def get_nickname(self)->str:
        return self.__nickname
    
    def get_id_number(self)->int:
        return self.__id_number
    
    def set_id_number(self, number:int):
        self.__id_number = number

    def set_actual_region_point(self,
            POINT:list[int]):
        self.__i_point_actual_region = POINT
    
    def get_actual_region_point(self)\
            ->list[int]:
        return self.__i_point_actual_region

    def set_origin_region_point(self,
            POINT:list[int]):
        self.__i_point_origin_region = POINT

    def get_origin_region_point(self)\
            ->list[int]:
        return self.__i_point_origin_region

    # -----------------------------------
    # STYLE TRAITS
    #

    def get_hairstyle_key(self)->str:
        INDEX = self.__hairstyle_number
        return HAIRSTYLE_K_TUPLE[INDEX]
    
    def set_hairstyle_key(self, 
                KEY:str)->None:
        INDEX = HAIRSTYLE_K_TUPLE\
            .index(KEY)
        self.__hairstyle_number = INDEX

    def get_clothing_style_key(self)->str:
        N = self\
            .__clothing_style_number
        return CLOTHING_STYLE_K_TUPLE[N]
    
    def set_clothing_style_key(self, 
                KEY:str)->None:
        idx = CLOTHING_STYLE_K_TUPLE\
            .index(KEY)
        self.__clothing_style_number \
            = idx
        
    def get_beard_style_key(self)->str:
        return self.__beard_style

    def set_beard_style_key(self, 
            KEY:str)->None:
        self.__beard_style = KEY

    def get_current_beard_style(self)->str:
        return self.__current_beard_style
    
    def set_current_beard_style(self, 
            KEY:str)->None:
        self.__current_beard_style = KEY

    def set_current_makeup_key(self,
            KEY:str):
        idx = MAKEUP_KEY_TUPLE\
            .index(KEY)
        self.__current_makeup_number\
            = idx
    
    def get_current_makeup_key(self):
        idx = self.__current_makeup_number
        return MAKEUP_KEY_TUPLE[idx]
    
    def set_makeup_key(self,
            KEY:str):
        idx = MAKEUP_KEY_TUPLE\
            .index(KEY)
        self.__makeup_number\
            = idx
    
    def get_makeup_key(self):
        idx = self.__makeup_number
        return MAKEUP_KEY_TUPLE[idx]

    # -------------------------------------
    # NEEDS 
    #

    def get_have_food(self)->bool:
        return self.__have_food
    
    def set_have_food(self, BOOL:bool)\
            ->None:
        self.__have_food = BOOL
    
    def get_have_water(self)->bool:
        return self.__have_water
    
    def set_have_water(self, BOOL:bool)\
            ->None:
        self.__have_water = BOOL
    
    def get_have_house(self)->bool:
        return self.__have_shelter
    
    def set_have_house(self, BOOL:bool)\
            ->None:
        self.__have_shelter = BOOL
    
    def get_have_clothes(self)->bool:
        return self.__have_clothes

    def set_have_clothes(self, BOOL:bool)\
            ->None:
        self.__have_clothes = BOOL

    def get_have_transportation(self)\
            ->bool:
        return self.__have_transportation
    
    def set_have_transportation(self, 
            BOOL:bool)->None:
        self.__have_transportation = BOOL
    
    def get_have_jov(self)->bool:
        return self.__have_jov
    
    def set_have_jov(self, BOOL:bool)\
            ->None:
        self.__have_jov = BOOL

    def get_have_comfort(self)->bool:
        return self.__have_comfort
    
    def set_have_comfort(self, BOOL:bool):
        self.__have_comfort = BOOL

    def get_have_luxuries(self)->bool:
        return self.__have_luxuries
    
    def set_have_luxuries(self, BOOL:bool):
        self.__have_luxuries = BOOL
    
    def get_have_toilet(self)->bool:
        return self.__have_toilet
    
    def set_have_toilet(self, BOOL:bool):
        self.__have_toilet = BOOL
    
    def get_have_fun(self)->bool:
        return self.__have_fun
    
    def set_have_fun(self, BOOL:bool):
        self.__have_fun = BOOL
    
    def get_have_social(self)->bool:
        return self.__have_social
    
    def set_have_social(self, BOOL:bool):
        self.__have_social = BOOL
    
    def get_have_beauty(self)->bool:
        return self.__have_beauty
    
    def set_have_beauty(self, BOOL:bool):
        self.__have_beauty = BOOL

    def get_have_heating(self)->bool:
        return self.__have_heating
    
    def set_have_heating(self, BOOL:bool):
        self.__have_heating = BOOL

    def get_have_lighting(self)->bool:
        return self.__have_lighting
    
    def set_have_lighting(self, BOOL:bool):
        self.__have_lighting = BOOL

    # -------------------------------------

    def get_is_inside(self)->bool:
        """
        Funcion que retorna verdadero
        si el ciudadano esta dentro de 
        casa o un edificio.
        """
        return self.is_inside
    
    def get_hide_hair(self)->bool:
        return self.hide_hair
    
    def set_hide_hair(self, BOOL:bool):
        self.hide_hair = BOOL
    
    def set_age_range_key(self, KEY:str):
        number = AGE_RANGE_KEY_TUPLE\
            .index(KEY)
        self.__age_range_number = number

    def get_age_range_key(self):
        index = self.__age_range_number
        return AGE_RANGE_KEY_TUPLE[index]
    
    def get_age_range_number(self)->int:
        return self.__age_range_number
    
    def set_age_range_number(self, 
            NUMBER:int)->None:
        self.__age_range_number = NUMBER

    def get_height_actual_key(self)->str:
        index = self.__height_actual_number
        return HEIGHT_KEY_TUPLE[index]
    
    def set_height_actual_key(self, 
                KEY:str)->None:
        number = HEIGHT_KEY_TUPLE.index(KEY)
        self.__height_actual_number = number

    def get_height_number(self)->int:
        return self.__height_actual_number
    
    def set_height_number(self, 
                NUMBER:int)->None:
        self.__height_actual_number = NUMBER    
    
    def get_hair_color_key(self)->str:
        idx = self.__hair_color_actual_n
        return HAIR_COLOR_K_TUPLE[idx]
    
    def set_hair_color_key(self, KEY:str)\
            ->None:
        number = HAIR_COLOR_K_TUPLE\
            .index(KEY)
        self.__hair_color_actual_n \
            = number
        
    def get_hair_color_number(self)->int:
        return self\
            .__hair_color_actual_n
    
    def set_hair_color_number(self, 
                NUMBER:int)->None:
        self.__hair_color_actual_n\
            = NUMBER
        
    

    def get_eye_color_key(self)->int:
        INDEX = self.__eye_color_number
        return EYE_COLOR_K_TUPLE[INDEX]

    def set_eye_color_key(self, KEY:str)\
            ->None:
        INDEX = EYE_COLOR_K_TUPLE.index(KEY)
        self.__eye_color_number = INDEX

    def get_eye_color_number(self)->int:
        return self.__eye_color_number
    
    def set_eye_color_number(self, 
                NUMBER:int)->None:
        self.__eye_color_number = NUMBER

    def get_eye_type_key(self)->str:
        I = self.__eye_type_number
        return EYE_TYPE_K_TUPLE[I]
    
    def set_eye_type_number(self, 
            NUMBER:int):
        self.__eye_type_number = NUMBER
    
    def set_eye_type_key(self, KEY:str)\
            ->None:
        I = EYE_TYPE_K_TUPLE.index(KEY)
        self.__eye_type_number = I

    def get_hair_type_key(self)->str:
        I = self.__hair_type_number
        return HAIR_TYPE_K_TUPLE[I]
    
    def set_hair_type_key(self, KEY:str)\
            ->None:
        I = HAIR_TYPE_K_TUPLE.index(KEY)
        self.__hair_type_number = I

    def set_hair_type_number(self, 
            NUMBER:int):
        self.__hair_type_number = NUMBER

    def get_skin_color_key(self)->str:
        I = self.__skin_color_number
        return SKIN_COLOR_K_TUPLE[I]
    
    def set_skin_color_key(self, KEY:str)\
            ->None:
        I = SKIN_COLOR_K_TUPLE.index(KEY)
        self.__skin_color_number = I

    def set_skin_color_number(self, 
            NUMBER:int):
        self.__skin_color_number = NUMBER

    def get_nose_type_key(self)->str:
        idx = self.__nose_type_number
        return NOSE_TYPE_KEY_TUPLE[idx]
    
    def set_nose_type_number(self, NUMBER): 
        self.__nose_type_number = NUMBER

    def set_mouth_type_number(self, 
            NUMBER:int):
        self.__mouth_type_number = NUMBER

    def get_mouth_type_key(self):
        idx = self.__mouth_type_number
        return MOUTH_TYPE_KEY_TUPLE[idx]

    def get_regional_group_key(self)->str:
        list_ = self.genes_self.data\
            .get_regional_group_list()
        I = self.__regional_group_idx
        return list_[I]
    
    def set_regional_group_key(self, 
                KEY:str)->None:
        list_ = self.genes_self.data\
            .get_regional_group_list()
        I = list_.index(KEY)
        self.__regional_group_idx = I
        self.genes_self\
            .data.set_regional_group_key(KEY)

    def get_is_bald(self)->bool:
        return self.__is_bald
    
    def set_is_bald(self, BOOL:bool)->None:
        self.__is_bald = BOOL

    def get_asp(self)->DateAsp:
        return self.date_asp
    
    def set_asp(self, date_asp:DateAsp)\
            ->None:
        self.date_asp = date_asp

    def get_relation(self)->Relationship:
        return self.relation
    
    def set_relation(self, 
            relationship:Relationship)\
            ->None:
        self.relation = relationship

    def get_culture_key(self)->str:
        NUMBER = self.__culture_number
        list_ = self.get_culture_key_list()
        return list_[NUMBER]
    
    def get_culture_key_list(self)->list:
        return CULTURE_KEY_LIST
    
    def set_culture_key(self, KEY:str)\
            ->None:
        list_ = self.get_culture_key_list()
        NUMBER = list_.index(KEY)
        self.__culture_number = NUMBER

    def get_ideology_key(self)->str:
        NUMBER = self.__ideology_number
        return IDEOLOGY_KEY_TUPLE[NUMBER]
    
    def set_ideology_key(self, KEY:str)\
            ->None:
        NUMBER = IDEOLOGY_KEY_TUPLE.index(
            KEY)
        self.__ideology_number = NUMBER

    def get_gender_key(self)->str:
        NUMBER = self.__gender_number
        return GENDER_KEY_TUPLE[NUMBER]
    
    def set_gender_key(self, KEY:str)->None:
        NUMBER = GENDER_KEY_TUPLE.index(
            KEY)
        self.__gender_number = NUMBER

    def get_is_dead(self)->bool:
        return self.is_dead
    
    def set_is_dead(self, BOOL:bool)->None:
        self.is_dead = BOOL

    def get_is_pregnant(self)->bool:
        return self.is_pregnant
    
    def set_is_pregnant(self, BOOL:bool)\
            ->None:
        self.is_pregnant = BOOL

    def get_is_giving_birth(self)->bool:
        return self.is_giving_birth
    
    def set_is_giving_birth(self, 
                BOOL:bool)->None:
        self.is_giving_birth = BOOL

    def get_is_a_mother(self)->bool:
        return self.is_a_mother
    
    def set_is_a_mother(self, BOOL:bool)\
                ->None:
        self.is_a_mother = BOOL

    def get_is_inside(self)->bool:
        return self.is_inside
    
    def set_is_inside(self, BOOL:bool)\
                ->None:
        self.is_inside

    def get_is_virgin(self)->bool:
        return self.is_virgin

    def set_is_virgin(self, BOOL:bool)->None:
        self.is_virgin = BOOL

    def get_is_legendary(self)->bool:
        return self.is_legendary
    
    def set_is_legendary(self, BOOL:bool)\
                ->None:
        self.is_legendary = BOOL

    def get_is_freckled(self)->bool:
        return self.__is_freckled
    
    def set_is_freckled(self, BOOL:bool)\
                ->None:
        self.__is_freckled = BOOL

    def get_personal_pronoun(self)->str:
        """
        Retorna el pronombre personal
        del personaje basado en su
        genero.
        """
        return PERSONAL_PRONOUN_TUPLE\
            [self.__gender_number]
    
    def get_possessive_pronoun(self)->str:
        """
        Retorna el pronombre posesivo
        del personaje basado en su
        genero.
        """
        return POSSESSIVE_PRONOUN_TUPLE\
            [self.__gender_number]
    
    # ------------------------------------

    # BEHAVIOR VALUES ---------------------

    def get_profession_key(self)->str:
        INDEX = self.__profession_number
        return PROFESSIONS_KEY_TUPLE[INDEX]
    
    def get_profession_item(self):
        k = self.get_profession_key()
        return CitizenData\
            .profession_depot\
                .get_item(k)

    def set_profession_key(self, 
                KEY:str)->None:
        INDEX = PROFESSIONS_KEY_TUPLE\
            .index(KEY)
        self.__profession_number = INDEX

    def get_days_pregnant(self)->int:
        return self.days_pregnant
    
    def set_days_pregnant(self, NUMBER:int)\
            ->None:
        self.days_pregnant = NUMBER

    def get_child_in_care(self)->any:
        return self.child_in_care
    
    def set_child_in_care(self, citizen)\
            ->None:
        self.child_in_care = citizen

    def get_cause_death_key(self)->str:
        return self.cause_death_key
    
    def set_cause_death_key(self, KEY:str)\
            ->None:
        self.cause_death_key = KEY

    def get_key_names(self):
        item = self\
            .get_cultural_group_item()
        return item.get_key_names()
    
    def get_fertility_by_age_range(self):
        return self.get_age_range_item()\
            .get_fertility()
    
    def get_archetype_key(self)->str:
        return self.__archetype_key

    def set_archetype_key(self, KEY:str)\
            ->None:
        self.__archetype_key = KEY

    def set_mood_points(self, NUMBER:int):
        self.__mood_points = NUMBER

    def get_mood_points(self)->int:
        return self.__mood_points
    
    def set_mood_value_key(self, 
            KEY:str):
        idx = MOOD_VALUE_KEY.index(KEY)
        self.__mood_value = idx
    
    def get_mood_value_key(self)->str:
        return MOOD_VALUE_KEY\
            [self.__mood_value]
    
    def get_has_infertility(self)->bool:
        return self.__has_infertility
    
    def set_has_infertility(self, 
            BOOL:bool):
        self.__has_infertility = BOOL

    # -------------------------------------
    # ITEMS 
    #

    def get_age_range_item(self):
        k = self.get_age_range_key()
        return CitizenData.age_range_depot\
            .get_age_range(k)

    def get_cultural_group_item(self)\
            ->CulturalGroupItem:
        KEY:str = self.get_culture_key()
        return CULTURE_GROUP_DEPOT\
                .get_item(KEY)


    # -----------------------------------