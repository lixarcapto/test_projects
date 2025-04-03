
import tkinter as tk
from PIL import Image, ImageTk
from ..button.Button import Button
from ..tool_tip.ToolTip import ToolTip

class ButtonIcon(Button):

    """
    Este modulo crea un boton con 
    una imagen de icono principalmente
    sin texto.
    """

    def __init__(self, window, 
                KEY:str, PATH = ""):
        super().__init__(window, "")
        self.__buffer_image\
            :ImageTk.PhotoImage = None
        self.__has_defined_size:bool = False
        self.__width:int = 0
        self.key = KEY
        self.__height:int = 0
        self.__path_image:str = PATH
        self.tooltip = ToolTip(
            self.widget, self.key)
        if(PATH != ""):
            self.set_path_image(PATH)

    def get_path_image(self)->str:
        return self.__path_image

    def set_size(self, WIDTH:int, 
                HEIGHT:int):
        self.__has_defined_size = True
        self.__width = WIDTH
        self.__height = HEIGHT
        self.__resize_image()

    def __resize_image(self):
        self.set_path_image(
            self.__path_image)

    def get_size(self)->tuple[int]:
        return (self.__height, self.widget)
    
    def get_height(self)->int:
        return self.__height
        
    def set_height(self, PIXEL_SIZE:int)\
            ->None:
        self.__height = PIXEL_SIZE
        self.__resize_image()

    def add_listener(self, 
            CALLBACK:callable):
        self.widget.bind("<Button-1>", 
                CALLBACK)

    def set_width(self, PIXEL_SIZE:int)\
            ->None:
        self.__width = PIXEL_SIZE
        self.__resize_image()
    
    def get_width(self)->int:
        return self.__width
        self.__resize_image()

    def set_path_image(self, PATH:str)\
            ->None:
        self.__path_image = PATH
        imagen_pil = Image.open(PATH)
        if(self.__has_defined_size):
            imagen_pil = imagen_pil\
                    .resize((
                self.__width, 
                self.__height
            ))
        imagen_tk = ImageTk.PhotoImage(
            imagen_pil)
        self.__buffer_image = imagen_tk
        self.widget.config(
            image=imagen_tk)