

import tkinter as tk
from PIL import Image, ImageTk
from ..widget_standard.WidgetStandard import WidgetStandard

class LabelImage(WidgetStandard):

    def __init__(self, window, 
            PATH:str = ""):
        super().__init__()
        self.widget = tk.Label(
                window.widget)
        self.__buffer_image:ImageTk = None
        if(PATH != ""):
            self.paint_image(PATH)

    def paint_image(self, PATH:str)->None:
        imagen_pil = Image.open(PATH)
        imagen_tk = ImageTk.PhotoImage(
            imagen_pil)
        self.widget.config(image=imagen_tk)
        self.__buffer_image = imagen_tk

    def pack(self):
        self.widget.pack(pady=5)