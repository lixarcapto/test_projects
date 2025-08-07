

from btpy.Btpy import Btpy
from btpy.btpy_images.mod.image_pil_canvas.ImagePilCanvas import ImagePilCanvas
from create_destiny_point import*

def main():
    print("init...")
    r = None
    # -------------------------------------
    

    for i in range(16):
        r = Btpy.random_probability(90)
        print(r)

    #---------------------------------
    print(r)

main() 