

from btpy.src.btpy.Btpy import Btpy

class Controller:

    def __init__(self, view, model) -> None:
        self.view = view
        self.model = model
        def update():
            self.model.scene.update()
            render_list = self.model\
                .scene.render()
            self.view.painter.draw_pod_array(
                render_list)
        Btpy.repeat_each_async(5, 100, 
            update)
        self.view.window.start()
