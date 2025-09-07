

import tkinter as tk
from PIL import Image, ImageTk
from ..widget_standard.WidgetStandard import WidgetStandard

class LabelImage(WidgetStandard):

    """
    This widget is used to write text 
    or draw a single image; it can't 
    contain both. It takes up slightly 
    more memory than label.
    """

    def __init__(self, window, 
            TITLE:str = ""):
        super().__init__(window)
        self.widget = tk.Label(
                self.margin)
        self.widget.pack(
            padx=1, 
            pady=1,
            fill=tk.BOTH,
            expand = True
        )
        self.__buffer_image:ImageTk = None
        self.__has_defined_size:bool = False
        self.__has_image:bool = False
        self.__width:int = 0
        self.__height:int = 0
        self.__path_image:str = ""
        self.set_title(TITLE)

    def set_title(self, TEXT:str)->None:
        self.widget.config(text = TEXT)
        self.widget.config(image = "")
        self.__buffer_image = None

    def get_path_image(self)->str:
        return self.__path_image

    def set_size(self, WIDTH:int, 
                HEIGHT:int):
        self.__has_defined_size = True
        self.__width = WIDTH
        self.__height = HEIGHT

    def __resize_image(self):
        if(not self.__has_image): 
            return None
        self.set_path_image(
            self.__path_image)

    def get_size(self)->tuple[int]:
        return (self.__height, self.widget)
    
    def get_height(self)->int:
        return self.__height
    
    def get_width(self)->int:
        return self.__width

    def set_path_image(self, PATH:str)\
            ->None:
        self.widget.config(text = "")
        self.__has_image = True
        self.__path_image = PATH
        self.__update_image()
        
    def __update_image(self):
        imagen_pil = Image.open(
            self.__path_image)
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