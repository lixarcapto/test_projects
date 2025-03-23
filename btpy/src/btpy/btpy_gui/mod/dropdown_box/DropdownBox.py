

from ..widget_standard.WidgetStandard import WidgetStandard
from tkinter import ttk

class DropdownBox(WidgetStandard):

    def __init__(self, window, 
            VALUES_LIST:list[str] = []):
        super().__init__()
        self.widget = ttk.Combobox(
            window.widget)
        if(VALUES_LIST != []):
            self.set_values_list(
                VALUES_LIST)
        
    def set_values_list(self, 
            VALUES_LIST:list[str]):
        self.widget.config(
            values = VALUES_LIST)
        self.set_value(VALUES_LIST[0])

    def get_value(self):
        return self.widget.get()
    
    def set_value(self, value):
        self.widget.set(value)
        
