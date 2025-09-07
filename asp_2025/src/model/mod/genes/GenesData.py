

from persistence.Persistence import Persistence
from .genes_constant import*
from ..regional_group_depot.RegionalGroupDepot import RegionalGroupDepot

class GenesData:

    """
    Clase que sirve para almacenar los 
    datos relacionados con la genetica 
    de los personajes.
    """

    GENETIC_KEYS_DICT:dict = Persistence\
        .read_genetic_keys_dict()
    regional_group_depot\
        = RegionalGroupDepot()

    def __init__(self):
        self.regional_group_key:str \
            = "northern_european"
        self.__regional_group_number\
            :int = 0
        self.__eye_color_number:int = 0
        self.__skin_color_number:int = 0
        self.__eye_type_number:int = 0
        self.__height_maximum:int = 2
        self.__hair_color_number:int = 0
        self.__hair_type_number:int = 0
        self.__nose_type:int = 0
        self.__mouth_type_number:int = 0
        # BOOLEANS TRAITS
        self.__is_bald:bool = False
        self.__is_freckled:bool = False
        self.__is_albino:bool = False
        self.__has_infertility:bool = False

    def set_regional_group_key(self, 
            KEY:str)->None:
        list_ = GenesData\
            .regional_group_depot\
                .get_keys()
        idx = list_\
            .index(KEY)
        self.__regional_group_number = idx

    def get_regional_group_key(self):
        list_ = GenesData\
            .regional_group_depot\
                .get_keys()
        idx = self.regional_group_key
        return list_[idx]
    
    def get_regional_group_number(self)\
            ->int:
        return self.__regional_group_number

    def get_is_freckled(self)->bool:
        return self.__is_freckled

    def set_is_freckled(self, BOOL:bool):
        self.__is_freckled = BOOL

    def get_is_bald(self)->bool:
        return self.__is_bald
    
    def set_is_bald(self, BOOL:bool):
        self.__is_bald = BOOL

    def get_is_albino(self)->bool:
        return self.__is_albino
    
    def set_is_albino(self, BOOL:bool):
        self.__is_albino = BOOL

    def set_regional_group_key(self, 
                KEY:str):
        self.regional_group_key = KEY

    def get_regional_group_key(self)->int:
        return self.regional_group_key

    def set_eye_color_number(self, 
            NUMBER:int):
        self.__eye_color_number = NUMBER

    def get_eye_color_number(self)->int:
        return self.__eye_color_number
    
    def set_eye_color_key(self, KEY:str):
        n = EYE_COLOR_K_TUPLE.index(KEY)
        self.__eye_color_number = n

    def set_eye_type_number(self, 
            NUMBER:int):
        self.__eye_type_number = NUMBER

    def get_eye_type_number(self)->int:
        return self.__eye_type_number
    
    def set_eye_type_key(self, KEY:str):
        n = EYE_TYPE_K_TUPLE.index(KEY)
        self.__eye_type_number = n
    
    def set_skin_color_number(self, 
            NUMBER:int):
        self.__skin_color_number = NUMBER

    def get_skin_color_number(self)->int:
        return self.__skin_color_number
    
    def set_skin_color_key(self, KEY:str):
        n = SKIN_COLOR_K_TUPLE.index(KEY)
        self.__skin_color_number = n
    
    def get_height_maximum_number(self)\
            ->int:
        return self.__height_maximum
    
    def set_height_maximum_number(self, 
            NUMBER:int):
        self.__height_maximum = NUMBER

    def set_height_maximum_key(self, 
            KEY:str):
        n = HEIGHT_MAX_KEY_TUPLE.index(KEY)
        self.__height_maximum = n
    
    def set_hair_color_number(self, 
            NUMBER:int):
        self.__hair_color_number = NUMBER

    def get_hair_color_number(self)->int:
        return self.__hair_color_number
    
    def set_hair_color_key(self, KEY:str):
        n = HAIR_COLOR_K_TUPLE.index(KEY)
        self.__hair_color_number = n
    
    def set_hair_type_number(self, 
            NUMBER:int):
        self.__hair_type_number = NUMBER

    def get_hair_type_number(self)->int:
        return self.__hair_type_number
    
    def set_hair_type_key(self, KEY:str):
        n = HAIR_TYPE_K_TUPLE.index(KEY)
        self.__hair_type_number = n

    def get_nose_type_number(self)->int:
        return self.__nose_type
    
    def set_nose_type_number(self, 
            NUMBER:int):
        self.__nose_type = NUMBER
    
    def set_nose_type_key(self, KEY:str):
        n = NOSE_TYPE_KEY_TUPLE.index(KEY)
        self.__nose_type = n

    def get_regional_group_list(self)->list:
        return GenesData\
            .regional_group_depot.get_keys()
    
    def get_mouth_type_number(self)->int:
        return self.__mouth_type_number
    
    def set_mouth_type_number(self, 
            NUMBER:int):
        self.__mouth_type_number = NUMBER

    def set_mouth_type_key(self, KEY:str):
        idx = MOUTH_TYPE_KEY_TUPLE\
            .index(KEY)
        self.__mouth_type_number = idx

    def get_has_infertility(self)->bool:
        return self.__has_infertility

    def set_has_infertility(self, 
            BOOL:bool):
        self.__has_infertility = BOOL
        
