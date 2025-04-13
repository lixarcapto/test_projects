

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class Frame(WidgetStandard):

    def __init__(self, window):
        super().__init__(window)
        self.widget = tk.Frame(
            self.margin)
        self.widget.pack(fill =tk.BOTH,
            expand=True)