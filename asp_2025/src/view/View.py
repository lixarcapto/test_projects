


from btpy.Btpy import Btpy
from model.Model import Model
from .TabCitizen import TabCitizen
from .TabRegion import TabRegion
from .TabMain import TabMain
from .TabMarket import TabMarket
from .TabConfig import TabConfig
from .TabTerritory import TabTerritory
import os

class View:

    def __init__(self):
        self.res_path:str = "./res/"
        self.model = Model()
        self.window_nav = Btpy.WindowNav(
            "tabs"
        )
        self.window_nav.set_size(
            1200, 700)
        def fn():
            k = self.window_nav\
                .get_actual_key_frame()
            self.window_nav.frame_dict[k]\
                .update()
        self.window_nav\
            .set_on_change_callback(
                fn
            )
        self.tab_citizen = TabCitizen(
                self.window_nav.widget)
        self.tab_citizen.model = self.model
        self.window_nav.add_frame(
            "citizen", self.tab_citizen
        )
        self.tab_region = TabRegion(
                self.window_nav.widget)
        self.tab_region.model = self.model
        self.window_nav.add_frame(
            "region", self.tab_region
        )
        self.tab_main = TabMain(
            self.window_nav.widget
        )
        self.tab_main.model = self.model
        self.window_nav.add_frame(
            "main", self.tab_main
        )
        self.tab_market = TabMarket(
            self.window_nav.widget
        )
        self.tab_market.model = self.model
        self.window_nav.add_frame(
            "market", self.tab_market
        )
        self.tab_config = TabConfig(
            self.window_nav.widget
        )
        self.tab_config.model = self.model
        self.window_nav.add_frame(
            "config", self.tab_config
        )
        self.tab_territory = TabTerritory(
            self.window_nav.widget
        )
        self.tab_territory.model = self.model
        self.window_nav.add_frame(
            "territory", self.tab_territory
        )
        self.window_nav.select_frame(
            "main")
        self.set_texture_pack(
            "default"
        )
        
    def set_texture_pack(self, PATH:str):
        path = "texture_pack/" + PATH + "/"
        self.tab_region.texture_pack\
            = path
        self.tab_citizen.texture_pack\
            = path
        self.tab_region.texture_pack\
            = path
        self.tab_market.texture_pack\
            = path

    def start(self):
        self.window_nav.start()