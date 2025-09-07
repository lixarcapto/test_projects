

from .region_constant import*

class RegionData:

    def __init__(self):
        # ---------------------------------
        # REGION TRAITS 
        #
        self.__name_region:str = ""
        self.__unique_number:int = 0
        self.__i_point:list[int] = [0, 0]
        self.__relief_number:int = 0
        self.__culture_key:str = ""
        self.__is_selected:bool = False
        self.__soil_type_index:int = 0
        self.__terrain_type_number:int = 0
        self.__latitudinal_zone = 0
        # --------------------------------
        # STATES REGION
        #
        self.__actual_temperature_n:int = 0
        self.__actual_wind_number:int = 0
        self.__actual_humidity_number\
            :int = 0
        self.__weather_event_number:int = 0
        self.__weather_event_key:str = ""
        self.__is_populated:bool = False
        #
        # -------------------------------
        # OBJECTS 
        #
        self.territory = None
        self.society = None

    def get_name_region(self)->str:
        return self.__name_region
    
    def set_name_region(self, NAME:str):
        self.__name_region = NAME

    def set_unique_number(self, NUMBER:int):
        self.__unique_number = NUMBER

    def get_unique_number(self)->int:
        return self.__unique_number
    
    def set_point(self, 
            POINT_LIST:list[int]):
        self.__i_point = POINT_LIST

    def get_point(self)->list[int]:
        return self.__i_point
    
    def get_relief_key(self)->str:
        idx = self.__relief_number
        return RELIEF_KEY_TUPLE[idx]
    
    def set_relief_key(self, KEY:str):
        idx = RELIEF_KEY_TUPLE.index(KEY)
        self.__relief_number = idx

    def set_is_selected(self, BOOL:bool):
        self.__is_selected = BOOL

    def get_is_selected(self)->bool:
        return self.__is_selected
    
    def set_culture_key(self, KEY:str):
        self.__culture_key = KEY

    def get_culture_key(self)->str:
        return self.__culture_key
    
    def set_soil_type_key(self, KEY:str):
        idx = SOIL_TYPE_TUPLE.index(KEY)
        self.__soil_type_index = idx

    def get_soil_type_key(self)->str:
        idx = self.__soil_type_index
        return SOIL_TYPE_TUPLE[idx]

    def get_terrain_type_key(self)->str:
        idx = self.__terrain_type_number
        return TERRAIN_TYPE_TUPLE[idx]
    
    def set_terrain_type_key(self, 
            KEY:str)->None:
        idx = TERRAIN_TYPE_TUPLE.index(idx)
        self.__terrain_type_number = idx

    def set_latitudinal_zone(self, 
            NUMBER:int):
        return self.__latitudinal_zone
    
    def get_latitudinal_zone(self)->int:
        return self.__latitudinal_zone

    def set_actual_temperature_key(self, 
            KEY:str):
        idx = TEMPERATURE_KEY_TUPLE.index(
            KEY)
        self.__actual_temperature_n = idx

    def get_actual_temperature_key(self)\
            ->str:
        idx = self.__actual_temperature_n
        return TEMPERATURE_KEY_TUPLE[idx]
    
    def set_actual_wind_key(self, KEY:str):
        idx = WIND_SPEED_KEY_TUPLE\
            .index(KEY)
        self.__actual_wind_number = idx

    def get_actual_wind_key(self)->str:
        idx = self.__actual_wind_number
        return WIND_SPEED_KEY_TUPLE[idx]
    
    def get_actual_humidity_key(self)->str:
        idx = self.__actual_humidity_number
        return HUMIDITY_KEY_TUPLE[idx]
    
    def set_actual_humidity_key(self, 
            KEY:str)->None:
        idx = HUMIDITY_KEY_TUPLE.index(KEY)
        self.__actual_humidity_number = idx



    """
        # --------------------------------
        # STATES REGION
        #
        self.__weather_event_number:int = 0
        self.__weather_event_key:str = ""
        self.__is_populated:bool = False
        #
        # -------------------------------
        # OBJECTS 
        #
        self.territory = None
        self.society = None
    """