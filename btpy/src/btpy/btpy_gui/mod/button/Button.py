

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class Button(WidgetStandard):

    def __init__(self, window, text = ""):
        super().__init__()
        self.widget = tk.Button(
            window.widget, 
            text="Haz clic aquí"
        )

    def set_text(self, TEXT:str):
        self.widget.config(text = TEXT)

    def add_listener(self, CALLBACK)->None:
        self.widget.config(
            command = CALLBACK)