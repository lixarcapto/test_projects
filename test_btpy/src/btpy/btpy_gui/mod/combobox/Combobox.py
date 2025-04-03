

from ..widget_standard.WidgetStandard import WidgetStandard
from tkinter import ttk
import tkinter as tk
from ..frame.Frame import Frame

class Combobox(WidgetStandard):

    def __init__(self, window, title:str,
            VALUES_LIST:list[str] = []):
        super().__init__()
        self.widget = None
        self.label_title = None
        self.combobox = None
        self.__init_components(window)
        self.set_title(title)
        if(VALUES_LIST != []):
            self.set_values_list(
                VALUES_LIST)
        
    def __init_components(self, window):
        self.widget = Frame(window)
        self.widget.set_border(1)
        self.label_title = tk.Label(
            self.widget.widget
        )
        self.combobox = ttk.Combobox(
            self.widget.widget)
        self.label_title.grid(
            row=0, column=0, sticky="w")
        self.combobox.grid(
            row=0, column=1, sticky="ew")
        
    def add_change_listener(self, CALLBACK):
        self.combobox.bind(
            "<<ComboboxSelected>>", 
            CALLBACK
        )
            
    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT)
        
    def set_size(self, CHAR_SIZE:int):
        self.combobox.config(
            width=CHAR_SIZE)
        
    def get_title(self)->str:
        return self.label_title.cget("text")
        
    def set_values_list(self, 
            VALUES_LIST:list[str]):
        self.combobox.config(
            values = VALUES_LIST)
        self.set_value(VALUES_LIST[0])

    def get_value(self):
        return self.combobox.get()
    
    def set_value(self, value):
        self.combobox.set(value)
        
