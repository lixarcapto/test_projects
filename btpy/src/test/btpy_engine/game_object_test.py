

import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)
# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

from btpy.Btpy import Btpy
from BulletGo import BulletGo

def main(): 
    window = Btpy.Window("game object")
    engine = Btpy.GameEngine(window, 
        "Engine")
    engine.canvas.set_background_color(
        "black")
    engine.pack()
    engine.scenario.set_size(500, 500)
    engine.canvas.set_size(500, 500)
    engine.scenario.create_gobject(
        "", "ANIMAL", [200, 200])
    engine.scenario.set_default_image_path(
        "star_a_50x50.png")
    gog = None
    id_ = ""
    for i in range(20):
        id_ = "star_" + str(i)
        engine.scenario.create_gobject(
            id_,
            "STANDARD", 
            [
                Btpy.rand_range([1, 499]), 
                Btpy.rand_range([1, 499])
            ]
        )
        gog = engine.scenario\
            .get_gobject(id_)
        gog.set_is_collidable(False)
        gog.set_is_solid(False)
        #gog.set_has_acceleration(True)
    engine.scenario.create_gobject("ship",
        "PLAYER", [100, 100])
    ship = engine.scenario\
        .get_gobject("ship")
    ship.set_animation_list(
        "african", "man_african_70x70.png")
    def fn(gobject):
        print(
            "acceleration",
            gobject.get_acceleration_point()
        )
        print(
            "speed point",
            gobject.get_speed_point()
        )
    ship.add_behavior("report", fn)
    speed = 5
    def fn(e):
        nonlocal ship, speed
        ship.move_up(speed)
    window.add_key_listener("Up", fn)
    def fn(e):
        nonlocal ship
        ship.launch_spawn("STANDARD")
    window.add_key_listener("a", fn)
    def fn(e):
        nonlocal ship, speed
        ship.move_down(speed)
    window.add_key_listener("Down", fn)
    def fn(e):
        nonlocal ship, speed
        ship.move_left(speed)
        print(ship.get_acceleration_point())
    window.add_key_listener("Left", fn)
    def fn(e):
        nonlocal ship, speed
        ship.move_right(speed)
        print(ship.get_acceleration_point())
    window.add_key_listener("Right", fn)
    engine.start()
    window.start()

main()