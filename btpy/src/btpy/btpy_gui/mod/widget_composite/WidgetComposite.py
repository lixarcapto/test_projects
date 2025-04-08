

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class WidgetComposite(WidgetStandard):

    def __init__(self, widget):
        super().__init__(widget)
        self.label_title = tk.Label(
            self.margin
        )
        self.label_title.config(
            bg = "white")
        self.label_title.grid(
            row = 0, column= 0, sticky="ew",
            padx=(2, 1), pady=(2, 0)
        )
        self.widget = tk.Frame(
            self.margin,
            borderwidth = 0.5,
            relief = "solid"
        )
        self.widget.config(bg = "yellow")
        self.widget.grid(
            row = 1, column= 0, sticky="ew",
            padx=(2, 1), pady=(0, 1)
        )

    def set_background_color(self, COLOR):
        super().set_background_color(COLOR)
        self.label_title.config(bg = COLOR)
    
    def set_foreground_color(self, COLOR):
        self.label_title.config(fg = COLOR)

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT)
        
    def get_title(self):
        return self.label_title.cget("text")