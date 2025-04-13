


import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..frame.Frame import Frame
import tkinter.font as font

class LabelLabel(WidgetStandard):

    def __init__(self, window, title = ""):
        super().__init__(window)
        self.widget = tk.Label(
            self.margin,
            borderwidth = 1,
            relief = "solid"
        )
        self.widget.config(
            bg = "#EEEEEE"
        )
        self.label_content = tk.Label(
            self.margin,
            anchor= "e",
            borderwidth = 1,
            relief = "solid"
        )
        self.label_content.config(
            bg = "white"
        )
        self.margin.columnconfigure(
            1, weight=1)
        # Alinea a la izquierda
        self.widget.grid(
            row=0, column=0, sticky="ew"
        )
        self.label_content.grid(
            row=0, column=1, sticky="ew"
        )
        # Alinea a la derecha
        self.set_title(title)

    def set_title(self, TITLE:str)->None:
        self.widget.config(
            text = TITLE)
        
    def get_title(self)->str:
        return self.widget.cget(
            "text")

    def set_text(self, TEXT:str):
        self.label_content.config(
            text = TEXT)

    def get_text(self)->str:
        return self.label_content.cget(
            "text")