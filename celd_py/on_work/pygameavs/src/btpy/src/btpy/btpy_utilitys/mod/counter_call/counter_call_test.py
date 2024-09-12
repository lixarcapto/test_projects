


from .CounterCall import*

def counter_call_test():
    print("--> counter_call_test")
    counter = CounterCall(10)
    r = 0
    while(counter.is_end()):
        r = counter.get()
    print(r == 10)
    
    