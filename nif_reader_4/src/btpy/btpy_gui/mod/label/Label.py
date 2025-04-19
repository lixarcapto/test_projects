


import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class Label(WidgetStandard):

    """
    It is a widget that is used 
    exclusively to write non-interactive 
    text in a few lines.
    """

    def __init__(self, window, 
            TITLE:str = ""):
        super().__init__(window)
        self.widget = tk.Label(
            self.margin,
            bg = "white",
            borderwidth = 1,
            relief= "solid",
            font = super().get_font()
        )
        self.widget.pack(
            padx=1, 
            pady=1,
            fill=tk.BOTH,
            expand = True
        )
        self.set_title(TITLE)

    def set_title(self, TEXT:str)->None:
        self.widget.config(text = TEXT)

    