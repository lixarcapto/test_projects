


import tkinter as tk
from ..frame.Frame import Frame
from ..widget_composite.WidgetComposite import WidgetComposite
from ..switch_check.SwitchCheck import SwitchCheck
from ....btpy_checkers.mod.is_index.is_index import*

class LabelList(WidgetComposite):

    """
    Checkbox type graphic component 
    that is used to ask the user to 
    enter multiple options from a list 
    by pressing click buttons.
    """

    def __init__(self, window,
            TITLE:str = ""):
        super().__init__(
            window,
            False
        )
        self.label_list = []
        self.text_list = []
        self.label_title\
            .set_background_color("white")
        self.symbol = ")."
        self.set_title(TITLE)
    
    # PUBLIC -----------------------------

    def set_symbol(self, SYMBOL:str):
        self.symbol = SYMBOL
        self.set_content(self.text_list)

    def set_content(self, 
            TEXT_LIST):
        self.text_list = TEXT_LIST
        self.label_list = []
        label = None
        i = 0
        f_text = ""
        for text in TEXT_LIST:
            f_text = f"{i}{self.symbol} {text}."
            label = tk.Label(
                self.widget, 
                text=f_text,
                font = self.default_font,
                background="white"
            )
            label.grid(
                column=0, 
                row=i, 
                sticky="ew"
            )
            i += 1
            