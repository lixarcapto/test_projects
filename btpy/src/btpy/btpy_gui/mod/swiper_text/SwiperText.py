
from ..swiper_standard.SwiperStandard import SwiperStandard
import tkinter as tk

class SwiperText(SwiperStandard):

    def __init__(self, window, 
            TEXT:str = ""):
        super().__init__(window, TEXT)
        self.label_text = tk.Label(
            self.get_center_frame().widget)
        def fn():
            e = self.get_index_element()
            self.label_text.config(
                text = e)
        self.set_update_callback(fn)

    def pack(self):
        super().pack()
        self.label_text.pack()
        