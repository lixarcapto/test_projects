


from tkinter import ttk
import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame

class PatternInput(WidgetComposite):

    def __init__(self, window, title:str,
            size = 5):
        super().__init__(window, False)
        self.button_list:list = []
        self.limit = 10
        self.__init_components(size)
        self.callback = None
        self.key_right = []
        self.key_list = []
        self.set_title(title)

    def set_key_right(self, key_list):
        self.key_right = key_list

    def add_listener(self, CALLBACK):
        self.callback = CALLBACK

    def __init_components(self, side_size):
        button = None
        total = side_size * side_size
        for i in range(total):
            button = tk.Button(
                self.widget,
                text = f"      "
            )
            self.button_list.append(
                button)
        n = 0
        for x in range(side_size):
            for y in range(side_size):
                print(f"x {x}", f"y {y}")
                self.button_list[n]\
                    .grid(
                        row = x, 
                        column = y
                    )
                n += 1
        # add listeners
        for i in range(total):
            button = self.button_list[i]
            def aux(number):
                def fn():
                    print("n ", number)
                    self.react_to_press(
                        number)
                return fn
            button.config(
                command = aux(i))
            
    def is_full(self):
        if(len(self.key_list) < self.limit):
            return False
        return True
    
    def format_buttons(self):
        button = None
        for i in range(len(self.button_list)):
            button = self.button_list[i]
            button.config(bg = "#EEEEEE")
        self.key_list = []
            
    def react_to_press(self, KEY:int):
        if(not self.is_full()):
            self.key_list.append(KEY)
            self.button_list[KEY]\
                .config(bg = "gray")
        if(self.key_is_right()):
            if(self.callback != None):
                self.callback()
                self.format_buttons()
        if(self.is_full()):
            self.format_buttons()

    def key_is_right(self):
        if(self.key_right \
                    == list(self.key_list)):
            return True
        return False
