

from btpy.Btpy import Btpy
import sys

n = 0

def main():
    print("init...")
    r = None
    # -------------------------------------
    
    window = Btpy.Window("titulo")
    window.set_is_fullscreen(True)
    button = Btpy.ButtonIcon(window, 
        "../res/image/fish.png")
    button.pack()
    dropdown = Btpy.DropdownBox(window,
            ["gusano", "sardina", "imitacion"])
    dropdown.pack()
    def fn():
        print(dropdown.get_value())
    button.add_listener(fn)
    window.start()

    #---------------------------------
    print(r)

main() 