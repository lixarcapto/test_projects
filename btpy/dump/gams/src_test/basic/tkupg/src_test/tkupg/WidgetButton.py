

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

    def set_image(self, route:str):
        img = tkinter.PhotoImage(file=route)
        self.widget.config(image = self.img)

    def set_photo(self, photoimage):
        self.img = photoimage
        self.widget.config(image = self.img)

    def add_listener(self, function):
        self.widget.config(command=function)

    def add_button_press(self, function):
        self.widget.bind("<ButtonPress>", 
            function)
