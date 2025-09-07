

from tkinter import ttk
import tkinter.font as tkFont
import tkinter as tk

class Button:

    def __init__(self, widget, 
            TEXT = ""):
        self.widget = ttk.Button(
            widget, 
            text=TEXT,
            style="TButton"
        )
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.default_style = ttk.Style()
        self.default_style.configure(
            "TButton", 
            font=self.default_font
        )
        
    def set_font_family(self, 
            FONT_FAMILY_KEY:str):
        self.default_font.config(
            size = FONT_FAMILY_KEY
        )
        self.default_style.configure(
            "TButton", 
            font=self.default_font
        )

    def set_font_size(self, SIZE):
        estilo = ttk.Style()
        self.default_font.config(
            size = SIZE
        )
        self.default_style.configure(
            "TButton", 
            font=self.default_font
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

    def add_listener(self, 
            CALLBACK_ARGS_X1)\
            ->None:
        self.widget.config(
            command = CALLBACK_ARGS_X1
        )

    def set_title(self, TEXT):
        self.widget.config(text = TEXT)

    def get_title(self):
        return self.widget.cget("text")
