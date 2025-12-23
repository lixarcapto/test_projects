

from ....btpy_checkers.mod.instanceof_iterable.instanceof_iterable import*
from ..counting_dict.CountingDict import CountingDict

class MultikeyDict:

    """
    This is a special dictionary 
    that allows storing values ​​with 
    multiple keys.
    """

    def __init__(self):
        self.dict:dict[str, any] = {}

    def has(self, KEY_LIST:list[str])\
            -> bool:
        """
        function that returns true if 
        there is any key in the 
        dictionary that shares at least 
        one key with the list of keys 
        sent.
        """
        self.__valid_key_list(KEY_LIST)
        for k in self.dict:
            for key_seeked in KEY_LIST:
                if(key_seeked in k):
                    return True
        return False
    
    def __get_most_matching_key(self,
            KEY_LIST:list[str])-> str:
        counting = CountingDict()
        for k in self.dict:
            for KEY_SEEKED in KEY_LIST:
                if(KEY_SEEKED in k):
                    counting.count(k)
        return counting.get_max()
    
    def get_first_with(self, KEY:str):
        pass

    def get_most_matched(self, KEY_LIST
            :list[str])\
            -> any:
        """
        Method that searches for the 
        key with the most matches with 
        the keys sent in the KEY_LIST 
        parameter.
        """
        self.__valid_key_list(KEY_LIST)
        k_result = self\
            .__get_most_matching_key(KEY_LIST)
        if(k_result != None):
            return self.dict[k_result]
        return None
    
    def set(self, KEY_LIST:list[str], 
            VALUE:any)\
            -> None:
        """
        method that adds a key value 
        pair to use as key the keys 
        sent in the list of the KEY_LIST 
        parameter.
        """
        self.__valid_key_list(KEY_LIST)
        key_str = str(KEY_LIST)
        self.dict[key_str] = VALUE

    def __str__(self):
        return self.dict
    
    def remove_most_matched(self, 
            KEY_LIST:list[str]):
        pass
    
    def remove_first_with(self, KEY:str):
        pass
    
    def remove_all_with(self, 
            KEY_LIST:list)-> None:
        """
        method that removes all 
        key-value pairs that contain 
        the indicated string in their 
        key.
        """
        self.__valid_key_list(KEY_LIST)
        k_result = self\
            .__get_most_matching_key(
                KEY_LIST)
        del(self.dict[k_result])

    def __valid_key_list(self, 
            ANY_TYPE:any)\
            -> None:
        if(not isinstance(ANY_TYPE, list)):
            raise Exception(f"<!>Error: The KEY parameter must be a list type, but its type is {type(ANY_TYPE)}, and its value is \"{ANY_TYPE}\".")
        if(not instanceof_iterable(
                ANY_TYPE, str)):
            raise Exception(f"<!>Error: The KEY_LIST parameter must be a list of string types and it is not, and its value is \"{ANY_TYPE}\".")