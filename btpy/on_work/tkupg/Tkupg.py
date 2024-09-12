


from ...src.btpy.btpy_gui.in_deps import*

class Tkupg:

    """
    Módulo que simplifica en parte el manejo 
    de los widgets de tkinter; y cambia el 
    sistema parametros parámetros indefinidos
    por un sistema de construcción con 
    parámetros predefinidos. Tambien añade 
    algunos widgets.
    """

    
    
    def pod_image(route, point = [0,0]):
        return {
            "type":"image",
            "route":route,
            "point":point
        }
    
    def pod_image_layout(route_arr, 
            point=[0,0]):
        return {
            "type":"image_layout",
            "route_array":route_arr,
            "point":point
        }
    
    def pod_line(point_1, point_2):
        return {
            "type":"line",
            "point_1":[0, 0],
            "point_2":[0, 0],
            "width":1,
            "color":"white"
        }
    
    def pod_polygon_line(
            line_arr:list[list[int]],
            color = "white", 
            width = 1):
        return {
            "type":"polygon",
            "line_array":line_arr,
            "width":width,
            "color":color
        }

    def pod_polygon(point_arr):
        return {
            "type":"polygon",
            "point_array":point_arr,
            
            "width":1,
            "color":"white"
        }
    
    def pod_text(text, point=[0,0]):
        return {
            "type":"text",
            "point": [0,0],
            "text":""
        }
