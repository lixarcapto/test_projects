


from .WidgetElement import WidgetElement
import tkinter.font
from PIL import ImageTk

class WidgetElementText(WidgetElement):

    def set_foreground(self, color):
        color = self.get_color(color)
        super().default_config()
        self.widget.config(fg=color)

    def set_font(self, font_name, size, 
                 style = "roman"):
        new_font = tkinter.font.Font(
            family=font_name, 
            size=size, 
            slant=style
        )
        self.widget.config(
            font=new_font)

    def set_text(self, text):
        pass

    def add_text(self, text):
        pass

    def get_text(self):
        pass

    def extract_text(self):
        pass

    def set_photo(self, photoimage):
        self.img = photoimage
        self.widget.config(image = self.img)

    def set_image(self, route:str):
        self.img = tkinter.PhotoImage(file=route)
        self.widget.config(image = self.img)
