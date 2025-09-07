




from .WidgetElement import WidgetElement
from ...btpy_maths.mod.center_square.center_square import*
import tkinter

class WidgetCircleGraph(WidgetElement):

    def __init__(self, window_tk):
        self.widget = tkinter.Canvas(
            window_tk.widget)

    def create_graph(
          self, dict_color, 
          size):
        self.set_size([size, size])
        radio = size / 2
        center_point = center_square(
            [2, 2], size, size, 
        )
        """
        Crea un gráfico circular en un Canvas de Tkinter, usando las claves del diccionario
        como colores para cada sección.
        """
        centro_x = center_point[0]
        centro_y = center_point[1]

        # Ángulo inicial
        angulo_inicial = 0

        # Calcular el ángulo de cada sección
        total = sum(dict_color.values())
        for color, valor in dict_color.items():
            angulo = valor / total * 360
            self.widget.create_arc(
                centro_x - radio, 
                centro_y - radio, 
                centro_x + radio, 
                centro_y + radio,
                start=angulo_inicial, 
                extent=angulo, 
                fill=color,
                width=3
            )
            angulo_inicial += angulo