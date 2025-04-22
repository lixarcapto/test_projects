

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

def main(): 
    window = Btpy.Window("game object")
    gog = Btpy.GameObject()
    gog.set_image_list("ship",
        ["./ship_70x70.png"])
    gog.point_location = [130, 300]
    gog.box_size_list = [70, 70]
    Btpy.GameObject.set_scenario_size(
        [400, 400]
    )
    canvas = Btpy.Canvas(window, "canvas")
    canvas.set_size(400, 400)
    canvas.set_background_color(
            "white")
    canvas.pack()
    canvas.set_draw_reflection(False)
    speed = 10
    window.add_key_listener(
        "Left", 
        lambda e:gog.move_left(speed)
    )
    window.add_key_listener(
        "Right", 
        lambda e:gog.move_right(speed)
    )
    bullet = Btpy.GameObject()
    bullet.point_location = [
             Btpy.rand_range([0, 350]), 
            0
            ]
    bullet.set_image_list("cat", [
        "./cat_1.png",
        "./cat_2.png"
    ])
    bullet.box_size_list = [70, 70]
    bullet.move_down(10)
    life_number = 3
    label = Btpy.Label(window, 
        f"life:{life_number}")
    label.pack(False, "top")
    def fn(e):
        nonlocal life_number
        label.set_title(
            f"life:{life_number}")
        canvas.repaint()
        canvas.draw_path_image(
            gog.point_location,
            gog.get_render()\
                ["image_key"]
        )
        canvas.draw_path_image(
            bullet.point_location,
            bullet.get_render()\
                ["image_key"]
        )
        print("bullet image", bullet.get_render()\
                ["image_key"])
        gog.update()
        bullet.update()
        if(bullet.point_location[1] >= 400):
            bullet.point_location = [
             Btpy.rand_range([0, 350]), 
            0
            ]
        if(gog.is_colliding(bullet)):
            print("is_colliding")
            life_number -= 1
    Btpy.repeat_each_async(0.60, fn)
    window.start()

main()