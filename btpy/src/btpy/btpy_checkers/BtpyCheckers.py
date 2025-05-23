

from .in_deps import*

class BtpyCheckers:

    """
    This is a static class that is 
    part of the BTPY split class. 
    It contains functions related to 
    data type checking.
    """

    def are_equal_strings(STRING_1:str, 
            STRING_2:str)-> bool:
        """
        Function that checks if two 
        strings are equal, ignoring case.
        FINAL
        """
        return are_equal_strings(STRING_1,
                STRING_2)
    
    def in_range(NUMBER: int|float, 
            RANGE_LIST_X2: list[int|float])\
            -> bool:
        """
        Function to identify if the input 
        number is contained within the 
        sending range. The range sent is 
        an integer array where index 0 
        is min and 1 is max.
        FINAL
        """
        return in_range(NUMBER, RANGE_LIST_X2)
    
    def is_number(ANY_DATA:any) -> bool:
        """
        Function that returns true if 
        the data sent is float or 
        integer type.
        FINAL
        """
        return is_number(ANY_DATA)
    
    def is_range(ANY_DATA:any)-> bool:
        """
        Function that returns true if the 
        data sent is a range in array 
        format, that is, an array of int 
        or float of size x2 where index 0 
        is min and index 1 is max; if the 
        data is not a range, it will return 
        false.
        FINAL
        """
        return is_range(ANY_DATA)

    def are_all_the_same(ARRAY:list)->bool:
        """
        TESTED
        Checks if all elements
        of an array are equal.
        """
        return are_all_the_same(ARRAY)
    
    def equal_string(STRING_1:str, 
        STRING_2:str)-> bool:
        """
        TESTED
        Function that checks if two 
        strings are equal, ignoring case.
        """
        return equal_string(STRING_1, 
            STRING_2)
    
    from typing import Callable

    def has_all(ITERABLE:list|dict|str, 
            FUNCTION:Callable)-> bool:
        """
        TESTED
        Function that returns true if
        the checker function applied to all
        the elements of the iterable return
        true when each element is received.
        """
        return has_all(ITERABLE, FUNCTION)
    
    def has_some(ITERABLE
            :list|dict|str|tuple|set, 
            FUNCTION:callable)->bool:
        """
        TESTED
        Function that returns true if 
        the verification function applied 
        to all elements returns false in 
        any case.
        """
        return has_some(ITERABLE, FUNCTION)

    def in_range(NUMBER: int|float, 
            RANGE_ARR_X2: list[int])\
            -> bool:
        """
        TESTED
        Function to identify if the input 
        number is contained within the 
        sending range. The range sent is 
        an integer array where index 0 
        is min and 1 is max.
        """
        return in_range(
            NUMBER, 
            RANGE_ARR_X2
        )
    
    def is_byte_127(ANY_DATA : any)\
            -> bool:
        """
        TESTED
        Function that returns true if 
        the data sent is a byte 127 type, 
        that is, an 8-bit integer between 
        the range -127 and 127.
        """
        return is_byte_127(ANY_DATA)
    
    def is_byte_256(ANY_DATA : any)\
        -> bool:
        """
        TESTED
        Function that returns true if 
        the data sent is a byte 256 type, 
        that is, an 8-bit integer in the 
        range between 0 and 256.
        """
        return is_byte_256(ANY_DATA)
    
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
        return is_colliding_rect(
            RECT_DICT_1, 
            RECT_DICT_2
        )
    
    def is_dict_square(ANY_DATA: any)\
            -> bool:
        """
        TESTED
        Function that verifies if the 
        data sent is a rectangle in 
        dictionary format; this format 
        must contain the keys x for 
        location x, y for location y, 
        width for the size in x and height 
        for the size in y.
        """
        return is_dict_rectangle(ANY_DATA)
    
    def is_error_return(ANY_DATA:any)\
            ->bool:
        """
        TESTED
        Function that tests whether a value
        is a return error such as 
        none, void string, void dict, void
        array, or void tuple
        """
        return is_error_return(ANY_DATA)
    
    def is_function(ANY_DATA : any)->bool:
        """
        TESTED
        Function that returns true if 
        the data sent is of function 
        type and returns false if it 
        is not. Lambda functions, named 
        functions, and methods are 
        considered functions.
        """
        return is_function(ANY_DATA)
    
    def is_hex_color(ANY_DATA : any)\
            -> bool:
        """
        TESTED
        Function that returns true if 
        the data sent is a hexadecimal 
        color code string (hex color) and 
        returns false if it is not.
        """
        return is_hex_color(ANY_DATA)
    
    def is_index(INDEX:int, ARRAY:list)\
            -> bool:
        """
        TESTED
        Function that returns true if 
        the index argument sent is a 
        correct index for the array sent.
        """
        return is_index(INDEX, ARRAY)
    
    def is_iterable(ANY_DATA:any)-> bool:
        """
        TESTED
        Function that returns true if
        the data sent is of an iterable 
        type; that is a list, set, dict, 
        tuple, or string type.
        """
        return is_iterable(ANY_DATA)

    def is_number(ANY_DATA:any) -> bool:
        """
        TESTED
        Function that returns true if 
        the data sent is of float or 
        integer type.
        """
        return is_number(ANY_DATA)
    
    def is_ordered_iterable(ANY_DATA:any)\
            -> bool:
        """
        TESTED
        Function that returns true if 
        the data sent is an ordered 
        iterable type such as list, 
        tuple, and string.
        """
        return is_ordered_iterable(
            ANY_DATA)
    
    def is_point_2D(ANY_DATA : any)->bool:
        """
        TESTED
        Function that returns true if 
        the data sent is a point 2D in 
        array format; that is, an array 
        of numbers with two elements where 
        the first element is the x 
        coordinate and the second element 
        is the y coordinate.
        """
        return is_point_2D(ANY_DATA)


    def is_point_3D(ANY_DATA : any)->bool:
        """
        TESTED
        Function that returns true if 
        the data sent is a 3D point in 
        array format; that is, an array 
        of numbers with two elements where 
        the first element is the x 
        coordinate, the second element is 
        the y coordinate, and the third 
        element is the z coordinate.
        """
        return is_point_3D(ANY_DATA)
    
    def is_point_in_rect(
            POINT2D:list[int|float], 
            RECT_ORIGEN_POINT2D
                :list[int|float], 
            HEIGHT:int|float, 
            WIDTH:int|float
            )-> bool:
        """
        TESTED
        Function that returns true if the 
        sent 2D point is inside the sent 
        rectangle; and returns false if 
        it is not inside.
        """
        return is_point_in_rect(
            POINT2D, 
            RECT_ORIGEN_POINT2D, 
            HEIGHT, 
            WIDTH
        )
    
    def is_point_list_2D(ANY_DATA : any)\
            -> bool:
        """
        Function that returns true if 
        the data sent is a pont list 
        in the format of an array of 
        numbers of size x2; and returns 
        false if it is not.
        """
        return is_point_list_2D(ANY_DATA)
    
    def is_point_list_3D(ANY_DATA : any)\
            -> bool:
        """
        Function that returns true if 
        the data sent is a pont list 
        in the format of an array of 
        numbers of size x3; and returns 
        false if it is not.
        """
        return is_point_list_3D(ANY_DATA)
    
    def is_range(RANGE_ARRAY_X2
            :list[int|float])\
            -> bool:
        """
        TESTED
        Function that returns true if the 
        data sent is a range in array 
        format, that is, an array of int 
        or float of size x2 where index 0 
        is min and index 1 is max; if the 
        data is not a range, it will return 
        false.
        """
        return is_range(RANGE_ARRAY_X2)
    
    def is_RGB(ANY_DATA : any)->bool:
        """
        TESTED
        function that returns true if the 
        data sent is an array in RGB 
        format, that is, an array of 
        integers of rank 256 of size x3. 
        If it is not, it returns false.
        """
        return is_RGB(ANY_DATA)
    
    def is_RGBA(ANY_DATA:any)->bool:
        """
        TESTED
        Function that returns true if 
        the data sent is an RGBA array; 
        that is, an x4 array where the 
        first 3 elements are integers of 
        range 256 that represent the 
        colors red, green and blue; and 
        the last element (index 3) is 
        the alpha value which is a float 
        of range 0 and 1.
        """
        return is_RGBA(ANY_DATA)
    
    def is_string_of_size(ANY_DATA:any, 
            SIZE:int)-> bool:
        """
        TESTED
        Function that returns true if 
        the data sent is a string of the 
        indicated size; and returns false
        if it is not.
        """
        return is_string_of_size(ANY_DATA,
            SIZE)
    
    def is_unordered_iterable(ANY_DATA:any)\
            -> bool:
        """
        Function that returns true if 
        the data sent is an unordered 
        iterable type such as dict 
        and set.
        """
        return is_unordered_iterable(
            ANY_DATA)
    
    def instanceof_iterable(
            ITERABLE:list|set|tuple|dict, 
            KEY_TYPE)-> bool:
        """
        TESTED
        Function that returns true if
        all elements of the iterable
        are the same type of data sent
        in the KEY_TYPE parameter.
        """
        return instanceof_iterable(
            ITERABLE, 
            KEY_TYPE
        )
    
    def is_checker_function(
            FUNCTION:callable)\
            -> bool:
        return is_checker_function(
            FUNCTION)
    
    def type_iterable(ITERABLE
            :list|tuple|dict|set)-> str:
        """
        TESTED
        Function that returns the data 
        type of the data contained within 
        an iterable if it is an iterable 
        of homogeneous types.
        """
        return type_iterable(ITERABLE)

    
    
    
