

from ..person.Person import Person
import random

class Society:

    def __init__(self):
        self.person_array = []
        None

    def size(self):
        return len(self.person_array)

    # return int
    def select_player(self):
        leng = len(self.person_array)
        code = random.randint(0, leng -1)
        return code

    """
        Funcion para buscar parejas para cada personaje
        ALGORITHM:
        * buscar una lista de ciudadanos solteros.
        * para cada personaje buscar elegir entre todos
        los personajes con mayores similitudes.
    """

    def look_for_couples(self):
        single_list_person = []
        person = None
        # busca los solteros
        for i in range(len(self.person_array)):
            person = self.person_array[i]
            if(person.data.is_single):
                single_list_person.append(person)
        # buscar pareja
        for i1 in self.person_array:
            person_search = self.person_array[i]
            if not person.data.is_single: continue
            for i2 in range(self.size()):
                person = random.choice(self.person_array)
                if not person.data.is_single: continue
                person_search.relate(person, 5, "another")
                person.relate(person, 5, "another")

    def encontrar_maximo(self, array):
        maximo = None
        maximo_puntos = float('-inf')
        # Inicializamos con el valor negativo infinito
        for diccionario in array:
            # Obtenemos el valor de puntos del diccionario
            puntos = diccionario.get("points", 0)
            if puntos > maximo_puntos:
                maximo = diccionario
                maximo_puntos = puntos
        return maximo

    # return string
    def write_player(self, code):
        person = self.get_person_by_code(code)
        return person.write()

    def make_the_desitions(self):
        person = None
        for i in range(self.size()):
            person = self.person_array[i]
            person = self.make_the_desition_in_person(person)
            self.person_array[i] = person

    def make_the_desition_in_person(self, person):
        decision_map = person.data.decision_map
        if("walk" == decision_map["key"]):
            person.data.location = "out"
        elif("rest" == decision_map["key"]):
            person.data.location = "inside"
        elif("meet_people" == decision_map["key"]):
            person.data.location = "out"
        return person

    def write(self):
        text = ""
        for i in range(self.size()):
            text += self.person_array[i].write() + "\n"
        return text

    def describe(self, player_code):
        text = "Appeared to be a"
        person = None
        for i in range(self.size()):
            person = self.person_array[i]
            # si es el mismo pj jugador lo salta
            if person.data.code == player_code: continue
            # si esta dentro de casa lo salta
            if not person.data.location == "inside": continue
            text += person.describe_appearance() + ". \n"
        return text

    def destroy(self):
        self.person_array.clear()

    def set_person(self, new_person):
        if (self.has_person(person)):
            person = None
            for i in range(self.size()):
                person = self.person_array[i]
                if(person.code == new_person.code):
                    self.person_array[i] = new_person
                    break
        else:
            self.person_array[i].append(new_person)

    def get_person_by_code(self, code):
        person = None
        for i in range(self.size()):
            person = self.person_array[i]
            if(person.data.code == code):
                return person

    def new(self, quantity, coordinate_array):
        person = None
        for i in range(quantity):
            person = Person()
            person.coordinate_array = coordinate_array
            person.randomize()
            self.person_array.append(person)
        self.advance_time()

    def advance_time(self):
        person = None
        for i in range(self.size()):
            person = self.person_array[i]
            person.advance_time()
            # si esta embarazada separa al bebe
            if(person.data.baby_can_walk):
                self.set_person(person.separate_the_baby())
        self.make_the_desitions()
        self.look_for_couples()

    def delete_person(self, delete_person):
        person = None
        for i in range(self.size()):
            person = self.person_array[i]
            if(delete_person.code == person.code):
                del(self.person_array[i])

    def has_person(self, seek_person):
        person = None
        for i in range(self.size()):
            if(seek_person.code == person.code):
                return True
        return False

    def extract_person_by_code(self, code):
        if not self.has(person): return None
        person = self.get_person_by_code(code)
        self.delete_person(person)
        return person
