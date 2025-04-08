

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class Button(WidgetStandard):

    """
    Este modulo crea un boton de texto
    que detecta eventos por click en su 
    area para ejecutar una funcion callback.
    """

    def __init__(self, window, 
            TITLE:str = ""):
        super().__init__(window)
        self.widget = tk.Button(
            self.margin, 
            text="Haz clic aquí"
        )
        self.widget.pack(
            padx=1, 
            pady=(2, 1)
        )
        self.set_title(TITLE)

    def set_title(self, TITLE:str)->None:
        self.widget.config(
            text = TITLE)
        
    def get_title(self)->str:
        return self.widget.cget(
            "text")
        
    def add_listener(self,
            CALLBACK:callable)->None:
        self.widget.bind("<Button-1>", 
                CALLBACK)
        