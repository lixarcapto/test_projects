

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ....btpy_images.mod.blacken_rgb.blacken_rgb import*
from ....btpy_images.mod.lightens_rgb.lightens_rgb import*
from ....btpy_checkers.mod.is_RGB.is_RGB import*
from ....btpy_transformers.mod.hex_to_RGB.hex_to_RGB import*

class OnFocusWidget(WidgetStandard):
    
    """
    Este widget permite crear un widget
    de tipo button de forma mas 
    facil con los efectos ON_FOCUS.
    """

    def __init__(self, window):
        super().__init__(window)
        self.is_enabled:bool = True
        self.__callback = None
        self.__background_color = ""
        self.__background_color_2 = ""
        self.margin_color_1 = self.margin\
            .cget("bg")
        self.margin_color_2 = "yellow"

    def add_widget(self, widget):
        super().add_widget(widget)
        self.set_background_color(
            "#CFCFCF"
        )
        self.add_default_listener()
        
    def set_foreground_color(self, COLOR):
        color_tk = self\
            .convert_to_tk_color(COLOR)
        self.widget.config(fg = color_tk)

    def set_background_color(self, COLOR):
        self.__background_color = self\
            .convert_to_tk_color(COLOR)
        color_tk = self\
            .convert_to_tk_color(COLOR)
        self.create_background_color_2(
            COLOR
        )
        if(self.widget != None):
            self.widget.config(
                bg = color_tk)
        
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

    def add_default_listener(self):
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
        self.set_is_underline(False)

    def __react_enter_event(self, e):
        if(not self.is_enabled):
            return None
        self.set_margin_color(
            self.margin_color_2)
        self.widget.config(
            bg = self.__background_color_2
        )
        self.set_is_underline(True)

    def enable(self):
        self.is_enabled = True
        self.widget.config(
            state="normal")

    def disable(self):
        self.is_enabled = False
        self.widget.config(
            state="disabled")
        
    def add_listener(self,
            CALLBACK:callable)->None:
        self.__callback = CALLBACK
        def fn(e):
            if(self.__callback != None
            and self.is_enabled):
                self.__callback(e)
        self.widget.bind("<Button-1>", fn)