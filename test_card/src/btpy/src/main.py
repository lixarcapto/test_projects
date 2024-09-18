

from btpy.Btpy import Btpy

def main():
    r = "None"
    #--------------------------------

    scenario = Btpy.Scenario()
    scenario.set_size(1300, 700)
    go1 = scenario.GObject()
    go1.set_route_image(
        "../res/image/cell.png")
    window = Btpy.Window()
    window.set_full_screen()
    painter = Btpy.Painter(window.widget)
    painter.pack_in_axe()
    painter.draw_image_dict(
        go1.get_image_dict())
    def action(e):
        result = go1.point_is_colliding(
            [e.x, e.y])
        if(result):
            print(f"is colliding {[e.x, e.y]}")
        else:
            print(f"is not colliding {[e.x, e.y]}")
    painter.left_click_listener(action)
    window.start()

   
    #------------------------------
    print(r)

main()