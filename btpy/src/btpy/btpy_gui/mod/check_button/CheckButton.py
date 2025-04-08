

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class CheckButton(WidgetStandard):

    def __init__(self, window, text = ""):
        super().__init__(window)
        self.is_selected = tk.BooleanVar()
        self.widget = tk.Checkbutton(
            self.margin, 
            text=text, 
            variable=self.is_selected, 
            onvalue=True, offvalue=False,
            borderwidth = 1,
            relief= "solid"
        )
        self.widget.pack(
            padx=1, 
            pady=(2, 1)
        )

    def set_title(self, TEXT:str):
        self.widget.config(text = TEXT)

    def get_title(self):
        return self.widget.cget("text")

    def set_value(self, BOOL):
        self.is_selected.set(BOOL)

    def get_value(self)->bool:
        return self.is_selected.get()