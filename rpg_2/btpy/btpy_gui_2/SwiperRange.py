
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class SwiperRange:

    def __init__(self, widget, 
            TITLE:str):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid"
        )
        self.label_title = None
        self.__range_list = [0, 1]
        self.__value = 0
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        button_font = tkFont\
            .Font(
                family="Arial", 
                size=12,
                weight="bold"
            )
        self.label_counter = tk.Label(
            self.widget,
            font = self.default_font
        )
        self.button_forward = tk.Button(
            self.widget, 
            text = " > ",
            font =  button_font,
            borderwidth=1,
            relief="solid"
        )
        self.label_value = tk.Label(
            self.widget,
            font = self.default_font
        )
        self.button_back = tk.Button(
            self.widget, 
            text = " < ",
            font = button_font,
            borderwidth=1,
            relief="solid"
        )
        self.button_back.grid(
            row = 0,
            column= 1
        )
        self.label_value.grid(
            row = 0,
            column= 2
        )
        self.button_forward.grid(
            row = 0,
            column= 3
        )
        self.label_counter.grid(
            row = 0,
            column= 4
        )
        self.__init_label_title()
        self.__add_default_listener()
        self.set_title(TITLE)

    def set_content(self, 
            RANGE_LIST:list[str]):
        self.__range_list = RANGE_LIST
        self.__value = RANGE_LIST[0]
        self.__update()

    def get_value(self):
        return self.__value
    
    def set_value(self, NUMBER:int):
        if(NUMBER < self.__range_list[0]):
            self.__value = self\
                .__range_list[0]
        elif(NUMBER > self.__range_list[1]):
            self.__value = self\
                .__range_list[1]
        self.__value = NUMBER
        self.__update()

    def __update(self):
        text_ = f" {self.get_value()} "
        self.label_value.config(
            text = text_
        )
        max_ = self.__range_list[1]
        min_ = self.__range_list[0]
        text_ = f" {min_} / {max_} "
        self.label_counter.config(
            text = text_
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

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT
        )

    def get_title(self):
        return self.label_title\
            .cget("text")
    
    def __forward_element(self, e):
        max_ = self.__range_list[1]
        if(self.__value < max_):
            self.__value += 1
        self.__update()

    def __back_element(self, e):
        min_ = self.__range_list[0]
        if(self.__value > min_):
            self.__value -= 1
        self.__update()
    
    def __add_default_listener(self):
        self.button_forward.bind(
            "<Button-1>", 
            self.__forward_element
        )
        self.button_back.bind(
            "<Button-1>", 
            self.__back_element
        )

    def __init_label_title(self):
        self.label_title = tk.Label(
            self.widget,
            font = self.default_font 
        )
        self.label_title.grid(
            row=0, 
            column=0, 
            sticky="ew",
            ipadx=5,
            ipady=5
        )