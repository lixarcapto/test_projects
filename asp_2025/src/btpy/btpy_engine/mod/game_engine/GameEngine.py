

from ..scenario.Scenario import Scenario
from ....btpy_gui.mod.canvas.Canvas import Canvas
from ....btpy_gui.mod.widget_composite.WidgetComposite import WidgetComposite
from ....btpy_utilitys.mod.repeat_each_async.repeat_each_async import*

class GameEngine(WidgetComposite):

    def __init__(self, widget, TITLE):
        super().__init__(widget, False)
        self.resources_path:str = "./"
        self.canvas = Canvas(self.widget)
        self.canvas.pack()
        self.scenario = Scenario()
        self.set_title(TITLE)
        self.__flag_repeater = None

    def start(self)->None:
        """
        Funcion que inicia la repetacion
        de un bucle de juego principal. 
        Este bucle consiste en un repintado
        del canvas, actualizacion del
        scenario, renderizado de los
        objetos del scenario y el 
        pintado del renderizado en el
        canvas.
        """
        def fn(n):
            self.__update()
        self.__flag_repeater \
            = repeat_each_async(0.60, fn)
        
    def __update(self):
        self.canvas.repaint()
        self.scenario.update()
        render_list = self.scenario\
            .get_render_list()
        for render in render_list:
            self.canvas.draw_path_image(
                render["point"],
                self.resources_path 
                + render["image_key"]
            )
        
    def stop(self):
        """
        Funcion que detiene el bucle
        del juego principal.
        """
        self.__flag_repeater.stop()
