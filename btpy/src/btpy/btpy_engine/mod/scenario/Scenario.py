

from ..gobject.GObject import GObject

class Scenario:

    GObject = GObject

    def __init__(self) -> None:
        self.gobject_list:GObject = []
        self.size_x = 0
        self.size_y = 0

    def get(self, KEY_OBJECT):
        for i, e in enumerate(self.gobject_list):
            if(e.get_id() == KEY_OBJECT):
                return e
        return None
                
    
    def set(self, GOBJECT):
        if(self.has(GOBJECT.get_id())):
            self.replace(GOBJECT)
        else:
            self.add(GOBJECT)
        
    def replace(self, GOBJECT):
        for i, e in enumerate(self.gobject_list):
            if(e.get_id() == GOBJECT.get_id()):
                self.gobject_list[i]\
                    = GOBJECT
                break

    def has(self, KEY_OBJECT):
        for e in self.gobject_list:
            if(e.get_id() == KEY_OBJECT):
                return True
        return False
        
    def object_clicked(self, POINT_CLICKED):
        LENG = len(self.gobject_list)
        go = None
        image_dict_list = []
        for i in range(LENG):
            go = self.gobject_list[i]
            if(go.point_is_colliding(
                    POINT_CLICKED)):
                return go.get_id()
        return ""

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
                go.get_image_layout_dict()
            )
        return image_dict_list

    def move(self):
        hitbox_list = []
        for i, go in enumerate(self.gobject_list):
            go.move(
                go.get_vector_arrow(),
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
