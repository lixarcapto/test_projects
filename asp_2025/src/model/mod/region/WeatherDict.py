

from .Weather import Weather
from btpy.Btpy import Btpy

class WeatherDict:

    def __init__(self):
        self.weather_dict\
            :dict[Weather] = {}
        self.__create_all_weathers()
        
    def choose_random_weather(self, 
            TEMPERATURE_K:str,
            WIND_SPEED_K:str,
            HUMIDITY_K:str):
        weather_k_list = []
        have_keys:bool = False
        for k in self.weather_dict:
            have_keys = self\
                .weather_dict[k].have_keys(
                    TEMPERATURE_K,
                    WIND_SPEED_K,
                    HUMIDITY_K
                )
            if(have_keys):
                weather_k_list.append(k)
        weather_k = Btpy.random_choice(
            weather_k_list)
        return weather_k
        
    def __create_all_weathers(self):
        self.__create_weather(
            "clear",
            [
            "frozen", 
            "cold", 
            "warm", 
            "hot", 
            "burning"
            ],
            [
            "stormy", 
            "fast", 
            "slow", 
            "windless"
            ],
            [
            "flooded", 
            "rainy", 
            "humid", 
            "dry", 
            "drought"
            ]
        )
        self.__create_weather(
            "cloudy",
            [
            "frozen", 
            "cold", 
            "warm", 
            "hot", 
            "burning"
            ],
            [
            "stormy", 
            "fast", 
            "slow", 
            "windless"
            ],
            [
            "flooded", 
            "rainy", 
            "humid", 
            "dry", 
            "drought"
            ]
        )
        self.__create_weather(
            "sky_gray",
            [
            "frozen", 
            "cold", 
            "warm", 
            "hot", 
            "burning"
            ],
            [
            "stormy", 
            "fast", 
            "slow", 
            "windless"
            ],
            [
            "flooded", 
            "rainy", 
            "humid", 
            "dry", 
            "drought"
            ]
        )

    def __create_weather(self, 
            KEY:str,
            TEMPERATURE_K_LIST:list[str],
            WIND_SPEED_K_LIST:list[str],
            HUMIDITY_K_LIST:list[str]):
        weather = Weather()
        weather.temperature_k_list\
            = TEMPERATURE_K_LIST
        weather.wind_speed_k_list\
            = WIND_SPEED_K_LIST
        weather.humidity_k_list\
            = HUMIDITY_K_LIST
        self.weather_dict[KEY] = weather