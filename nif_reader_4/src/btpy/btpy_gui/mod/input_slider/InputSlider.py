

import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite

class InputSlider(WidgetComposite):

    def __init__(self, window, text = ""):
        super().__init__(window, True)
        self.slider = None
        self.is_in_horizontal = False
        self.__init_components()
        self.set_title(text)
    
    def __init_components(self):
        self.slider = tk.Scale(
            self.widget,
            orient=tk.HORIZONTAL,
            tickinterval = 0
        )
        # dibujar ------------------------
        self.slider.pack()

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