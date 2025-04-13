

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
        self.back_color_1 = "gray"
        self.back_color_2 = "yellow"
        self.widget.pack(
            padx=1, 
            pady=(2, 1)
        )
        self.add_default_listener()
        self.set_title(TITLE)

    def set_background_color(self, COLOR):
        return super()\
            .set_background_color(COLOR)
        self.back_color_1 = COLOR

    def set_focus_color(self, COLOR):
        self.back_color_2 = COLOR

    def add_default_listener(self):
        def enter_fn(e):
            self.set_margin_color(
                self.back_color_2)
        self.widget.bind("<Enter>", 
                enter_fn)
        def leave_fn(e):
            self.set_margin_color(
                self.back_color_1)
        self.widget.bind("<Leave>", 
                leave_fn)

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
        