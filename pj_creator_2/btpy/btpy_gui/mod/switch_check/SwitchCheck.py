

import tkinter as tk
from ..on_focus_widget.OnFocusWidget import OnFocusWidget

class SwitchCheck(OnFocusWidget):

    def __init__(self, window, 
            TITLE:str = ""):
        super().__init__(window)
        self.__value:tk.BooleanVar \
            = tk.BooleanVar()
        widget = tk.Checkbutton(
            self.margin, 
            text=TITLE, 
            variable=self.__value, 
            onvalue=True, offvalue=False,
            anchor="w"
        )
        self.add_widget(widget)
        self.widget.config(
            font = self.default_font
        )

    def set_content(self, TEXT:str):
        self.widget.config(text=TEXT)
        
    def add_on_change_listener(self, 
            CALLBACK_ARGS_X0:callable):
        self.widget.config(
            command= CALLBACK_ARGS_X0)

    def set_value(self, BOOL):
        self.__value.set(BOOL)

    def get_value(self)->bool:
        return self.__value.get()