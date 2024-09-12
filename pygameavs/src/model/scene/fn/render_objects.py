


"""
función que convierte los objetos en 
cámara en una lista de objetos 
gráficos pre-renderizados
"""
def render_gobjects(gobject_arr):
    # crear los render images
    final_render_list = []
    dict = {}
    go = None
    print(f"size object recieved {len(gobject_arr)} from render_gobjects")
    for go in gobject_arr:
        render_list = go.render()
        final_render_list = render_list \
            + final_render_list
    # almacenar objetos renderizados
    return final_render_list

def create_render_image():
        return {
            "type":"render_image",
            "route":"",
            "point":[0, 0]
        }