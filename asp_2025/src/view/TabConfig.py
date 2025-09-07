

from btpy.Btpy import Btpy
import os

class TabConfig(Btpy.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.model = None
        self.button_save = Btpy.Button(
            self.widget, " save "
        )
        self.button_save.pack()
        self.swiper_initial_towns\
            = Btpy.SwiperRange(
                self.widget, 
                "Towns", 
                [1, 5]
            )
        self.swiper_initial_towns.pack()
        self.swiper_height_zone\
            = Btpy.SwiperRange(
                self.widget, 
                "Zone height", 
                [1, 3]
            )
        self.swiper_height_zone.pack()
        def fn(e):
            dict_ = {}
            n = self.swiper_initial_towns\
                .get_value()
            dict_["INITIAL_TOWNS"] = n
            n = self.swiper_height_zone\
                .get_value()
            dict_["HEIGHT_ZONES"] = n
            self.model.set_config_dict(
                dict_
            )
        self.button_save.add_listener(fn)

    def update(self):
        dict_ = self.model\
            .get_config_data_dict()
        v = dict_["RANGE_HEIGHT_ZONES"]
        self.swiper_height_zone\
            .set_content(v)
        v = dict_["RANGE_INITIAL_TOWNS"]
        self.swiper_initial_towns\
            .set_content(v)