
from ..swiper_standard.SwiperStandard import SwiperStandard
import tkinter as tk
from ..label_image.LabelImage import LabelImage
from ..simple_card.SimpleCard import SimpleCard

class SwiperCard(SwiperStandard):

    """
    Este es un modulo que crea un 
    deslizador de imagenes de una manera
    facil y comoda.
    """

    def __init__(self, window, 
            TEXT:str = ""):
        super().__init__(window, TEXT)
        self.card = SimpleCard(
            self.get_center_frame(),
            "vertical",
            False
        )
        # dibujar -----------------------
        self.card.draw_in_direction()
        self.icon_size_list = [200, 200]
        def fn():
            card_dict = self.get_value()
            print("card_dict", card_dict)
            self.card.set_title(
                card_dict["title"])
            self.card.set_icon(
                card_dict["path"],
                self.icon_size_list
            )
            self.card.set_description(
                card_dict["description"])
        self.set_update_callback(fn)
