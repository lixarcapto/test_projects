


from .WidgetElementText import WidgetElementText
import tkinter
from PIL import ImageTk

class WidgetIcon(WidgetElementText):

    def __init__(self, window_tk, 
            route):
        self.widget = tkinter.Label(
            window_tk.widget)
        self.set_image(route)
        self.set_background("red")

    def set_photo(self, photoimage):
        self.img = photoimage
        self.widget.config(image = self.img)

    def set_image(self, route:str):
        self.img = tkinter.PhotoImage(file=route)
        self.widget.config(image = self.img)


    def set_text(self, string):
        self.widget.config(text=string)

    def add_text(self, new_text):
        text = self.widget.cget("text")
        text += new_text
        self.widget.config(text=text)
        

    def get_text(self):
        return self.widget.cget("text")

    def extract_text(self):
        text = self.widget.cget("text")
        self.widget.config(text="")
        return text
