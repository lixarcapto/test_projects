
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from PIL import Image, ImageTk

class ButtonIcon(WidgetStandard):

    def __init__(self, window, PATH = ""):
        super().__init__()
        self.widget = tk.Button(
            window.widget
        )
        self.buffer_image\
            :ImageTk.PhotoImage = None
        if(PATH != ""):
            self.paint_image(PATH)

    def paint_image(self, PATH:str)->None:
        imagen_pil = Image.open(PATH)
        imagen_tk = ImageTk.PhotoImage(
            imagen_pil)
        self.buffer_image = imagen_tk
        self.widget.config(image=imagen_tk)

    def add_listener(self, CALLBACK)->None:
        self.widget.config(
            command = CALLBACK)