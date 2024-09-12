

from .in_deps import*
import os
import random
import time

class Basic:

    """
    Módulo de funcionalidades básicas para 
    mejorar la experiencia de desarrollo 
    en python.
    """

    def random_bool() -> bool:
        return random_bool()
    
    def random_choice(array):
        return random_choice(array)
    
    def random_without(range: int, 
        repeated_int_ar: list,
        is_exclusive:bool = False
        ) -> int:
        return random_without(
            range, 
            repeated_int_ar, 
            is_exclusive
        )
    
    def random_probability(porcentage: int)\
          -> bool:
        return random_probability(porcentage)
    
    def repeat(repetition: int, 
           seconds: int, 
           function):
        repeat(repetition, 
           seconds, 
           function)
        
    # return array or dict
    def map(array, function):
        return map(array, function)
    
    def iterator(array, 
                 is_cycle = False):
        return Iterator(array, is_cycle)
    
    def get_abc_tuple():
        return ABC_TUPLE
    
    def get_number_tuple():
        return NUMBER_TUPLE
    
    def get_animal_array():
        return ANIMAL_ARRAY
    
    def get_vegetable_dict():
        return VEGETABLE_DICT
    
    def init_array(range, value = None):
        return init_array(range, value)
    
    """
    Function that calculates the 
    average of the numbers in 
    the sent array.
    """
    def calculate_mid(array:list)->float:
        return calculate_mid(array)
    
    def deep(array) -> int:
        return deep(array)
    
    def key_by_index(dict, index: int) \
        -> str:
        return key_by_index(dict, int)
    
    # return string_list
    def get_keys(dict) -> list:
        return get_keys(dict)
    
    """
    Function to identify if the input 
    number is contained within the 
    sending range.
    Ex:
        code: print(in_range(5, [4, 6]))
        output: True
    """
    def in_range(number: int, range: list)\
        -> bool:
        return in_range(number, range)
    
    def part_from_percent(percent: int, 
        total: int) -> float:
        return part_from_percent(percent, 
            total)
    
    def percent_from_part(part: int, 
        total: int)-> float:
        return percent_from_part(part, 
            total)
    
    def total_from_part(percent, 
        part: int) -> float:
        return total_from_part(percent, 
            part)
    
    """
    function to validate the sent string; 
    this validates if the string is a 
    string, is not empty and is greater 
    than the minimum (optional)
    """
    def valid_string(data: str, 
             min_size = -1,
             is_strict = False):
        valid_string(data, min_size, is_strict)

    def randint_list(size: int, 
        range_arr: list) -> list:
        return randint_list(int, range_arr)
    
    # return number
    def set_inrange(value: int, 
            range_arr: list):
        return set_inrange(value, range_arr)
    
    # return number
    def sum_in_range(value_a, value_b, 
                    range_arr):
        return sum_in_range(value_a, 
            value_b, range_arr)
    
    def dict_to_array(dict) -> list:
        return dict_to_array(dict)
    
    # not return
    def valid_index(index: int, leng: int):
        return valid_index(index, leng)
    
    # return element type
    def sum_array(array):
        return sum_array(array)
    
    def percent_to_index(percent, limit):
        return percent_to_index(percent, 
                    limit)
    
    # useless
    def fuse(array_a, array_b) -> list:
        return fuse(array_a, array_b)
    
    def is_error(value):
        return is_error(value)
    
    # return int
    def random_without_repeat(range_arr, 
        repeated_int_ar,
        is_exclusive = False):
        return random_without_repeat(
            range_arr, 
            repeated_int_ar,
            is_exclusive)
    
    def random_ip():
        return random_ip()
    
    def missing_numbers(number_list):
        return missing_numbers(number_list)
    
    def switch():
        return Switch()
    
    def counter_call(limit: int):
        return CounterCall(limit)
    
    def probability():
        return Probability()
    
    # return int
    def compare_strings(strig_primal, 
            string_to_compare):
        return compare_strings(strig_primal, 
            string_to_compare)
    
    def related_dict(similar_percent: int = 70):
        return RelatedDict(similar_percent)
    
    # useless; ramplazable por string[index]
    # return char
    def charat(string:str, index:int) -> str:
        return charat(string, index)
    
    def cut_from(string: str, caracter: str)\
    -> str:
        return cut_from(string, caracter)
    
    def cut_until(string: str, caracter: str)\
    -> str:
        return cut_until(string, caracter)
    
    # return string_array
    def divide_string(index:int, string:str)\
        -> list:
        return divide_string(index, string)
    
    # return string
    def next_word(text: str, 
            searched_string: str):
        return next_word(text, 
            searched_string)
    
    def get_between(base:str, start:str,
        end:str) -> str:
        return get_between(base, start, end)
    
    def insert_string(index:int, base_string:str, 
        new_string:str) -> str:
        return insert_string(index,
            base_string, new_string)
    
    def normalize(text: str) -> str:
        return normalize(text)
    
    def split_by(string, dividers_arr: list):
        return split_by(string, dividers_arr)
    
    def simil_search(array:list, element:str, 
        required_percent:int) -> str:
        return simil_search(array, element, 
                required_percent)
    
    def get_description(string,
        separator_string, range_string_array):
        return get_description(
            string,
            separator_string, 
            range_string_array
            )
    
    """
    Function that converts the elements of 
    an array into the keys of a dictionary; 
    with the data sent as an element.
    EXAMPLE:
        array = ['a', 'b', 'c', 'd', 'e']
        result:list = Basic.array_to_dict(array)
        print(result)
    OUTPUT:
        {'a': None, 'b': None, 'c': None, 
        'd': None, 'e': None}
    """
    def array_to_dict(array:list, 
    data_type = None)->dict:
        return array_to_dict(array, 
            data_type)
    
    """
    Function that returns an element of 
    the array if the sent function returns 
    true. If the element does not exist, 
    it returns a value of none.
    EXAMPLES: 
    """
    def seek(function, array:list) ->list:
        return seek(function, array)
    
    """
    Function that applies the strip function 
    to all strings in a string array.
    """
    def strip_array(array:list[str])\
        ->list[str]:
        return strip_array(array)
    
    """
    function that replaces an element of the 
    sent array with the new element, looking 
    for an element that returns true in the 
    sent function.
    """
    def update(function, array:list, element)\
        ->list:
        return update(function, array, element)
    
    def whats_ranges(ranges_named:dict, 
            number:int)->list[str]:
        return whats_ranges(ranges_named,
                number)
    
    def count_keys(keys_array:list[str])\
        ->dict[int]:
        return count_keys(keys_array)
    
    # upgrade
    def layout_image(name_image_arr:\
            list[str] = []):
        return LayoutImage(name_image_arr)
    
    # upgrade
    def motion_image(self, name = ""):
        return MotionImage(name)
    
    def crono():
        return Crono()
    
    def pause(seconds:int):
        time.sleep(seconds)
    
    def splitip(text:str, divider:str)\
            ->list[str]:
        return splitip(text, divider)
    
    def repeat_in_thread(interval:int, 
        action, limit:int = -1)->None:
        return repeat_in_thread(interval,
            action, limit)
    
    def route_in_nested_dict(seek_string:str,
        dict:dict[dict]) ->list[str]:
        return route_in_nested_dict(
            seek_string, dict)
    
    def random_point(range_ar):
        return [
            Basic.randrange(range_ar),
            Basic.randrange(range_ar)
        ]

    def random_point_ar(quantity, range_ar):
        point_array = []
        point = None
        for i in range(quantity):
            point = Basic.random_point(
                range_ar)
            point_array.append(point)
        return point_array

    # useless por f format que es mas rapido
    def enclose(symbol, text):
        return symbol + text + symbol
    
    def randindex(array):
        return random.randint(0,
            len(array) -1)

    def randrange(range_arr):
        return random.randint(range_arr[0], 
                range_arr[1])
    
    def clean_console():
        os.system ("cls")

    # upgrade
    def date_manager()->DateManager:
        return DateManager()
    
    def has_all(array, function):
        return has_all(array, function)

    def has_some(array, function):
        return has_some(array, function)
    
    def has_none(array, function):
        return has_none(array, function)
    
    def new_thread(function):
        return new_thread(function)
    
    def range_space():
        return RangeSpace()
    
    # return point
    def move_point(
        old_point:list[int], 
        new_point:list[int], 
        range_space
        ) -> list[int]:
        return move_point(old_point, 
            new_point, range_space)
    
    def is_number(data) -> bool:
        return is_number(data)
    
    # mejorar
    def resize_image(route, range_arr)->str:
        return resize_image(route, range_arr)
    
    def is_byte(data)-> bool:
        return is_byte(data)
    
    def is_rgb(data):
        return is_rgb(data)

