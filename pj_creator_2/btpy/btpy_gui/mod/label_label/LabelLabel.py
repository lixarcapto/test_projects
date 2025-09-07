


import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..frame.Frame import Frame
import tkinter.font as font

class LabelLabel(WidgetStandard):

    def __init__(self, window, title = ""):
        super().__init__(window)
        self.widget = tk.Label(
            self.margin,
            borderwidth = 1,
            relief = "solid"
        )
        self.key = ""
        self.widget.config(
            bg = "white"
        )
        self.label_content = tk.Label(
            self.margin,
            anchor= "e",
            borderwidth = 1,
            relief = "solid"
        )
        self.label_content.config(
            bg = "white"
        )
        self.margin.columnconfigure(
            1, weight=1)
        # Alinea a la izquierda
        self.widget.grid(
            row=0, column=0, sticky="nsew"
        )
        self.label_content.grid(
            row=0, column=1, sticky="nsew"
        )
        # Alinea a la derecha
        self.set_title(title)

    def set_content_color(self, 
            BACKGROUND, FOREGROUND):
        self.label_content.config(
            bg = BACKGROUND, 
            fg = FOREGROUND
        )

    def set_font_content(self,
            FAMILY, SIZE, IS_BOLD):
        font_ = font.Font(
                family=FAMILY, 
                size=SIZE, 
                )
        if(IS_BOLD):
            font_.config(weight="bold")
        self.label_content.config(
            font= font_)

    def set_title(self, TITLE:str)->None:
        self.key = TITLE
        self.widget.config(
            text = " " + TITLE + " ")
        
    def get_title(self)->str:
        return self.key

    def set_content(self, TEXT:str):
        self.label_content.config(
            text = TEXT)

    def get_content(self)->str:
        return self.label_content.cget(
            "text")
    
    def set_font_size(self, SIZE:int):
        super().set_font_size(SIZE)
        self.default_font.config(
            size = SIZE)
        self.label_content.config(
            font = self.default_font
        )

    def set_content_foreground_color(self, 
            COLOR):
        f_color = self\
            .convert_to_tk_color(COLOR)
        self.label_content.config(
            fg = f_color)
        
    def set_content_background_color(self, 
            COLOR):
        f_color = self\
            .convert_to_tk_color(COLOR)
        self.label_content.config(
            bg = f_color)