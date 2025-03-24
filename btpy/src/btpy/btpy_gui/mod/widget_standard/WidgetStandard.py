

import tkinter as tk
from PIL import Image, ImageTk

class WidgetStandard:

    def __init__(self):
        self.widget = None
        self.font_type:str = "Arial"
        self.font_size:int = 14
        self.font_style:str = ""

    def pack(self, MARGIN:int = 0):
        self.widget.pack(
            pady=MARGIN, padx=MARGIN)
    
    def unpack(self)-> None:
        self.widget.pack_forget()

    def get_font(self):
        return self.widget.cget("font")
    
    def set_font(self, type, size, style):
        self.font_type = type
        self.font_size = size
        self.font_style = style
        self.__update_font()

    def set_text(self, TEXT:str)->None:
        pass

    def get_text(self)-> str:
        pass

    def set_text_color(self, COLOR):
        self.widget.config(fg = COLOR)

    def get_text_color(self):
        return self.widget.cget("fg")

    def set_background_color(self, COLOR):
        self.widget.config(bg = COLOR)

    def get_background_color(self):
        return self.widget.cget("bg")

    def get_font_type(self):
        return self.font_type
    
    def set_border(self, PIXEL_WIDTH:int):
        self.widget.config(
            borderwidth = PIXEL_WIDTH,
            relief = "solid"
        )
    
    def set_font_type(self, FONT_TYPE:str):
        self.font_type = FONT_TYPE
        self.__update_font()

    def place(self, X, Y, WIDTH, HEIGHT):
        self.widget.place(
            x=X, y=Y, 
            width=WIDTH, 
            height=HEIGHT
        )

    def justify_text(self, 
            justify_key:str):
        self.widget.config(
            justify=justify_key)

    def __update_font(self):
        self.widget.config(font=(
            self.get_font_type(), 
            self.get_font_size(), 
            self.get_font_style()
        ))
    
    def get_font_size(self):
        return self.font_size
    
    def set_font_size(self, SIZE:int):
        self.font_size = SIZE
        self.__update_font()
    
    def get_font_style(self):
        return self.font_style
    
    def set_font_style(self, STYLE:str):
        self.font_style = STYLE
        self.__update_font()
    