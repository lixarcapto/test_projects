
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class BinarySlider:

    def __init__(self, widget):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid" 
        )
        self.__key_list = []
        self.__text_list = []
        self.label_option_1 = None
        self.label_option_2 = None
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.slider = ttk.Scale(
            self.widget,
            from_=0,
            to=2,
            orient=tk.HORIZONTAL
        )
        self.slider.set(1)
        self.slider.grid(
            row=0, 
            column=1, 
            sticky="ew"
        )
        self.__init_label_alternative()

    def get_value(self)->int:
        idx = self.slider.get()
        return self.__key_list[idx]

    def set_value(self, KEY:str):
        idx = self.__key_list.index(KEY)
        self.slider.set(idx)

    def set_component(self, 
            KEYS_LIST:list):
        self.__key_list = KEYS_LIST
        self.__text_list = KEYS_LIST
        self.set_content(KEYS_LIST)

    def set_content(self, TEXT_LIST):
        self.label_option_1.config(
            text = TEXT_LIST[0]
        )
        self.label_option_2.config(
            text = TEXT_LIST[1]
        )
    
    def __init_label_alternative(self):
        self.label_option_1 = tk.Label(
            self.widget,
            anchor="center",
            font = self.default_font
        )
        self.label_option_1.grid(
            row=0, 
            column=0, 
            sticky="ew",
            ipadx=5,
            ipady=5
        )
        self.label_option_2 = tk.Label(
            self.widget,
            anchor="center",
            font = self.default_font
        )
        self.label_option_2.grid(
            row=0, 
            column=2, 
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