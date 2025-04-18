


import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame
from ..create_photo_image.create_photo_image import*
from ..sort_in_grid.sort_in_grid import*

class ButtonBoxIcon(WidgetComposite):

    """
    Este componente sirve para crear
    una caja de botones de tipo icono 
    de forma facil y rapida.
    """

    def __init__(self, window, title:str):
        super().__init__(window)
        self.grid_size:int = 1
        self.__button_icon_dict:dict = {}
        self.set_title(title)
        self.buffer_image_list = []
        
    def set_grid_size(self, COLUMNS:int):
        self.grid_size = COLUMNS

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
        dict_ = self.__button_icon_dict
        list_ = list(dict_.values())
        sort_in_grid(
            list_,
            self.grid_size
            )
            