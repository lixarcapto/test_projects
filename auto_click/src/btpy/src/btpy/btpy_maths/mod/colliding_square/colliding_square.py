

def square_dict(point, size_x, size_y):
    return {
      'x': point[0], 
      'y': point[1], 
      'width': size_x, 
      'height': size_y
    }


def colliding_square(square1:dict[int], 
      square2:dict[int])->bool:
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
    # Check if the right edge of 
    # square1 is to the left of the 
    # left edge of square2
    if square1['x'] + square1['width'] <= square2['x']:
        return False
    # Check if the left edge of 
    # square1 is to the right of the 
    # right edge of square2
    if square1['x'] >= square2['x'] + square2['width']:
        return False
    # Check if the bottom edge of 
    # square1 is above the top edge 
    # of square2
    if square1['y'] + square1['height'] <= square2['y']:
        return False
    # Check if the top edge of 
    # square1 is below the bottom edge 
    # of square2
    if square1['y'] >= square2['y'] + square2['height']:
        return False
    # No edge cases were met, so the 
    # squares must be colliding
    return True