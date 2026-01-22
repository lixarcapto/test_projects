
import tkinter as tk
from btpy.Btpy import Btpy
from Model import Model

class View:

    def __init__(self):
        self.window = Btpy.Window(
            "titulo")
        self.model = Model()
        self.top_bar_frame = tk.Frame(
            self.window.widget
        )
        self.top_bar_frame.grid(
            row = 0, column=0
        )
        self.right_bar_frame = tk.Frame(
            self.window.widget
        )
        self.right_bar_frame.grid(
            row = 1, column=3
        )
        self.button_frame = tk.Frame(
            self.window.widget
        )
        self.button_frame.grid(
            row = 1, column=3
        )
        self.label_money = Btpy.LabelLabel(
            self.top_bar_frame,
            "money"
        )
        self.label_money.pack(
            True, "right")
        self.label_happiness = Btpy.LabelLabel(
            self.top_bar_frame,
            "happiness"
        )
        self.label_happiness.pack(
            True, "right")
        self.init_right_bar_frame()
        self.button_advance = Btpy\
            .Button(self.right_bar_frame,
                "advance one year"
            )
        self.button_advance.pack(
            True, "top"
        )
        self.button_advance_x5 = Btpy\
            .Button(self.right_bar_frame,
                "advance 5 years"
            )
        self.button_advance_x5.pack(
            True, "top"
        )
        self.button_advance.add_listener(
            self.advance_one_year
        )
        self.button_advance_x5.add_listener(
            self.advance_5_years
        )
        self.subsidized_key_box = Btpy.CheckBox(
            self.right_bar_frame, 
            "subsidized"
        )
        self.subsidized_key_box.pack(
            True, "top"
        )
        self.swiper_visas = Btpy.SwiperRange(
            self.right_bar_frame,
            "annual visas"
        )
        self.swiper_visas.pack(
            True, "top"
        )
        self.swiper_visas.set_content(
            [0, 100]
        )
        def fn():
            v = self.swiper_visas\
                .get_value()
            self.model\
                .annual_entry_permits = v
        self.swiper_visas.add_change_listener(
            fn
        )
        self.subsidized_key_box.set_components(
            self.model.professions_list
        )
        def fn():
            list_ = self.subsidized_key_box\
                .get_value()
            self.model.subsidized_sector_list\
                = list_
        self.subsidized_key_box\
            .add_change_listener(fn)
        self.text_area = Btpy.TextArea(
            self.window.widget,
            "resources"
        )
        self.text_area.grid(
            1, 1
        )
        self.window.start()

    def init_right_bar_frame(self):
        self.left_bar_frame = tk.Frame(
            self.window.widget
        )
        self.left_bar_frame.grid(
            row = 1, column= 0
        )
        self.label_pop = Btpy.LabelLabel(
            self.left_bar_frame,
            "population"
        )
        self.label_pop.pack(
            True, "bottom")
        self.label_woman_pop = Btpy.LabelLabel(
            self.left_bar_frame,
            "females"
        )
        self.label_woman_pop.pack(
            True, "bottom")
        self.label_man_pop = Btpy.LabelLabel(
            self.left_bar_frame,
            "males"
        )
        self.label_man_pop.pack(
            True, "bottom")
        self.label_moms_pop = Btpy.LabelLabel(
            self.left_bar_frame,
            "moms"
        )
        self.label_moms_pop.pack(
            True, "bottom")
        self.label_childs_pop = Btpy.LabelLabel(
            self.left_bar_frame,
            "childs"
        )
        self.label_childs_pop.pack(
            True, "bottom")
        self.label_emigrants = Btpy.LabelLabel(
            self.left_bar_frame,
            "number of emigrants"
        )
        self.label_emigrants.pack(
            True, "bottom")
        self.label_total_deaths = Btpy.LabelLabel(
            self.left_bar_frame,
            "total deaths"
        )
        self.label_total_deaths.pack(
            True, "bottom")
        self.label_year_deaths = Btpy.LabelLabel(
            self.left_bar_frame,
            "year deaths"
        )
        self.label_year_deaths.pack(
            True, "bottom")
        self.label_starvation_deaths = Btpy.LabelLabel(
            self.left_bar_frame,
            "starvation deaths"
        )
        self.label_starvation_deaths.pack(
            True, "bottom")
        self.label_natural_deaths = Btpy.LabelLabel(
            self.left_bar_frame,
            "natural deaths"
        )
        self.label_natural_deaths.pack(
            True, "bottom")
        self.fatal_birth_deaths = Btpy.LabelLabel(
            self.left_bar_frame,
            "fatal birth"
        )
        self.fatal_birth_deaths.pack(
            True, "bottom")
        
    def update_values(self):
        self.label_pop.set_value(
            self.model.population
        )
        self.label_man_pop.set_value(
            self.model.man_population
        )
        self.label_woman_pop.set_value(
            self.model.woman_population
        )
        self.label_moms_pop.set_value(
            self.model.moms_population
        )
        self.label_childs_pop.set_value(
            self.model.childs_population
        )
        self.label_total_deaths.set_value(
            self.model.total_deaths
        )
        self.label_year_deaths.set_value(
            self.model.year_deaths
        )
        self.label_natural_deaths.set_value(
            self.model.natural_deaths
        )
        self.label_starvation_deaths.set_value(
            self.model.starvation_deaths
        )
        self.fatal_birth_deaths.set_value(
            self.model.fatal_birth_deaths
        )
        self.label_money.set_value(
            self.model.money
        )
        self.label_emigrants.set_value(
            self.model.number_emigrants
        )
        txt = self.model.write_resources_table()
        self.text_area.set_value(txt)
        self.label_happiness.set_value(
            f"{self.model.total_happiness} / {self.model.max_happiness}"
        )

    def advance_one_year(self):
        self.model.advance_one_year()
        self.update_values()

    def advance_5_years(self):
        for i in range(5):
            self.model.advance_one_year()
        self.update_values()
        
        
        