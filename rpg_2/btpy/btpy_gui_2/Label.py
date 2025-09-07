

from tkinter import ttk
import tkinter.font as tkFont

class Label:

    def __init__(self, widget, 
            TEXT:str):
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.widget = ttk.Label(
            widget, 
            text=TEXT,
            font = self.default_font
        )
        self.widget.config(
            background="white")
        
        
    def get_title(self):
        return self.widget.cget("text")

    def set_title(self, TEXT:str):
        self.widget.config(text = TEXT)
        
    def set_font_family(self, 
            FONT_FAMILY_KEY:str):
        self.default_font.config(
            size = FONT_FAMILY_KEY
        )
        self.widget.config(
            font=self.default_font
        )
        
    def set_font_size(self, SIZE):
        self.default_font.config(
            size = SIZE
        )
        self.widget.config(
            font=self.default_font
        )

    def grid(self, ROW, COLUMN, 
             STICKY = ""):
        self.widget.grid(
            row = ROW, column= COLUMN,
            sticky= STICKY,
            ipadx=5, ipady=5
        )

    def place(self, 
            LOCATION_X:int, 
            LOCATION_Y:int):
        self.widget.place(
            x=LOCATION_X,
            y=LOCATION_Y
        )
