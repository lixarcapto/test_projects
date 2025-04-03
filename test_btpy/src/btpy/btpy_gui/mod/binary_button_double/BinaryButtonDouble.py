

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..frame.Frame import Frame

class BinaryButtonDouble(WidgetStandard):

    def __init__(self, window, 
            title, 
            content_list:list[str] = []):
        super().__init__()
        self.widget = None
        self.label_title = None
        self.button_1 = None
        self.button_2 = None
        self.selection_bg_color = ""
        self.selection_fg_color = ""
        self.foreground_color = ""
        self.background_color = ""
        self.value:bool = False
        self.__init_components(window)
        self.selection_bg_color = "blue"
        self.selection_fg_color = "white"
        self.foreground_color = self\
            .button_1.cget("fg")
        self.background_color = self\
            .button_1.cget("bg")
        self.set_title(title)
        if(content_list != []):
            self.set_content(content_list)
        self.react_click_1()
        self.add_default_listener()

    def __init_components(self, window):
        self.widget = Frame(window)
        self.widget.set_border(1)
        self.label_title = tk.Label(
            self.widget.widget
        )
        self.button_1 = tk.Button(
            self.widget.widget
        )
        self.button_2 = tk.Button(
            self.widget.widget
        )

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT)

    def get_title(self)->str:
        return self.label_title.cget("text")

    def set_content(self, 
            content_list:list[str]):
        self.button_1.config(
            text = content_list[0])
        self.button_2.config(
            text = content_list[1])
        
    def set_back_select_color(self, COLOR):
        self.selection_bg_color = COLOR
    
    def set_text_select_color(self, COLOR):
        self.foreground_color = COLOR

    def set_background_color(self, COLOR):
        super().set_background_color(COLOR)
        self.background_color = COLOR

    def set_foreground_color(self, COLOR):
        super().set_foreground_color(COLOR)
        self.foreground_color = COLOR
        
    def get_value(self)->bool:
        return self.value
    
    def set_value(self, BOOL:bool):
        self.value = BOOL

    def react_click_1(self):
        self.value = True
        self.button_1.config(
            bg = self.selection_bg_color)
        self.button_2.config(
            bg = self.background_color)
        #
        self.button_1.config(
            fg = self.selection_fg_color)
        self.button_2.config(
            fg = self.foreground_color)
        
    def react_click_2(self):
        self.value = False
        self.button_1.config(
            bg = self.background_color)
        self.button_2.config(
            bg = self.selection_bg_color)
        #
        self.button_1.config(
            fg = self.foreground_color)
        self.button_2.config(
            fg = self.selection_fg_color)
        
    def add_default_listener(self):
        self.button_1.config(
            command = self.react_click_1
        )
        self.button_2.config(
            command = self.react_click_2
        )

    def pack(self, MARGIN:int = 0):
        self.widget.pack(MARGIN)
        self.label_title.grid(
            row = 0, column= 0
        )
        self.button_1.grid(
            row = 0, column= 1
        )
        self.button_2.grid(
            row = 0, column= 2
        )
