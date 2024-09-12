


def set_point_in_cam(gobject_arr,
            point_arr):
        # asigna los puntos a los objetos
        for i in range(len(gobject_arr)):
            print(f"index {i} to leng object_arr {len(gobject_arr)} and leng point_arr {len(point_arr)}from set_point_in_cam")
            gobject_arr[i].point_in_cam \
             = list(point_arr[i])
        return gobject_arr