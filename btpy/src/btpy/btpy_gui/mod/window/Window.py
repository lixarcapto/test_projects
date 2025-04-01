

import tkinter as tk

class Window:
    def __init__(self, title:str):
        self.widget = tk.Tk()
        self.widget.title(title)
        self.width = 0
        self.height = 0
        self.is_fullscreen = False
        self.init_basic_listeners()

    def set_title(self, text):
        self.widget.title(text)

    def set_alpha(self, alpha:float):
        self.widget.wm_attributes(
            '-alpha', alpha)

    def init_basic_listeners(self):
        def exit_full_screen(event):
            self.set_is_fullscreen(False)
        self.widget.bind("<Escape>", 
            exit_full_screen)
        def open_full_screen(event):
            self.set_is_fullscreen(True)
        self.widget.bind("<F11>", 
            open_full_screen)

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

    def fullscreen(self):
        if self.is_fullscreen:
            self.widget.attributes(
                "-fullscreen", False)
            self.is_fullscreen = False
        else:
            self.widget.attributes(
                "-fullscreen", True)
            self.is_fullscreen = True

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
        realizar cuando se cierre la ventana
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