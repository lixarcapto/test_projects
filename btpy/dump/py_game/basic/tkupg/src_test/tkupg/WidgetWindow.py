

from .WidgetBase import WidgetBase
import tkinter

class WidgetWindow(WidgetBase):

    def __init__(self):
        self.widget = tkinter.Tk()

    """
        Funcion para congirar la pantalla como
        fullscreen.
    """
    def set_full_screen(self):
        self.widget.attributes( "-fullscreen", True )
        self.widget.bind( "<F11>", self.__toggle_full_screen )
        self.widget.bind( "<Escape>", self.__quit_full_screen )

    """
    Método que ajusta la ventana como la 
    primera capa permanente en la interfaz 
    gráfica del SO.
    """
    def set_as_first_layer_in_SO(self, bool):
        self.widget.attributes('-topmost', 
            bool)
    
    """
    Bring the window to the front and give it 
    focus
    """
    def bring_to_the_front(self):
        self.widget.focus_force()

    def set_text(self, text):
        self.widget.title(text)

    def set_size(self, range):
        self.widget.pack_propagate(False)
        geometry = f"{range[0]}x{range[1]}"
        self.widget.geometry(geometry)

    def start(self):
        self.widget.mainloop()

    # PRIVATE --------------------------------

    def __toggle_full_screen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.widget.attributes("-fullscreen", self.fullScreenState)

    def __quit_full_screen(self, event):
        self.fullScreenState = False
        self.widget.attributes("-fullscreen", self.fullScreenState)
