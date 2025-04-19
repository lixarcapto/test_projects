

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from tkinter import font
from ..label_image.LabelImage import LabelImage

class WidgetComposite(WidgetStandard):

    def __init__(self, widget, 
            is_horizontal:bool = False):
        super().__init__(widget)
        self.key = ""
        self.label_title = LabelImage(
            self.margin
        )
        self.widget = tk.Frame(
            self.margin
        )
        self.widget.config(bg = "yellow")
        self.title_is_displayed\
            :bool = False
        self.is_horizontal = is_horizontal
        if(is_horizontal):
            self.set_in_horizontal()
        else:
            self.set_in_vertical()
        super().set_background_color("#EEEEEE")
        font_ = font.Font(
            family="Arial", 
            size=12
        )
        self.label_title.widget.config(
            font = font_,
            bg = "#EEEEEE"
        )
        self.set_title_background(
            "#BABABA")
        
    def set_font(self, FONT):
        super().set_font(FONT)
        self.label_title.set_font(FONT)

    def hide_title(self):
        self.label_title.widget\
            .grid_forget()
    
    def show_title(self):
        if(self.is_horizontal):
            self.label_title.margin.grid(
                row = 0, column= 0, 
                sticky="nsew",
                padx=(2, 0), pady=(2, 1)
            )
        else:
            self.label_title.margin.grid(
                row = 0, column= 0, 
                sticky="nsew",
                padx=(2, 1), pady=(2, 0)
            )

    def set_in_horizontal(self):
        self.widget.grid(
            row = 0, column= 1, 
            sticky="nsew",
            padx=1, pady=(1, 1)
        )

    def set_in_vertical(self):
        self.widget.grid(
            row = 1, column= 0, 
            sticky="nsew",
            padx=1, pady=(0, 1)
        )

    def set_background_color(self, COLOR):
        super().set_background_color(COLOR)
        self.label_title.widget\
            .config(bg = COLOR)
    
    def set_foreground_color(self, COLOR):
        self.label_title.widget\
            .config(fg = COLOR)

    def set_title_foreground(self, COLOR):
        self.label_title.widget\
            .config(fg = COLOR)

    def set_title_background(self, COLOR):
        self.label_title.widget\
            .config(bg = COLOR)
        
    def set_icon_path(self, PATH:str):
        self.label_title.set_path_image(
            PATH)
        if(not self.title_is_displayed
        and PATH != ""):
            self.title_is_displayed = True
            self.show_title()
        if(PATH == ""
        and self.title_is_displayed):
            self.title_is_displayed = False
            self.hide_title()

    def set_title(self, TEXT:str):
        self.key = TEXT
        self.label_title.set_title(TEXT)
        if(not self.title_is_displayed
        and TEXT != ""):
            self.title_is_displayed = True
            self.show_title()
        if(TEXT == ""
        and self.title_is_displayed):
            self.title_is_displayed = False
            self.hide_title()
        
    def get_title(self):
        return self.get_title()