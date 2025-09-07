

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class TextField:

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
        self.__init_label_title()
        self.set_title(TITLE)
        self.entry = ttk.Entry(
            self.widget, 
            width=30,  # Define el ancho del campo en caracteres
            font = self.default_font
        )
        self.entry.grid(
            row=0, 
            column=1, 
            sticky="nsew"
        )

    def set_input_size(self, WIDTH:int):
        self.entry.config(width = WIDTH)

    def __init_label_title(self):
        self.label_title = tk.Label(
            self.widget,
            anchor="w",
            font = self.default_font,
            borderwidth=1,
            relief="solid" 
        )
        self.label_title.grid(
            row=0, 
            column=0, 
            sticky="nsew",
            ipadx=5,
            ipady=5
        )

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT
        )

    def get_title(self):
        return self.label_title\
            .cget("text")

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

    def get_value(self)->str:
        return self.entry.get()

    def set_value(self, TEXT:str):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, TEXT)

    def set_is_password(self):
        self.config(show="*")