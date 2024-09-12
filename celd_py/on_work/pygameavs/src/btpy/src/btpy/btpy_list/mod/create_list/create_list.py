



def create_list(size:list):
    array = []
    for y in range(size[0]):
        array.append(None)
        if(not len(size) > 2): continue
        array[y] = []
        for x in range(size[1]):
            array[y].append(None)
            if(not len(size) == 3): continue
            array[y][x] = []
            for z in range(size[2]):
                array[y][x].append(None)
    return array


                
