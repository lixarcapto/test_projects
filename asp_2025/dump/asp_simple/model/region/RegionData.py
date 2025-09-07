


from ..society.Society import Society
from ..market.Market import Market
from .region_const import*

class RegionData:

    """
    Clase que almacena los datos en RAM 
    de las regiones.
    """

    RELIEF_TUPLE = RELIEF_TUPLE
    SOIL_TYPE_TUPLE = SOIL_TYPE_TUPLE
    BIOME_TUPLE = BIOME_TUPLE
    TEMPERATURE_TUPLE = TEMPERATURE_TUPLE
    WIND_SPEED_TUPLE = WIND_SPEED_TUPLE
    HUMIDITY_TUPLE = HUMIDITY_TUPLE
    CLIME_TUPLE = CLIME_TUPLE

    def __init__(self):
        # IDENTITY -------------------------
        self.__point_index:list[int] = [0, 0]
        self.__number:int = 0
        self.__name:str = ""
        #
        # TRAITS ---------------------------
        self.__relief:int = 0
        self.__soil_type:int = 0
        self.__culture:str = "german"
        self.__biome:str = "forest"
        self.__property:str = ""
        #
        # STATES ----------------------------
        self.__temperature:int = 2
        self.__wind_speed:int = 2
        self.__humidity:int = 2
        self.__clime:str = "clean"
        self.__water_quality:int = 4
        self.__air_quality:int = 4
        self.__is_inhabited:bool = False
        #
        # OTHER ------------------------------
        self.market:Market = Market()
        self.society:Society = None

    # IDENTITY -----------------------------

    def get_point_index(self)->list[int]:
        return self.__point_index
    
    def set_point_index(self, 
            point_arr:list[int])->None:
        self.__point_index = point_arr

    def get_number(self)->int:
        return self.__number
    
    def set_number(self, NUMBER:int)->None:
        self.__number = NUMBER

    def set_name(self, NAME:str):
        self.__name = NAME

    def get_name(self)->str:
        return self.__name
    
    # -----------------------------------
    
    # TRAITS ---------------------------
    
    def get_relief(self)->int:
        return self.__relief
    
    def set_relief(self, RELIEF_KEY:int):
        self.__relief = RELIEF_KEY

    def get_relief_key(self)->str:
        return RELIEF_TUPLE[self.__relief]

    def get_soil_type(self)->int:
        return self.__soil_type
    
    def set_soil_type(self, 
            SOIL_TYPE_KEY:int):
        self.__soil_type = SOIL_TYPE_KEY

    def get_soil_type_key(self)->str:
        return SOIL_TYPE_TUPLE[
            self.__soil_type]

    def get_culture(self)->str:
        return self.__culture
    
    def set_culture(self, CULTURE_KEY:str):
        self.__culture = CULTURE_KEY

    def get_biome(self)->str:
        return self.__biome
    
    def set_biome(self, BIOME_KEY:str):
        self.__biome = BIOME_KEY 

    def get_owner_id(self):
        return self.__property
    
    def set_owner_id(self, ID:str):
        self.__property = ID 

    # ------------------------------------

    # STATES ----------------------------
        
    def get_temperature(self)->int:
        return self.__temperature
    
    def set_temperature(self, 
            TEMPERATURE:int)->None:
        self.__temperature = TEMPERATURE

    def get_wind_speed(self)->int:
        return self.__wind_speed
    
    def set_wind_speed(self, 
            WIND_SPEED:int):
        self.__wind_speed = WIND_SPEED

    def get_humidity(self)->int:
        return self.__humidity
    
    def set_humidity(self, HUMIDITY:int):
        self.__humidity = HUMIDITY

    def set_clime(self, CLIME_KEY:str):
        self.__clime = CLIME_KEY

    def get_clime(self)->str:
        return self.__clime
    
    def get_is_inhabited(self)->bool:
        return self.__is_inhabited
    
    def set_is_inhabited(self, BOOL:bool):
        self.__is_inhabited = BOOL

    def get_water_quality(self)->int:
        return self.__water_quality
    
    def set_water_quality(self, INT:int):
        self.__water_quality = INT

    def get_air_quality(self)->int:
        return self.__air_quality
    
    def set_air_quality(self, INT:int):
        self.__air_quality = INT
    
        

    