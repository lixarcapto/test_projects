

from btpy.src.btpy.Btpy import Btpy
from ..go.Go import Go

class Scene:

    def __init__(self) -> None:
        self.go_matrix = []
        self.size_x = 0
        self.size_y = 0
        self.size_celd = 70
        self.query_event = []
        Go.SIZE_IMAGE = self.size_celd

    def update(self):
        self.update_go()
        self.collect_event()
        self.process_event()

    def process_event(self):
        for event in self.query_event:
            if(event[0] == "move"):
                self.move_go(
                    event[1],
                    event[2]
                )

    def collect_event(self):
        matrix = self.go_matrix
        go = None
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                go = matrix[x][y]
                if(go == None): continue
                self.query_event \
                    = self.query_event\
                    + go.collect_event()
                
    def update_go(self):
        matrix = self.go_matrix
        go = None
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                go = matrix[x][y]
                if(not go == None):
                    go.update()
                    matrix[x][y] = go
        self.go_matrix = matrix

    def move_go(self, id, point):
        if(self.go_in(point)): return None
        go = self.extract_go(id)
        self.insert_in(go, point)

    def insert_in(self, go, point):
        self.go_matrix[point[0]][point[1]]\
            = go

    def create_go(self):
        return Go()

    def set_size(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

    def write(self):
        matrix = self.go_matrix
        go = None
        txt = ""
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                go = matrix[x][y]
                if(not go == None):
                    txt += f"{go.write()}\n"
        return txt

    def render(self):
        render_list = []
        matrix = self.go_matrix
        go = None
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                go = matrix[x][y]
                if(not go == None):
                    render_list \
                        = render_list \
                        + go.render([x, y])
        return render_list

    def create_go_matrix(self):
        self.go_matrix = Btpy.create_list(
            [self.size_x, self.size_y])
    
    def get_go(self, id):
        matrix = self.go_matrix
        go = None
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                go = matrix[x][y]
                if(go.id == id):
                    return go
        return None
    
    def extract_go(self, id):
        matrix = self.go_matrix
        go = None
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                go = matrix[x][y]
                matrix[x][y] = None
                if(go.id == id):
                    return go
        return None
    
    def set_go(self, new_go):
        matrix = self.go_matrix
        go = None
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                go = matrix[x][y]
                if(go.id == new_go.id):
                    go = new_go
                    matrix[x][y] = go
                    break
        self.go_matrix = matrix

    def has_go(self, go):
        matrix = self.go_matrix
        go = None
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                go = matrix[x][y]
                if(go.id == id):
                    return True
        return False

    def go_in(self, point):
        x = point[0]
        y = point[1]
        go = self.go_matrix[x][y]
        if(go == None): return False
        else: return True

    def count_spaces(self):
        matrix = self.go_matrix
        n = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if(matrix[x][y] == None):
                    n += 1
        return n
    
    def insert_random(self, go):
        point_list = self.get_free_points()
        point = Btpy.random_choice(
            point_list)
        self.go_matrix[point[0]][point[1]]\
         = point
    
    def get_free_points(self):
        matrix = self.go_matrix
        point_list = []
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if(matrix[x][y] == None):
                    point_list = [x, y]
        return point_list

    def insert_go(self, new_go):
        matrix = self.go_matrix
        is_break = False
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if(matrix[x][y] == None):
                    new_go.point = [x, y]
                    matrix[x][y] = new_go
                    is_break = True
                    break
            if(is_break): break
        self.go_matrix = matrix


