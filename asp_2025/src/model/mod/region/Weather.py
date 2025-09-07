

from btpy.Btpy import Btpy

class Weather:

    def __init__(self):
        self.temperature_k_list\
            :list[str] = []
        self.wind_speed_k_list\
            :list[str] = []
        self.humidity_k_list\
            :list[str] = []
        
    def have_keys(self, 
            TEMPERATURE_K:str,
            WIND_SPEED_K:str,
            HUMIDITY_K:str)->bool:
        check_list:list[bool] = []
        check_list.append(TEMPERATURE_K\
            in self.temperature_k_list)
        check_list.append(WIND_SPEED_K\
            in self.wind_speed_k_list)
        check_list.append(HUMIDITY_K\
            in self.humidity_k_list)
        return Btpy.has_all(
            check_list, 
            lambda e:e==True
        )
        
        