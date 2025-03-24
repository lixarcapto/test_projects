

from btpy.Btpy import Btpy
import sys

n = 0

def main():
    print("init...")
    r = None
    # -------------------------------------
    
    window = Btpy.Window("titulo")
    window.set_is_fullscreen(True)
    button = Btpy.SelectButton(window,
            "click")
    button.pack()
    button_2 = Btpy.Button(window, 
        "unpress")
    button_2.pack()
    def fn():
        button.set_value(False)
    button_2.add_listener(fn)
    window.start()

    #---------------------------------
    print(r)

main() 