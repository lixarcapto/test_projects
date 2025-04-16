

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from tkinter import font

class WidgetComposite(WidgetStandard):

    def __init__(self, widget, 
            is_horizontal:bool = False):
        super().__init__(widget)
        self.key = ""
        self.label_title = tk.Label(
            self.margin,
            borderwidth = 1,
            relief = "solid"
        )
        self.label_title.config(
            bg = "white")
        self.widget = tk.Frame(
            self.margin
        )
        self.widget.config(bg = "yellow")
        self.title_is_displayed:bool = False
        self.is_horizontal = is_horizontal
        if(is_horizontal):
            self.set_in_horizontal()
        else:
            self.set_in_vertical()
        super().set_background_color("#EEEEEE")
        self.label_title.config(
            bg = "#EEEEEE")
        font_ = font.Font(
            family="Arial", 
            size=12
        )
        self.label_title.config(
            font = font_)
        self.set_title_background("#BABABA")
        
    def hide_title(self):
        self.label_title.grid_forget()
    
    def show_title(self):
        if(self.is_horizontal):
            self.label_title.grid(
                row = 0, column= 0, 
                sticky="nsew",
                padx=(2, 0), pady=(2, 1)
            )
        else:
            self.label_title.grid(
                row = 0, column= 0, 
                sticky="nsew",
                padx=(2, 1), pady=(2, 0)
            )

    def set_in_horizontal(self):
        self.widget.grid(
            row = 0, column= 1, 
            sticky="nsew",
            padx=1, pady=(1, 1)
        )

    def get_font(self)->font.Font:
        self.label_title.cget("font")

    def set_in_vertical(self):
        self.widget.grid(
            row = 1, column= 0, 
            sticky="nsew",
            padx=1, pady=(0, 1)
        )

    def set_background_color(self, COLOR):
        super().set_background_color(COLOR)
        self.label_title.config(bg = COLOR)
    
    def set_foreground_color(self, COLOR):
        self.label_title.config(fg = COLOR)

    def set_title_foreground(self, COLOR):
        self.label_title.config(fg = COLOR)

    def set_title_background(self, COLOR):
        self.label_title.config(bg = COLOR)

    def set_title(self, TEXT:str):
        self.key = TEXT
        self.label_title.config(
            text = TEXT)
        if(not self.title_is_displayed
        and TEXT != ""):
            self.title_is_displayed = True
            self.show_title()
        if(TEXT == ""
        and self.title_is_displayed):
            self.title_is_displayed = False
            self.hide_title()
        
        self.label_title.config(
            text = "  " + TEXT + "  ")
        
    def get_title(self):
        return self.key