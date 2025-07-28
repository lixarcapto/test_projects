

from ..is_dict_rectangle.is_dict_rectangle import*

def is_colliding_rect(
        RECT_DICT_1:dict[int], 
        RECT_DICT_2:dict[int])->bool:
    """
    This function checks if two squares 
    are colliding based on their 
    coordinates and dimensions. By gemini.
    square = {
      "x":location_x
      "y":location_y
      "width":size_x
      "height":size_y
    }
    """
    if(not is_dict_rectangle(RECT_DICT_1)):
        raise Exception(f"<!>Error: The parameter RECT_DICT_1 is not a valid dictionary-format rectangle; its value is (\"{RECT_DICT_1}\").")
    if(not is_dict_rectangle(RECT_DICT_2)):
        raise Exception(f"<!>Error: The parameter RECT_DICT_2 is not a valid dictionary-format rectangle; its value is (\"{RECT_DICT_2}\").")
    # Check if the right edge of 
    # square1 is to the left of the 
    # left edge of square2
    side_x_1 = RECT_DICT_1['x'] \
      + RECT_DICT_1['width']
    if side_x_1 <= RECT_DICT_2['x']:
        return False
    # Check if the left edge of 
    # square1 is to the right of the 
    # right edge of square2
    side_x_2 = RECT_DICT_2['x'] \
      + RECT_DICT_2['width']
    if RECT_DICT_1['x'] >= side_x_2:
        return False
    # Check if the bottom edge of 
    # square1 is above the top edge 
    # of square2
    side_y_1 = RECT_DICT_1['y'] \
      + RECT_DICT_1['height']
    if side_y_1 <= RECT_DICT_2['y']:
        return False
    # Check if the top edge of 
    # square1 is below the bottom edge 
    # of square2
    side_y_2 = RECT_DICT_2['y'] \
      + RECT_DICT_2['height']
    if RECT_DICT_1['y'] >= side_y_2:
        return False
    # No edge cases were met, so the 
    # squares must be colliding
    return True