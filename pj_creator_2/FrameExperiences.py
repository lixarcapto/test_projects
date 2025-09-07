


from btpy.Btpy import Btpy
import tkinter as tk
from Model import Model

class FrameExperiences:

    def __init__(self, widget, model):
        self.model:Model = model
        self.frame = tk.Frame(
            widget
        )
        self.romantic_exp_cbox = Btpy.ComboBox(
            self.frame, "romantic experiences"
        )
        self.romantic_exp_cbox.grid(0, 0)
        list_ = Model\
            .romantic_experience_translator\
                .get_text_list()
        print(list_)
        self.romantic_exp_cbox.set_components(
            list_
        )
        self.add_default_listeners()

    def update_romantic_exp(self):
        k = self.romantic_exp_cbox\
            .get_value()
        self.model.character\
            .romantic_experience_k = k

    def add_default_listeners(self):
        self.romantic_exp_cbox\
            .add_change_listener(
                self.update_romantic_exp
            )