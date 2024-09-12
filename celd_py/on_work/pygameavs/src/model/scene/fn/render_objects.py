


"""
función que convierte los objetos en 
cámara en una lista de objetos 
gráficos pre-renderizados
"""
def render_gobjects(gobject_arr):
    # crear los render images
    render_image_list = []
    dict = {}
    go = None
    print(f"size object recieved {len(gobject_arr)} from render_gobjects")
    for go in gobject_arr:
        dict = create_render_image()
        dict["route"] = go.get_image_route()
        dict["point"] = go.point_in_cam
        render_image_list.append(dict)
    # almacenar objetos renderizados
    return render_image_list

def create_render_image():
        return {
            "type":"render_image",
            "route":"",
            "point":[0, 0]
        }