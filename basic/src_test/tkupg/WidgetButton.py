

from .WidgetElementText import WidgetElementText
import tkinter

class WidgetButton(WidgetElementText):

    def __init__(self, window_tk):
        self.widget = tkinter.Button(
            window_tk.widget)
        super().default_config()
        self.img = None

    def set_text(self, string):
        self.widget.config(text=string)

    def add_listener(self, function):
        self.widget.config(command=function)

    def add_button_press(self, function):
        self.widget.bind("<ButtonPress>", 
            function)
