
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

class ChipInputCombo:

    def __init__(self, widget):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid" 
        )
        self.__text_list:list[str] = []
        self.__key_list:list[str] = []
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.combobox = self.combobox = ttk.Combobox(
            self.widget,
            font = self.default_font
        )
        self.combobox.grid(
            row=0, column=0
        )
        self.button_add = tk.Button(
            self.widget,
            text = " Add ",
            font = self.default_font
        )
        self.button_add.grid(
            row=0, column=1
        )
        self.subframe = tk.Frame(
            self.widget
        )
        self.subframe.grid(
            row=1, column=0, sticky="nsew"
        )
        self.button_selected_dict = {}
        self.__add_default_listener()

    def get_value(self):
        return list(
                self.button_selected_dict\
                    .keys()
            )
    
    def set_value(self, KEY_LIST:list[str]):
        self.__destroy_all_buttons()
        for k in KEY_LIST:
            self\
                .__create_button_selected(k)

    def set_components(self, 
            KEY_LIST:list[str]):
        self.__text_list = KEY_LIST
        self.__key_list = KEY_LIST
        self.combobox.config(
            values = KEY_LIST)
        self.combobox.set(KEY_LIST[0])

    def set_content(self, 
            TEXT_LIST:list[str]):
        self.__text_list = TEXT_LIST
        self.combobox.config(
            values = TEXT_LIST
        )
        self.combobox.set(TEXT_LIST[0])

    def __create_button_selected(self,
            TEXT:str, KEY:str):
        if(KEY in self.button_selected_dict):
            return None
        button = tk.Button(
            self.subframe, 
            text = TEXT,
            font = self.default_font
        )
        button.pack(expand=True, fill="x")
        def fn():
            self.__destroy_button(KEY)
        button.config(command = fn)
        self.button_selected_dict[KEY]\
            = button
        
    def __destroy_all_buttons(self):
        for k in self.button_selected_dict:
            self.button_selected_dict[k]\
                .pack_forget()
        self.__create_button_selected = {}
        
    def __destroy_button(self, KEY):
        self.button_selected_dict[KEY]\
            .pack_forget()
        del(self.button_selected_dict[KEY])

    def __add_default_listener(self):
        def fn():
            v = self.combobox.get()
            k = self.__get_key(v)
            self.__create_button_selected(
                v, k
            )
        self.button_add.config(
            command=fn
        )

    def __get_key(self, TEXT:str):
        idx = self.__text_list.index(TEXT)
        return self.__key_list[idx]

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

    def pack(self, 
            IS_EXPANDABLE:bool = False,
            SIDE_KEY:str = "left"):
        """
        SIDE_KEY:
        * left
        * top
        * right
        * bottom
        """
        if(IS_EXPANDABLE):
            self.widget.pack(
                fill=tk.BOTH, 
                expand=True,
                side = SIDE_KEY
            )
        else:
            self.widget.pack(
                side = SIDE_KEY
            )