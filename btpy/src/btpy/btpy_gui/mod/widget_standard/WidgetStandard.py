

import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as font

class WidgetStandard:

    def __init__(self):
        self.widget = None
        self.font_type:str = "Arial"
        self.font_size:int = 14
        self.font_style:str = "roman"
        self.is_bold = False
        self.is_underline = False
        self.is_overstrike = False

    def set_is_bold(self, BOOL):
        self.is_bold = BOOL
        self.__update_font()

    def set_is_underline(self, BOOL):
        self.is_underline = BOOL
        self.__update_font()

    def set_is_overstrike(self, BOOL):
        self.is_overstrike = BOOL
        self.__update_font()

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

    def set_title(self, TEXT:str)->None:
        pass

    def get_title(self)-> str:
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
        new_weight = "normal"
        if(self.is_bold):
            new_weight = "bold"
        new_font = font.Font(
            family=self.get_font_type(),
            size=self.get_font_size(),
            weight=new_weight,
            slant=self.get_font_style(),
            underline=self.is_underline,
            overstrike=self.is_overstrike,
        )
        self.widget.config(font=new_font)
    
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
    