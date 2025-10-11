


import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..frame.Frame import Frame
from tkinter import font

class ButtonSymbol(WidgetComposite):

    def __init__(self, window, 
            TITLE:str = "", 
            symbol:str = ""):
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
            bg = "red",
            fg = "white",
            font = font_
        )
        self.set_symbol(symbol)
        self.label.pack()
        self.add_default_listener()

    def set_symbol(self, SYMBOL):
        self.label.config(
            text = f" {SYMBOL} ")
        
    def set_color_symbol(self, 
            background, foreground):
        self.label.config(
            bg = background,
            fg = foreground
        )
        
    def add_listener(self, CALLBACK,
            EVENT_KEY:str = "default"):
        if(EVENT_KEY == "default"):
            self.label.bind("<Button-1>", 
                CALLBACK)
            self.label_title.widget.bind("<Button-1>", 
                CALLBACK)
        elif(EVENT_KEY == "mouse_enter"):
            self.label.bind("<Enter>", 
                CALLBACK)
            self.label_title.widget.bind("<Enter>", 
                CALLBACK)
        elif(EVENT_KEY == "mouse_leave"):
            self.label.bind("<Leave>", 
                CALLBACK)
            self.label_title.widget.bind("<Leave>", 
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
