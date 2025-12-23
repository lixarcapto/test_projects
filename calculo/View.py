
import tkinter as tk
from btpy.Btpy import Btpy

class View:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Interfaz Simple")
        self.window.geometry("300x150")
        
        self.ip_empleados = Btpy.TextField(
            self.window, "empleados")
        self.ip_empleados.grid(0, 0)
        self.ip_sueldos = Btpy.TextField(
            self.window, "sueldo")
        self.ip_sueldos.grid(1, 0)
        self.ip_materias_primas = Btpy.TextField(
            self.window, "costo producto")
        self.ip_materias_primas.grid(2, 0)
        self.ip_costos = Btpy.TextField(
            self.window, "costos")
        self.ip_costos.grid(3, 0)
        self.btn_calcular = Btpy.Button(
            self.window, "calcular"
        )
        self.btn_calcular.grid(3, 0)
        self.btn_calcular.add_listener(
            self.calcular
        )
        self.set_default()
        self.window.mainloop()

    def set_default(self):
        self.ip_sueldos.set_value(0)
        self.ip_empleados.set_value(0)
        self.ip_materias_primas.set_value(0)

    def calcular(self):
        sueldo = int(
            self.ip_sueldos.get_value()
            )
        empleados = int(
            self.ip_empleados.get_value()
            )
        materias_primas =  int(
            self.ip_materias_primas.get_value()
            )
        costos = (sueldo * empleados)\
            + materias_primas
        self.ip_costos.set_value(costos)