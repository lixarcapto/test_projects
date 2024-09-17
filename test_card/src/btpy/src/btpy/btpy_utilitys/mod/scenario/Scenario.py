

from ..gobject.GObject import GObject

class Scenario:

    GObject = GObject

    def __init__(self) -> None:
        self.gobject_list:GObject = []
        self.size_x = 0
        self.size_y = 0

    def add(self, gobject):
        self.gobject_list.append(gobject)

    def set_size(self, SIZE_X, SIZE_Y):
        self.size_x = SIZE_X
        self.size_y = SIZE_Y

    def render(self):
        LENG = len(self.gobject_list)
        go = None
        image_dict_list = []
        for i in range(LENG):
            go = self.gobject_list[i]
            image_dict_list.append(
                go.get_image_paint_dict()
            )
        return image_dict_list

    def move(self):
        hitbox_list = []
        for i, go in enumerate(self.gobject_list):
            go.move(
                go.move_arrow,
                self.size_x,
                self.size_y,
                self.gobject_list
            )
            self.gobject_list[i] = go

    def free(self):
        for i, go in enumerate(self.gobject_list):
            go.free()
            self.gobject_list[i] = go

    def update(self):
        self.move()
        LENG = len(self.gobject_list)
        for i in range(LENG):
            self.gobject_list[i].update()
        self.free()
