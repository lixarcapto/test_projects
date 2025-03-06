



def flatten(matrix:list[list])->list[any]:
    plane_list:list[any] = []
    for sublist in matrix:
        for e in sublist:
            plane_list.append(e)
    return plane_list