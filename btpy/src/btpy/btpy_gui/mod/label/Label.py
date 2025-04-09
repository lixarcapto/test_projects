


import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class Label(WidgetStandard):

    def __init__(self, window, text = ""):
        super().__init__(window)
        self.widget = tk.Label(
                window.widget)
        self.set_title(text)

    def set_title(self, TEXT:str)->None:
        self.widget.config(text = TEXT)