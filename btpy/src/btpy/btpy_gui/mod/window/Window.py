

import tkinter as tk
from ..create_photo_image.create_photo_image import*

class Window:
    def __init__(self, title:str):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.config(bg = "gray")
        self.widget = tk.Frame(self.window)
        self.widget.pack(
            padx=2, pady=2,
            expand=True, fill=tk.BOTH
        )
        self.label_back = None
        self.buffer_image = None
        self.width = 0
        self.height = 0
        self.is_fullscreen = False
        self.__init_basic_listeners()

    def set_background(self, COLOR:str):
        self.widget.config(bg = COLOR)

    def set_path_image(self, PATH:str, 
            SIZE_LIST:list[int] = []):
        if(SIZE_LIST == []):
            self.buffer_image \
            = create_photo_image(
                PATH
            )
        else:
            self.buffer_image \
            = create_photo_image(
                PATH, 
                SIZE_LIST
            )
        self.buffer_image
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

    def get_background(self):
        return self.widget.cget("bg")

    def set_margin(self, COLOR:str):
        self.window.config(bg = COLOR)

    def get_margin(self):
        self.window.cget("bg")

    def set_title(self, text):
        self.window.title(text)

    def set_alpha(self, alpha:float):
        self.window.wm_attributes(
            '-alpha', alpha)

    def __init_basic_listeners(self):
        def exit_full_screen(event):
            self.set_is_fullscreen(False)
        self.window.bind("<Escape>", 
            exit_full_screen)
        def open_full_screen(event):
            self.set_is_fullscreen(True)
        self.window.bind("<F11>", 
            open_full_screen)

    def set_is_fullscreen(self, bool):
        self.is_fullscreen = bool
        self.window.attributes(
                "-fullscreen", bool)

    def get_is_fullscreen(self):
        return self.is_fullscreen

    def set_size(self, WIDTH:int, 
            HEIGHT:int):
        self.width = WIDTH
        self.height = HEIGHT
        self.window.geometry(
            f"{WIDTH}x{HEIGHT}")
        
    def set_location(self, X, Y):
        # Establecer tamaño y posición de la ventana
        self.window.geometry(
        f"{self.width}x{self.height}+{X}+{Y}")

    def fullscreen(self):
        if self.is_fullscreen:
            self.window.attributes(
                "-fullscreen", False)
            self.is_fullscreen = False
            self.window.update()
        else:
            self.window.attributes(
                "-fullscreen", True)
            self.is_fullscreen = True
            self.window.update()

    """
    Método que ajusta la ventana como la 
    primera capa permanente en la interfaz 
    gráfica del SO.
    """
    def set_as_first_layer_in_SO(self, bool):
        self.window.attributes('-topmost', 
            bool)
        
    def add_close_action(self, CALLBACK):
        """
        Funcion que añade una accion a 
        realizar cuando se cierre la ventana
        """
        def simple_decorator():
            CALLBACK()
            self.window.destroy()
        self.window.protocol(
            "WM_DELETE_WINDOW", 
            simple_decorator
        )

    """
    Bring the window to the front and give it 
    focus
    """
    def bring_to_the_front(self):
        self.window.focus_force()

    def start(self):
        self.window.mainloop()