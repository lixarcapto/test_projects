

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..simple_card.SimpleCard import SimpleCard

class ItemFrame(WidgetStandard):

    def __init__(self, window, 
                 TITLE:str = ""):
        super().__init__(window)
        self.card = SimpleCard(
            self.margin,
            "horizontal", 
            TITLE
        )
        self.size_icon_list:\
            list[int] = [80, 80]
        self.card.margin.grid(
            row = 1, column = 0
        )
        self.widget = tk.Frame(self.margin)
        self.widget.grid(
            row = 1, column = 0
        )
        self.set_margin_color("black")

    def set_title(self, TEXT:str):
        self.card.set_title(TEXT)

    def set_description(self, TEXT:str):
        self.card.set_description(TEXT)

    def set_icon(self, PATH:str):
        self.card.set_icon(PATH, 
            self.size_icon_list)
