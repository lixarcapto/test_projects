

from app.model.mod.perception.Perception import Perception
from btpy.src.btpy.Btpy import Btpy
import random

def main():
    pers = Perception()
    pers.add_image("RED")
    pers.add_image("BLUE")
    print(pers.resume())

main()