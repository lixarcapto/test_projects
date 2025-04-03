
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ...mod.create_photo_image.create_photo_image import*
from ....btpy_transformers.mod.RGB_to_hex.RGB_to_hex import*

class ButtonIconOverlay(WidgetStandard):

    def __init__(self, window):
        super().__init__()
        # Crear el Canvas
        self.widget = tk.Canvas(
            window.widget,
            bg="white")
        self.buffer_image = None
        self.path = ""
        self.title = ""
        self.size_font = 20
        self.text_color = "red"
        self.height = 0
        self.width = 0
        self.callback = None
        self.add_default_listener()

    def pack(self):
        self.widget.pack()

    def add_default_listener(self):
        def fn(e):
            self.draw_rgba_rectangle()
            if(self.callback != None):
                self.callback(e)
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

    

    def __update(self):
        self.widget.delete("all")
        if(self.path != ""):
            self.draw_image(self.path)
        if(self.title != ""):
            self.draw_text(self.title,
            self.size_font)
        
    def set_path(self, PATH):
        self.path = PATH
        self.__update()
        
    def set_text(self, TEXT):
        self.title = TEXT
        self.__update()
        
    def set_size(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        self.widget.config(
            width=WIDTH, 
            height=HEIGHT
        )

    def add_listener(self, CALLBACK):
        self.callback = CALLBACK
        
    def draw_image(self, PATH):
        photo_image = create_photo_image(
            PATH, [
                self.width,
                self.height
            ]
        )
        self.buffer_image = photo_image
        self.widget.create_image(
            (self.width / 2) + 2, 
            (self.height / 2) + 2, 
            image=photo_image
        )
        
    def draw_text(self, TEXT, SIZE):
        self.widget.create_text(
            self.width / 2, 
            self.height / 2, 
            text=TEXT,
            fill=self.text_color,
            font=("Arial", 
                  SIZE, 
                  "bold"
            )
        )

    def draw_rgba_rectangle(self):
        self.widget.create_rectangle(
            0  + 3, 0  + 3, 
            self.width, 
            self.height, 
            outline="black",
            width= 3
        )