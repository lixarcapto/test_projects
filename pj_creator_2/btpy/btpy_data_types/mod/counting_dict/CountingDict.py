

from ....btpy_utilitys.mod.max_key.max_key import max_key, min_key

class CountingDict:

    """
    Count dict is a data type used to 
    easily count the number of 
    repetitions of string keys in a 
    dataset. This class counts keys 
    one by one using the count method; 
    it obtains the most repeated key 
    with get_max and the least repeated 
    with get_min; it stores the 
    repetitions as a dictionary of 
    integers.
    TESTED
    """

    def __init__(self, 
                KEY_LIST:list[str] = []):
        self.__dict:dict[int] = {}
        if(KEY_LIST != []):
            self.count_list(KEY_LIST)

    def get(self)-> dict:
        """
        Gets the dictionary of integers 
        with the number of repetitions 
        of each key.
        """
        return self.__dict
    
    def get_max(self)-> str:
        """
        Get the most repeated key in 
        the dictionary.
        """
        if(self.__dict == {}):
            return None
        return max_key(self.__dict)
    
    def get_min(self)-> str:
        """
        Get the least repeated key 
        in the dictionary.
        """
        if(self.__dict == {}):
            return None
        return min_key(self.__dict)
    
    def clean(self)-> None:
        """
        Completely cleans the dictionary.
        """
        self.__dict = {}

    def count_list(self, 
                KEY_LIST:list[str])->None:
        """
        Counts the repetitions of each 
        string in the sent list.
        """
        for k in KEY_LIST:
            self.count(k)

    def count(self, KEY:str)-> None:
        """
        Counts the repetition of a 
        sent key string.
        """
        if(not KEY in self.__dict):
            self.__dict[KEY] = 1
        else:
            self.__dict[KEY] += 1