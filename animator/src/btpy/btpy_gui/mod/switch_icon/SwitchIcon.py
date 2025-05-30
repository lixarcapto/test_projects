

import tkinter as tk
from PIL import Image, ImageTk
from ..button.Button import Button
from ..tool_tip.ToolTip import ToolTip
from ..create_photo_image.create_photo_image import*

class SwitchIcon(Button):

    """
    Este modulo crea un boton binario
    que al presionarse cambiar el valor
    de una variable boolean interna. 
    Ademas contiene dos imagenes que 
    puede intercalar que representan
    al estado de la variable.
    """

    def __init__(self, window, 
                KEY:str, PATH_1:str = "",
                PATH_2:str = ""):
        super().__init__(window, "")
        self.__buffer_image_1\
            :ImageTk.PhotoImage = None
        self.__buffer_image_2\
            :ImageTk.PhotoImage = None
        self.__has_defined_size:bool \
            = False
        self.__width:int = 0
        self.__height:int = 0
        self.__value:bool = False
        self.__key:str = KEY
        self.__path_image_true:str \
            = PATH_1
        self.__path_image_false:str \
            = PATH_2
        self.__callback = None
        self.tooltip = None
        self.__init_tooltip()
        if(PATH_1 != "" 
                and PATH_2 != ""):
            self.set_path_image_true(
                PATH_1)
            self.set_path_image_false(
                PATH_2)
        self.__add_default_listener()
        self.__paint_image_false()

    def add_listener(self, 
            CALLBACK:callable):
        self.__callback = CALLBACK

    def __init_tooltip(self):
        self.tooltip = ToolTip(
            self.widget, self.__key)

    def get_value(self)->bool:
        return self.__value
    
    def set_value(self, BOOL:bool):
        self.__value = BOOL
        self.__update_image()

    def __update_image(self):
        if(self.__value):
            self.__paint_image_false()
        else:
            self.__paint_image_true()

    def __add_default_listener(self):
        def fn(e):
            if(self.__value):
                self.__value = False
            else:
                self.__value = True
            self.__update_image()
            self.__callback(e)
        self.widget.bind("<Button-1>", fn)

    def set_size(self, WIDTH:int, 
                HEIGHT:int):
        self.__has_defined_size = True
        self.__width = WIDTH
        self.__height = HEIGHT
        self.__resize_image()
        self.__update_image()

    def __resize_image(self):
        self.set_path_image_true(
            self.__path_image_true)
        self.set_path_image_false(
            self.__path_image_false)
        
    def __update_image(self):
        if(self.__value):
            self.__paint_image_true()
        else:
            self.__paint_image_false()
        
    def get_title(self)->str:
        return self.__key
        
    def set_title(self, TEXT:str):
        self.__key = TEXT
        self.__init_tooltip()

    def get_size(self)->tuple[int]:
        return (self.__width, 
                self.__height)
    
    def get_height(self)->int:
        return self.__height
        
    def set_height(self, PIXEL_SIZE:int)\
            ->None:
        self.__height = PIXEL_SIZE
        self.__resize_image()
        self.__update_image()

    def set_width(self, PIXEL_SIZE:int)\
            ->None:
        self.__width = PIXEL_SIZE
        self.__resize_image()
        self.__update_image()
    
    def get_width(self)->int:
        return self.__width

    def get_path_image_true(self)->str:
        return self.__path_image_true
    
    def get_path_image_false(self)->str:
        return self.__path_image_false
    
    def __paint_image_true(self)->None:
        self.widget.config(
            image = self.__buffer_image_1)
        
    def __paint_image_false(self)->None:
        self.widget.config(
            image = self.__buffer_image_2)

    def set_path_image_true(self, 
            PATH:str)->None:
        self.__path_image_true = PATH
        self.__buffer_image_1 \
            = create_photo_image(
                PATH,
                [self.get_width(),
                self.get_height()]
            )
        self.__update_image()
    
    def set_path_image_false(self, 
            PATH:str)->None:
        self.__path_image_false = PATH
        self.__buffer_image_2 \
            = create_photo_image(
                PATH,
                [self.get_width(),
                self.get_height()]
            )
        self.__update_image()