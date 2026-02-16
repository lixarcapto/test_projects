


class Switch:

    """
    TESTED
    Switch class to make automatic 
    changes to boolean variables with 
    each call at the switch method. 
    To use it, you simply create an 
    object with a boolean
    -style name and check it with 
    is_true().
    """

    def __init__(self, 
            state_boolean = True)-> None:
        self.__boolean:bool = state_boolean

    def switch(self)-> None:
        if(self.__boolean): 
            self.__boolean = False
        else: 
            self.__boolean = True
    
    def is_true(self)-> bool:
        return self.__boolean