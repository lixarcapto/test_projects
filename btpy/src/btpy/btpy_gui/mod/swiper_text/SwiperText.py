
from ..swiper_standard.SwiperStandard import SwiperStandard
import tkinter as tk

class SwiperText(SwiperStandard):

    def __init__(self, window, 
            TEXT:str = ""):
        super().__init__(window, TEXT)
        self.label_text = None
        self.__init_components()
        def fn():
            e = self.get_value()
            self.label_text.config(
                text = e)
        self.set_update_callback(fn)
        
    def __init_components(self):
        self.label_text = tk.Label(
            self.get_center_frame().widget)
        # dibujar -----------------------
        self.label_text.pack()
        