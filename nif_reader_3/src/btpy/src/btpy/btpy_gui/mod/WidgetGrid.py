

from .WidgetTextual import WidgetTextual
import tkinter

class WidgetGrid(WidgetTextual):

    def __init__(self, widget, size_x, 
            size_y):
        self.widget = tkinter.Frame(
            widget)
        self.button_grid = None
        super().default_config()
        self.point_selected = [0, 0]
        self.img_buffer = None
        self.init(self.widget, size_x, 
            size_y)

    def init(self, window_tk, size_x, size_y):
        matrix = []
        array = []
        for i in range(size_x):
            array = []
            for j in range(size_y):
                button = tkinter.Button(self.widget, 
                    text=f"[{i}, {j}]")
                button.grid(row=i, column=j)
                array.append(button)
            matrix.append(array)
        self.button_grid = matrix

    def add_click_listener(self, function):
        size_y = len(self.button_grid)
        size_x = 0
        e = None
        # Ni idea como esto funciono
        def auxiliar(i, j):
            def cloujure(event):
                self.on_click(i, j)
                function(event)
            return cloujure
        for y in range(size_y):
            size_x = len(self.button_grid)
            for x in range(size_x):
                e = self.button_grid[x][y]
                e.bind(
                    "<ButtonPress-1>", 
                    auxiliar(x, y)
                )
                self.button_grid[x][y] = e


    def on_click(self, i, j):
        self.point_selected = [i, j]
                
    
