

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class SelectButton(WidgetStandard):

    def __init__(self, window, text = ""):
        super().__init__()
        self.is_selected = tk.BooleanVar()
        self.widget = tk.Checkbutton(
            window.widget, 
            text=text, 
            variable=self.is_selected, 
            onvalue=True, offvalue=False,
            borderwidth = 1,
            relief= "solid"
        )

    def set_text(self, TEXT:str):
        self.widget.config(text = TEXT)

    def get_text(self):
        return self.widget.cget("text")

    def set_value(self, BOOL):
        self.is_selected.set(BOOL)

    def get_value(self)->bool:
        return self.is_selected.get()