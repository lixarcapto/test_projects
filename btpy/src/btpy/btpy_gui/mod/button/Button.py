

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ....btpy_images.mod.blacken_rgb.blacken_rgb import*
from ....btpy_images.mod.lightens_rgb.lightens_rgb import*
from ....btpy_checkers.mod.is_RGB.is_RGB import*
from ....btpy_transformers.mod.hex_to_RGB.hex_to_RGB import*

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
        self.__background_color = ""
        self.__background_color_2 = ""
        self.margin_color_1 = self.margin\
            .cget("bg")
        self.margin_color_2 = "yellow"
        self.widget.pack(
            padx=1, 
            pady=(2, 1),
            fill=tk.BOTH,
            expand=True
        )
        self.__add_default_listener()
        self.set_title(TITLE)
        self.set_background_color(
            [205, 205, 205]
        )

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
        self.__background_color = self\
            .convert_to_tk_color(COLOR)
        color_tk = self\
            .convert_to_tk_color(COLOR)
        self.widget.config(bg = color_tk)
        self.create_background_color_2(
            COLOR
        )
        
    def create_background_color_2(self,
            COLOR):
        color = COLOR
        if(not is_RGB(color)):
            color = hex_to_RGB(color)
        color = lightens_rgb(color, 0.5)
        tk_color = self\
            .convert_to_tk_color(color)
        self.__background_color_2 \
            = tk_color
        print(tk_color)

    def set_focus_color(self, COLOR):
        self.margin_color_2 = self\
            .convert_to_tk_color(COLOR)

    def get_focus_color(self):
        return self.margin_color_2

    def __add_default_listener(self):
        self.widget.bind("<Enter>", 
            self.__react_enter_event)
        self.widget.bind("<Leave>", 
            self.__react_leave_event)
        
    def __react_leave_event(self, e):
        self.set_margin_color(
            self.margin_color_1)
        self.widget.config(
            bg = self.__background_color
        )

    def __react_enter_event(self, e):
        if(not self.is_enabled):
            return None
        self.set_margin_color(
            self.margin_color_2)
        self.widget.config(
            bg = self.__background_color_2
        )

    def set_title(self, TITLE:str)->None:
        self.key = TITLE
        self.widget.config(text = TITLE)
        
    def get_title(self)->str:
        return self.key
        
    def add_listener(self,
            CALLBACK:callable)->None:
        self.__callback = CALLBACK
        def fn(e):
            if(self.__callback != None
            and self.is_enabled):
                self.__callback(e)
        self.widget.bind("<Button-1>", fn)
        