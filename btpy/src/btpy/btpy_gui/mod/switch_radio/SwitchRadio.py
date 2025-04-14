
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class SwitchRadio(WidgetStandard):

    def __init__(self, window, 
            variable_, 
            number, 
            text = ""):
        super().__init__(window)
        self.is_selected = tk.BooleanVar()
        self.widget = tk.Radiobutton(
            self.margin, 
            text = text, 
            variable= variable_,
            value = number,
            borderwidth = 1,
            relief= "solid",
            anchor="w"
        )
        self.back_color_1\
            = self.margin.cget("bg")
        self.back_color_2 = "yellow"
        self.widget.pack(
            padx=1, 
            pady=1,
            fill=tk.BOTH, 
            expand=True
        )
        self.add_default_listener()

    def add_listener(self, CALLBACK):
        self.widget.bind("<Button-1>",
            CALLBACK
        )
        self.margin.bind("<Button-1>",
            CALLBACK
        )
        
    
    def add_default_listener(self):
        def enter_fn(e):
            self.set_margin_color(
                self.back_color_2)
        self.widget.bind("<Enter>", 
                enter_fn)
        def leave_fn(e):
            self.set_margin_color(
                self.back_color_1)
        self.widget.bind("<Leave>", 
                leave_fn)
        
    def set_background_color(self, COLOR):
        return super()\
            .set_background_color(COLOR)
        self.back_color_1 = COLOR

    def set_focus_color(self, COLOR):
        self.back_color_2 = COLOR

    def set_title(self, TEXT:str):
        self.widget.config(text = TEXT)

    def get_title(self):
        return self.widget.cget("text")