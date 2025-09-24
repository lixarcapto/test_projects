

import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame
from ..button.Button import Button

class Option(WidgetComposite):

    def __init__(self, widget, 
            TITLE:str):
        super().__init__(widget, False)
        self.set_title(TITLE)
        self.label_title.config(
            bg = "gray")
        self.label_content = tk.Label(
            self.widget
        )
        self.frame_button = tk.Frame(
            self.widget
        )
        self.button_true = Button(
            self.frame_button, "no"
        )
        self.button_true\
            .set_background_color("green")
        self.button_true\
            .set_font_color("white")
        self.button_false = Button(
            self.frame_button, "yes"
        )
        self.button_false\
            .set_background_color("red")
        self.button_false\
            .set_font_color("white")
        self.__value:bool = False
        self.label_content.grid(
            row = 0, column = 0
        )
        self.frame_button.grid(
            row = 1, column = 0
        )
        self.button_true.draw_in_grid(0, 0)
        self.button_false.draw_in_grid(0, 1)
        self.callback = None
        self.__add_default_listener()

    def get_value(self)->bool:
        return self.__value

    def add_listener(self, CALLBACK):
        self.callback = CALLBACK

    def __add_default_listener(self):
        def fn(e):
            if(self.callback != None):
                self.__value = False
                self.callback(
                    self.__value)
        self.button_false.add_listener(fn)
        def fn(e):
            if(self.callback != None):
                self.__value = True
                self.callback(
                    self.__value)
        self.button_true.add_listener(fn)

    def set_content(self, 
            TEXT_CONTENT:str, 
            TRUE_TEXT:str, FALSE_TEXT:str):
        self.button_true.set_title(
            TRUE_TEXT)
        self.button_false.set_title(
            FALSE_TEXT)
        self.label_content.config(
            text = TEXT_CONTENT)
        
    def set_true_text(self, TEXT:str):
        self.button_true.config(
            text = TEXT)
        
    def set_false_text(self, TEXT:str):
        self.button_false.config(
            text = TEXT)
        
    def set_content_text(self, TEXT:str):
        self.label_content.config(
            text = TEXT)
        
    
    