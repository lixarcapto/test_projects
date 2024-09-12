

from btpy.src.btpy.Btpy import Btpy
import tkinter as tk

class View:

    def __init__(self) -> None:
        self.window = Btpy.Window()
        self.window.set_size([700, 700])
        self.label_arr = []
        self.combo_arr = []
        self.limit_label_combo = 60
        self.size_column = 20
        self.button = None
        self.button_random = None
        # opciones seleccionables
        self.option_dict = {}
        self.init_label_combo()
    
    def start(self):
        self.window.start()

    def render_in_label_combo(self):
        i = 0
        for k in self.option_dict:
            self.label_arr[i].set_text(k)
            self.combo_arr[i].set_option_list(
                self.option_dict[k])
            i += 1


    def render(self, render_dict):
        self.option_dict = render_dict[
            "OPTION_DICT"
        ]
        self.render_in_label_combo()

    def request(self):
        char_dict = self.get_selected_dict()
        view_message = {}
        view_message["character_dict"] \
            = char_dict
        return view_message

    def get_selected_dict(self)->dict:
        char_dict = {}
        for i, k in enumerate(self.option_dict):
            char_dict[k]= self.combo_arr[i]\
                .get_selected()
        return char_dict

    def init_label_combo(self):
        label = None
        combo = None
        x = 0
        y = 0
        for i in range(self.limit_label_combo):
            label = Btpy.Label(self.window)
            label.widget.grid(
                row=x, 
                column=y
            )
            self.label_arr.append(label)
            combo = Btpy.Combobox(self.window)
            combo.widget.grid(
                row=x, 
                column=y +1
            )
            self.combo_arr.append(combo)
            if(x >= self.size_column):
                x = 0
                y += 2
            else:
                x += 1
        self.button = Btpy.Button(self.window)
        self.button.set_text("print")
        x = self.size_column + 1
        self.button.widget.grid(
                row=x, 
                column=0
        )
        self.button_random = Btpy.Button(self.window)
        self.button_random.set_text(
            "random")
        x = self.size_column + 2
        self.button_random.widget.grid(
                row=x, 
                column=0
        )
        