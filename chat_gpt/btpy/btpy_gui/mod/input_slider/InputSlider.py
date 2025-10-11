

import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite

class InputSlider(WidgetComposite):

    def __init__(self, window, 
            is_horizontal:bool, text = ""):
        super().__init__(window, 
            is_horizontal)
        self.slider = None
        self.__int_var_value:tk.IntVar \
            = tk.IntVar()
        self.value = 0
        self.is_in_horizontal \
            = is_horizontal
        self.__init_components()
        self.set_title(text)
    
    def __init_components(self):
        def fn(e):
            self.value = e
        self.slider = tk.Scale(
            self.widget,
            tickinterval = 0,
            showvalue=True,
            highlightthickness=0,
            font = super().get_font(),
            command= fn
        )
        if(self.is_in_horizontal):
            self.slider.config(
                orient=tk.HORIZONTAL,
            )
        else:
            self.slider.config(
                orient=tk.VERTICAL
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
        
    def set_mark_interval(self, SIZE:int):
        self.slider.config(
            tickinterval = SIZE)

    def set_slide_distance(self, 
            SIZE_PIXEL:int)->str:
        """
        Function that assigns a 
        distance in pixels for the jump 
        of the slider marker slide.
        """
        self.slider.config(
            resolution = SIZE_PIXEL)

    def set_is_in_horizontal(self, BOOL):
        self.is_in_horizontal = BOOL
        if(BOOL):
            self.slider.config(
                orient=tk.HORIZONTAL)
        else:
            self.slider.config(
                orient=tk.VERTICAL)
            
    def get_value(self)->bool:
        return self.value
    
    def set_value(self, VALUE:bool):
        self.slider.set(VALUE)

    def set_marker_width(self, 
            SIZE_PIXEL:int):
        self.slider.config(
            sliderlength=SIZE_PIXEL
        )

    def set_bar_size(self, 
                WIDTH:int, HEIGHT:int):
        self.slider.config(
           length = WIDTH,
           width = HEIGHT
        )

    def set_slider_background_color(self, 
                COLOR:str):
        self.slider.config(
           highlightcolor= COLOR,
           bg = COLOR
        )
    
    def set_slider_foreground_color(self, 
                COLOR:str):
        self.slider.config(
           fg = COLOR
        )

    def set_bar_color(self,
            COLOR:str):
        self.slider.config(
            troughcolor = COLOR
        )

    def set_on_focus_color(self, 
            COLOR:str):
        self.slider.config(
            activebackground = COLOR
        )

    def add_on_change_listener(self, 
            CALLBACK_ARGS_X1:callable):
        self.slider.config(
            command=CALLBACK_ARGS_X1
        ) 