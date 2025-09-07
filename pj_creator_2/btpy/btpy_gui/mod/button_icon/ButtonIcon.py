
import tkinter as tk
from PIL import Image, ImageTk
from ..button.Button import Button
from ..tool_tip.ToolTip import ToolTip
from ...mod.create_photo_image.create_photo_image import*
from ..create_photo_image.create_photo_image import*
from ....btpy_persistence.mod.get_root.get_root import*


class ButtonIcon(Button):

    """
    Este modulo crea un boton con 
    una imagen de icono principalmente
    sin texto.
    """

    def __init__(self, window, 
                TITLE:str, PATH = ""):
        super().__init__(window, "")
        self.__buffer_image\
            :ImageTk.PhotoImage = None
        self.__has_defined_size:bool = False
        self.__width:int = 0
        self.__title = TITLE
        self.__height:int = 0
        self.__path_image:str = PATH
        self.tooltip = None
        self.__init_tooltip()
        if(PATH != ""):
            self.set_path_image(PATH)

    def add_listener(self, CALLBACK):
        self.widget.bind("<Button-1>", 
            CALLBACK)

    def set_title(self, TEXT:str):
        self.__title = TEXT

    def get_title(self)->str:
        return self.__title

    def get_path_image(self)->str:
        return self.__path_image

    def set_size_image(self, WIDTH:int, 
                HEIGHT:int):
        self.__has_defined_size = True
        self.__width = WIDTH
        self.__height = HEIGHT
        self.__resize_image()

    def __resize_image(self):
        self.set_path_image(
            self.__path_image)
        
    def __init_tooltip(self):
        self.tooltip = ToolTip(
            self.widget, self.__title)

    def get_size_image(self)->tuple[int]:
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

    def set_path_image(self, PATH:str)\
            ->None:
        self.__path_image = PATH
        if(self.__has_defined_size):
            self.__buffer_image \
                = create_photo_image(
                    PATH,
                    [
                    self.__width, 
                    self.__height
                    ]
                )
        else:
            self.__buffer_image \
                = create_photo_image(
                    PATH
                )
        self.widget.config(
            image=self.__buffer_image)