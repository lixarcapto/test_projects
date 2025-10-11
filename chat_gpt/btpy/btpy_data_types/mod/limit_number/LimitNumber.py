



from ....btpy_maths.mod.sum_in_range.sum_in_range import*
from ....btpy_maths.mod.set_in_range.set_in_range import*
from ....btpy_checkers.mod.is_range.is_range import*

class LimitNumber:

    """
    This class is a numeric data type 
    that allows the stored number to 
    be modified without exceeding 
    the predetermined limit ranges.
    TESTED
    """

    def __init__(self, NUMBER:int|float, 
            RANGE_LIST_X2:list[int|float]\
            ) -> None:
        """
        receives the numeric value of 
        the data to be stored (value) 
        and a range of type numeric 
        list x2 to limit the values ​
        ​of the stored number (value).
        """
        self.__number:int|float = 0
        self.__range_arr:list[int|float] \
            = [0, 0]
        self.set_range_arr(RANGE_LIST_X2)
        self.set(NUMBER)

    def set_range_arr(self, RANGE_ARR_X2\
            :list[int|float])-> None:
        """
        Function used to assign a limit 
        range for the number stored by 
        the object. This range is an 
        array of numbers of size x2 
        where index 0 is the minimum 
        and index 1 is the maximum.
        """
        if(not is_range(RANGE_ARR_X2)):
            raise Exception(
                f"The parameter RANGE_ARR_X2 is not a range type in a valid array format. Its value is \"{RANGE_ARR_X2}\"")
        self.__range_arr = RANGE_ARR_X2
        self.set(self.__number)
        
    def set(self, NUMBER:int|float)\
            -> None:
        """
        Assigns the number sent to 
        the value of the limit number, 
        keeping the value within the 
        predetermined range. If the 
        assigned number is greater or 
        less than the range, it assigns 
        the value to the closest limit.
        """
        if(not isinstance(NUMBER, int)
        and not isinstance(NUMBER, float)):
            raise Exception(
            """
            The parameter NUMBER is 
            not float or int, its 
            value is
            """
            f" \"{NUMBER}\"."
            )
        self.__number = set_in_range(
            NUMBER, 
            self.__range_arr
        )

    def is_at_maximum(self)-> bool:
        """
        returns true if the data value 
        is in the maximum range and 
        false otherwise.
        """
        if(self.__number
                == self.__range_arr[1]):
            return True 
        return False

    def is_at_minimum(self)-> bool:
        """
        returns true if the data value 
        is in the minimum range and 
        false otherwise.
        """
        if(self.__number
                == self.__range_arr[0]):
            return True 
        return False

    def sum(self, NUMBER:int|float)-> None:
        """
        Adds the number sent to the 
        value of limit number keeping 
        the result in the predetermined 
        range.
        """
        if(not isinstance(NUMBER, int)
        and not isinstance(NUMBER, float)):
            raise Exception(
            """
            The parameter NUMBER is not 
            float or int, its value is
            """
            + f" \"{NUMBER}\"."
            )
        self.__number = sum_in_range(
            self.__number,
            NUMBER, 
            self.__range_arr
        )

    def get(self)-> int | float:
        """
        Gets the current value of 
        the data type,
        """
        return self.__number