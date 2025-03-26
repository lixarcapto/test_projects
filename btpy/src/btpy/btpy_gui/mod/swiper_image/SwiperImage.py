
from ..swiper_standard.SwiperStandard import SwiperStandard
import tkinter as tk
from ..label_image.LabelImage import LabelImage

class SwiperImage(SwiperStandard):

    """
    Este es un modulo que crea un 
    deslizador de imagenes de una manera
    facil y comoda.
    """

    def __init__(self, window, 
            TEXT:str = ""):
        super().__init__(window, TEXT)
        self.label_image = LabelImage(
            self.get_center_frame())
        def fn():
            e = self.get_index_element()
            self.label_image.set_path_image(
                e
            )
        self.set_update_callback(fn)

    def set_image_size(self, WIDTH:int, 
                HEIGHT:int):
        self.label_image.set_size(WIDTH,
            HEIGHT)

    def pack(self):
        super().pack()
        self.label_image.pack()