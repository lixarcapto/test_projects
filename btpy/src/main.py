

from btpy.Btpy import Btpy
from btpy.btpy_utilitys.mod.open_browser_in_time.open_browser_in_time import*

def main():
    print("init...")
    r = None
    # -------------------------------------
    
    window = Btpy.Window("ventana")
    window.set_as_first_layer_in_SO(True)
    button = Btpy.Button(window, "play")
    button.pack()
    def fn(e):
        Btpy.open_browser_in_time(30,
        "https://music.youtube.com/watch?v=TNf3GPizM58"
        )
    button.add_listener(fn)
    window.start()
    

    #---------------------------------
    print(r)

main() 