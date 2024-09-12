

from model.Model import Model
from model.go_factory.GObject import GObject

def main():
    model = Model("prueba")
    model.create_map(100, 100)
    model.set_size_screen(1200, 700)
    model.go_manager.scene.create_player("main",
            1200, 700)
    model.create_gobject("cosa", "GObject",
        [250, 250])
    model.create_gobject("three1", "GVegetable",
        [270, 270])
    model.start()

main()