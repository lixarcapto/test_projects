

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

    def unpack(self):
        self.widget.pack_forget()

    def set_title(self, TEXT:str):
        self.widget.config(text = TEXT)

    def get_title(self):
        return self.widget.cget("text")
        
    def add_listener(self, EVENT_KEY:str,
            CALLBACK:callable)->None:
        """
        * "RIGHT_CLICK"
        * "LEFT_CLICK"
        * "WHEEL_CLICK"
        * "MOUSE_OVER"
        * "MOUSE_LEAVE"
        """
        if(EVENT_KEY == "LEFT_CLICK"):
            self.widget.bind("<Button-1>", 
                lambda e:CALLBACK())
        elif(EVENT_KEY == "RIGHT_CLICK"):
            self.widget.bind("<Button-3>", 
                lambda e:CALLBACK())
        elif(EVENT_KEY == "WHEEL_CLICK"):
            self.widget.bind("<Button-2>", 
                lambda e:CALLBACK())
        elif(EVENT_KEY == "MOUSE_OVER"):
            self.widget.bind("<Enter>", 
                lambda e:CALLBACK())
        elif(EVENT_KEY == "MOUSE_LEAVE"):
            self.widget.bind("<Leave>", 
                lambda e:CALLBACK())
        