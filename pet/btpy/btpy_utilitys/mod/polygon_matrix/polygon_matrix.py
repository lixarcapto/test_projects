


def polygon_matrix(size_celd, 
      size_x, size_y):
   size_x += 1
   size_y += 1
   line_arr = []
   # horizontales
   p_origen = [0, 0]
   p_destiny = [0, 0]
   line = [[0, 0], [0, 0]]
   y_location = 0
   for i in range(size_y +1):
      p_origen = [0, y_location]
      p_destiny = [size_x * size_celd, 
                  y_location]
      y_location += size_celd
      line = [p_origen, p_destiny]
      line_arr.append(line)
   # horizontales
   x_location = 0
   for i in range(size_x +1):
      p_origen = [x_location, 0]
      p_destiny = [x_location, size_y* size_celd]
      line = [p_origen, p_destiny]
      x_location += size_celd
      line_arr.append(line)
   return line_arr