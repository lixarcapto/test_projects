

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard


class SwipperNumber(WidgetStandard):

    def __init__(self, window, TEXT = ""):
        super().__init__()
        self.widget = tk.Frame(
            window.widget,
            borderwidth = 1,
            relief= "solid"
        )
        self.__value:int|float = 0
        self.__increment = 1
        self.__range_list:list = [0, 1]
        self.label = None
        self.button_down = None
        self.label_number = None
        self.button_up = None
        self.__init_components()
        self.__init_default_listener()
        self.set_text(TEXT)
        self.__update_label_number()

    def __init_components(self):
        self.label = tk.Label(
            self.widget)
        self.button_down = tk.Button(
            self.widget, text = "<")
        self.label_number = tk.Label(
            self.widget
        )
        self.button_up = tk.Button(
            self.widget, text = ">")
        self.label.grid(row=0, column=0, padx=5, pady=5)
        self.button_down.grid(row=0, column=1, padx=5, pady=5)
        self.label_number.grid(row=0, column=2, padx=5, pady=5)
        self.button_up.grid(row=0, column=3, padx=5, pady=5)

    def set_text(self, TEXT:str):
        self.label.config(text = TEXT)

    def get_increment(self)->int|float:
        return self.__increment
    
    def set_increment(self, 
            INCREMENT:int|float)-> None:
        self.__increment = INCREMENT

    def set_range_list(self, RANGE_LIST
            :list[int|float]):
        self.__range_list = RANGE_LIST
        self.__value = RANGE_LIST[0]
        self.__update_label_number()
        
    def __init_default_listener(self):
        self.__add_increment_listener()
        self.__add_decrement_listener()

    def __update_label_number(self):
        self.label_number.config(
            text = f" {self.__value} ")
        
    def __add_increment_listener(self):
        def increment():
            result = self.__value + self\
                .__increment
            maximum = self.__range_list[1]
            if(maximum > result):
                self.__value = result
            else:
                self.__value = maximum
            self.__update_label_number()
        self.button_up.config(
            command=increment)
        
    def __add_decrement_listener(self):
        def decrement():
            result = self.__value - self\
                .__increment
            minimum = self.__range_list[0]
            if(minimum < result):
                self.__value = result
            else:
                self.__value = minimum
            self.__update_label_number()
        self.button_down.config(
            command=decrement)
        
    def pack(self):
        self.widget.pack()