

from btpy.Btpy import Btpy

def main():
    r = "None"
    #--------------------------------

    scenario = Btpy.Scenario()
    scenario.set_size(1300, 700)
    scenario.set_resource_folder(
        "../res/image"
    )
    scenario.set_image_format("png")
    go1 = scenario.GObject()
    window = Btpy.Window()
    window.set_full_screen()
    go1.add_image_layout(
        ["animation/spider_1"]
    )
    go1.add_image_layout(
        ["animation/spider_2"]
    )
    go1.set_vector_arrow([10, 0])
    go2 = scenario.GObject()
    go2.add_image_layout(
        "cell")
    go2.set_location([300, 0])
    scenario.set(go2)
    scenario.set(go1)
    painter = Btpy.Painter(window.widget)
    painter.pack_in_axe()
    painter.set_background_color("white")
    render = None
    def action(i):
        render = scenario.render()
        painter.repaint()
        painter.draw_image_layout_dict_array(
            render
        )
        print(render)
        print(f"repeat {i}")
        scenario.update()
    Btpy.repeat_each_async(0.4, action, 60)
    window.start()

   
    #------------------------------
    print(r)

main()