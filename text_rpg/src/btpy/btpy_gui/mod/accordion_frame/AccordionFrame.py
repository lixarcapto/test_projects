

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..button_symbol.ButtonSymbol import ButtonSymbol
class AccordionFrame(WidgetStandard):

    def __init__(self, window, 
            TITLE:str = ""):
        super().__init__(window)
        self.is_open:bool = False
        self.button_title = ButtonSymbol(
            self.margin, 
            TITLE,
            "\\/"
        )
        # ↓ ↑
        self.button_title.margin.grid(
            row = 0, column= 0,
            padx=1, pady=(1, 0)
        )
        self.activated_by_mouseenter\
            :bool = False
        self.widget = tk.Frame(self.margin)
        self.add_default_listener()

    def add_default_listener(self):
        # left click ---------------------
        def fn(e):
            if(self.is_open):
                self.is_open = False
            else:
                self.is_open = True
            if(self.is_open):
                self.execute_open_event()
            else:
                self.execute_close_event()
        self.button_title.add_listener(fn)
        # enter ----------------------
        def fn(e):
            if(self.activated_by_mouseenter):
                self.execute_open_event()
        self.button_title.add_listener(
            fn, "mouse_enter"
        )
        # leave --------------------------
        def fn(e):
            if(self.activated_by_mouseenter):
                self.execute_close_event()
        self.button_title.add_listener(
            fn, "mouse_leave"
        )

    def set_activated_by_mouseenter(self, 
                BOOL:bool):
        self.activated_by_mouseenter = BOOL

    def execute_open_event(self):
        self.widget.grid(
            row = 1, column= 0,
            padx=1, pady=(0, 1)
        )
        self.button_title\
            .set_symbol("\\/")
        
    def execute_close_event(self):
        self.widget.grid_forget()
        self.button_title\
            .set_symbol("/\\")
        
    def set_title(self, TITLE:str)->None:
        self.button_title.config(
            text = TITLE)
        
    def get_title(self)->str:
        return self.button_title.cget(
            "text")