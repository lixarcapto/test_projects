

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
    slider = Btpy.InputSlider(window)
    slider.set_mark_interval(15)
    slider.set_slide_distance(15)
    slider.set_range([0, 100])
    slider.pack()
    window.start()

    #---------------------------------
    print(r)

main() 