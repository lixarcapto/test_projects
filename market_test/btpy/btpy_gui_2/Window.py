

import tkinter as tk
from PIL import Image, ImageTk

class Window:

    def set_path_image(self, PATH:str):
        imagen_pil = Image.open(PATH)
        imagen_pil = imagen_pil\
                    .resize((
                self.width, 
                self.height
        ))
        photo_image = tk.PhotoImage(
            imagen_pil
        )
        imagen_tk = ImageTk.PhotoImage(
            imagen_pil)
        self.buffer_image = imagen_tk
        self.label_back = tk.Label(
            self.widget, 
            image=self.buffer_image
        )  
        # Etiqueta con la imagen
        self.label_back.place(
            x=0, y=0, 
            relwidth=1, relheight=1
        )  
        # Cubre el frame

    def __init__(self, title:str):
        self.widget = tk.Tk()
        self.widget.title(title)
        self.widget.config(bg = "gray")
        self.label_back = None
        self.buffer_image = None
        self.width = 500
        self.height = 500
        self.key_callback_dict\
            :dict[str, callable] = {}
        self.is_fullscreen = False
        self.__init_basic_listeners()

    def set_background(self, COLOR:str):
        self.widget.config(bg = COLOR)

    def get_background(self):
        return self.widget.cget("bg")

    def set_margin(self, COLOR:str):
        self.widget.config(bg = COLOR)

    def get_margin(self):
        self.widget.cget("bg")

    def set_title(self, text):
        self.widget.title(text)

    def set_alpha(self, alpha:float):
        self.widget.wm_attributes(
            '-alpha', alpha)

    def __init_basic_listeners(self):
        def exit_full_screen(event):
            self.set_is_fullscreen(False)
        self.widget.bind("<Escape>", 
            exit_full_screen)
        def open_full_screen(event):
            self.set_is_fullscreen(True)
        self.widget.bind("<F11>", 
            open_full_screen)
        self.__add_default_key_listener()

    def set_is_fullscreen(self, bool):
        self.is_fullscreen = bool
        self.widget.attributes(
                "-fullscreen", bool)

    def get_is_fullscreen(self):
        return self.is_fullscreen

    def set_size(self, WIDTH:int, 
            HEIGHT:int):
        self.width = WIDTH
        self.height = HEIGHT
        self.widget.geometry(
            f"{WIDTH}x{HEIGHT}")
        
    def set_location(self, X, Y):
        # Establecer tamaño y posición de la ventana
        self.widget.geometry(
        f"{self.width}x{self.height}+{X}+{Y}")

    def __fullscreen(self):
        if self.is_fullscreen:
            self.widget.attributes(
                "-fullscreen", False)
            self.is_fullscreen = False
            self.widget.update()
        else:
            self.widget.attributes(
                "-fullscreen", True)
            self.is_fullscreen = True
            self.widget.update()

    """
    Método que ajusta la ventana como la 
    primera capa permanente en la interfaz 
    gráfica del SO.
    """
    def set_as_first_layer_in_SO(self, bool):
        self.widget.attributes('-topmost', 
            bool)
        
    def add_close_action(self, CALLBACK):
        """
        Funcion que añade una accion a 
        realizar cuando se cierre 
        la ventana
        """
        def simple_decorator():
            CALLBACK()
            self.widget.destroy()
        self.widget.protocol(
            "WM_DELETE_WINDOW", 
            simple_decorator
        )

    """
    Bring the window to the front and give it 
    focus
    """
    def bring_to_the_front(self):
        self.widget.focus_force()

    def start(self):
        self.widget.mainloop()

    def __add_default_key_listener(self):
        def fn(event):
            key = event.keysym 
            print("key", key)
            key_dict = self.key_callback_dict
            if(key in key_dict):
                key_dict[key](event)
        self.widget.bind("<Key>", fn)

    def add_key_listener(self, 
            KEY:str,
            CALLBACK_ARGS_X1:callable):
        self.key_callback_dict[KEY]\
            = CALLBACK_ARGS_X1

    