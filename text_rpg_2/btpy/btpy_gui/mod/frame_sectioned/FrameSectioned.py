

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class FrameSectioned(WidgetStandard):

    def __init__(self, window):
        super().__init__(window)
        self.widget = tk.Frame(
            self.margin)
        self.widget.pack(
            padx=1,
            pady=1,
            fill =tk.BOTH,
            expand=True
        )
        self.head = tk.Frame(
            self.widget, borderwidth = 1,
            relief = "solid"
        )
        self.head.grid(
            row = 0, column= 0,
            sticky="nswe",
            columnspan=3
        )
        self.widget.columnconfigure(
            0, weight= 1)
        self.side_right = tk.Frame(
            self.widget, borderwidth = 1,
            relief = "solid"
        )
        self.side_right.grid(
            row = 1, column= 2, 
            sticky="nswe"
        )
        self.widget.rowconfigure(
            1, weight= 2)
        self.widget.columnconfigure(
            1, weight= 2)
        self.center = tk.Frame(
            self.widget, borderwidth = 1,
            relief = "solid"
        )
        self.center.grid(
            row = 1, column= 1, 
            sticky="nswe"
        )
        self.side_left = tk.Frame(
            self.widget, borderwidth = 1,
            relief = "solid"
        )
        self.side_left.grid(
            row = 1, column= 0, 
            sticky="nswe"
        )
        self.widget.columnconfigure(
            2, weight= 1)
        self.feet = tk.Frame(
            self.widget, borderwidth = 1,
            relief = "solid"
        )
        self.feet.grid(
            row = 2, column= 0, 
            sticky="nswe",
            columnspan=3
        )