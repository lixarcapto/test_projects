

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class WidgetComposite(WidgetStandard):

    def __init__(self, widget, 
            is_horizontal:bool = False):
        super().__init__(widget)
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
        if(is_horizontal):
            self.set_in_horizontal()
        else:
            self.set_in_vertical()
        super().set_background_color("#EEEEEE")
        self.label_title.config(
            bg = "#EEEEEE")
        self.set_margin_color("gray")
        self.set_title_background("#EEEEEE")
        

    def set_in_horizontal(self):
        self.label_title.grid(
            row = 0, column= 0, 
            sticky="nsew",
            padx=(2, 0), pady=(2, 1)
        )
        self.widget.grid(
            row = 0, column= 1, 
            sticky="nsew",
            padx=(0, 1), pady=(2, 1)
        )

    def set_in_vertical(self):
        self.label_title.grid(
            row = 0, column= 0, sticky="nsew",
            padx=(2, 1), pady=(2, 0)
        )
        self.widget.grid(
            row = 1, column= 0, sticky="nsew",
            padx=(2, 1), pady=(0, 1)
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
        self.label_title.config(
            text = TEXT)
        
    def get_title(self):
        return self.label_title.cget("text")