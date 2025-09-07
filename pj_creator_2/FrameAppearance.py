

from btpy.Btpy import Btpy
import tkinter as tk
from Model import Model

class FrameAppearance:

    def __init__(self, widget, model):
        self.model:Model = model
        self.frame = tk.Frame(
            widget
        )
        self.skin_cbox = Btpy.ComboBox(
            self.frame, "Skin"
        )
        self.skin_cbox.grid(0, 0)
        self.load_data()

    def load_data(self):
        list_ = Model.skin_translator\
            .get_keys()
        self.skin_cbox.set_components(
            list_
        )