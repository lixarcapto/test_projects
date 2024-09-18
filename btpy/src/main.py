

from btpy.Btpy import Btpy

def main():
    r = "None"
    #--------------------------------

    scenario = Btpy.Scenario()
    scenario.set_size(1300, 700)
    go1 = scenario.GObject()
    window = Btpy.Window()
    window.set_full_screen()
    painter = Btpy.Painter(window.widget)
    painter.pack_in_axe()
    painter.draw_image_layout_dict(
        go1.get_image_layout_dict()
    )
    window.start()

   
    #------------------------------
    print(r)

main()