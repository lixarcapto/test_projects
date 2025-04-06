
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ...mod.create_photo_image.create_photo_image import*
from ....btpy_transformers.mod.RGB_to_hex.RGB_to_hex import*
from ..get_image_size.get_image_size import*

class ButtonIconOverlay(WidgetStandard):

    """
    Component that creates a button 
    with a background image and overlay 
    text that, when pressed, creates a 
    colored border while the click event 
    is active.
    """

    def __init__(self, window, 
            TITLE:str = "", PATH:str = ""):
        super().__init__()
        # Crear el Canvas
        self.widget = tk.Canvas(
            window.widget,
            bg="white")
        self.__buffer_image = None
        self.__path:str = ""
        self.__title:str = ""
        self.__size_font:int = 20
        self.__foreground_color:str = "red"
        self.__height:int = 0
        self.__width:int = 0
        self.__callback:callable = None
        self.__add_default_listener()
        if(TITLE != ""):
            self.set_title(TITLE)
        if(PATH != ""):
            self.set_path_image(PATH)

    def __add_default_listener(self):
        def fn(e):
            self.__draw_rgba_rectangle()
            if(self.__callback != None):
                self.__callback(e)
        self.widget.bind(
            "<Button-1>", 
            fn
        )
        def fn(e):
            self.__update()
        self.widget.bind(
            "<ButtonRelease-1>", 
            fn
        )

    def set_font_size(self, SIZE:int):
        self.__size_font = SIZE

    def get_font_size(self)->int:
        return self.__size_font
    
    def set_foreground_color(self, COLOR):
        self.__foreground_color = COLOR

    def get_foreground_color(self):
        return self.__foreground_color

    def __update(self):
        self.widget.delete("all")
        if(self.__path != ""):
            self.__draw_image(self.__path)
        if(self.__title != ""):
            self.__draw_text(self.__title,
            self.__size_font)
        
    def set_path_image(self, PATH:str)\
            ->None:
        """
        Function that assigns a background 
        image to the button using a path.
        """
        self.__path = PATH
        # 
        if(self.__width == 0 
        and self.__height == 0):
            self.use_size_image()
        self.__update()

    def use_size_image(self):
        size_list = get_image_size(
            self.__path)
        self.set_size(size_list[0], 
            size_list[1])
        self.resize()
        
    def set_title(self, TEXT:str)->None:
        """
        Function that assigns a title 
        to the component label.
        """
        self.__title = TEXT
        self.__update()

    def get_title(self, TEXT:str)->str:
        return self.__title
    
    def resize(self):
        self.widget.config(
            width=self.__width, 
            height=self.__height
        )
        
    def set_size(self, WIDTH, HEIGHT):
        self.__width = WIDTH
        self.__height = HEIGHT
        self.__use_auto_size = False
        self.resize()

    def add_listener(self, CALLBACK):
        self.__callback = CALLBACK
        
    def __draw_image(self, PATH):
        photo_image = create_photo_image(
            PATH, [
                self.__width,
                self.__height
            ]
        )
        self.__buffer_image = photo_image
        self.widget.create_image(
            (self.__width / 2) + 2, 
            (self.__height / 2) + 2, 
            image=photo_image
        )
        
    def __draw_text(self, TEXT, SIZE):
        self.widget.create_text(
            self.__width / 2, 
            self.__height / 2, 
            text=TEXT,
            fill=self.__foreground_color,
            font=("Arial", 
                  SIZE, 
                  "bold"
            )
        )

    def __draw_rgba_rectangle(self):
        self.widget.create_rectangle(
            0  + 3, 0  + 3, 
            self.__width, 
            self.__height, 
            outline="black",
            width= 3
        )