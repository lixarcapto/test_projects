

from .WidgetTextual import WidgetTextual
import tkinter
from tkinter import ttk

class WidgetComboBox(WidgetTextual):

    def __init__(self, window_tk):
        self.widget = ttk.Combobox(
            window_tk.widget, 
            state="readonly")
        super().default_config()
        self.img = None

    def set_option_list(self, array:str):
        self.widget.config(values = array)
        self.widget.current(0)

    def select_option(self, text):
        self.widget.set(text)

    def select_option_index(self, index):
        self.widget.current(index) 

    def get_selected(self)->str:
        return self.widget.get()
    
    def get_index_selected(self)->str:
        return self.widget.current()
    
    def add_listener_select(self, function):
        self.widget.bind(
            "<<ComboboxSelected>>", 
            function
        )
    
    def replace_option(self, text, new_text):
        values = list(self.widget[text])
        self.widget[text] = values \
            + [new_text]
