

from ..constants.abc_array import ABC_ARRAY
from .remove_diferent import*
from .split_text_by_strings import*

"""
    Funcion que separa y obtiene las palabras de
    un texto a pesar de otros simbolos.
"""
# return string_array
def separate_the_words(text):
    abc_array = ABC_ARRAY
    abc_array.append(" ")
    text = remove_diferent(text, abc_array)
    words_array = split_text_by_strings(text,
        [",", " ", "."])
    words_array = list(map(lambda e: e.strip(),
        words_array))
    return words_array
