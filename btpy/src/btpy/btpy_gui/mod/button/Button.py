

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class Button(WidgetStandard):

    def __init__(self, window, text = ""):
        super().__init__()
        self.widget = tk.Button(
            window.widget, 
            text="Haz clic aquí"
        )

    def set_title(self, TEXT:str):
        self.widget.config(text = TEXT)

    def get_title(self):
        return self.widget.cget("text")

    def add_listener(self, CALLBACK)->None:
        self.widget.config(
            command = CALLBACK)