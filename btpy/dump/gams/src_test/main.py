

from basic.btpy.btpy import Btpy
from basic.tkupg.tkupg import Tkupg
from Scene import Scene

def main():
    window = Tkupg.window()
    window.set_full_screen()
    painter = Tkupg.painter(window)
    painter.pack_in_axe(
        painter.AXE_EXPANSION.BOTH)
    scene = Scene()
    go = scene.create_go()
    src = "./res/image/girl_pix_test.png"
    go.set_src_image(src)
    print(go.write())
    array = []
    array.append(go.to_paint_order())
    painter.draw_paint_order_map_array(array)
    window.start()


main()