


from .WidgetTextual import WidgetTextual
import tkinter as tk

class WidgetPressTime(WidgetTextual):

    def __init__(self, widget):
        self.widget = tk.Button(
            widget)
        self.root = widget
        self.tiempo_espera=2000
        self.tiempo_espera = self.tiempo_espera  
        # Tiempo en milisegundos
        self.widget.bind("<Enter>", 
            self.iniciar_temporizador)
        self.widget.bind("<Leave>", 
            self.cancelar_temporizador)
        self.temporizador = None
        self.call_back = None
        super().default_config()

    def iniciar_temporizador(self, event):
        self.temporizador = self.root.after(self.tiempo_espera, self.activar_evento)

    def cancelar_temporizador(self, event):
        if self.temporizador:
            self.root.after_cancel(self.temporizador)
            self.temporizador = None

    def add_listener(self, CALL_BACK):
        self.call_back = CALL_BACK

    def activar_evento(self):
        if(self.call_back != None):
            self.call_back()
        # Aquí puedes colocar el código para ejecutar tu evento
        # Por ejemplo, abrir una nueva ventana, ejecutar una función, etc.