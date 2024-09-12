




class Controller:

    """
    Componente destinado a la interacción 
    de la vista y el modelo
    """
    def __init__(self, model, view) -> None:
        self.view = view
        self.model = model
        pass