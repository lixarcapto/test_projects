

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard


class InputSlider(WidgetStandard):

    def __init__(self, window):
        super().__init__()
        self.widget = tk.Scale(
            window.widget, 
            from_=0, 
            to=100, 
            orient=tk.HORIZONTAL, 
            length=300, 
            resolution=1, 
            tickinterval=20
        )
        self.is_in_horizontal = False

    def set_range(self, RANGE_LIST
            :list[int|float])->None:
        self.widget.config(
            from_= RANGE_LIST[0],
            to= RANGE_LIST[1]
        )

    def set_leng_bar(self, PIXEL_SIZE):
        self.widget.config(
            length = PIXEL_SIZE)
        
    def set_mark_interval(self, SIZE):
        self.widget.config(
            tickinterval = SIZE)

    def set_slide_distance(self, SIZE):
        self.widget.config(
            resolution = SIZE)

    def set_is_in_horizontal(self, BOOL):
        self.is_in_horizontal = BOOL
        if(BOOL):
            self.widget.config(
                orient=tk.HORIZONTAL)
        else:
            self.widget.config(
                orient=tk.VERTICAL)