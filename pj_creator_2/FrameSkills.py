

from btpy.Btpy import Btpy
import tkinter as tk
from Model import Model

class FrameSkills:

    def __init__(self, widget, model):
        self.model:Model = model
        self.frame = tk.Frame(
            widget
        )
        self.skill_check_box = Btpy.CheckBox(
            self.frame, "Skills"
        )
        self.skill_check_box.grid(0, 0)
        list_ = Model.skill_translator\
            .get_keys()
        self.skill_check_box.set_components(
            list_
        )
        list_ = Model.skill_translator\
            .get_text_list()
        self.skill_check_box.set_content(
            list_
        )
        self.skill_check_box.set_columns(4)
        def fn():
            list_ = self.skill_check_box\
                .get_value()
            self.model.character\
                .skills_list = list_
        self.skill_check_box.add_change_listener(
            fn
        )