

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class TextField(WidgetStandard):

    def __init__(self, window):
        super().__init__()
        self.widget = tk.Entry(
            window.widget)

    def set_is_password(self):
        self.config(show="*")

    def get_title(self)->str:
        return self.widget.get()

    def set_title(self, TEXT:str):
        self.widget.insert(0, TEXT)

    def set_character_width(self, 
            CHAR_NUMBER:int):
        self.widget.config(
            width = CHAR_NUMBER)
