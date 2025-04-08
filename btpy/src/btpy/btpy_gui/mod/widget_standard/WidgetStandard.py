

import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as font
from ....btpy_transformers.mod.RGB_to_hex.RGB_to_hex import*
from ....btpy_checkers.mod.is_RGB.is_RGB import*

class WidgetStandard:

    """
    TODO: ahora los widgets se 
    componen de dos frames, el widget
    principal que contiene el label 
    title, y el segundo widget que es
    un frame contenedor, esto
    permite crear margenes y titulos 
    mas faciles.

    Crear dos tipos de widgets, los simples
    y los compuestos.
    """

    class POSITION:
        CENTER = None
        TOP = tk.TOP
        BOTTOM = tk.BOTTOM
        LEFT = tk.LEFT
        RIGHT = tk.RIGHT

    def __init__(self, widget):
        self.margin = None
        # permite recibir objetos
        # widget wrappers y widgets TK
        if(hasattr(widget, "widget")):
            self.margin = tk.Frame(
                widget.widget)
        else:
            self.margin = tk.Frame(
                widget)
        self.margin.config(bg = "red")
        self.widget = None
        self.is_underline = False
        self.is_overstrike = False

    def get_font(self):
        return self.widget.cget("font")

    def set_is_bold(self, BOOL):
        weight_ = "normal"
        if(BOOL):
            weight_ = "bold"
        font_ = self.widget.cget("font")
        font_.config(weight = weight_)
        self.widget.config(font = font_)
        

    def get_is_bold(self)->bool:
        result = self.widget.cget("font")\
            .actual()["weight"]
        if("bold" == result): return True
        return False

    def set_is_underline(self, BOOL):
        font_ = self.widget.cget("font")
        font_.config(underline = BOOL)
        self.widget.config(font = font_)

    def get_is_underline(self)->bool:
        return self.widget.cget("font")\
            .actual()["underline"]

    def set_is_overstrike(self, BOOL):
        font_ = self.widget.cget("font")
        font_.config(overstrike = BOOL)
        self.widget.config(font = font_)

    def get_is_overstrike(self)->bool:
        return self.widget.cget("font")\
            .actual()["overstrike"]

    def pack(self, MARGIN:int = 0):
        self.margin.pack(
            padx = 1 + MARGIN,
            pady = (2 + MARGIN, 
                    1 + MARGIN), 
            ipadx=1, 
            ipady=1
        )
    
    def unpack(self)-> None:
        self.widget.pack_forget()

    def get_font(self):
        return self.widget.cget("font")
    
    def set_font(self,  FONT):
        self.widget.config(font =FONT)
        self.__update_font()

    def set_title(self, TITLE:str)->None:
        pass
        
    def get_title(self)->str:
        pass

    def set_foreground_color(self, COLOR):
        f_color = COLOR
        if(is_RGB(COLOR)):
            f_color = RGB_to_hex(COLOR)
        self.widget.config(fg = f_color)

    def get_foreground_color(self):
        pass

    def get_margin_color(self):
        return self.margin.cget("bg")

    def set_margin_color(self, COLOR):
        f_color = COLOR
        if(is_RGB(COLOR)):
            f_color = RGB_to_hex(COLOR)
        self.margin.config(bg = f_color)

    def set_background_color(self, COLOR):
        f_color = COLOR
        if(is_RGB(COLOR)):
            f_color = RGB_to_hex(COLOR)
        self.widget.config(bg = f_color)

    def get_background_color(self, COLOR):
        pass

    def get_background_color(self):
        return self.widget.cget("bg")
    
    def set_border(self, PIXEL_WIDTH:int):
        self.widget.config(
            borderwidth = PIXEL_WIDTH,
            relief = "solid"
        )

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
            slant=self.get_font_family(),
            underline=self.is_underline,
            overstrike=self.is_overstrike,
        )
        self.widget.config(font=new_font)
    
    def get_font_size(self):
        return self.widget.cget("font")\
            .actual()["size"]
    
    def set_font_size(self, SIZE:int):
        font_ = self.widget.cget("font")
        font_.config(size = SIZE)
        self.widget.config(font = font_)
    
    def get_font_family(self):
        return self.widget.cget("font")\
            .actual()["family"]
    
    def set_font_family(self, FAMILY:str):
        font_ = self.widget.cget("font")
        font_.config(family = FAMILY)
        self.widget.config(font = font_)
    