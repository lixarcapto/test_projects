

import tkinter as tk

class Window:
    def __init__(self, title:str):
        self.widget = tk.Tk()
        self.widget.title(title)
        self.width = 0
        self.height = 0
        self.is_fullscreen = False
        self.init_basic_listeners()

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

    def start(self):
        self.widget.mainloop()