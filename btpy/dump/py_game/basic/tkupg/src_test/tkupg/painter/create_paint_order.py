


"""
Función que sirve para crear diccionarios 
de tipo Paint order. Un Paint order es un 
formato creado por mí para almacenar órdenes 
de dibujado para un canva. Cada paint order 
contiene un comando de dibujo, existen 
varios tipos. El primero es el image que 
contiene un array de nombres de imagenes, 
una direccion de la imagen, un formato,
un intervalo de tamaño, y un punto de 
locacion. El segundo es un poligon qué
contiene un array de puntos; un color, 
un ancho.
"""
def paint_order_image() -> dict:
    paint_order = {
    "paint_order": "image",
    "image_names_array" : [],
    "direction": "",
    "format": "",
    "location_x" : "0",
    "location_y" : "0",
    "point_location": [0, 0],
    "size_range": [0, 0]
    }
    return paint_order

def paint_order_point() -> dict:
    paint_order = {
    "paint_order": "poligon",
    "poligon" : [],
    "width": 0,
    "color_key": ""
    }
    return paint_order