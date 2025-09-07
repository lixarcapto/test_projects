

from btpy.Btpy import Btpy
from btpy.btpy_images.mod.image_pil_canvas.ImagePilCanvas import ImagePilCanvas
from create_destiny_point import*

def main():
    print("init...")
    r = None
    # -------------------------------------
    

    r = Btpy.write_as_list(
        ["perro", "gato", "jirafa"],
        "animals"
    )

    #---------------------------------
    print(r)

main() 