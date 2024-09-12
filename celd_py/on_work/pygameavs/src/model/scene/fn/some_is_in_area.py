


from btpy.src.btpy.Btpy import Btpy

def some_is_in_area(square, gobject_dict):
    e = None
    r = False
    for k in gobject_dict:
        e = gobject_dict[k]
        r = Btpy.colliding_square(
            square,
            e.get_box_square()
        )
    return r