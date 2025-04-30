

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
    canvas = Btpy.Canvas(window, "canvas")
    canvas.set_size(400, 400)
    canvas.set_background_color(
            "black")
    canvas.pack()
    canvas.set_draw_reflection(False)
    speed = 10
    scenario = Btpy.Scenario()
    scenario.set_default_image_path(
        "./bullet_70x70.png"
    )
    scenario.set_size(1000, 1000)
    gog = Btpy.GameObject("ship")
    gog.set_hitbox_size(70, 70)
    gog.set_layer(1)
    gog.set_is_solid(True)
    gog.set_animation_list("ship", 
        "ship_70x70.png")
    window.add_key_listener(
        "Left", 
        lambda e:gog.move_left(speed)
    )
    window.add_key_listener(
        "Right", 
        lambda e:gog.move_right(speed)
    )
    window.add_key_listener(
        "Up", 
        lambda e:gog.move_up(speed)
    )
    window.add_key_listener(
        "Down", 
        lambda e:gog.move_down(speed)
    )
    gog.point_location = [100, 100]
    scenario.set_gobject_class(
        "BULLET", BulletGo)
    scenario.set_gobject(gog)
    scenario.create_gobject("", "BULLET",
        [200, 200]
    )
    n = 0
    ship = None
    pt_ship = None 
    pt_cam = None
    path_res = "./"
    def fn(e):
        nonlocal n
        canvas.repaint()
        scenario.update()
        ship = scenario.get_gobject("ship")
        scenario.center_cam_in(
            ship.get_location())
        print(f"update {n}")
        n += 1
        render_list = scenario\
            .get_render_list()
        for render in render_list:
            canvas.draw_path_image(
                render["point"],
                path_res + render["image_key"]
            )

    Btpy.repeat_each_async(0.60, fn)
    window.start()

main()