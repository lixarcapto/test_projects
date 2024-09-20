

from btpy.Btpy import Btpy

def main():
    r = "None"
    #--------------------------------

    scenario = Btpy.Scenario()
    scenario.set_size(1300, 700)
    go1 = scenario.GObject()
    window = Btpy.Window()
    window.set_full_screen()
    go1.add_image_layout(
        ["../res/image/animation/spider_1.png"]
    )
    go1.add_image_layout(
        ["../res/image/animation/spider_2.png"]
    )
    go1.set_vector_arrow([10, 0])
    scenario.add(go1)
    painter = Btpy.Painter(window.widget)
    painter.pack_in_axe()
    painter.set_background_color("white")
    print(go1.animation.image_layout_arr2d)
    def action(i):
        painter.repaint()
        painter.draw_image_layout_dict(
            go1.get_image_layout_dict()
        )
        print(f"repeat {i}")
        scenario.update()
        go1.animation.next()
    Btpy.repeat_each_async(3, action, 60)
    window.start()

   
    #------------------------------
    print(r)

main()