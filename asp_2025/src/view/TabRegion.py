

from btpy.Btpy import Btpy
import os

class TabRegion(Btpy.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.texture_pack:str = ""
        self.res_path:str = "./res/"
        self.canvas = None
        self.model = None
        self.__init_components()

    def pack_forget(self):
        self.main_frame.pack_forget()

    def __init_components(self):
        self.__init_canvas()

    def __init_canvas(self):
        self.canvas = Btpy.Canvas(
            self.widget, "canvas"
        )
        self.canvas.set_size(600, 600)
        self.canvas.pack("left")
        def fn(e):
            point = self.canvas\
                .get_point_cursor()
            self.model.detect_click_square(
                point
            )
            self.update()
        self.canvas.add_right_click_listener(
            fn
        )

    def update(self):
        self.canvas.repaint()
        render = self.model\
            .render_square_matrix()
        self.draw_square_matrix(render)

    def draw_square(self, POINT,
            key_list):
        path_list = []
        path = ""
        for k in key_list:
            path = self.res_path \
                + self.texture_pack \
                + "/square/" + k \
                + ".png"
            if(not os.path.exists(path)):
                continue
            path_list.append(path)
        self.canvas.draw_image_layers(
            POINT,
            path_list
        )
        
    def draw_square_matrix(self, 
            square_matrix):
        x_size = 0
        key_list = []
        location_y = 0
        location_x = 0
        size_square = 100
        point = [0, 0]
        for x in range(len(square_matrix)):
            x_size = len(square_matrix[x])
            for y in range(x_size):
                key_list = square_matrix\
                    [x][y]
                point = [
                    location_x, 
                    location_y
                ].copy()
                self.draw_square(
                    point,
                    key_list
                )
                location_y += size_square
            location_x += size_square
            location_y = 0    

