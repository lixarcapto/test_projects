

from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

class ComboBox:

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
        self.__key_list:list[str] = []
        self.__text_list:list[str] = []
        self.combobox = ttk.Combobox(
            self.widget,
            font = self.default_font
        )
        self.combobox.grid(
            row=0, column=1, 
            sticky="nsew",
            padx=1, pady=(2, 1)
        )
        self.__init_label_title()
        self.set_title(TITLE)

    def add_change_listener(self,
            CALLBACK_ARGS_0:any):
        self.combobox.bind(
            "<<ComboboxSelected>>", 
            lambda e:CALLBACK_ARGS_0()
        )

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

    def set_size(self, CHAR_SIZE:int)\
            ->None:
        self.combobox.config(
            width=CHAR_SIZE)
        
    def set_components(self, 
            KEY_LIST:list[str]):
        self.__key_list = KEY_LIST
        self.set_content(KEY_LIST)
        
    def set_content(self, 
            TEXT_LIST:list[str])->None:
        self.__text_list = TEXT_LIST
        self.combobox.config(
            values = TEXT_LIST)
        self.set_value(
            self.__key_list[0]
        )

    def get_value(self)->str:
        text = self.combobox.get()
        idx = self.__text_list.index(text)
        return self.__key_list[idx]
    
    def set_value(self, TEXT:str)\
            ->None:
        idx = self.__key_list.index(TEXT)
        text = self.__text_list[idx]
        self.combobox.set(text)