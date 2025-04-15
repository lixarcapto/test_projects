

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class SwitchCheck(WidgetStandard):

    def __init__(self, window, text = ""):
        super().__init__(window)
        self.is_selected = tk.BooleanVar()
        self.widget = tk.Checkbutton(
            self.margin, 
            text=text, 
            variable=self.is_selected, 
            onvalue=True, offvalue=False,
            borderwidth = 1,
            relief= "solid",
            anchor="w"
        )
        self.back_color_1 = "gray"
        self.back_color_2 = "yellow"
        self.widget.pack(
            padx=2, 
            pady=(2, 2),
            fill=tk.BOTH, 
            expand=True
        )
        self.add_default_listener()
    
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

    def set_value(self, BOOL):
        self.is_selected.set(BOOL)

    def get_value(self)->bool:
        return self.is_selected.get()