

import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from tkinter import font

class TextField(WidgetComposite):

    def __init__(self, window, 
                TEXT:str = ""):
        super().__init__(window, True)
        self.label_title\
            .set_background_color("#FFFFFF")
        self.entry = tk.Entry(
            self.widget
        )
        font_ = font.Font(
                family="Arial", 
                size=12, 
                weight="bold"
                )
        self.label_symbol = tk.Label(
            self.widget,
            font = font_,
            bg = "gray",
            fg = "white"
        )
        self.entry.grid(
            row = 0, column= 0
        )
        self.is_shadow_text = False
        self.symbol_is_added = False 
        self.add_default_listener()
        self.set_title(TEXT)

    def add_default_listener(self):
        def fn(e):
            if(self.is_shadow_text):
                self.remove_shadow_text()
        self.entry.bind("<Button-1>", fn)

    def remove_shadow_text(self):
        self.is_shadow_text = False
        self.entry.config(
            fg = "black"
        )
        self.entry.delete(0, tk.END)

    def remove_symbol(self):
        if(not self.symbol_is_added): 
            return None
        self.label_symbol.grid_forget()

    def set_right_input(self):
        if(self.symbol_is_added): 
            return None
        self.label_symbol.config(
            text = " ✓ ",
            bg = "green",
            fg = "white"
        )
        self.label_symbol.grid(
            row = 0, column= 1
        )

    def set_wrong_input(self):
        if(self.symbol_is_added): 
            return None
        self.label_symbol.config(
            text = "  X  ",
            bg = "red",
            fg = "white"
        )
        self.label_symbol.grid(
            row = 0, column= 1
        )

    def set_shadow_text(self, TEXT):
        self.is_shadow_text = True
        self.entry.config(
            fg = "gray"
        )
        self.entry.delete(0, tk.END)
        self.entry.insert(0, TEXT)

    def set_is_password(self):
        self.config(show="*")

    def get_value(self)->str:
        return self.entry.get()

    def set_value(self, TEXT:str):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, TEXT)

    def set_character_width(self, 
            CHAR_NUMBER:int):
        self.entry.config(
            width = CHAR_NUMBER)
