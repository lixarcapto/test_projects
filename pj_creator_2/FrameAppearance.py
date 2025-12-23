

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
        self.hair_color_cbox = Btpy.ComboBox(
            self.frame, "Hair color"
        )
        self.hair_color_cbox.grid(1, 0)
        self.hair_style_cbox = Btpy.ComboBox(
            self.frame, "Hair style"
        )
        self.hair_style_cbox.grid(2, 0)
        self.load_data()
        self.add_listener_update()

    def add_listener_update(self):
        self.skin_cbox.add_change_listener(
            self.update_data
        )
        self.hair_color_cbox.add_change_listener(
            self.update_data
        )
        self.hair_style_cbox.add_change_listener(
            self.update_data
        )

    def update_data(self):
        k = self.skin_cbox.get_value()
        self.model.character.skin_color = k
        k = self.hair_color_cbox.get_value()
        self.model.character.hair_color = k
        k = self.hair_style_cbox.get_value()
        self.model.character.hair_style = k

    def load_data(self):
        list_ = Model.skin_translator\
            .get_keys()
        self.skin_cbox.set_components(
            list_
        )
        list_ = Model.hair_color_translator\
            .get_keys()
        self.hair_color_cbox.set_components(
            list_
        )
        list_ = Model.hair_style_translator\
            .get_keys()
        self.hair_style_cbox.set_components(
            list_
        )