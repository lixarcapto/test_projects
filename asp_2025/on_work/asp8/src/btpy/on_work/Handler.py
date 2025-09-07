


class Handler:

    """
    Implementacion heredable del 
    responsability chain pattern.
    """

    def __init__(self) -> None:
        self.handler = None
    
    def execute(self, result):
        if(not self.handler == None):
            return self.handler.execute(result)
        return result

    def add_handler(self, handler):
        if(self.handler == None):
            self.handler = handler
        else:
            self.handler.add_handler(handler)