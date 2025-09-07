


from btpy.Btpy import Btpy
import tkinter as tk
from Model import Model

class FrameConfig:

    def __init__(self, widget, model):
        self.model:Model = model
        self.frame = tk.Frame(
            widget
        )
        # -----------------------------
        # SAVE
        self.button_save = Btpy.Button(
            self.frame, "Save"
        )
        self.button_save.grid(0, 0, "ew")
        def fn():
            self.model.save_as_docx()
        self.button_save.add_listener(fn)
        # ------------------------------
        # GENDER
        self.lenguage_cbox = Btpy.ComboBox(
            self.frame, "Lenguage"
        )
        self.lenguage_cbox.grid(1, 0, "ew")
        self.lenguage_cbox.set_components(
            Model.lenguage_keys
        )
        self.lenguage_cbox\
            .add_change_listener(
                self.change_lenguage_key
            )
        # ------------------------------

    def change_lenguage_key(self):
        key = self.lenguage_cbox.get_value()
        self.model.save_lenguage_key()
        self.model.set_lenguage_key(key)