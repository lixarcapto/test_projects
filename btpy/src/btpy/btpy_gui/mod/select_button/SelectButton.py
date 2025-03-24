
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class SelectButton(WidgetStandard):

    def __init__(self, window, TEXT = ""):
        super().__init__()
        self.widget = tk.Button(
            window.widget,
            text = TEXT
        )
        self.press_background = "blue"
        self.press_foreground = "white"
        self.original_background = ""
        self.original_foreground = ""
        self.is_selected:bool = False
        self.__add_default_listener()
        self.original_background\
            = self.widget.cget("bg")
        self.original_foreground\
            = self.widget.cget("fg")
        # #F0F0F0

    def get_value(self)->bool:
        return self.is_selected
    
    def set_value(self, BOOL:bool)->None:
        self.is_selected = BOOL
        if(self.is_selected):
            self.select()
        else:
            self\
            .deselect()

    def select(self):
        self.is_selected = True
        self.widget.config(
            bg= self.press_background,
            fg= self.press_foreground
        )

    def deselect(self):
        self.is_selected = False
        self.widget.config(
            bg= self.original_background,
            fg= self.original_foreground
        )

    def __add_default_listener(self):
        def fn():
            if(self.is_selected):
                self.deselect()
            else:
                self.select()
        self.widget.config(command= fn)