

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class SwitchCheck(WidgetStandard):

    def __init__(self, window, 
            TITLE:str = ""):
        super().__init__(window)
        self.__value:tk.BooleanVar \
            = tk.BooleanVar()
        self.widget = tk.Checkbutton(
            self.margin, 
            text=TITLE, 
            variable=self.__value, 
            onvalue=True, offvalue=False,
            anchor="w"
        )
        self.back_color_1 = self\
            .margin.cget("bg")
        self.back_color_2 = "yellow"
        self.widget.pack(
            padx=1, 
            pady=1,
            fill=tk.BOTH, 
            expand=True
        )
        self.__add_default_listener()
    
    def __add_default_listener(self):
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
        
    def add_on_change_listener(self, 
            CALLBACK_X0:callable):
        self.widget.config(
            command= CALLBACK_X0)
        
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
        self.__value.set(BOOL)

    def get_value(self)->bool:
        return self.__value.get()