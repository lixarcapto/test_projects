


import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..frame.Frame import Frame
from tkinter import font

class SelfdestructButton(WidgetComposite):

    def __init__(self, window, 
            TITLE:str = ""):
        super().__init__(window, True)
        self.widget.config(
            borderwidth = 1,
            relief = "solid"
        )
        self.set_title(TITLE)
        font_ = font.Font(
                family="Arial", 
                size=12, 
                weight="bold"
                )
        self.back_color_1 = "gray"
        self.back_color_2 = "yellow"
        self.label = tk.Label(
            self.widget,
            text = " X ", 
            bg = "red",
            fg = "white",
            font = font_
        )
        self.label.pack()
        self.add_default_listener()
        
    def add_listener(self, CALLBACK):
        self.label.bind("<Button-1>", 
                CALLBACK)
        self.label_title.bind("<Button-1>", 
                CALLBACK)
        self.margin.bind("<Button-1>", 
                CALLBACK)
        
    def add_default_listener(self):
        def enter_fn(e):
            self.set_margin_color(
                self.back_color_2)
        self.margin.bind("<Enter>", 
                enter_fn)
        def leave_fn(e):
            self.set_margin_color(
                self.back_color_1)
        self.margin.bind("<Leave>", 
                leave_fn)
        
    def set_background_color(self, COLOR):
        return super()\
            .set_background_color(COLOR)
        self.back_color_1 = COLOR

    def set_focus_color(self, COLOR):
        self.back_color_2 = COLOR
