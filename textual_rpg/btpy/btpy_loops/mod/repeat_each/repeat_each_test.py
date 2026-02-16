



from .repeat_each import*

def repeat_each_test():
    print("--> repeat_each_test")
    r = []
    def f(n):
        r.append(0)
        if(n == 3): return False
    repeat_each(0.1, f)
    print(r == [0, 0, 0, 0])

    print("")