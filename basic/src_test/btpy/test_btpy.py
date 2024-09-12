


from .mod.random_bool.test_random_bool import*
from .mod.cut_from.cut_from_test import*
from .mod.cut_from.cut_until_test import*
from .mod.remove_char.remove_char_test import*
from .mod.url_split.url_split_test import*

def test_btpy():
    test_random_bool()
    cut_from_test()
    cut_until_test()
    remove_char_test()
    url_split_test()