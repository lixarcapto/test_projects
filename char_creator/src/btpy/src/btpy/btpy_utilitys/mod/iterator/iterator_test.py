


from .Iterator import*
from ....btpy_utilitys.mod.print_test.print_test import*

@print_test
def iterator_test(test_arr):
    # test de limitado
    iterator = Iterator([3, 2, 1, 0])
    array = []
    while(iterator.next()):
        array.append(iterator.get())
    test_arr.append([3, 2, 1, 0] == array)
    # test de ciclico
    iterator2 = Iterator([3, 2, 1, 0], 
            is_cycle=True)
    array = []
    n = 0
    while(iterator2.next()):
        array.append(iterator2.get())
        if(n >= 7):
            break
        n += 1
    test_arr.append(
        [3, 2, 1, 0, 3, 2, 1, 0] == array
    )