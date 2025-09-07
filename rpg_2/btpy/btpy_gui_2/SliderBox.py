

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class SliderBox:

    def __init__(self, widget, TITLE:str):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid" 
        )
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.frame = tk.Frame(
            self.widget
        )
        self.frame.grid(
            column= 0,
            row = 1
        )
        self.__key_list:list = []
        self.__text_list:list = []
        self.slider_list:list = []
        self.label_title = None
        self.__init_label_title()
        self.set_title(TITLE)

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT
        )

    def get_title(self):
        return self.label_title\
            .cget("text")

    def __init_label_title(self):
        self.label_title = tk.Label(
            self.widget,
            anchor="w",
            font = self.default_font
        )
        self.label_title.grid(
            row=0, 
            column=0, 
            sticky="ew",
            ipadx=5,
            ipady=5
        )

    def set_value(self, DICT:dict):
        idx = 0
        for slider in self.slider_list:
            slider.set_min()
        for k in DICT:
            idx = self.__get_index(k)
            self.slider_list[idx]\
                .set_value(DICT[k])
            
    def get_value(self)->dict:
        dict_ = {}
        leng = len(self.slider_list)
        k = ""
        value = 0
        for i in range(leng):
            k = self.__key_list[i]
            value = self.slider_list[i]\
                .get_value()
            dict_[k] = value
        return dict_

    def __get_index(self, KEY:str):
        return self.__key_list.index(KEY)

    def set_range_for_all(self,             
            RANGE_LIST:list[int]):
        for slider in self.slider_list:
            slider.set_range_list(
                RANGE_LIST
            )

    def set_value_for_all(self, 
                VALUE:int):
        for slider in self.slider_list:
            slider.set_value(VALUE)

    def set_components(self, 
            KEY_LIST:list[str]):
        self.__clean_slider_list()
        self.__key_list = KEY_LIST
        self.__text_list = KEY_LIST
        slider = None
        for k in KEY_LIST:
            slider = InputSlider(
                self.frame, k
            )
            self.slider_list.append(
                slider
            )
        self.set_columns(1)

    def __clean_slider_list(self):
        for i in range(len(self.slider_list)):
            self.slider_list[i]\
                .widget.grid_forget()
        self.slider_list = []

    def add_change_listener(self,
            CALLBACK_ARGS_X0:any):
        for slider in self.slider_list:
            slider.add_change_listener(
                CALLBACK_ARGS_X0
            )

    def set_content(self, 
            TEXT_LIST:list[str]):
        self.__text_list = TEXT_LIST
        i = 0
        for slider in self.slider_list:
            slider.set_title(
                self.__text_list[i]
            )
            i += 1

    def set_columns(self, COLUMNS):
        leng = len(self.slider_list)
        x = 0
        y = 0
        for i in range(leng):
            self.slider_list[i]\
                .widget.grid(
                    column = x,
                    row = y,
                    sticky = "ew"
                )
            x += 1
            if(x >= COLUMNS):
                x = 0
                y += 1

    def grid(self, ROW, COLUMN, 
             STICKY = ""):
        self.widget.grid(
            row = ROW, column= COLUMN,
            sticky= STICKY
        )

    def place(self, 
            LOCATION_X:int, 
            LOCATION_Y:int):
        self.widget.place(
            x=LOCATION_X,
            y=LOCATION_Y
        )
    

class InputSlider:

    def __init__(self, widget,
            TITLE:str = ""):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid" 
        )
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.slider = ttk.Scale(
            self.widget,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL
        )
        self.slider.grid(
            row=0, 
            column=2, 
            sticky="ew"
        )
        self.__range_list:list[int] = [0, 0]
        self.__init_label_title()
        self.__init_label_ranges()
        self.set_title(TITLE)
        self.set_range_list([0, 100])
        self.__callback = None
        def fn(e):
            self.__update()
        self.slider.config(
            command = fn
        )
        self.__add_default_listener()

    def __add_default_listener(self):
        def fn(e):
            self.__update()
            if(self.__callback != None):
                self.__callback()
        self.slider.config(
            command = fn
        )

    def set_range_list(self, 
            RANGE_LIST:list[int]):
        self.__range_list = RANGE_LIST
        self.slider.config(
            from_=RANGE_LIST[0],
            to=RANGE_LIST[1]
        )
        v = self.__range_list[0]
        
        self.set_value(v)
        self.__update()

    def get_range_list(self):
        return self.__range_list
    
    def __update(self):
        range_ = self.get_range_list()
        self.label_value.config(
            text = f" {self.get_value()} "
        )
        self.label_max.config(
            text = f" {range_[0]} / {range_[1]} "
        )

    def set_max(self):
        self.set_value(
            self.__range_list[1])
        
    def set_min(self):
        self.set_value(
            self.__range_list[0])

    def get_value(self)->int:
        return int(self.slider.get())

    def set_value(self, NUMBER:int):
        self.slider.set(NUMBER)
        self.__update()

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = f" {TEXT} "
        )

    def get_title(self):
        return self.label_title\
            .cget("text")
    
    def __init_label_ranges(self):
        self.label_value = tk.Label(
            self.widget,
            anchor="center",
            font = self.default_font
        )
        self.label_value.grid(
            row=0, 
            column=3, 
            sticky="ew",
            ipadx=5,
            ipady=5
        )
        self.label_max = tk.Label(
            self.widget,
            anchor="center",
            font = self.default_font
        )
        self.label_max.grid(
            row=0, 
            column=1, 
            sticky="ew",
            ipadx=5,
            ipady=5
        )

    def add_change_listener(self,
            CALLBACK_ARGS_X0:any):
        self.__callback = CALLBACK_ARGS_X0

    def __init_label_title(self):
        self.label_title = tk.Label(
            self.widget,
            anchor="w",
            font = self.default_font
        )
        self.label_title.grid(
            row=0, 
            column=0, 
            sticky="ew",
            ipadx=5,
            ipady=5
        )
        
    def grid(self, ROW, COLUMN, 
             STICKY = ""):
        self.widget.grid(
            row = ROW, column= COLUMN,
            sticky= STICKY
        )

    def place(self, 
            LOCATION_X:int, 
            LOCATION_Y:int):
        self.widget.place(
            x=LOCATION_X,
            y=LOCATION_Y
        )
