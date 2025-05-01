

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
    engine.pack()
    engine.scenario.set_default_image_path(
        "bullet_70x70.png")
    gog = None
    id_ = ""
    for i in range(10):
        id_ = "star_" + str(i)
        engine.scenario.create_gobject(
            id_,
            "STANDARD", 
            Btpy.randint_list(2, [0, 300])
        )
        gog = engine.scenario\
            .get_gobject(id_)
        gog.set_is_collidable(False)
        gog.set_is_solid(False)
        engine.scenario.set_gobject(gog)
        gog = engine.scenario\
            .get_gobject(id_)
        print(
            gog.get_is_solid(),
            gog.get_is_collidable()
        )
        print("quantity", engine.scenario\
              .get_gobject_quantity())
    engine.scenario.create_gobject("ship",
        "STANDARD", [100, 100])
    ship = engine.scenario\
        .get_gobject("ship")
    ship.set_animation_list("ship", 
        "ship_70x70.png")
    ship.set_has_cam_focus(True)
    ship.set_is_collidable(False)
    ship.set_is_solid(False)
    def fn(e):
        nonlocal ship
        ship.move_up(30)
        print(ship.point_motion)
    window.add_key_listener("Up", fn)
    def fn(e):
        nonlocal ship
        ship.move_down(30)
        print(ship.point_motion)
    window.add_key_listener("Down", fn)
    engine.start()
    window.start()

main()