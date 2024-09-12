

from model.Model import Model
from model.go_factory.GObject import GObject

def main():
    scene = Model("prueba")
    scene.set_map_size(1200, 1200)
    scene.set_size_screen(1200, 700)
    scene.scene.create_player("main",
            1200, 700)
    scene.create_gobject("cosa", "GObject",
        [250, 250])
    scene.start()

main()