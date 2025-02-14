


from .true_percentage import*

def true_percentage_test():
    print("true_percentage_test")
    r = true_percentage(
        [True, True, False, False])
    print(r == 50.0)

    print("")