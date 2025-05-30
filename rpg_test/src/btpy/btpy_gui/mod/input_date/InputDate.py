

import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame
from ....btpy_gui.mod.combobox.Combobox import Combobox
from tkinter import ttk
from ....btpy_utilitys.mod.date.Date import Date
from ....btpy_gui.mod.text_field.TextField import TextField

class InputDate(WidgetComposite):

    def __init__(self, window, title:str):
        super().__init__(window)
        self.date = None
        self.combobox_day = None
        self.combobox_month = None
        self.combobox_year = None
        self.__init_components()
        self.update_months()
        self.set_title(title)
        self.__add_default_listener()

    def get_value(self):
        return self.date
    
    def set_value(self, DATE):
        self.date = DATE

    def __add_default_listener(self):
        self.__add_save_day_listener()
        self.__add_save_month_listener()
        self.__add_save_year_listener()

    def __add_save_day_listener(self):
        def fn(e):
            day = self.combobox_day\
                .get_value()
            self.date.set_day(int(day))
        self.combobox_day\
            .add_change_listener(fn)
        
    def __add_save_month_listener(self):
        def fn(e):
            month = self.combobox_month\
                .get_value()
            number_month = self.date\
                .get_month_number(month)
            self.date.set_month(
                number_month)
        self.combobox_month\
            .add_change_listener(fn)
            
    def __add_save_year_listener(self):
        def fn(e):
            year = self.combobox_year\
                .get_value()
            self.date.set_year(int(year))
        self.combobox_year\
            .add_change_listener(fn)

    def __init_components(self):
        self.date = Date(1, 1, 2025)
        self.combobox_day = Combobox(
            self.widget, "day")
        self.combobox_day.set_size(3)
        self.combobox_month = Combobox(
            self.widget, "month")
        self.combobox_month.set_size(10)
        self.combobox_year = Combobox(
            self.widget, "year")
        self.combobox_year.set_size(5)
        # dibujar ------------------------
        self.combobox_day.margin.grid(
            row=0, column=0
        )
        self.combobox_month.margin.grid(
            row=0, column=1
        )
        self.combobox_year.margin.grid(
            row=0, column=2
        )

    def set_recomended_years(self, 
                YEARS_LIST:list[str]):
        self.combobox_year.set_values_list(
            YEARS_LIST
        )


    def update_months(self):
        days_list = []
        for i in range(1, 31):
            days_list.append(str(i))
        self.combobox_day.set_values_list(
            days_list)
        self.combobox_month.set_values_list(
            self.date\
                .get_months_names()
        )