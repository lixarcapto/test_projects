



from ....btpy_maths.mod.sum_in_range.sum_in_range import*
from ....btpy_maths.mod.set_in_range.set_in_range import*

class LimitNumber:

    def __init__(self, number, range_arr) -> None:
        self.__number = number
        self.__range_arr = range_arr

    def sum(self, number):
        self.__number = sum_in_range(
            self.__number,
            number, 
            self.__range_arr
        )

    def get(self):
        return self.__number

    def asign(self, number):
        self.__number = set_in_range(
            number, 
            self.__range_arr
        )