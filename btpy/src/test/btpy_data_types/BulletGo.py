


import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)
# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

from btpy.btpy_engine.mod.game_object\
    .GameObject import GameObject

class BulletGo(GameObject):

    def __init__(self, ID = ""):
        super().__init__(ID)
        self.set_is_mortal(True, 20)
        self.set_hitbox_size(70, 70)
        self.set_animation_list("bullet", 
        "bullet_70x70.png")
        