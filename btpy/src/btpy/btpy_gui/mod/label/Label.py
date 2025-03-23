


import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class Label(WidgetStandard):

    def __init__(self, window, text = ""):
        super().__init__()
        self.widget = tk.Label(
                window.widget)
        self.set_text(text)

    def set_text(self, TEXT:str)->None:
        self.widget.config(text = TEXT)

    def pack(self):
        self.widget.pack(pady=5)