

from btpy.Btpy import Btpy

from get_grid_index import*
from create_matrix_2d import*
from matrix_bool_is_connect import*
from distribuite_energy import*

class View:

    def __init__(self):
        self.window = Btpy.Window(
            "electronic")
        self.type_objects = [
                "cable",
                "switch"
            ]
        self.type_object_selected = 0
        self.canvas = Btpy.Canvas(
            self.window.widget, "canvas"
        )
        self.panel_tools = Btpy.ButtonBox(
            self.window.widget, "tools"
        )
        self.panel_tools.set_components(
            self.type_objects
        )
        self.panel_tools.set_columns(
            len(self.type_objects)
        )
        self.panel_tools.grid(0, 0)
        self.canvas.grid(1, 0)
        self.panel_size = 30
        self.celd_size = 20
        self.matrix = create_matriz_2d(
            self.panel_size,
            self.panel_size,
            0
        )
        self.matrix_type = create_matriz_2d(
            self.panel_size,
            self.panel_size,
            0
        )
        self.canvas.set_size(500, 500)
        self.draw_panel()
        def fn(e):
            i_p = get_grid_index(
                self.canvas.get_point_cursor(),
                self.celd_size,
                self.panel_size,
                self.panel_size
            )
            self.matrix[i_p[0]][i_p[1]]\
                = 1
            self.matrix_type[i_p[0]][i_p[1]]\
                = self.type_object_selected
            self.draw_panel()
            print(i_p)
        self.canvas\
            .add_right_click_listener(fn)
        def fn(e):
            i_p = get_grid_index(
                self.canvas.get_point_cursor(),
                self.celd_size,
                self.panel_size,
                self.panel_size
            )
            self.matrix[i_p[0]][i_p[1]]\
                = 0
            self.matrix_type[i_p[0]][i_p[1]]\
                = 0
            self.draw_panel()
            print(i_p)
        self.canvas\
            .add_left_click_listener(fn)
        def fn(idx):
            self.type_object_selected\
                = idx
            print("type ", self.type_object_selected)
        self.panel_tools\
            .add_single_listener(fn)
        def fn(n):
            self.advance_time()
        Btpy.repeat_each_async(
            3,
            fn
        )
        self.window.start()

    def advance_time(self):
        self.matrix = reset_energy(
            self.matrix
        )
        self.update_behavior()
        self.detect_if_is_connect()
        self.draw_panel()

    def update_behavior(self):
        code_type = 0
        for y in range(len(self.matrix_type)):
            for x in range(len(self.matrix_type[y])):
                code_type = self\
                    .matrix_type[y][x]
                if(code_type == 1):
                    print("valor cable is " + str(self\
                    .matrix[y][x]))
                    if(self\
                    .matrix[y][x] == 0):
                        self.matrix[y][x] = 1
                        print("cambio a cable 1")
                    else:
                        self.matrix[y][x] = 0
                        print("cambio a cable 0")
                    print("cable is " + str(self\
                    .matrix[y][x]))

    def detect_if_is_connect(self):
        self.matrix = distribuite_energy(
            self.matrix
        )

    def draw_panel(self):
        self.canvas.repaint()
        x = 0
        y = 0
        p = [0, 0]
        for i in range(self.panel_size * self.panel_size):
            if(self.matrix[y][x] != 0):
                if(self.matrix[y][x] == 2):
                    self.canvas.set_fill_color(
                        "yellow")
                elif(self.matrix[y][x] == 1):
                    self.canvas.set_fill_color(
                        "orange")
                self.canvas.draw_rectangle(
                    p,
                    self.celd_size,
                    self.celd_size
                )
            x += 1
            p[0] += self.celd_size
            if(x >= self.panel_size):
                x = 0
                y += 1
                p[0] = 0
                p[1] += self.celd_size