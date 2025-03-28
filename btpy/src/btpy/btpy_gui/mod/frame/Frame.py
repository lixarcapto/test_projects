

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class Frame(WidgetStandard):

    def __init__(self, window):
        super().__init__()
        self.widget = tk.Frame(
            window.widget)
        
    def pack(self, MARGIN:int = 0):
        self.widget.pack(
            padx=MARGIN, pady=MARGIN
        )

    def unpack(self):
        self.widget.pack_forget()