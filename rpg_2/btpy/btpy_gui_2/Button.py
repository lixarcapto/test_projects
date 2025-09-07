

from tkinter import ttk
import tkinter.font as tkFont

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
