

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
        self.widget = None
        # la default font contiene
        # la informacion sobre la 
        # fuente que utiliza el widget
        self.default_font = font.Font(
            family="Arial", 
            size=11
        )
        # permite recibir objetos
        # widget wrappers y widgets TK
        if(hasattr(widget, "widget")):
            self.margin = tk.Frame(
                widget.widget
            )
        else:
            self.margin = tk.Frame(
                widget)
        # configura el color negro
        # para el margin
        self.margin.config(
            bg = "black"
        )

    def add_widget(self, widget):
        """
        Permite agregar un widget
        principal al componente de 
        forma automatica.
        """
        self.widget = widget
        self.widget.config(
            bg = "#F0F0F0"
        )
        self.widget.pack(
            padx=1, 
            pady=1,
            fill=tk.BOTH,
            expand=True
        )

    def get_font(self):
        return self.default_font

    def set_is_bold(self, BOOL):
        weight_ = "normal"
        if(BOOL):
            weight_ = "bold"
        self.default_font.config(
            weight = weight_)
        self.widget.config(
            font = self.default_font
        )

    def get_is_bold(self)->bool:
        result = self.default_font\
            .cget("font")
        if("bold" == result): return True
        return False

    def set_is_underline(self, BOOL):
        self.default_font.config(
            underline = BOOL)
        self.widget.config(
            font = self.default_font
        )

    def get_is_underline(self)->bool:
        return self.default_font\
            .cget("underline")
    
    def place_forget(self):
        self.margin.place_forget()
    
    def pack_forget(self):
        self.margin.pack_forget()

    def grid_forget(self):
        self.margin.grid_forget()

    def set_is_overstrike(self, BOOL):
        self.default_font.config(
            overstrike = BOOL)
        self.widget.config(
            font = self.default_font
        )

    def get_is_overstrike(self)->bool:
        return self.widget.cget("font")\
            .actual()["overstrike"]

    def pack(self, 
            IS_EXPANDABLE:bool = False,
            SIDE_KEY:str = "left"):
        """
        SIDE_KEY:
        * left
        * top
        * right
        * bottom
        """
        if(IS_EXPANDABLE):
            self.margin.pack(
                fill=tk.BOTH, 
                expand=True,
                side = SIDE_KEY
            )
        else:
            self.margin.pack(
                side = SIDE_KEY
            )


    def grid(self, ROW:int, COLUMN:int,
            STICKY:str = ""):
        if(STICKY == ""):
            self.margin.grid(row = COLUMN,
                column=ROW)
        else:
            self.margin.grid(
                row = COLUMN,
                column=ROW,
                sticky=STICKY
            )
    
    def set_font(self,  FONT):
        self.default_font = FONT

    def set_title(self, TITLE:str)->None:
        self.widget.config(text = TITLE)
        
    def get_title(self)->str:
        return self.widget.cget("text")

    def convert_to_tk_color(self, COLOR):
        f_color = COLOR
        if(is_RGB(COLOR)):
            f_color = RGB_to_hex(COLOR)
        return f_color

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

    def get_background_color(self):
        return self.widget.cget("bg")
    
    def set_border(self, PIXEL_WIDTH:int):
        self.widget.config(
            borderwidth = PIXEL_WIDTH,
            relief = "solid"
        )

    def place(self, X, Y, WIDTH, HEIGHT):
        self.margin.place(
            x=X, y=Y, 
            width=WIDTH, 
            height=HEIGHT
        )

    def justify_text(self, 
            justify_key:str):
        self.widget.config(
            justify=justify_key)
    
    def get_font_size(self):
        return self.default_font\
            .cget("size")
    
    def set_font_size(self, SIZE:int):
        self.default_font.config(
            size = SIZE)
        self.widget.config(
            font = self.default_font
        )
    
    def get_font_family(self):
        return self.default_font\
            .cget("family")
    
    def set_font_family(self, FAMILY:str):
        """
        Font family keys:
        * "Arial"
        * "Times New Roman"
        * "Calibri" 
        * "Cambria"
        * "Verdana"
        """
        self.default_font.config(
            family = FAMILY)
        self.widget.config(
            font = self.default_font
        )
    