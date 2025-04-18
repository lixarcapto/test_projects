

def is_point_2D(ANY_DATA : any)->bool:
     """
     Function that returns true if 
     the data sent is a point 2D in array 
     format; that is, an array of 
     numbers with two elements where 
     the first element is the x 
     coordinate and the second element 
     is the y coordinate.
     """
     return __is_point(ANY_DATA, 2)


def is_point_3D(ANY_DATA : any)->bool:
     """
     Function that returns true if 
     the data sent is a 3D point in 
     array format; that is, an array 
     of numbers with two elements where 
     the first element is the x 
     coordinate, the second element is 
     the y coordinate, and the third 
     element is the z coordinate.
     """
     return __is_point(ANY_DATA, 3)

def __is_point(ANY_DATA:any, SIZE:int)\
               -> bool:
        # if is not a list
        if(not type(ANY_DATA) == list):
            return False
        # if is litle
        if(not len(ANY_DATA) == SIZE):
            return False
        # If the coordinates are not 
        # numbers
        for e in ANY_DATA: 
            if(not type(e) == int
            and not type(e) == float):
                return False
        return True