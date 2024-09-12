

from .Painter import Painter
from ..Tkupg import Tkupg

def painter_test():
    window = Tkupg.window()
    window.set_full_screen()
    painter = Tkupg.painter(window)
    painter.pack_in_axe(painter\
        .AXE_EXPANSION.BOTH)
    dict = {
        "type":"image_layout",
        "route_array":
        ["../res/image/layout_1.png",
         "../res/image/layout_2.png"],
        "point":[200,0]
    }
    array = []
    array.append(dict)
    painter.draw_pod_array(array)
    window.start()
    print("painter successful test")

painter_test()