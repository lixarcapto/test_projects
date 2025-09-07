


from btpy.Btpy import Btpy
import tkinter as tk
from Model import Model

class FrameTraits:

    def __init__(self, widget, model):
        self.model:Model = model
        self.frame = tk.Frame(
            widget
        )
        self.archetipe_cbox = Btpy.ComboBox(
            self.frame, "Archetype"
        )
        self.archetipe_cbox.grid(0, 0)
        list_ = self.model\
            .get_personality_tropes_keys()
        self.archetipe_cbox.set_components(
            list_
        )
        self.trait_slider_box = Btpy.SliderBox(
            self.frame, 
            "traits"
        )
        self.trait_slider_box.grid(1, 0)
        list_ = self.model.traits_keys_ttr\
            .get_keys()
        self.trait_slider_box.set_components(
            list_
        )
        list_ = self.model.traits_keys_ttr\
            .get_text_list()
        self.trait_slider_box.set_content(
            list_
        )
        self.trait_slider_box\
            .set_range_for_all([-1, 1])
        self.trait_slider_box\
            .set_value_for_all(0)
        self.trait_slider_box\
            .set_columns(3)
        def fn():
            dict_ = self.trait_slider_box\
                .get_value()
            self.model.character\
                .traits_dict = dict_
            print("update traits")
        self.trait_slider_box\
            .add_change_listener(fn)
        self.archetipe_cbox\
            .add_change_listener(
                self.update_archetype
            )
        
    def update_archetype(self):
        key = self.archetipe_cbox\
            .get_value()
        dict_ = Model\
            .personality_trope_dict[key]
        self.trait_slider_box.set_value(
            dict_
        )

    def pack(self):
        self.frame.pack()
