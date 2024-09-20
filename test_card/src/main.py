


from Model import Model 
from View import View
from Card import Card
from btpy.src.btpy.Btpy import Btpy
import sys
import threading

def main():
    """
    NOTE: Analizar por que este codigo
    si funciona y el mio no..
    """
    model = Model()
    view = View()

    def main_thread():
        # Use a global variable to indicate the thread's exit condition
        global is_on
        is_on = True

        def action():
            global is_on
            print("exit try")
            is_on = False

        view.window.add_close_action(action)

        while is_on:
            if view.has_event:
                print("update")
                view.has_event = False
                message = view.request()
                model.receive(message)
                message = model.render()
                view.receibe(message)

    # Create a new thread for the main_thread function
    thread = threading.Thread(target=main_thread)

    # Start the thread and the main loop
    thread.start()
    view.start()

    # Wait for the thread to finish before exiting
    thread.join()
    sys.exit(0)
    """
    model = Model()
    view = View()
    is_on = True
    @Btpy.new_thread
    def main_thread():
        def action():
            print("exit try")
            is_on = False
        view.window.add_close_action(action)
        while(is_on):
            if(view.has_event):
                print("update")
                view.has_event = False
                message = model.render()
                view.receibe(message)
        sys.exit(0)
    main_thread()
    view.start()
    """

main()