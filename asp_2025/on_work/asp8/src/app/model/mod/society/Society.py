


from ..person.Person import Person

class Society:

    MAXIMUM = 40

    def __init__(self) -> None:
        self.__person_list = []
        self.event_queue = []
        self.leng = 0

    def perceive(self):
        person = None
        for i in range(len(self.__person_list)):
            person = self.__person_list[i]
            if(person.is_outside()):
                person.set_object_description(
                    self.get_person_outside()
                )
            self.__person_list[i] = person

    def get_person_outside(self):
        person = None
        description_arr = []
        for i in range(len(self.__person_list)):
            person = self.__person_list[i]
            if(person.is_outside()):
                description_arr.append(
                    person.describe_appearance()
                )
            self.__person_list[i] = person
        return description_arr
    
    def active_decision(self):
        person = None
        description_arr = []
        for i in range(len(self.__person_list)):
            person = self.__person_list[i]
            # gestion el talk
            if(person.get_desicion() == "TALK"):
                id = self.get_focus_id()
                person_focus = self.get(id)
                result = person_focus\
                    .narrative_write()
                person.add_description(
                    "FOCUS_PERSON",
                    result
                )
            self.__person_list[i] = person
        return description_arr

    def update(self, region_description):
        # event locals
        self.process_events()
        # updates memorys
        self.perceive()
        self.set_region_description(
            region_description)

    def set_region_description(self, 
            region_description):
        person = None
        for i in range(len(self.__person_list)):
            person = self.__person_list[i]
            person.set_region_description(
                region_description
            )
            self.__person_list[i] = person

    def add(self, person):
        self.leng += 1
        if(self.leng >= Society.MAXIMUM):
            return None
        self.__person_list.append(person)

    def replace(self, new_person):
        person = None
        for i in range(len(self.__person_list)):
            person = self.__person_list[i]
            if(person.get_id() == id):
                person = new_person
                break

    def set(self, person):
        if(self.has(person.get_id())):
            self.replace(person)
            return None
        self.add(person)

    def has(self, id):
        person = None
        for i in range(len(self.__person_list)):
            person = self.__person_list[i]
            if(person.get_id() == id):
                return True
        return False

    def get(self, id):
        person = None
        for i in range(len(self.__person_list)):
            person = self.__person_list[i]
            if(person.get_id() == id):
                return person
        return None
    
    def process_events(self):
        for event in self.event_queue:
            if(event[0] == "attack"):
                self.effect_attack(event)

    def effect_attack(self, event):
        id_objetive = event[1]
        value = event[2]
        person = self.get(id_objetive)
        person.receibe_attack(value)
        self.set(person)

    def pick_events(self):
        for i in range(len(self.__person_list)):
            person = self.__person_list[i]
            self.event_queue = self.event_queue\
                + person.pick_events()
    
    def get_all_person_id(self):
        array = []
        person = None
        for i in range(len(self.__person_list)):
            person = self.__person_list[i]
            array.append(person.get_id())
        return array
    
    def randomize(self, quantity, culture):
        for i in range(quantity):
            self.add(Person(culture))

    def write(self):
        txt = ""
        person = None
        for i in range(len(self.__person_list)):
            person = self.__person_list[i]
            txt += person.write() + "\n\n"
        return txt

