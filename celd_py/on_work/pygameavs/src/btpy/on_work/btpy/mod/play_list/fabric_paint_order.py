



"""
Funcion que crea un objeto paint_order_map
compatible con las funcionalidades de 
Painter.
"""
def fabric_paint_order(
    image_names_array:list[str],
    direction:str,
    format:str,
    point_arr:list[int]
    ) -> dict:
        paint_order_map = {
        "image_names_array" : image_names_array,
        "direction": direction,
        "format": format,
        "location_x" : point_arr[0],
        "location_y" : point_arr[1]
        }
        return paint_order_map