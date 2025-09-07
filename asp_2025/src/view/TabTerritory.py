

from btpy.Btpy import Btpy
import os

class TabTerritory(Btpy.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.model = None
        self.canvas = Btpy.Canvas(
            self.widget, "main"
        )
        self.canvas.set_size(800, 600)
        self.canvas.pack(
            True, "left")
        
    def update(self):
        list_ = self.model\
            .render_territory()
        print("RENDER TERRITORY", list_)
        folder = "./res/texture_pack/default/structures/"
        extension = ".png"
        path = ""
        point = [0, 0]
        limit_x = 800
        size_image = 80
        for e in list_:
            path = folder + e + extension
            self.canvas\
                .draw_path_image(
                    point,
                    path
                )
            point[0] += size_image
            if(size_image >= limit_x):
                point[0] = 0
                point[1] += size_image