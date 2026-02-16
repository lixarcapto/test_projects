


from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

class ChipInput:

    def __init__(self, widget, 
            TITLE:str = ""):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid"
        )
        self.widget.pack()
        self.frame_options = tk.Frame(
            self.widget,
            borderwidth=1,
            relief="solid"
        )
        self.frame_options.pack()
        self.frame_selected = tk.Frame(
            self.widget,
        )
        self.frame_selected.pack()
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.button_list = []
        self.key_list = []
        self.key_selected = []
        self.button_selected_dict = {}

    def clean_options(self):
        key_to_delete_arr = []
        for k in self.button_list:
            key_to_delete_arr.append(k)
        for k in key_to_delete_arr:
            self.button_list[k]\
                .grid_forget()
            del(self.button_list[k])

    def set_components(self, KEY_LIST):
        self.clean_options()
        self.key_list = KEY_LIST
        button = None
        for k in KEY_LIST:
            button = tk.Button(
                self.frame_options,
                text = k,
                font = self.default_font
            )
            self.button_list.append(
                button
            )
            def aux(k):
                def fn():
                    self.press_option(k)
                return fn
            button.config(
                command = aux(k)
            )
        self.__sort_components()

    def clean_selected(self):
        self.key_selected = []
        key_to_delete_arr = []
        for k in self.button_selected_dict:
            key_to_delete_arr.append(k)
        for k in key_to_delete_arr:
            self.button_selected_dict[k]\
                .grid_forget()
            del(self\
                .button_selected_dict[k])

    def destroy_option(self, KEY):
        idx = self.key_selected\
            .index(KEY)
        del(self.key_selected[idx])
        self.button_selected_dict[KEY]\
            .grid_forget()
        del(self.button_selected_dict[KEY])

    def press_option(self,
            KEY):
        if(KEY in self.key_selected):
            return None
        button = tk.Button(
                self.frame_selected,
                text = KEY,
                font = self.default_font,
                background="red",
                foreground="white"
            )
        def aux(KEY):
            def fn():
                self.destroy_option(KEY)
            return fn
        button.config(
            command = aux(KEY)
        )
        self.button_selected_dict\
            [KEY] = button
        self.key_selected.append(KEY)
        self.__sort_button_selected()

    def __sort_components(self):
        n = 0
        for button in self.button_list:
            button.grid(
                row = 0, column = n
            )
            n += 1

    def __sort_button_selected(self):
        n = 0
        button = None
        for k in self.button_selected_dict:
            button = self\
                .button_selected_dict[k]
            button.grid(
                row = 0, column = n
            )
            n += 1

    def get_value(self):
        return self.key_selected
            
    def set_value(self, KEY_LIST):
        self.clean_selected()
        for k in KEY_LIST:
            self.press_option(k)