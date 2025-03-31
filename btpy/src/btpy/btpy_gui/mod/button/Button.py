

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class Button(WidgetStandard):

    """
    Este modulo crea un boton de texto
    que detecta eventos por click en su 
    area para ejecutar una funcion callback.
    """

    def __init__(self, window, text = ""):
        super().__init__()
        self.widget = tk.Button(
            window.widget, 
            text="Haz clic aquí"
        )
        self.set_title(text)

    def pack(self, MARGIN:int = 0):
        self.widget.pack(
            padx=MARGIN, pady=MARGIN
        )

    def unpack(self):
        self.widget.pack_forget()

    def set_title(self, TEXT:str):
        self.widget.config(text = TEXT)

    def get_title(self):
        return self.widget.cget("text")
        
    def add_listener(self,
            CALLBACK:callable)->None:
        self.widget.bind("<Button-1>", 
                CALLBACK)
        