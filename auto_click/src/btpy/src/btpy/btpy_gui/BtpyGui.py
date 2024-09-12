

from .in_deps import*
from ..btpy_const.BtpyConst import BtpyConst

class BtpyGui(BtpyConst):

    """
     clase que contiene envolturas para 
     los componentes gráficos detectar 
     con la intención de facilitar el 
     uso de tkinter.
    """

    def Window():
        return WidgetWindow()

    def Input(window):
        return WidgetInput(window)

    def Button(window):
        return WidgetButton(window)
    
    def Link(window, url):
        return WidgetLink(window, url)

    def Label(window):
        return WidgetLabel(window)
    
    def Combobox(window):
        return WidgetComboBox(window)
    
    def Grid(window, size_x, 
            size_y):
        return WidgetGrid(window, size_x, 
            size_y)
    
    def Painter(window)->Painter:
        return Painter(window)
    
    def WidgetCircleGraph(window):
        return WidgetCircleGraph(window)
    
    def WidgetPressTime(window):
        return WidgetPressTime(window)
    
    def Frame(window):
        return WidgetFrame(window)