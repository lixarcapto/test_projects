


import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..frame.Frame import Frame
from ..button_icon.ButtonIcon \
    import ButtonIcon

class ButtonBoxIcon(WidgetStandard):

    """
    Este componente sirve para crear
    un grid de botones de tipo icono 
    de forma facil y rapida.
    """

    def __init__(self, window, title:str):
        super().__init__()
        self.widget = None
        self.label_title = None
        self.inner_frame = None
        self.grid_size:int = 1
        self.__button_icon_dict:dict = {}
        self.__init_components(window,
            title)
        
    def set_grid_size(self, SIZE:int):
        self.grid_size = SIZE

    def __init_components(self, window,
            title)->None:
        self.widget = Frame(
            window
        )
        self.widget.set_border(1)
        self.label_title = tk.Label(
            self.widget.widget, 
            text = title
        )
        self.inner_frame = Frame(
            self.widget)
        self.inner_frame.set_border(1)

    def create_button_dict(self, 
            KEY_LIST:list[str], 
            PATH_LIST:list[str])->None:
        button = None
        n = 0
        for k in KEY_LIST:
            button = ButtonIcon(
                self.inner_frame,
                k,
                PATH_LIST[n]
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
            button.widget.config(
                command = aux(k))
            
    def unpack(self)-> None:
        for button in self.__button_icon_dict:
            button.grid_forget()
        self.inner_frame.unpack()
        self.label_title.pack_forget()
        self.widget.unpack()
            
    def pack(self)-> None:
        """
        Esta funcion organiza los botones
        como un grid con el tamaño indicado.
        """
        x:int = 0
        y:int = 0
        self.widget.pack()
        self.label_title.pack()
        self.inner_frame.pack(3)
        button = None
        for k in self.__button_icon_dict:
            button = self.__button_icon_dict[k] 
            button.widget.grid(
                row=x, column=y,
                sticky=tk.NSEW
            )
            x += 1
            if(x == self.grid_size):
                y += 1
                x = 0
            