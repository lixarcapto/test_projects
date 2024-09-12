


from .draw_image import*
from .draw_line import*
from .draw_polygon import*

"""
Funcion que dibuja un diccionario
de paint_order_map.
"""
def draw_pod_array(painter_data, 
        pod_array):
    # adapta los dicts a un formato list
    array = []
    if(type(pod_array) == dict):
        array.append(pod_array)
        pod_array = array
    # limpia el buffer de imagenes
    painter_data.clean_image_buffer()
    for pod in pod_array:
        if(pod["type"] == "image"):
            painter_data = __draw_POD_image(
                painter_data, pod)
        elif(pod["type"] == "image_layout"):
            painter_data = __draw_POD_image_layout(
                painter_data, pod)
        elif(pod["type"] == "line"):
            painter_data = __draw_POD_line(
                painter_data, pod)
        elif(pod["type"] == "polygon"):
            painter_data = __draw_POD_polygon(
                painter_data, pod)
    return painter_data

"""
Función que dibuja un Paint order de 
tipo image.
"""
def __draw_POD_image(painter_data, pod:dict)\
            ->None:
    painter_data = draw_image(\
        painter_data,
        pod["route"],
        int(pod["point"][0]),
        int(pod["point"][1])
    )
    return painter_data

def __draw_POD_image_layout(painter_data, 
        pod:dict)->None:
    for route in pod["route_array"]:
        painter_data = draw_image(\
            painter_data,
            route,
            int(pod["point"][0]),
            int(pod["point"][1])
        )
    return painter_data

def __draw_POD_line(painter_data, pod:dict)\
        ->None:
    painter_data = draw_line(
        painter_data,
        pod["point_1"],
        pod["point_2"],
        pod["color"],
        pod["width"]
    )
    return painter_data
            
def __draw_POD_polygon(painter_data,
        paint_order):
    po = paint_order
    painter_data = draw_polygon(
        painter_data,
        po["point_array"],
        po["color"],
        po["width"]
    )
    return painter_data

def __draw_POD_polygon(painter_data,
        paint_order):
    po = paint_order
    painter_data = draw_line_arr(
        painter_data,
        po["line_array"],
        po["color"],
        po["width"]
    )
    return painter_data

    