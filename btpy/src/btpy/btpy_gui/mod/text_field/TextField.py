

import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite

class TextField(WidgetComposite):

    def __init__(self, window, 
                TEXT:str = ""):
        super().__init__(window, True)
        self.label_title.config(
            bg = "#EEEEEE")
        self.entry = tk.Entry(
            self.widget
        )
        self.entry.pack()
        self.set_title(TEXT)

    def set_is_password(self):
        self.config(show="*")

    def get_value(self)->str:
        return self.widget.get()

    def set_value(self, TEXT:str):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, TEXT)

    def set_character_width(self, 
            CHAR_NUMBER:int):
        self.entry.config(
            width = CHAR_NUMBER)
