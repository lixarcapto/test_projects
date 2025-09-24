
import tkinter as tk
from PIL import Image, ImageTk
from ..on_focus_widget.OnFocusWidget import OnFocusWidget

class ButtonIconText(OnFocusWidget):

    def __init__(self, window, 
                 TITLE = ""):
        super().__init__(window)
        widget = tk.Button(
            self.margin
        )
        self.add_widget(widget)
        self.buffer_image\
            :ImageTk.PhotoImage = None
        self.set_title(TITLE)
        self.set_text_position("LEFT")

    def set_title(self, TEXT:str):
        self.widget.config(text = TEXT)

    def get_title(self)->str:
        return self.widget.cget("text")

    def set_text_position(self, 
            POSITION_KEY:str):
        """
        * "TOP"
        * "LEFT"
        * "BOTTOM"
        * "RIGHT"
        """
        if(POSITION_KEY == "TOP"):
            self.widget.config(
                compound=tk.TOP)
        elif(POSITION_KEY == "LEFT"):
            self.widget.config(
                compound=tk.LEFT)
        elif(POSITION_KEY == "BOTTOM"):
            self.widget.config(
                compound=tk.BOTTOM)
        elif(POSITION_KEY == "RIGHT"):
            self.widget.config(
                compound=tk.RIGHT)


    def paint_image(self, PATH:str)->None:
        imagen_pil = Image.open(PATH)
        imagen_tk = ImageTk.PhotoImage(
            imagen_pil)
        self.buffer_image = imagen_tk
        self.widget.config(image=imagen_tk)