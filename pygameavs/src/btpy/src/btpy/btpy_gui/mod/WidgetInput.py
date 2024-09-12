


from .WidgetElement import WidgetElement
import tkinter as tk

class WidgetInput(WidgetElement):

    def __init__(self, window_tk):
        self.widget = tk\
            .Text(window_tk.widget)
        super().default_config()

    def reset_index(self):
        """
        Función que  localiza el índice 
        del input en el inicio del texto
        """
        self.widget.mark_set("insert", 1.0)
        self.widget.see("insert")

    
    def set_text(self, text):
        """
        función que reasigna todo el 
        texto enviado
        """
        self.widget.delete("1.0", tk.END)
        self.widget.insert(tk.END, text, 'end')

    
    def add_text(self, text):
        """
        función que suma el texto 
        enviado al final del texto 
        actual
        """
        self.widget.insert(tk.END, text, 'end')

    def get_text(self):
        return self.widget.get("1.0", tk.END)

    def extract_text(self):
        """
         función que obtiene el texto 
         y borra el texto del componente
        """
        text = self.widget.get("1.0", tk.END)
        self.widget.delete("1.0", tk.END)
        return text
    
    def add_enter_listener(self, function):
        """
        función que añade una funcion 
        para activar al presionar la 
        tecla enter
        """
        self.widget.bind("<Return>", 
            function)
