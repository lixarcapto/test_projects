


class UniqueInt:

    def __init__(self) -> None:
        self.__number = 0

    def get(self):
        result = self.__number
        self.__number += 1
        return result
    
    def reset(self):
        self.__number = 0