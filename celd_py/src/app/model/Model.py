

from .mod.scene.Scene import Scene

class Model:

    def __init__(self, persistence) -> None:
        self.persistence = persistence
        self.scene = Scene()
        self.scene.set_size(30, 30)
        self.scene.create_go_matrix()
        go = self.scene.create_go()
        self.scene.insert_go(go)