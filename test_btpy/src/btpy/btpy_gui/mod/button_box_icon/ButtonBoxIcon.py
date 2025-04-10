


import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame
from ..create_photo_image.create_photo_image import*

class ButtonBoxIcon(WidgetComposite):

    """
    Este componente sirve para crear
    un grid de botones de tipo icono 
    de forma facil y rapida.
    """

    def __init__(self, window, title:str):
        super().__init__(window)
        self.grid_size:int = 1
        self.__button_icon_dict:dict = {}
        self.set_title(title)
        self.buffer_image_list = []

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT)
        
    def get_title(self)->str:
        return self.label_title.cget("text")
        
    def set_grid_size(self, SIZE:int):
        self.grid_size = SIZE

    def set_content(self, 
            KEY_LIST:list[str], 
            PATH_LIST:list[str]
        ):
        """
        Funcion que crea una lista de 
        botones de tipo icono recibiendo
        una lista de claves y rutas
        de imagenes para cada boton.
        """
        self.__create_button_dict(
            KEY_LIST,
            PATH_LIST
        )
        self.__arrange_button_dict()

    def __create_button_dict(self, 
            KEY_LIST:list[str], 
            PATH_LIST:list[str])->None:
        self.__button_icon_dict = {}
        self.buffer_image_list = []
        button = None
        n = 0
        image = None
        for k in KEY_LIST:
            image = create_photo_image(
                PATH_LIST[n])
            self.buffer_image_list.append(
                image
            )
            button = tk.Button(
                self.widget,
                text = k,
                image = image,
                bg = "gray"
            )
            self.__button_icon_dict[k] \
                = button
            n += 1
            
    def add_listener_to(self, 
            KEY_BUTTON:str, 
            CALLBACK:callable):
        button = self.__button_icon_dict\
            [KEY_BUTTON]
        button.bind("<Button-1>", 
            CALLBACK)
            
    def add_single_listener(self, 
                CALLBACK:callable):
        """
        Esta funcion recibe una callback
        que ejecutara el boton cada
        vez que se presione enviando
        el texto identificador del boton
        como argumento. Sirve para
        crear un listener unico para
        todos los botones.
        """
        button = None
        for k in self.__button_icon_dict:
            button = self.__button_icon_dict[k]
            def aux(key):
                def fn():
                    CALLBACK(key)
                return fn
            button.config(
                command = aux(k)
            )

    def __arrange_button_dict(self):
        x:int = 0
        y:int = 0
        button = None
        for k in self.__button_icon_dict:
            button = self.__button_icon_dict[k] 
            button.grid(
                row=x, column=y,
                sticky=tk.NSEW
            )
            x += 1
            if(x == self.grid_size):
                y += 1
                x = 0
            