


import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..frame.Frame import Frame
import tkinter.font as font

class LabelLabel(WidgetStandard):

    def __init__(self, window, title = ""):
        super().__init__()
        self.widget = None
        self.label_title = None
        self.label_text = None
        self.__init_components(window)
        self.set_title(title)

    def get_title(self)->str:
        return self.label_title.cget(
            "text")

    def set_title(self, TEXT:str)->None:
        self.label_title.config(
            text = TEXT)

    def set_text(self, TEXT:str):
        self.label_text.config(text = TEXT)

    def get_text(self)->str:
        return self.label_text.cget(
            "text")
    
    def __init_components(self, window):
        self.widget = Frame(
            window
        )
        self.widget.set_border(1)
        self.label_title = tk.Label(
            self.widget.widget)
        self.label_text = tk.Label(
            self.widget.widget,
            bg = "white")
        # draw components
        self.label_title.grid(
            row=0, 
            column=0, 
            sticky="w"
        )  
        # Alinea a la izquierda
        self.label_text.grid(
            row=0, 
            column=1, 
            sticky="e"
        )  
        # Alinea a la derecha