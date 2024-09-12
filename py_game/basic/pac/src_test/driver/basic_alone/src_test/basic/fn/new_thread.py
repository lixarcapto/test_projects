
import threading

"""
Decorador para crear de forma fácil y ágil 
nuevos hilos.
"""
def new_thread(function):
        def wrapper(route):
            __create_thread(function, route)
        return wrapper

def __create_thread(target_function, 
        *args, **kwargs):
    # Create a new thread object
    thread = threading.Thread(
        target=target_function, 
        args=args, 
        kwargs=kwargs
    )
    # Start the thread execution
    thread.start()