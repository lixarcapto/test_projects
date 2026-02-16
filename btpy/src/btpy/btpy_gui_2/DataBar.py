


import tkinter as tk

class DataBar:

    def __init__(self, widget, 
            TEXT = ""):
        self.widget = tk\
            .Canvas(
                widget,
                bg="white"
            )
        self.widget.pack()
        self.size_range = [0, 0]
        self.value = 40
        self.set_size([100, 40])

    def set_value(self, value):
        self.value = value
        self.__update()

    def __update(self):
        self.widget.create_rectangle(
            0, 0, 
            self.size_range[0], 
            self.size_range[1], 
            outline="black",
            fill="black"
        )
        self.widget.create_rectangle(
            0, 0, 
            self.value, 
            self.size_range[1], 
            outline="green",
            fill="green"
        )

    def set_size(self, size_range):
        self.size_range = size_range
        self.widget.config(
            width=size_range[0],
            height=size_range[1]
        )
        self.__update()
        