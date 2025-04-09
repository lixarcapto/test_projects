
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class SelectButton(WidgetStandard):

    """
    This component creates a binary 
    text button that changes color 
    each time it is pressed.
    """

    def __init__(self, window, TEXT = "")\
            -> None:
        super().__init__(window)
        self.widget = tk.Button(
            self.margin,
            text = TEXT,
            bg = "white"
        )
        self.widget.pack(
            padx=1, 
            pady=(2, 1)
        )
        self.press_background = "#0C0C0C"
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

    def get_title(self)->str:
        return self.widget.cget("text")
    
    def set_title(self, TEXT:str)->None:
        self.widget.config(text = TEXT)

    def get_value(self)->bool:
        return self.is_selected
    
    def set_value(self, BOOL:bool)->None:
        self.is_selected = BOOL
        if(self.is_selected):
            self.__select()
        else:
            self\
            .__deselect()

    def __select(self)-> None:
        self.is_selected = True
        self.widget.config(
            bg= self.press_background,
            fg= self.press_foreground
        )

    def __deselect(self)-> None:
        self.is_selected = False
        self.widget.config(
            bg= self.original_background,
            fg= self.original_foreground
        )

    def __add_default_listener(self)->None:
        def fn():
            if(self.is_selected):
                self.__deselect()
            else:
                self.__select()
        self.widget.config(command= fn)