
import threading


def new_thread(function):
    """
    Decorador para crear de forma 
    fácil y ágil nuevos hilos.
    """
    def wrapper():
        __create_thread(function)
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