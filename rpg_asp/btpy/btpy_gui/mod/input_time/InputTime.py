

import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..frame.Frame import Frame
from ..combobox.Combobox import Combobox
from tkinter import ttk
from ....btpy_utilitys.mod.time.Time import Time
from ..text_field.TextField import TextField
from ....btpy_utilitys.mod.time.Time import Time

class InputTime(WidgetComposite):

    def __init__(self, window, title:str):
        super().__init__(window, True)
        self.time = None
        self.combobox_hour = None
        self.combobox_minute = None
        self.combobox_second = None
        self.__init_components()
        self.__add_default_listener()
        self.update_options()
        self.set_title(title)

    def __init_components(self):
        self.time = Time(1, 1, 1)
        self.combobox_hour = Combobox(
            self.widget, "hour")
        self.combobox_hour.set_size(3)
        self.combobox_minute = Combobox(
            self.widget, "minute")
        self.combobox_minute.set_size(3)
        self.combobox_second = Combobox(
            self.widget, "second")
        self.combobox_second.set_size(3)
        # dibujar ------------------------
        self.combobox_hour.margin.grid(
            row=0, column=0
        )
        self.combobox_minute.margin.grid(
            row=0, column=1
        )
        self.combobox_second.margin.grid(
            row=0, column=2
        )

    def get_value(self):
        return self.time
    
    def set_value(self, DATE):
        self.time = DATE

    def __add_default_listener(self):
        self.__add_save_hour_listener()
        self.__add_save_minute_listener()
        self.__add_save_second_listener()

    def __add_save_hour_listener(self):
        def fn(e):
            hour = self.combobox_hour\
                .get_value()
            self.time.set_hour(int(hour))
        self.combobox_hour\
            .add_change_listener(fn)
        
    def __add_save_minute_listener(self):
        def fn(e):
            minute = self.combobox_minute\
                .get_value()
            self.time.set_minute(
                int(minute))
        self.combobox_minute\
            .add_change_listener(fn)
            
    def __add_save_second_listener(self):
        def fn(e):
            second = self.combobox_second\
                .get_value()
            self.time.set_second(
                int(second))
        self.combobox_second\
            .add_change_listener(fn)

    def set_recomended_years(self, 
                YEARS_LIST:list[str]):
        self.combobox_second.set_content(
            YEARS_LIST
        )


    def update_options(self):
        list_60_numbers = []
        for i in range(0, 60):
            list_60_numbers.append(str(i))
        self.combobox_minute.set_content(
            list_60_numbers)
        self.combobox_second.set_content(
            list_60_numbers)
        list_24_numbers = []
        for i in range(0, 24):
            list_24_numbers.append(str(i))
        self.combobox_hour.set_content(
            list_24_numbers)