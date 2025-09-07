


from ..society.Society import Society
from .region_constant import*
from ..market.Market import Market
from btpy.Btpy import Btpy
from ..date_asp.DateAsp import DateAsp
from .WeatherDict import WeatherDict
from ..territory.Territory import Territory
from ..postcard.Postcard import Postcard

class Region:

    init_citizens = 10
    market = Market()
    date_asp = DateAsp()
    weather_dict = WeatherDict()

    def __init__(self, NUMBER:int, 
            INDEX_X:int, INDEX_Y:int):
        self.name:str = ""
        self.territory = Territory()
        self.unique_number:int = NUMBER
        self.i_point:list[int] \
            = [INDEX_X, INDEX_Y]
        self.society:Society = None
        self.is_populated:bool = False
        self.relief_number:int = 0
        self.culture_key:str = ""
        self.is_selected:bool = False
        self.soil_type_index:int = 0
        self.__terrain_type_number:int = 0
        self.latitudinal_zone = 0
        self.actual_temperature_n:int = 0
        self.actual_wind_number:int = 0
        self.actual_humidity_number:int = 0
        self.weather_event_number:int = 0
        self.weather_event_key:str = ""

    def get_postcard(self)->Postcard:
        pcd = Postcard()
        pcd.relief_key = self\
            .get_relief_key()
        pcd.terrain_type_key = self\
            .get_terrain_type_key()
        pcd.weather_event_key = self\
            .weather_event_key
        return pcd

    def get_actual_temperature_key(self)\
            ->str:
        return TEMPERATURE_KEY_TUPLE\
            [self.actual_temperature_n]
    
    def set_actual_temperature_key(self,
            KEY:str)->None:
        idx = TEMPERATURE_KEY_TUPLE.index(
            KEY)
        self.actual_temperature_n = idx
    
    def get_actual_wind_key(self)->str:
        return WIND_SPEED_KEY_TUPLE\
            [self.actual_wind_number]
    
    def set_actual_wind_key(self, KEY:str)\
            ->None:
        idx = WIND_SPEED_KEY_TUPLE.index(KEY)
        self.actual_wind_number = idx
    
    def get_actual_humidity_key(self)->str:
        return HUMIDITY_KEY_TUPLE\
            [self.actual_humidity_number]
    
    def set_actual_humidity_key(self, 
                KEY:str)->None:
        idx = HUMIDITY_KEY_TUPLE.index(KEY)
        self.actual_humidity_number = idx

    def get_soil_type_key(self)->str:
        return SOIL_TYPE_TUPLE\
            [self.soil_type_index]
    
    def set_soil_type_key(self, KEY:str)\
            ->None:
        idx = self.soil_type_index
        return SOIL_TYPE_TUPLE[idx]
    
    def set_terrain_type_key(self, KEY:str):
        idx = TERRAIN_TYPE_TUPLE.index(KEY)
        self.__terrain_type_number = idx

    def get_terrain_type_key(self)->str:
        idx = self.__terrain_type_number
        return TERRAIN_TYPE_TUPLE[idx]
    
    def generate_weather(self)->None:
        weather_k:str = Region.weather_dict\
            .choose_random_weather(
                self.get_actual_temperature_key(),
                self.get_actual_wind_key(),
                self.get_actual_humidity_key()
            )
        self.weather_event_key = weather_k

    def randomize(self):
        self.soil_type_key = Btpy\
            .random_choice(list(SOIL_TYPE_TUPLE))
        self.relief_number = Btpy\
            .rand_range([
                0, len(RELIEF_KEY_TUPLE) -1
            ])
        terrain_k = Btpy.random_choice(
            list(TERRAIN_TYPE_TUPLE)
        )
        self.set_terrain_type_key(
            terrain_k)

    def get_relief_key(self)->str:
        return RELIEF_KEY_TUPLE\
            [self.relief_number]
    
    def set_relief_key(self, 
            RELIEF_KEY:str)->None:
        self.relief_number \
            = RELIEF_KEY_TUPLE.index(
                RELIEF_KEY)

    def get_citizen_id_list(self)\
            ->list[int]:
        if(self.is_populated):
            return self.society\
                .get_citizen_id_list()
        else:
            return []

    def is_pay_day(self)->bool:
        """
        Funcion que verifica si es 
        el dia de pago; este es el 
        ultimo dia del mes en tiempo
        del simulador.
        """
        is_pay_day = False
        day = Region.date_asp\
            .get_day_code()
        last_day = Region.date_asp\
            .get_days_by_month()
        if(day == last_day -1):
            return True
        return False

    def advance_one_month(self):
        self.generate_weather()
        is_pay_day = self.is_pay_day()
        Region.market = self.territory\
            .produce_resources(
                Region.market
            )
        postcard = self.get_postcard()
        if(self.is_populated):
            Region.market = self.society\
                .advance_one_day(
                    Region.market, 
                    is_pay_day,
                    postcard
                )
            if(is_pay_day):
                Region.market\
                    .advance_one_day()
        Region.date_asp.advance_one_day()

    def write(self):
        txt = ""
        txt += f"{self.unique_number=}\n"
        txt += f"{self.i_point=}\n"
        txt += f"{self.latitudinal_zone=}\n"
        txt += f"{self.get_humidity_key()=}\n"
        txt += f"{self.get_wind_speed_key()=}\n"
        txt += f"{self.get_relief_key()=}\n"
        txt += f"{self.get_temperature_key()=}\n"
        if(self.is_populated):
            txt += self.society.write()
        return txt
    
    def populate(self, CULTURE_KEY:str):
        self.is_populated = True
        self.culture_key = CULTURE_KEY
        postcard = self.get_postcard()
        self.society = Society()
        # region point debe ser 
        # antes de populate society
        self.society.set_region_point(
            self.i_point
        )
        self.society.populate_society(
            Region.init_citizens,
            CULTURE_KEY,
            postcard
        )

    def render_territory(self)->list:
        return self.territory\
            .render_structures()

    def render_square_layout(self)\
            ->list[str]:
        """
        Funcion que renderiza la
        region como una cuadricula
        de un mapa cuadriculado.
        """
        list_ = []
        key:str = ""
        key = "terrain_type_" + self\
            .get_terrain_type_key()
        list_.append(key)
        key = "relief_" + self\
            .get_relief_key()
        list_.append(key)
        if(self.is_populated):
            k = "town"
            list_.append(k)
        return list_

    def render_layout_list(self)->list[str]:
        list_ = []
        key = "sky_" \
            + Region.date_asp\
                .get_month_name()
        list_.append(key)
        key = "weather_"\
            + self.weather_event_key
        list_.append(key)
        key = "relief_" \
            + self.get_relief_key()\
            + "_" + self.soil_type_key
        list_.append(key)
        return list_