

from model.Model import Model
from view.View import View
from btpy.src.btpy.Btpy import Btpy
import sys
import threading

class Controller:

    def __init__(self) -> None:
        self.view = View()
        self.model = Model()

    def turn_off(self):
        print("turn off activado")
        self.view.destroy()
        sys.exit(0)

    def update(self):
        message = self.view.request()
        self.model.receive(message)
        message = self.model.request()
        self.view.receive(message)

    def start(self):
        self.view.add_update_listener(
            self.update
        )
        #self.view.window.widget.after(10, 
         #   self.update)
        self.update()
        self.view.start()
        
        

    
