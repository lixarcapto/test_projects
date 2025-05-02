


from .in_deps import*

class Tkupg:

    """
    Módulo que simplifica en parte el manejo 
    de los widgets de tkinter; y cambia el 
    sistema parametros parámetros indefinidos
    por un sistema de construcción con 
    parámetros predefinidos. Tambien añade 
    algunos widgets.
    """

    def window():
        return WidgetWindow()

    def input(window):
        return WidgetInput(window)

    def button(window):
        return WidgetButton(window)
    
    def link(window, url):
        return WidgetLink(window, url)

    def label(window):
        return WidgetLabel(window)
    
    def icon(window, route):
        return WidgetIcon(window, route)

    def painter(window):
        return Painter(window)
