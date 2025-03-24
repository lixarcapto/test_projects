

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard


class InputSlider(WidgetStandard):

    def __init__(self, window, text = ""):
        super().__init__()
        self.widget = tk.Frame(
            window.widget,
            borderwidth = 1,
            relief= "solid"
        )
        self.label = tk.Label(self.widget)
        self.slider = tk.Scale(
            self.widget,
            orient=tk.HORIZONTAL,
            tickinterval = 0
        )
        self.is_in_horizontal = False
        self.set_text(text)

    def set_text(self, TEXT:str):
        self.label.config(text = TEXT)

    def get_text(self)->str:
        return self.label.cget("text")

    def pack(self):
        self.widget.pack()
        self.label.grid(row=0, column=0, 
            padx=10, pady=10)
        self.slider.grid(row=0, 
            column=1, padx=10, pady=10)

    def set_range(self, RANGE_LIST
            :list[int|float])->None:
        self.slider.config(
            from_= RANGE_LIST[0],
            to= RANGE_LIST[1]
        )

    def set_width(self, PIXEL_SIZE):
        self.slider.config(
            length = PIXEL_SIZE)
        
    def set_mark_interval(self, SIZE):
        self.slider.config(
            tickinterval = SIZE)

    def set_slide_distance(self, SIZE):
        self.slider.config(
            resolution = SIZE)

    def set_is_in_horizontal(self, BOOL):
        self.is_in_horizontal = BOOL
        if(BOOL):
            self.slider.config(
                orient=tk.HORIZONTAL)
        else:
            self.slider.config(
                orient=tk.VERTICAL)