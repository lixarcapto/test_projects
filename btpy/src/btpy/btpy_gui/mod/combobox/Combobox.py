

from ..widget_standard.WidgetStandard import WidgetStandard
from tkinter import ttk
import tkinter as tk
from ..frame.Frame import Frame

class Combobox(WidgetStandard):

    def __init__(self, window, title:str,
            VALUES_LIST:list[str] = []):
        super().__init__()
        self.widget = Frame(window)
        self.widget.set_border(1)
        self.label_title = tk.Label(
            self.widget.widget,
            text = title
        )
        self.combobox = ttk.Combobox(
            self.widget.widget)
        if(VALUES_LIST != []):
            self.set_values_list(
                VALUES_LIST)
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
        
    def get_title(self)->str:
        return self.label_title.cget("text")
            
    def pack(self, MARGIN:int = 0):
        self.widget.pack(MARGIN)
        
    def set_values_list(self, 
            VALUES_LIST:list[str]):
        self.combobox.config(
            values = VALUES_LIST)
        self.set_value(VALUES_LIST[0])

    def get_value(self):
        return self.combobox.get()
    
    def set_value(self, value):
        self.combobox.set(value)
        
