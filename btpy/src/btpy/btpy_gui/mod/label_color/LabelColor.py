

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..frame.Frame import Frame

class LabelColor(WidgetStandard):

    def __init__(self, window, title,
            color = ""):
        super().__init__()
        self.widget = Frame(
            window
        )
        self.widget.set_border(1)
        self.label_title = tk.Label(
            self.widget.widget
        )
        self.label_color = tk.Label(
            self.widget.widget
        )
        self.label_color.config(
            text = "     "
        )
        self.set_title(title)
        self.set_label_color(color)

    def pack(self, MARGIN:int = 0):
        self.widget.pack(MARGIN)
        self.label_title.grid(
            row = 0, column = 0,
            padx= 2, pady= 2
        )
        self.label_color.grid(
            row = 0, column = 1,
            padx= 2, pady= 2
        )

    def unpack(self):
        self.widget.unpack()
        self.label_title.grid_forget()
        self.label_color.grid_forget()
        
    def set_label_color(self, color):
        self.label_color.config(
            bg = color,
            borderwidth=1,
            relief = "solid"
        )

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT)
        
    def get_title(self)->str:
        return self.label_title.cget("text")
