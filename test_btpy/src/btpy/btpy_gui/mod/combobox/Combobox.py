

from tkinter import ttk
import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame

class Combobox(WidgetComposite):

    def __init__(self, window, title:str,
            VALUES_LIST:list[str] = []):
        super().__init__(window, True)
        self.combobox = None
        self.__init_components(window)
        self.set_title(title)
        if(VALUES_LIST != []):
            self.set_values_list(
                VALUES_LIST)
        
    def __init_components(self, window):
        self.combobox = ttk.Combobox(
            self.widget)
        self.label_title.grid(
            row=0, column=0, sticky="w")
        self.combobox.grid(
            row=0, column=1, sticky="ew")
        
    def add_change_listener(self, CALLBACK):
        self.combobox.bind(
            "<<ComboboxSelected>>", 
            CALLBACK
        )
        
    def set_size(self, CHAR_SIZE:int):
        self.combobox.config(
            width=CHAR_SIZE)
        
    def set_values_list(self, 
            VALUES_LIST:list[str]):
        self.combobox.config(
            values = VALUES_LIST)
        self.set_value(VALUES_LIST[0])

    def get_value(self):
        return self.combobox.get()
    
    def set_value(self, value):
        self.combobox.set(value)
        
