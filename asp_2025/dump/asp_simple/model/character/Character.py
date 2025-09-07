


from .in_deps import*

class Character: 

    """
    Clase que representa a un personaje
    ficticio.
    """

    """
    Los maximos y minimos ancestrales
    indican la edad de los primeros
    generados artificialmente.
    """
    MAX_YEARS_ANCESTRAL = 65
    MIN_YEARS_ANCESTRAL = 12
    PROFFESION_TUPLE = profession_tuple
    SALUTE_DICT = salute_dict
    CULTURE_TUPLE = CULTURE_TUPLE
    last_id = 0

    def __init__(self):
        self.d:CharacterData = None
        self.d = CharacterData()
        # END ------------------------------
        self.init_calls()

    def init_calls(self)->None:
        """
        Ejecuta las llamadas a las funciones
        de inicio del objeto.
        """
        self.generate_id()

    def create_description(self)\
            ->Description:
        desc = Description()
        # si no esta en casa.
        if(not self.d.get_action() == "resting"):
            desc.character_presentation\
                = self.write_presentation()
        desc.character_states\
            = self.write_states()
        desc.character_relations\
            = self.write_relations()
        return desc

    def randomize(self, CULTURE:str):
        self.randomize_genes()
        self.d.set_culture(CULTURE)
        self.randomize_identity(CULTURE)
        
    def randomize_genes(self):
        """
        Randomiza los genes de los 
        personaje ancestrales.
        """
        self.d.genetics.randomize_ancestors(
            "mediterranean"
        )
        self.d.genetics.mix_genes()
        self.manifests_genes()
        
    def manifests_genes(self):
        """
        Copia los datos geneticos para
        dar las caracteristicas al
        personaje.
        """
        gen = self.d.genetics.own_gen
        self.d.set_skin_color(
            gen.get_skin_color())
        self.d.set_eye_color(
            gen.get_eye_color())
        self.d.set_eye_type(
            gen.get_eye_type())
        self.d.set_hair_type(
            gen.get_hair_type())
        self.d.set_hair_color(
            gen.get_hair_color())
        self.d.set_maximum_size(
            gen.get_maximum_size())

    def calculate_age_range(self):
        """
        Identifica el rango de edad del
        personaje basado en su tiempo
        de vida.
        """
        range_key = Btpy.whats_range(
            AGE_RANGE_DICT, 
            self.d.age_time.year
        )[0]
        self.d.set_age_range(range_key)

    def get_gender_age_range(self)->str:
        GENDER = self.d.get_gender()
        AGE_RANGE = self.d.get_age_range()
        if(GENDER == "female"):
            return AGE_RANGE_FEMALE[AGE_RANGE]
        else:
            return AGE_RANGE_MALE[AGE_RANGE]

    def randomize_identity(self, culture)->None:
        """
        Genera datos aleatorios para
        el personaje.
        """
        #
        # genera el gender
        gender = ""
        if(Btpy.random_bool()):
            gender = "MALE"
        else:
            gender = "FEMALE"
        self.d.set_gender(gender)
        #
        # genera name
        name = Btpy.random_name(
            gender, culture)
        self.d.set_name(name)
        name = Btpy.random_name(
            gender, culture)
        self.d.set_second_name(name)
        #
        # genera lastname
        lastname = Btpy.random_lastname(
            culture)
        self.d.set_lastname(lastname)
        lastname = Btpy.random_lastname(
            culture)
        self.d.set_second_lastname(lastname)
        #
        # genera age time
        self.d.age_time.year = Btpy\
            .rand_range(
                [self.MIN_YEARS_ANCESTRAL,
                self.MAX_YEARS_ANCESTRAL]
            )
        salute = Persistence\
            .get_salute(culture)
        self.d.set_salute(salute)

    def generate_id(self)->None:
        """
        Genera un ID unico para el personaje.
        """
        self.d.set_id(Character.last_id)
        Character.last_id += 1

    def talk(self, text:str):
        match text:
            case "hello":
                return self.write_presentation()
            case "state":
                return self.write_needs()
            case _:
                return "I don't understand"

    def write_presentation(self):
        """
        Funcion que escribe la presentacion
        completa del personaje como 
        un saludo.
        """
        return write_presentation(self.d)
    
    def write_relations(self)->str:
        """
        Describe sus relaciones sociales.
        """
        return self.d.relations\
            .write_relations()
    
    def write_states(self)->str:
        """
        Describe sus estados personales
        y emociones.
        """
        return self.write_needs()
    
    def update_character(self)->None:
        """
        Funcion que actualiza los datos del
        personaje
        """
        pass

    def write_needs(self)->str:
        """
        Funcion que escribe las nesesidades
        del personaje como si tiene hambre
        o sed.
        """
        txt = f"i'm feel({self.d.get_mood_points()}) "
        if(self.d.get_has_food()):
            txt += ", hungry"
        if(self.d.get_has_water()):
            txt += ", thirsty"
        if(self.d.get_has_health()):
            txt += ", sick"
        if(self.d.get_has_sanitation()):
            txt += ", dirty"
        if(self.d.get_has_dress()):
            txt += ", nude"
        return txt 
    
    def relate(self, character):
        """
        Relaciona al personaje con el
        personaje enviado.
        """
        self.d.relations.set_relation(
            character.d.get_name(), 
            character.d.get_id()
        )
    
    def advance_one_day(self)->None:
        """
        Funcion que avansa un dia en 
        el tiempo para el personaje.
        """
        self.format_needs()
        self.calcule_mood()
        self.d.age_time.advance_one_day()
        self.calculate_age_range()
        self.randomize_action()

    def randomize_action(self):
        """
        Randomiza las acciones del 
        personaje a diario.
        """
        key = Btpy.random_choice(
            list(CharacterData.ACTION_TUPLE))
        self.d.set_action(key)

    def write_appearance(self):
        return write_appearance(self.d)

    def format_needs(self)->None:
        self.d = format_needs(self.d)
    
    def calcule_mood(self):
        """
        Funcion que calcula el humor del
        personaje. Lo hace sumando las
        nesesidades faltantes.
        """
        self.d.set_mood_points(0)
        if(self.d.get_has_water()):
            self.d.sum_mood_points(1)
        if(self.d.get_has_food()):
            self.d.sum_mood_points(1)
        if(self.d.get_has_fun()):
            self.d.sum_mood_points(1)
        if(self.d.get_has_dress()):
            self.d.sum_mood_points(1)
        if(self.d.get_has_refreshing()):
            self.d.sum_mood_points(1)
        if(self.d.get_has_heating()):
            self.d.sum_mood_points(1)
        if(self.d.get_has_sanitation()):
            self.d.sum_mood_points(1)
        if(self.d.get_has_health()):
            self.d.sum_mood_points(1)
        
