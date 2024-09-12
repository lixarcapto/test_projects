



# return point
def center_square(point:list[int], 
        size_x:int, 
        size_y:int)->list[int]:
  """
  This function calculates the center 
  point of a square represented by 
  a dictionary.
  """
  # Get the center coordinates
  return [
      point[0] + size_x // 2,
      point[1] + size_y // 2
  ]