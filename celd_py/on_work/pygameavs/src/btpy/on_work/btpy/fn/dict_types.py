


def square():
    return {
        "type":"square",
        "x":0,
        "y":0,
        "width":0,
        "height":0
    }

def render_image():
    return {
        "type":"image",
        "route":"",
        "point":[0,0]
    }

def render_line(point1, point2, width, rgb):
    return {
        "type":"line",
        "point1":point1,
        "point2":point2,
        "width":width,
        "rgb":rgb
    }