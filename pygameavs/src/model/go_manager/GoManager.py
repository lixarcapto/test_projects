

from ..scene.Scene import Scene

class GoManager:

    """
     Clase dedicada al manejo y control 
     de eventos de una clase scene.
    """
    def __init__(self, scene) -> None:
        self.scene = scene
        self.__event_queue = []

    # PUBLIC ACCESORS -----------------------

    def set_scene(self, scene):
        self.scene = scene

    def get_scene(self):
        return self.scene

    # PUBLIC MUTATORS ------------------------

    def update(self):
        self.__pick_events()
        self.__process_event()

    def clear_event_asociated(self, ID:str)\
            ->None:
        new_array = []
        for e in self.__event_queue:
            if(not ID in e):
                new_array.append(e)
        self.__event_queue = new_array

    # PRIVATE ---------------------------------

    
    
    def __process_event(self):
        """
        Función selectora que procesa los 
        eventos almacenados en la cola de 
        eventos.
        """
        for event in self.__event_queue:
            print(f"{event} from __process_event")
            if(event[0] == "sense_change"):
                self.scene.effect_sense_change(
                    event)
            if(event[0] == "move"):
                self.scene.effect_move(event)
            if(event[0] == "move_cam"):
                self.scene.effect_move_cam(
                    event)
        # solo para kill
        for event in self.__event_queue:
            if(event[0] == "kill"):
                self.effect_kill(event)
            if(event[0] == "transform"):
                self.scene.effect_transform(
                    event)
        self.__free()

    def effect_kill(self, EVENT):
        self.scene.effect_kill(EVENT[1])
        self.clear_event_asociated(
            EVENT[1]
        )

    def __free(self):
        self.__event_queue.clear()

    def __pick_events(self):
        """
        Función que recolecta los eventos 
        desencadenados en los objetos de 
        la lista de objetos y los almacena 
        en la cola de eventos.
        """
        event_list = self.scene.pick_events()
        self.__event_queue = self.__event_queue \
            + event_list
        
    