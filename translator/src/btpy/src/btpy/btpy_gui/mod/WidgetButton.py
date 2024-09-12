

from .WidgetTextual import WidgetTextual
import tkinter

class WidgetButton(WidgetTextual):

    def __init__(self, window_tk):
        self.widget = tkinter.Button(
            window_tk.widget)
        super().default_config()
        self.img = None

    def add_listener(self, function):
        self.widget.config(command=function)

    def add_click_listener(self, function):
        """
         función que añade un listener 
         a los clics del Mouse
        """
        self.widget.bind("<ButtonPress>", 
            function)