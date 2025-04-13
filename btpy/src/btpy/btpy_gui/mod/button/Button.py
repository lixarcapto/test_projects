

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
            self.margin
        )
        self.__callback = None
        self.is_enabled:bool = True
        self.back_color_1 = "gray"
        self.back_color_2 = "yellow"
        self.widget.pack(
            padx=1, 
            pady=(2, 1)
        )
        self.__add_default_listener()
        self.set_title(TITLE)

    def enable(self):
        self.is_enabled = True
        self.widget.config(
            state="normal")

    def disable(self):
        self.is_enabled = False
        self.widget.config(
            state="disabled")
        
    def set_foreground_color(self, COLOR):
        color_tk = self\
            .convert_to_tk_color(COLOR)
        self.widget.config(fg = color_tk)

    def set_background_color(self, COLOR):
        color_tk = self\
            .convert_to_tk_color(COLOR)
        self.widget.config(bg = color_tk)

    def set_focus_color(self, COLOR):
        self.back_color_2 = self\
            .convert_to_tk_color(COLOR)

    def get_focus_color(self):
        return self.back_color_2

    def __add_default_listener(self):
        def enter_fn(e):
            if(not self.is_enabled):
                return None
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
        self.__callback = CALLBACK
        def fn(e):
            if(self.__callback != None
            and self.is_enabled):
                self.__callback(e)
        self.widget.bind("<Button-1>", fn)
        