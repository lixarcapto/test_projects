


from .create_list import*

def create_list_test():
    print("--> create_list_test")

    r = create_list([2, 3])
    print(len(r) == 2 and len(r[0]) == 3)

    r = create_list([2, 3, 4])
    print(len(r) == 2 \
          and len(r[0]) == 3 \
          and len(r[0][0]) == 4)

    print("")