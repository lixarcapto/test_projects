
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class SwiperText:

    def __init__(self, widget, 
            TITLE:str):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid"
        )
        self.label_title = None
        self.__text_list = []
        self.__idx = 0
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
        self.button_forward.grid(
            row = 0,
            column= 2
        )
        self.label_value.grid(
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
            TEXT_LIST:list[str]):
        self.__text_list = TEXT_LIST
        self.__idx = 0
        self.__update()

    def get_value(self):
        return self.__text_list\
            [self.__idx]
    
    def set_value(self, TEXT:str):
        idx = self.__text_list.index(
            TEXT)
        self.__idx = idx
        self.__update()

    def __update(self):
        text_ = f" {self.get_value()} "
        self.label_value.config(
            text = text_
        )
        max_ = len(self.__text_list) -1
        text_ = f" {self.__idx} / {max_} "
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
        leng = len(self.__text_list)
        if(self.__idx < leng -1):
            self.__idx += 1
        self.__update()

    def __back_element(self, e):
        if(self.__idx > 0):
            self.__idx -= 1
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