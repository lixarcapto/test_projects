

from .WidgetBase import WidgetBase
import tkinter
from .create_popup import create_popup

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

    def create_popup(self, text_message:str, 
        opciones:list[str])\
        ->str:
        """
        Funcion que muestra un pop-up con 
        botones para seleccionar una opción. 
        Recibe una lista de opciones en 
        formato string y retorna el indice 
        de la opcion seleccionada.
        """
        return create_popup(text_message, 
            opciones)

    def set_alpha(self, alpha:float):
        self.widget.wm_attributes(
            '-alpha', alpha)

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

    def set_size(self, SIZE_X, SIZE_Y):
        self.widget.pack_propagate(False)
        geometry = f"{SIZE_X}x{SIZE_Y}"
        self.widget.geometry(geometry)

    def start(self):
        self.widget.mainloop()

    # PRIVATE --------------------------------

    def __toggle_full_screen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.widget.attributes("-fullscreen", self.fullScreenState)

    def __quit_full_screen(self, event):
        self.fullScreenState = False
        self.widget.attributes("-fullscreen",
            self.fullScreenState)
