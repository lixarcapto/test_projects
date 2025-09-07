

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

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
