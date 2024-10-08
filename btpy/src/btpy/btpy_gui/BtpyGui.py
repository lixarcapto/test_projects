

from .in_deps import*
from ..btpy_engine.BtpyEngine import BtpyEngine

class BtpyGui(BtpyEngine):

    """
     clase que contiene envolturas para 
     los componentes gráficos detectar 
     con la intención de facilitar el 
     uso de tkinter.
    """

    Window = WidgetWindow
    Input = WidgetInput
    Button = WidgetButton
    Link = WidgetLink
    Label = WidgetLabel
    Combobox = WidgetComboBox
    Grid = WidgetGrid
    Painter = Painter
    CircleGraph = WidgetCircleGraph
    PressTime = WidgetPressTime
    Frame = WidgetFrame
    PanelButton = WidgetPanelButton