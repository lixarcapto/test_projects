
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from PIL import Image, ImageTk

class ButtonIconText(WidgetStandard):

    def __init__(self, window, 
                 TITLE = ""):
        super().__init__(window)
        self.button = tk.Button(
            self.margin
        )
        self.button.pack(
            padx=1, 
            pady=(2, 1)
        )
        self.buffer_image\
            :ImageTk.PhotoImage = None
        self.set_title(TITLE)
        self.set_text_position("LEFT")

    def set_title(self, TEXT:str):
        self.button.config(text = TEXT)

    def get_title(self)->str:
        return self.button.cget("text")

    def set_text_position(self, 
            POSITION_KEY:str):
        """
        * "TOP"
        * "LEFT"
        * "BOTTOM"
        * "RIGHT"
        """
        if(POSITION_KEY == "TOP"):
            self.button.config(
                compound=tk.TOP)
        elif(POSITION_KEY == "LEFT"):
            self.button.config(
                compound=tk.LEFT)
        elif(POSITION_KEY == "BOTTOM"):
            self.button.config(
                compound=tk.BOTTOM)
        elif(POSITION_KEY == "RIGHT"):
            self.button.config(
                compound=tk.RIGHT)


    def paint_image(self, PATH:str)->None:
        imagen_pil = Image.open(PATH)
        imagen_tk = ImageTk.PhotoImage(
            imagen_pil)
        self.buffer_image = imagen_tk
        self.button.config(image=imagen_tk)

    def add_listener(self, CALLBACK)->None:
        self.button.config(
            command = CALLBACK)